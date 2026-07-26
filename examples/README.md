# CRA Reference Implementation

This directory makes the Continuous Reliability Assurance (CRA) proposal
executable. The proposal in
[`proposals/continuous-reliability-assurance-for-financial-ai.md`](../proposals/continuous-reliability-assurance-for-financial-ai.md)
defines a trigger taxonomy, an evidence bundle, escalation levels, and
ownership rules. This directory expresses those as a machine-readable schema
and a small evaluator, so the model can be run, tested, and disagreed with
concretely rather than only read.

Everything here is **illustrative reference material**. It is not normative
standards text, and it does not reproduce any copyrighted standards content.

## Contents

```text
examples/
├── README.md
├── schema/
│   └── cra-evidence-bundle.schema.json   JSON Schema for the minimum evidence bundle
├── python/
│   └── cra_eval.py                        Escalation evaluator and conformance checker
└── samples/
    ├── credit-decisioning-calibration-drift.json
    ├── fraud-detection-monitoring-outage.json
    ├── llm-assistant-prompt-change.json
    ├── agentic-vendor-model-update.json
    └── aml-understated-nonconformant.json
```

## Requirements

Python 3.8 or later. Standard library only, no third-party packages.

## Running

```bash
cd examples/python

# Evaluate every sample bundle
python3 cra_eval.py ../samples/*.json

# Evaluate one bundle and emit machine-readable output
python3 cra_eval.py --json ../samples/agentic-vendor-model-update.json

# Run the built-in test vectors
python3 cra_eval.py --selftest
```

Exit codes: `0` clean, `1` at least one bundle produced an error-severity
conformance finding, `2` a bundle was unreadable or structurally invalid.

## What the evaluator does

**1. Validates the minimum evidence bundle.** Section 3 of the proposal defines
six artifacts a CRA review must minimally produce: trigger record, delta
description, reliability impact analysis, monitoring snapshot, decision record,
and owner and approver sign-off. The validator rejects a bundle that is missing
any of them, and checks the A-E trigger taxonomy and materiality classes from
section 2.

The canonical contract is
[`schema/cra-evidence-bundle.schema.json`](schema/cra-evidence-bundle.schema.json).
The Python validator mirrors it so the tool runs with nothing installed; use any
JSON Schema validator against that file for full conformance checking.

**2. Recommends an escalation level.** Section 4 states that thresholds should
not be fixed performance numbers alone, but should combine metric
deterioration, customer or financial impact, duration of degradation,
detectability, availability of compensating controls, and autonomy level. The
evaluator scores each of those six factors additively and maps the total onto
escalation levels 1-5:

| Factor | Values and points |
| --- | --- |
| Trigger materiality | informational 0, review_required +2, approval_required +4, restrict_or_stop_use +6 |
| Customer or financial impact | none 0, low +1, moderate +2, high +3, severe +4 |
| Duration of degradation | transient 0, short +1, sustained +2, persistent +3 |
| Detectability | automated_monitoring 0, internal_review +1, external_party +2 |
| Compensating controls | effective -2, partial -1, none 0 |
| Autonomy level | advisory 0, human_in_loop +1, human_on_loop +2, autonomous +3 |

| Score | Escalation level |
| --- | --- |
| 1 or below | Level 1 — Observe |
| 2 to 4 | Level 2 — Review |
| 5 to 7 | Level 3 — Restrict |
| 8 to 10 | Level 4 — Escalate |
| 11 or above | Level 5 — Suspend or Roll Back |

The weights are a **defensible default, not a recommendation**. The proposal is
explicit that institutions should predefine their own materiality and
escalation thresholds; the point of publishing weights is that a scoring model
you can inspect and argue with is more useful than one left implicit.

The model reproduces the worked example in section 4: a modest decline in a
decision-support system evaluates to Level 2 Review, while the same decline in
an autonomous action workflow evaluates to Level 3 Restrict. Both cases are
asserted in `--selftest`.

**3. Reports conformance findings.** The evaluator flags:

- an independent control owner who is also the business or technical owner,
  which collapses the challenge separation required by section 5
- a Level 3 or above recommendation with no approver sign-off
- a Level 4 or above recommendation with no governance forum notification
- a performance degradation trigger with no recorded root cause
- a monitoring snapshot taken while monitoring was not intact
- a recorded escalation level that diverges from the evaluated one, treated as
  an error where the institution recorded a *lower* level than the factors
  support
- a control decision that is incoherent with the recommended level

## Sample bundles

The first four samples are conformant and cover the use cases in section 8 and
four of the five trigger categories:

| Sample | Trigger | Autonomy | Evaluated level |
| --- | --- | --- | --- |
| `credit-decisioning-calibration-drift` | A, performance degradation | human_in_loop | 3 — Restrict |
| `llm-assistant-prompt-change` | C, system change | human_on_loop | 2 — Review |
| `fraud-detection-monitoring-outage` | D, control failure | human_on_loop | 4 — Escalate |
| `agentic-vendor-model-update` | C, system change | autonomous | 5 — Suspend or Roll Back |

`aml-understated-nonconformant` is **deliberately non-conformant** and exists to
demonstrate the checks firing. It records Level 2 for a situation the factors
evaluate at Level 4, has no approver, notifies no governance forum, and names
the same person as both business owner and independent control owner. Running
the full sample set therefore exits `1` by design.

## Known limitations

These are real weaknesses in the model as published, not caveats added for
form. Each is a candidate for future work.

**Regulatory exposure has no distinct input.** The only impact axis is customer
or financial impact. The AML sample shows the consequence: a regulatory inquiry
into a surveillance control scores low on customer financial impact even though
regulatory exposure is the entire point of the trigger. A future revision should
separate customer harm, financial loss, and regulatory or supervisory exposure.

**Suspension is not always an available action.** The model can recommend Level
5 for systems where suspending operation would itself be a control failure — an
AML transaction monitoring engine being the clearest case. Institutions need to
overlay a constraint on which control decisions are permissible per system
before the recommendation is actionable.

**Additive scoring hides interaction effects.** Autonomy and compensating
controls interact in ways a sum does not capture: effective human review does
not merely offset autonomy points, it changes what failure modes are reachable
at all. A more faithful model would gate on autonomy before scoring.

**Metric deterioration is not scored directly.** Section 4 lists it as a
threshold factor, but the evaluator takes materiality as an input rather than
deriving it from the `metrics` array in the bundle. Bundles carry baseline,
observed, and threshold values, so deriving a deterioration contribution from
them is a natural next step.

## Relationship to the standards discussed in this repository

The evaluator is an operational layer, not a conformance tool for any
published standard. It assumes the governance frame that ISO/IEC 42001
provides, the risk framing of ISO/IEC 23894, the lifecycle structure of
ISO/IEC 5338, and the reliability assessment concept of ISO/IEC TS 25570, and
implements only the reassessment logic the CRA proposal argues is missing
between them. See
[`mappings/ai-standards-landscape.md`](../mappings/ai-standards-landscape.md)
and
[`mappings/financial-ai-controls-gap-matrix.md`](../mappings/financial-ai-controls-gap-matrix.md).

## Licence

MIT, as per the repository [LICENSE](../LICENSE).
