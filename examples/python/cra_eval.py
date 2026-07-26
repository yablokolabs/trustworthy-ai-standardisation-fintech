#!/usr/bin/env python3
"""Reference implementation of the CRA escalation evaluator and bundle checker.

This operationalises three parts of the Continuous Reliability Assurance
proposal in ``proposals/continuous-reliability-assurance-for-financial-ai.md``:

* the minimum evidence bundle (section 3), as a structural validator
* the threshold design factors and escalation levels 1-5 (section 4), as a
  transparent additive scoring model
* the ownership separation rules (section 5), as conformance checks

The scoring weights below are **illustrative, not normative**. The proposal
states that institutions should predefine their own materiality and escalation
thresholds; this module supplies a defensible default so that the CRA model can
be executed, tested and argued with, rather than only read.

Standard library only. No third-party dependencies.

Usage::

    python3 cra_eval.py ../samples/*.json
    python3 cra_eval.py --selftest
    python3 cra_eval.py --json ../samples/credit-decisioning-calibration-drift.json
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from typing import Any, Dict, List, Tuple

SCHEMA_VERSION = "0.1.0"

# --------------------------------------------------------------------------
# Section 4 threshold design factors.
#
# The proposal states thresholds should not be fixed performance numbers alone,
# but should combine metric deterioration, customer or financial impact,
# duration of degradation, detectability, availability of compensating
# controls, and autonomy level of the system. Each factor below maps to one of
# those, so a score can be explained line by line to a reviewer.
# --------------------------------------------------------------------------

MATERIALITY_BASE = {
    "informational": 0,
    "review_required": 2,
    "approval_required": 4,
    "restrict_or_stop_use": 6,
}

IMPACT_POINTS = {"none": 0, "low": 1, "moderate": 2, "high": 3, "severe": 4}

DURATION_POINTS = {"transient": 0, "short": 1, "sustained": 2, "persistent": 3}

# Detectability: a problem found by an external party is worse than one the
# institution's own monitoring surfaced.
DETECTION_POINTS = {
    "automated_monitoring": 0,
    "internal_review": 1,
    "external_party": 2,
}

COMPENSATING_CONTROL_POINTS = {"effective": -2, "partial": -1, "none": 0}

# Autonomy acts as the threshold multiplier described in section 4: the same
# deterioration justifies review in a decision-support system but restriction
# in an autonomous action workflow.
AUTONOMY_POINTS = {
    "advisory": 0,
    "human_in_loop": 1,
    "human_on_loop": 2,
    "autonomous": 3,
}

# Escalation levels 1-5 from section 4, as inclusive lower bounds.
ESCALATION_BANDS: List[Tuple[int, int, str]] = [
    (1, 1, "Observe"),
    (2, 4, "Review"),
    (5, 7, "Restrict"),
    (8, 10, "Escalate"),
    (11, 10**6, "Suspend or Roll Back"),
]

TRIGGER_CATEGORIES = {
    "A_performance_degradation",
    "B_distribution_context_change",
    "C_system_change",
    "D_control_failure",
    "E_external_challenge",
}

SYSTEM_CLASSES = {
    "stable_predictive",
    "continually_retrained",
    "llm_assistant",
    "agentic",
}

IMPACT_TIERS = {"low", "moderate", "high", "critical"}

DECISIONS = {
    "continue",
    "continue_with_increased_observation",
    "constrain",
    "revalidate",
    "retrain",
    "rollback",
    "escalate",
    "retire",
}

MINIMUM_BUNDLE_ARTIFACTS = [
    ("trigger_record", "Trigger record"),
    ("delta_description", "Delta description"),
    ("reliability_impact_analysis", "Reliability impact analysis"),
    ("monitoring_snapshot", "Monitoring snapshot"),
    ("decision_record", "Decision record"),
    ("ownership", "Owner and approver sign-off"),
]

# Decisions that are coherent with each escalation level. Used for advisory
# consistency checks, not hard validation, since local policy may differ.
LEVEL_EXPECTED_DECISIONS = {
    1: {"continue", "continue_with_increased_observation"},
    2: {"continue", "continue_with_increased_observation", "revalidate", "retrain", "constrain"},
    3: {"constrain", "revalidate", "retrain", "rollback", "escalate"},
    4: {"constrain", "revalidate", "retrain", "rollback", "escalate", "retire"},
    5: {"rollback", "escalate", "retire", "constrain"},
}


class BundleError(Exception):
    """Raised when a bundle cannot be scored because it is structurally invalid."""


# --------------------------------------------------------------------------
# Structural validation
#
# The canonical contract is schema/cra-evidence-bundle.schema.json. These checks
# mirror it so the tool runs with no third-party validator installed; use any
# JSON Schema validator against that file for full conformance checking.
# --------------------------------------------------------------------------


def _require(obj: Dict[str, Any], key: str, path: str) -> Any:
    if key not in obj or obj[key] in (None, ""):
        raise BundleError(f"missing required field: {path}{key}")
    return obj[key]


def _require_enum(obj: Dict[str, Any], key: str, allowed, path: str) -> str:
    value = _require(obj, key, path)
    if value not in allowed:
        raise BundleError(
            f"{path}{key} has invalid value {value!r}; expected one of "
            f"{sorted(allowed)}"
        )
    return value


def validate_structure(bundle: Dict[str, Any]) -> None:
    """Raise BundleError if required fields or enum values are missing/invalid."""
    if not isinstance(bundle, dict):
        raise BundleError("bundle must be a JSON object")

    _require(bundle, "bundle_id", "")

    for key, label in MINIMUM_BUNDLE_ARTIFACTS:
        if key not in bundle or not isinstance(bundle[key], dict):
            raise BundleError(
                f"minimum evidence bundle incomplete: {label} ({key}) is absent"
            )

    system = _require(bundle, "system", "")
    _require(system, "system_id", "system.")
    _require(system, "name", "system.")
    _require_enum(system, "system_class", SYSTEM_CLASSES, "system.")
    _require_enum(system, "autonomy_level", AUTONOMY_POINTS, "system.")
    _require_enum(system, "impact_tier", IMPACT_TIERS, "system.")

    trigger = bundle["trigger_record"]
    _require(trigger, "trigger_id", "trigger_record.")
    _require_enum(trigger, "category", TRIGGER_CATEGORIES, "trigger_record.")
    _require_enum(trigger, "materiality", MATERIALITY_BASE, "trigger_record.")
    _require_enum(trigger, "detection_source", DETECTION_POINTS, "trigger_record.")
    _require(trigger, "detected_at", "trigger_record.")
    _require(trigger, "summary", "trigger_record.")

    delta = bundle["delta_description"]
    _require(delta, "summary", "delta_description.")
    _require_enum(delta, "duration", DURATION_POINTS, "delta_description.")

    impact = bundle["reliability_impact_analysis"]
    _require_enum(
        impact, "customer_financial_impact", IMPACT_POINTS, "reliability_impact_analysis."
    )
    _require(impact, "assessment", "reliability_impact_analysis.")
    if "compensating_controls" in impact:
        _require_enum(
            impact,
            "compensating_controls",
            COMPENSATING_CONTROL_POINTS,
            "reliability_impact_analysis.",
        )

    _require(bundle["monitoring_snapshot"], "captured_at", "monitoring_snapshot.")

    decision = bundle["decision_record"]
    _require_enum(decision, "decision", DECISIONS, "decision_record.")
    _require(decision, "rationale", "decision_record.")
    _require(decision, "decided_at", "decision_record.")
    recorded = decision.get("recorded_escalation_level")
    if recorded is not None and recorded not in (1, 2, 3, 4, 5):
        raise BundleError(
            "decision_record.recorded_escalation_level must be an integer 1-5, "
            f"got {recorded!r}"
        )

    ownership = bundle["ownership"]
    for role in ("business_owner", "technical_owner", "independent_control_owner"):
        party = ownership.get(role)
        if not isinstance(party, dict):
            raise BundleError(f"ownership.{role} is required (section 5)")
        _require(party, "id", f"ownership.{role}.")
        _require(party, "role_title", f"ownership.{role}.")


# --------------------------------------------------------------------------
# Escalation scoring
# --------------------------------------------------------------------------


def level_for_score(score: int) -> Tuple[int, str]:
    clamped = max(1, score)
    for index, (low, high, name) in enumerate(ESCALATION_BANDS, start=1):
        if low <= clamped <= high:
            return index, name
    return 5, ESCALATION_BANDS[-1][2]


def evaluate(bundle: Dict[str, Any]) -> Dict[str, Any]:
    """Score a validated bundle and return the recommendation plus its breakdown."""
    validate_structure(bundle)

    system = bundle["system"]
    trigger = bundle["trigger_record"]
    delta = bundle["delta_description"]
    impact = bundle["reliability_impact_analysis"]
    controls = impact.get("compensating_controls", "none")

    contributions = [
        ("trigger materiality", trigger["materiality"], MATERIALITY_BASE[trigger["materiality"]]),
        (
            "customer or financial impact",
            impact["customer_financial_impact"],
            IMPACT_POINTS[impact["customer_financial_impact"]],
        ),
        ("duration of degradation", delta["duration"], DURATION_POINTS[delta["duration"]]),
        (
            "detectability",
            trigger["detection_source"],
            DETECTION_POINTS[trigger["detection_source"]],
        ),
        (
            "compensating controls",
            controls,
            COMPENSATING_CONTROL_POINTS[controls],
        ),
        (
            "autonomy level",
            system["autonomy_level"],
            AUTONOMY_POINTS[system["autonomy_level"]],
        ),
    ]

    score = sum(points for _, _, points in contributions)
    level, level_name = level_for_score(score)

    return {
        "bundle_id": bundle["bundle_id"],
        "system_id": system["system_id"],
        "system_name": system["name"],
        "trigger_category": trigger["category"],
        "score": score,
        "recommended_level": level,
        "recommended_level_name": level_name,
        "contributions": [
            {"factor": factor, "value": value, "points": points}
            for factor, value, points in contributions
        ],
        "conformance_findings": conformance_findings(bundle, level),
    }


# --------------------------------------------------------------------------
# CRA conformance checks
# --------------------------------------------------------------------------


def conformance_findings(bundle: Dict[str, Any], recommended_level: int) -> List[Dict[str, str]]:
    """Return findings against the proposal's ownership and evidence rules."""
    findings: List[Dict[str, str]] = []

    def add(severity: str, rule: str, detail: str) -> None:
        findings.append({"severity": severity, "rule": rule, "detail": detail})

    ownership = bundle["ownership"]
    decision = bundle["decision_record"]
    impact = bundle["reliability_impact_analysis"]
    trigger = bundle["trigger_record"]
    monitoring = bundle["monitoring_snapshot"]

    def party_id(role: str):
        party = ownership.get(role)
        return party.get("id") if isinstance(party, dict) else None

    business = party_id("business_owner")
    technical = party_id("technical_owner")
    control = party_id("independent_control_owner")

    # Section 5: ownership should be split deliberately.
    if control and control in {business, technical}:
        add(
            "error",
            "section 5 ownership separation",
            "independent_control_owner is the same party as the business or "
            "technical owner, which collapses independent challenge",
        )
    if business and business == technical:
        add(
            "warning",
            "section 5 ownership separation",
            "business_owner and technical_owner are the same party",
        )

    # Section 4 level 3+: restriction implies an accountable approver.
    if recommended_level >= 3 and not isinstance(ownership.get("approver"), dict):
        add(
            "error",
            "section 4 level 3 approver",
            f"recommended level {recommended_level} requires an approver "
            "sign-off, but ownership.approver is absent",
        )

    # Section 4 level 4: notify relevant governance forums.
    if recommended_level >= 4 and not decision.get("governance_forum_notified", False):
        add(
            "error",
            "section 4 level 4 governance notification",
            f"recommended level {recommended_level} requires governance forum "
            "notification, but decision_record.governance_forum_notified is false",
        )

    # Section 3: root cause analysis where deterioration is observed.
    if trigger["category"] == "A_performance_degradation" and not impact.get("root_cause"):
        add(
            "warning",
            "section 3 reassessment evidence",
            "performance degradation trigger without a recorded root_cause",
        )

    # Category D and section 6: a monitoring outage undermines the snapshot.
    if monitoring.get("monitoring_intact") is False:
        add(
            "warning",
            "section 6 monitoring integrity",
            "monitoring_snapshot.monitoring_intact is false, so live evidence "
            "in this bundle is weakened and should not be read as assurance",
        )

    # Section 3: restriction decisions should record the temporary controls applied.
    if recommended_level >= 3 and not decision.get("temporary_controls"):
        add(
            "warning",
            "section 3 reassessment evidence",
            f"recommended level {recommended_level} without any recorded "
            "temporary_controls",
        )

    # Divergence between the institution's recorded level and this evaluation.
    recorded = decision.get("recorded_escalation_level")
    if recorded is not None and recorded != recommended_level:
        severity = "error" if recorded < recommended_level else "warning"
        add(
            severity,
            "recorded vs evaluated level",
            f"bundle records level {recorded} but the threshold factors "
            f"evaluate to level {recommended_level}",
        )

    # Advisory coherence between level and decision taken.
    expected = LEVEL_EXPECTED_DECISIONS.get(recommended_level, set())
    if decision["decision"] not in expected:
        add(
            "warning",
            "level and decision coherence",
            f"decision {decision['decision']!r} is unusual at level "
            f"{recommended_level}; expected one of {sorted(expected)}",
        )

    return findings


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

