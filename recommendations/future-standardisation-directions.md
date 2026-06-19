# Future Standardisation Directions

## Purpose

This document proposes actionable areas for future standards work that would
improve the practical assurance of trustworthy AI systems in financial
services.

## Financial AI Systems

Future work should define a stronger sector-facing profile for financial AI
controls. Financial services operate under concentrated expectations for
evidence, auditability, materiality, and customer impact. General-purpose AI
standards do not fully resolve these sector-specific needs.

Recommended direction:

- develop implementation profiles or technical reports for financial AI
  governance and assurance
- define examples of control objectives for credit, fraud, surveillance, and
  customer support use cases
- clarify how AI controls interact with existing model risk, operational risk,
  and compliance frameworks

## Quantitative ML Systems

Quantitative ML systems need more explicit guidance on adaptation under market
change, regime shifts, and model portfolio interactions.

Recommended direction:

- define governance patterns for model refresh frequency and change tolerance
- specify evidence expectations for model promotion in volatile environments
- develop metrics for temporal robustness, calibration drift, and stability
  under extreme but plausible conditions

## Agentic AI

Agentic systems require dedicated standards work because they introduce action
authority, tool orchestration, and workflow-level risk that are not captured
well by single-model assurance methods.

Recommended direction:

- define control concepts for bounded action authority and delegated decision
  limits
- standardise logging expectations for plan, tool, and execution traces
- define failure categories for multi-step autonomous workflows
- specify assurance patterns for human intervention and safe fallback modes

## AI Reliability Metrics

Future standards should move beyond generic reliability language and provide
stronger guidance on measurable indicators suitable for production oversight.

Recommended direction:

- define core and optional reliability metrics for different AI system classes
- include metrics for degradation rate, recovery time, alert precision, and
  intervention effectiveness
- distinguish model-level, workflow-level, and user-facing reliability

## Continuous Assurance

Current standards are stronger on governance structure than on continuous
assurance. Financial AI requires operating models that treat post-deployment
assessment as a standing obligation.

Recommended direction:

- define event-driven and periodic assurance review patterns
- standardise reassessment triggers tied to drift, incidents, and material
  process changes
- define minimum evidence sets for continued production approval

## Governance Frameworks

Governance frameworks should be made more explicit for multi-model estates,
third-party model usage, and cross-functional accountability.

Recommended direction:

- define governance artifacts for model portfolios rather than individual
  systems only
- clarify accountability models for vendors, deployers, and internal users
- standardise escalation pathways for unresolved assurance concerns

## AI Lifecycle Monitoring

Lifecycle monitoring deserves its own stronger treatment. The key issue is not
only whether monitoring exists, but whether it is connected to change control,
incident handling, and business accountability.

Recommended direction:

- define minimum monitoring coverage across data, model, workflow, and
  downstream control layers
- standardise how monitoring evidence feeds validation, retraining, and
  retirement decisions
- promote observability practices that support root cause analysis rather than
  superficial alerting

## Recommended Near-Term Outputs

If standards bodies or related initiatives were to prioritize short-term
deliverables, the following would be high value:

- a technical report on reliability assurance for adaptive AI systems
- a profile for trustworthy AI controls in financial services
- guidance on agentic AI accountability and operational logging
- a metrics catalogue for continuous assurance of production AI systems
- a practice note on retraining governance and release control

## Closing View

The main requirement for future standards work is not more abstract principle
statements. It is more operational clarity. Financial-sector AI practitioners
need standards outputs that help them decide when systems remain acceptable,
when they no longer do, and what evidence is required to justify that answer.

