# Standards Review Log

## Purpose

This log provides a structured way to record standards reviews, standards-body
engagement observations, and follow-up recommendations. It is designed to
support repeatable analysis and final fellowship reporting.

## How to Use This Log

Each review entry should record:

- the date of review or engagement
- the standard or initiative reviewed
- a concise public scope summary
- observations relevant to trustworthy AI in finance
- identified gaps or unresolved questions
- recommended next actions
- links to supporting evidence

## Entry 1 — ISO/IEC 42001

### Date

2026-06-19

### Standard Reviewed

ISO/IEC 42001 — AI management systems

### Scope Summary

Reviewed the publicly visible positioning of ISO/IEC 42001 as a management
system framework for establishing, implementing, maintaining, and improving AI
governance processes at the organizational level.

### Observations

- The management system framing is useful for assigning accountability and
  integrating AI controls into existing governance structures.
- The standard is highly relevant for firms that need a repeatable governance
  backbone across multiple AI use cases rather than one-off model controls.
- It does not, by itself, provide sufficient depth on production reliability
  metrics, adaptive behavior, or financial-sector model performance monitoring.

### Gaps Identified

- Limited direct guidance for quantitative reliability thresholds in live
  financial systems
- Limited specificity for retraining governance in continuously updated models
- No sector-specific treatment of model portfolios, market regime change, or
  agentic operational workflows

### Recommendations

- Use ISO/IEC 42001 as a governance anchor, not as a standalone control set
- Pair it with lifecycle, risk, and reliability-focused work when defining
  operational controls
- Track where financial-sector control expectations require more specific
  implementation guidance than management system language alone provides

### Evidence Links

- `mappings/ai-standards-landscape.md`
- `mappings/fintech-controls-mapping.md`

## Entry 2 — ISO/IEC 23894

### Date

2026-06-19

### Standard Reviewed

ISO/IEC 23894 — AI risk management

### Scope Summary

Reviewed the publicly visible positioning of ISO/IEC 23894 as a framework for
identifying, analyzing, evaluating, and treating AI-related risks across the
AI system lifecycle.

### Observations

- The standard is useful for framing reliability, harm, and control failure as
  risk management questions rather than only technical defects.
- It provides a good bridge between AI-specific concerns and enterprise risk
  thinking, especially where governance bodies need structured risk treatment
  logic.
- Its practical value depends heavily on local interpretation because it does
  not define financial-sector operating thresholds, evidence bundles, or
  production escalation rules in sufficient detail.

### Gaps Identified

- Limited operational specificity for residual risk acceptance in live AI
  systems
- Limited guidance on how drift, vendor updates, and LLM behavior should reopen
  risk review
- No clear sector-specific model for connecting AI risk framing with model risk
  management, operational resilience, and regulatory escalation

### Recommendations

- Use ISO/IEC 23894 to structure risk logic, but define local rules for
  trigger-based reassessment and materiality thresholds
- Pair risk treatment with explicit evidence expectations for continued use
  decisions
- Interpret reliability degradation, prompt change, vendor regression, and
  workflow instability as risk events that can reopen governance review

### Evidence Links

- `mappings/ai-standards-landscape.md`
- `mappings/financial-ai-controls-gap-matrix.md`
- `proposals/continuous-reliability-assurance-for-financial-ai.md`

## Entry 3 — ISO/IEC 5338

### Date

2026-06-19

### Standard Reviewed

ISO/IEC 5338 — AI system life cycle processes

### Scope Summary

Reviewed the publicly visible positioning of ISO/IEC 5338 as a lifecycle
process standard covering AI system activities from development through
operation, maintenance, and retirement.

### Observations

- The lifecycle framing is useful because many trust failures in finance arise
  at handoff points between design, validation, deployment, and ongoing
  maintenance.
- The standard supports disciplined process structuring, but does not by itself
  specify how financial institutions should govern frequent retraining,
  externally sourced model changes, or post-deployment revalidation.