SEVERITY_MARK = {"error": "[ERROR]  ", "warning": "[WARNING]"}


def format_report(result: Dict[str, Any]) -> str:
    lines = []
    lines.append(f"Bundle:  {result['bundle_id']}")
    lines.append(f"System:  {result['system_name']} ({result['system_id']})")
    lines.append(f"Trigger: {result['trigger_category']}")
    lines.append("")
    lines.append("Threshold factors (section 4):")
    width = max(len(c["factor"]) for c in result["contributions"])
    for contribution in result["contributions"]:
        lines.append(
            f"  {contribution['factor']:<{width}}  "
            f"{contribution['value']:<22} {contribution['points']:+d}"
        )
    lines.append(f"  {'total score':<{width}}  {'':<22} {result['score']:>2}")
    lines.append("")
    lines.append(
        f"Recommended escalation: Level {result['recommended_level']} "
        f"- {result['recommended_level_name']}"
    )

    findings = result["conformance_findings"]
    if findings:
        lines.append("")
        lines.append("Conformance findings:")
        for finding in findings:
            mark = SEVERITY_MARK.get(finding["severity"], finding["severity"])
            lines.append(f"  {mark} {finding['rule']}: {finding['detail']}")
    else:
        lines.append("")
        lines.append("Conformance findings: none")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------


