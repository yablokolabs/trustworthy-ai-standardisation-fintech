# Reliability Gaps in Current AI Standards

## Purpose

This document identifies reliability questions that are not yet fully covered
by current AI standards and related initiatives, especially from the
perspective of financial services production environments.

## Concept Drift

Current standards recognize change and monitoring needs, but they generally do
not provide enough practical direction on how to classify, quantify, and
govern concept drift in live decision systems.

For financial services, this gap matters because:

- market conditions can change faster than validation cycles
- fraud behavior adapts in response to deployed controls
- customer populations shift due to macroeconomic events or policy changes

The unresolved need is a standardised way to connect drift detection to
materiality thresholds, business impact, approval triggers, and fallback
actions.

## Continually Trained Models

Standards and lifecycle guidance are stronger for periodically updated systems
than for models that learn or are refreshed continuously. The main gap is not
awareness that change occurs, but governance for how much autonomous model
change is acceptable before the system is effectively a new model.

This creates several open questions:

- what evidence is sufficient for pre-approved update boundaries
- how validation should be sampled across frequent releases
- when human review must interrupt automated retraining pipelines
- how cumulative small changes should be assessed over time

Financial institutions need stronger norms for controlled adaptation without
losing approval discipline.

## Agentic AI Systems

Agentic AI introduces reliability issues that go beyond single-model accuracy.
An agent may plan, call tools, retrieve external information, and chain
multiple actions with partial autonomy.

Existing standards do not yet provide enough operational specificity for:

- bounding action authority
- validating tool-use reliability
- monitoring multi-step failure propagation
- assigning accountability for emergent workflow behavior

This gap is especially material in financial operations where an incorrect
action sequence can produce customer harm, control breaches, or unauthorized
transaction effects.

## LLM-Based Systems

LLM-based systems challenge traditional reliability assessment because output
quality depends on prompts, context windows, retrieval behavior, model
versioning, and human interaction patterns.

The current gap is not only technical measurement, but assurance design:

- how to define acceptable output stability for high-impact tasks
- how to monitor hallucination risk in operational contexts
- how to govern prompt and policy changes as production changes
- how to evaluate performance when answers are probabilistic and contextual

In financial services, LLM reliability needs task-specific thresholds rather
than generic capability claims.

## Runtime Reliability Assessment

Most standards are stronger on design-time and governance-time structure than
on runtime reliability assurance. They do not yet provide a complete model for
how reliability should be reassessed continuously in deployment.

A stronger standardisation approach is needed for:

- periodic versus event-driven reassessment
- triggers for out-of-cycle review
- interaction between service degradation and business continuity controls
- reliability evidence expected after a production incident

This is central in finance because production conditions are not static enough
for one-time validation logic to remain sufficient.

## Monitoring and Observability

Monitoring is widely acknowledged, but observability for AI systems remains
under-specified. Many current approaches still treat monitoring as a list of
metrics rather than a capability for diagnosing why reliability is changing.

Key unresolved areas include:

- linking input anomalies to output deterioration
- tracing behavior across model, data, retrieval, and workflow layers
- correlating model alerts with operational incidents and customer outcomes
- defining minimum observability expectations for third-party AI services

Financial firms require observability that supports investigation, challenge,
and response under time pressure.

## Production Retraining Governance

Retraining governance is a repeated weak point. Existing lifecycle and risk
concepts help, but they often do not define how retraining should be governed
when triggers are frequent and market conditions are unstable.

The missing detail includes:

- retraining eligibility criteria
- minimum evidence before promotion to production
- separation of duties in automated pipelines
- rollback expectations when the new version degrades performance

Without stronger norms here, firms may either over-constrain adaptation or
allow changes that outpace governance.

## Reliability Metrics for Adaptive Systems

Traditional metrics such as accuracy or area under curve are not enough for
adaptive and context-sensitive systems. Standards work still needs more mature
definitions for reliability metrics that reflect:

- calibration stability over time
- performance degradation rate after distribution shift
- robustness across customer or market segments
- recovery speed after intervention
- workflow-level reliability for composite and agentic systems

Financial services need metrics that can support escalation, board reporting,
and audit review, not just technical tuning.

## Summary Interpretation

The main gap across current standards is not a lack of governance intent. It
is the lack of operational precision for systems that learn, adapt, retrieve,
or act in changing environments.

For financial services, the next generation of standards work needs to move
from static conformance concepts toward continuous assurance concepts. That
means reliability must be treated as a monitored control outcome, not just a
property assessed before release.