- Its strongest contribution is process structure; its weakest area is
  operational specificity for live adaptive systems.

### Gaps Identified

- Limited guidance for retraining governance tiers and evidence requirements
- Limited treatment of monitoring-triggered revalidation in production
- Limited specificity for vendor model updates, emergency fixes, and adaptive
  workflow systems

### Recommendations

- Use ISO/IEC 5338 to define lifecycle checkpoints, then add
  financial-sector-specific stage-gate evidence requirements
- Treat retraining, prompt changes, retrieval changes, and vendor updates as
  lifecycle events that may reopen approval conditions
- Link lifecycle maintenance activities to continuous reliability assurance
  rather than relying only on periodic review

### Evidence Links

- `mappings/ai-standards-landscape.md`
- `mappings/financial-ai-controls-gap-matrix.md`
- `gap-analysis/reliability-gaps.md`
- `proposals/continuous-reliability-assurance-for-financial-ai.md`
- `evidence/index.md`

## Entry 4 — ISO/IEC TS 25570

### Date

2026-06-19

### Standard Reviewed

ISO/IEC TS 25570 — Reliability assessment of AI systems

### Scope Summary

Reviewed the publicly visible positioning of ISO/IEC TS 25570 as a technical
specification focused on reliability assessment for AI systems operating under
intended and changing conditions.

### Observations

- This is the most directly relevant of the reviewed standards for live
  reliability in financial AI.
- It usefully elevates reliability into a distinct assurance concern rather
  than leaving it buried within generic governance or risk language.
- Its practical limitation is that financial institutions still need an
  additional operating model for reassessment triggers, escalation thresholds,
  and evidence expectations in live environments.

### Gaps Identified

- Limited explicit treatment of reliability metrics for adaptive, LLM-based,
  and agentic systems
- Limited guidance on how reliability reassessment should be triggered after
  drift, retraining, incidents, or vendor changes
- No mature decision model for when degradation requires restriction, rollback,
  or formal escalation

### Recommendations

- Use ISO/IEC TS 25570 as the anchor for reliability assessment, but extend it
  with trigger-based continuous assurance logic
- Develop local rules for reliability materiality, intervention thresholds, and
  post-incident reassessment
- Use the specification as a foundation for a broader continuous reliability
  assurance approach in financial AI

### Evidence Links

- `mappings/ai-standards-landscape.md`
- `gap-analysis/reliability-gaps.md`
- `mappings/financial-ai-controls-gap-matrix.md`
- `proposals/continuous-reliability-assurance-for-financial-ai.md`
- `evidence/index.md`

## Entry 5 — Cross-Standard Comparative Synthesis

### Date

2026-06-19

### Standard Reviewed

Comparative analysis of ISO/IEC 42001, ISO/IEC 23894, ISO/IEC 5338, and
ISO/IEC TS 25570

### Scope Summary

Synthesized the four standards against financial AI control domains including
inventory, accountability, validation, runtime monitoring, concept drift,
incident management, audit evidence, third-party AI oversight, LLM governance,
and agentic AI governance.

### Observations

- The four standards are complementary rather than interchangeable: governance,
  risk, lifecycle, and reliability are distributed across them.
- Their combined coverage is still insufficient for several live financial AI
  control problems, especially drift response, retraining governance,
  third-party AI assurance, and governance of LLM or agentic systems.
- The main implementation problem is not selecting the right single standard;
  it is integrating several partial viewpoints into a defensible operational
  control model.

### Gaps Identified

- No integrated cross-standard model for continuous reliability supervision
- No mature doctrine for LLM governance or agentic AI governance
- Limited standards guidance on evidence bundles, trigger-based reassessment,
  and escalation thresholds for live financial AI systems

### Recommendations

- Use the cross-standard matrix as a comparative control tool rather than a
  descriptive landscape only
- Focus future analysis on integrated operating models rather than additional
  high-level summaries