def _vector(materiality, impact, duration, detection, controls, autonomy):
    return {
        "bundle_id": "SELFTEST",
        "system": {
            "system_id": "sys",
            "name": "selftest",
            "system_class": "stable_predictive",
            "autonomy_level": autonomy,
            "impact_tier": "moderate",
        },
        "trigger_record": {
            "trigger_id": "t",
            "category": "A_performance_degradation",
            "materiality": materiality,
            "detected_at": "2026-07-01T00:00:00Z",
            "detection_source": detection,
            "summary": "selftest",
        },
        "delta_description": {"summary": "selftest", "duration": duration},
        "reliability_impact_analysis": {
            "customer_financial_impact": impact,
            "compensating_controls": controls,
            "assessment": "selftest",
            "root_cause": "selftest",
        },
        "monitoring_snapshot": {"captured_at": "2026-07-01T00:00:00Z"},
        "decision_record": {
            "decision": "continue",
            "rationale": "selftest",
            "decided_at": "2026-07-01T00:00:00Z",
        },
        "ownership": {
            "business_owner": {"id": "b", "role_title": "Business Owner"},
            "technical_owner": {"id": "t", "role_title": "Technical Owner"},
            "independent_control_owner": {"id": "c", "role_title": "Control Owner"},
        },
    }


def selftest() -> int:
    """Check the scoring model against cases stated or implied by the proposal."""
    cases = [
        # The worked example in section 4: a modest decline in a decision-support
        # system justifies review, while the same decline in an autonomous action
        # workflow justifies restriction.
        (
            "section 4 example, decision-support",
            _vector("review_required", "low", "short", "automated_monitoring", "partial", "advisory"),
            2,
        ),
        (
            "section 4 example, autonomous workflow",
            _vector("review_required", "low", "short", "automated_monitoring", "partial", "autonomous"),
            3,
        ),
        # An informational trigger with effective compensating controls should
        # not escalate beyond observation.
        (
            "informational trigger, controls effective",
            _vector("informational", "none", "transient", "automated_monitoring", "effective", "advisory"),
            1,
        ),
        # A stop-use trigger found externally, persistent, high impact, on an
        # autonomous system should reach the top of the scale.
        (
            "severe sustained failure, autonomous",
            _vector("restrict_or_stop_use", "severe", "persistent", "external_party", "none", "autonomous"),
            5,
        ),
        # Approval-required with moderate impact on a human-on-loop system.
        (
            "approval required, human on loop",
            _vector("approval_required", "moderate", "sustained", "internal_review", "partial", "human_on_loop"),
            4,
        ),
    ]

    failures = 0
    for name, bundle, expected_level in cases:
        result = evaluate(bundle)
        actual = result["recommended_level"]
        status = "ok  " if actual == expected_level else "FAIL"
        if actual != expected_level:
            failures += 1
        print(
            f"[{status}] {name}: score {result['score']:>2} -> level {actual} "
            f"(expected {expected_level})"
        )

    # Structural validation must reject an incomplete bundle.
    incomplete = _vector("review_required", "low", "short", "automated_monitoring", "none", "advisory")
    del incomplete["monitoring_snapshot"]
    try:
        evaluate(incomplete)
    except BundleError:
        print("[ok  ] incomplete bundle rejected by validator")
    else:
        print("[FAIL] incomplete bundle was not rejected")
        failures += 1

    # Ownership collapse must be reported as an error finding.
    collapsed = _vector("review_required", "low", "short", "automated_monitoring", "none", "advisory")
    collapsed["ownership"]["independent_control_owner"] = {
        "id": "b",
        "role_title": "Business Owner",
    }
    findings = evaluate(collapsed)["conformance_findings"]
    if any(f["severity"] == "error" and "ownership" in f["rule"] for f in findings):
        print("[ok  ] ownership collapse reported as error")
    else:
        print("[FAIL] ownership collapse not reported")
        failures += 1

    print()
    print("selftest failures:", failures)
    return 1 if failures else 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Evaluate CRA evidence bundles against the escalation model in "
            "proposals/continuous-reliability-assurance-for-financial-ai.md"
        )
    )
    parser.add_argument("paths", nargs="*", help="bundle JSON files or glob patterns")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of text")
    parser.add_argument("--selftest", action="store_true", help="run the built-in test vectors")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()

    if not args.paths:
        parser.print_help()
        return 2

    expanded: List[str] = []
    for pattern in args.paths:
        matches = sorted(glob.glob(pattern))
        expanded.extend(matches if matches else [pattern])

    results = []
    exit_code = 0

    for path in expanded:
        if not os.path.exists(path):
            print(f"{path}: no such file", file=sys.stderr)
            exit_code = 2
            continue
        try:
            with open(path, "r", encoding="utf-8") as handle:
                bundle = json.load(handle)
        except json.JSONDecodeError as exc:
            print(f"{path}: invalid JSON: {exc}", file=sys.stderr)
            exit_code = 2
            continue

        try:
            result = evaluate(bundle)
        except BundleError as exc:
            print(f"{path}: bundle invalid: {exc}", file=sys.stderr)
            exit_code = 2
            continue

        result["source"] = os.path.basename(path)
        results.append(result)

        if any(f["severity"] == "error" for f in result["conformance_findings"]):
            exit_code = max(exit_code, 1)

        if not args.json:
            print(f"=== {os.path.basename(path)} ===")
            print(format_report(result))
            print()

    if args.json:
        print(json.dumps(results, indent=2))

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