- Prioritize work on continuous assurance, vendor model oversight, and adaptive
  system governance

### Evidence Links

- `mappings/financial-ai-controls-gap-matrix.md`
- `mappings/fintech-controls-mapping.md`
- `gap-analysis/reliability-gaps.md`
- `evidence/index.md`

## Entry 6 — Continuous Reliability Assurance Proposal

### Date

2026-06-19

### Standard Reviewed

Cross-standard proposal: Continuous Reliability Assurance (CRA) for financial
AI

### Scope Summary

Developed an original proposal for Continuous Reliability Assurance as an
operational layer connecting governance, risk management, lifecycle control,
and reliability assessment for live financial AI systems.

### Observations

- Existing standards contain important building blocks but do not provide a
  sufficiently explicit model for trigger-based reliability reassessment in
  dynamic environments.
- Financial AI systems increasingly require assurance models that can respond
  to concept drift, vendor updates, retraining, LLM behavior changes, and
  agentic workflow instability.
- CRA is best understood not as a replacement standard, but as an integration
  proposal for applying existing standards to live-system supervision.

### Gaps Identified

- Missing standardised trigger taxonomy for reassessment in production
- Missing common evidence bundle for continued-use decisions after live changes
- Missing escalation model linking reliability deterioration to governance
  action and operational restriction

### Recommendations

- Use CRA as a candidate conceptual contribution for future standards or
  technical report development
- Test CRA against concrete financial AI use cases such as credit decisioning,
  fraud detection, AML monitoring, LLM assistants, and agentic workflows
- Develop follow-on work defining metrics, thresholds, and example evidence
  packs for real institutional deployment

### Evidence Links

- `proposals/continuous-reliability-assurance-for-financial-ai.md`
- `mappings/financial-ai-controls-gap-matrix.md`
- `gap-analysis/reliability-gaps.md`
- `evidence/index.md`

## Entry 7 — BSI ART/1 Engagement and Public Dissemination

### Date

2026-07-22

### Standard Reviewed

Engagement activity: BSI ART/1, the UK national mirror committee to ISO/IEC
JTC 1/SC 42 (Artificial intelligence)

### Scope Summary

Followed up the BSI observer registration with a formal email submission of
two repository documents — the Continuous Reliability Assurance (CRA)
proposal and the financial-AI controls gap matrix — as technical input to the
committee, with the StandICT.eu 2029 fellowship funding openly declared.
Published a public technical article summarising the fellowship analysis.

### Observations

- CRA proposal and controls gap matrix transmitted to BSI as PDF attachments,
  with links to the canonical repository versions.
- Confirmation of observer status, the next committee or panel meeting date,
  and guidance on the appropriate contribution route into SC 42 work were
  requested.
- Dissemination article published 22 July 2026: "Four ISO Standards, One
  Missing Layer: Trustworthy AI in Financial Services"
  (https://medium.com/@santhosh.kbr/four-iso-standards-one-missing-layer-trustworthy-ai-in-financial-services-7ec5d1f58845).

### Gaps Identified

- Formal contribution routing into SC 42 via national mirror committee
  processes remains pending BSI guidance.

### Recommendations

- Attend the next available ART/1 meeting (virtually) and present the CRA
  proposal.
- Record contribution identifiers in this log when assigned.

### Evidence Links

- `proposals/continuous-reliability-assurance-for-financial-ai.md`
- `mappings/financial-ai-controls-gap-matrix.md`
- `evidence/index.md` (EVID-2026-07-22-009)

## Reusable Entry Template

Copy the structure below for each additional review.

```markdown
## Entry Title

### Date

YYYY-MM-DD

### Standard Reviewed

Standard name or initiative

### Scope Summary

Short summary based on public information only

### Observations

- Observation 1
- Observation 2
- Observation 3

### Gaps Identified

- Gap 1
- Gap 2

### Recommendations

- Recommendation 1
- Recommendation 2

### Evidence Links

- Path or URL
- Path or URL
```
