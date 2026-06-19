# Financial AI Controls Gap Matrix

## Purpose

This document compares four AI standards against control domains that matter in
financial AI implementation:

- ISO/IEC 42001
- ISO/IEC 23894
- ISO/IEC 5338
- ISO/IEC TS 25570

The goal is not to restate what each standard is about. The goal is to
identify where they help, where they overlap, and where they remain
insufficient for financial institutions that need defensible governance,
runtime assurance, and audit-ready evidence for live AI systems.

## How to Read This Matrix

The coverage ratings below assess **practical control usefulness** for
financial institutions, not formal conformance potential.

- **Strong Coverage:** the standard addresses the domain in a sufficiently
  direct way to support control design
- **Partial Coverage:** the standard contributes meaningfully, but leaves major
  implementation questions open
- **Limited Coverage:** the standard is only indirectly useful or only covers a
  narrow slice of the domain
- **No Explicit Coverage:** the domain is not directly treated as a distinct
  control problem

## Coverage Matrix

| Control Domain | ISO/IEC 42001 | ISO/IEC 23894 | ISO/IEC 5338 | ISO/IEC TS 25570 |
| --- | --- | --- | --- | --- |
| Model inventory and classification | Partial Coverage | Partial Coverage | Partial Coverage | Limited Coverage |
| Accountability and ownership | Strong Coverage | Partial Coverage | Partial Coverage | Limited Coverage |
| Model validation | Partial Coverage | Partial Coverage | Partial Coverage | Partial Coverage |
| Reliability assessment | Limited Coverage | Partial Coverage | Partial Coverage | Strong Coverage |
| Runtime monitoring | Partial Coverage | Partial Coverage | Partial Coverage | Partial Coverage |
| Concept drift management | Limited Coverage | Partial Coverage | Limited Coverage | Partial Coverage |
| Retraining governance | Partial Coverage | Partial Coverage | Partial Coverage | Limited Coverage |
| Incident management | Partial Coverage | Partial Coverage | Limited Coverage | Limited Coverage |
| Audit evidence | Strong Coverage | Partial Coverage | Partial Coverage | Limited Coverage |
| Third-party AI oversight | Partial Coverage | Partial Coverage | Partial Coverage | Limited Coverage |
| LLM governance | Limited Coverage | Limited Coverage | Limited Coverage | No Explicit Coverage |
| Agentic AI governance | Limited Coverage | Limited Coverage | Limited Coverage | No Explicit Coverage |

## Comparative Analysis by Control Domain

### Model Inventory and Classification

**Coverage**

- **ISO/IEC 42001:** supports inventory discipline indirectly because
  governance cannot operate without knowing which AI systems are in scope.
- **ISO/IEC 23894:** supports risk-based classification logic, but not a
  concrete inventory design.
- **ISO/IEC 5338:** supports system definition across the lifecycle, which
  helps identify what is being developed and maintained.
- **ISO/IEC TS 25570:** has limited value here because it assumes a system is
  already identified and moves quickly toward reliability assessment.

**Where standards overlap**

- `42001`, `23894`, and `5338` all require some way to define the AI system
  being governed, assessed, or maintained.
- None of them gives a financial institution a ready-made classification model
  for high-impact, adaptive, or externally sourced AI systems.

**Gaps, ambiguities, and under-specified areas**

- No standard clearly distinguishes:
  - analytical models
  - customer-facing decision systems
  - LLM assistants
  - embedded vendor AI
  - multi-model or agentic workflows
- None gives enough guidance on whether classification should be based on:
  - use case criticality
  - customer impact
  - autonomy level
  - retraining behavior
  - regulatory sensitivity

**Practical implications for financial institutions**

Without a stronger classification model, firms tend to either over-classify
everything as high risk or under-classify modern systems that do not resemble
traditional models. Both outcomes are expensive: the first creates governance
drag, and the second creates control blind spots.

**Original recommendation**

Use the standards as a baseline, but create an internal financial-AI taxonomy
that classifies systems by:

- decision impact
- autonomy level
- adaptivity level
- use of external models or tools
- customer and regulatory sensitivity

The classification scheme should drive governance depth, validation scope, and
monitoring intensity.

### Accountability and Ownership

**Coverage**

- **ISO/IEC 42001:** provides the strongest basis because management system
  discipline depends on assigning roles, authority, and review mechanisms.
- **ISO/IEC 23894:** contributes through risk ownership and risk treatment
  accountability.
- **ISO/IEC 5338:** contributes through lifecycle role definition and handoff
  discipline.
- **ISO/IEC TS 25570:** has only limited coverage because it assumes
  assessment responsibility but does not anchor enterprise governance.

**Where standards overlap**

- `42001`, `23894`, and `5338` all imply that responsibilities must be
  allocated across governance, risk, and execution.
- All three stop short of defining how ownership should be split between
  product, engineering, model risk, compliance, and operations teams.

**Gaps, ambiguities, and under-specified areas**

- No standard resolves who owns live reliability once a model leaves
  development.
- No standard clearly distinguishes ownership for:
  - model performance
  - policy compliance
  - retraining decisions
  - incident response
  - vendor escalation
- The standards are especially weak on ownership in composite systems where one
  business process depends on several models, retrieval layers, and
  orchestration logic.

**Practical implications for financial institutions**

In practice, accountability gaps appear at production boundaries. First-line
teams may own delivery, second-line teams may own challenge, and operations may
own incidents, but no one owns the combined assurance problem. That becomes
acute in fraud, customer communications, and AI-supported operations.

**Original recommendation**

Define accountability at three levels:

- **system owner** for business acceptability and control funding
- **technical owner** for performance, monitoring, and change discipline
- **control owner** for independent challenge, policy interpretation, or
  regulatory alignment

Financial institutions should not rely on a single “model owner” construct for
modern AI systems.

### Model Validation

**Coverage**

- **ISO/IEC 42001:** supports validation governance, documentation, and review
  expectations, but not validation methods.
- **ISO/IEC 23894:** helps identify what should be validated from a risk
  perspective.
- **ISO/IEC 5338:** contributes lifecycle structure for verification and
  validation activities.
- **ISO/IEC TS 25570:** contributes reliability-oriented testing logic, but not
  full validation doctrine.

**Where standards overlap**

- `23894` and `5338` overlap around the idea that lifecycle checkpoints should
  reflect risk.
- `42001` and `5338` overlap on procedural discipline and record keeping.
- `TS 25570` overlaps with validation only where reliability is a material part
  of the validation case.

**Gaps, ambiguities, and under-specified areas**

- No standard provides enough operational specificity for validation of:
  - adaptive models
  - LLM-based assistants
  - retrieval-augmented systems
  - agentic workflows
- There is limited guidance on when validation must be re-opened because of:
  - drift
  - prompt changes
  - tool changes
  - vendor model updates
- None of the standards gives a strong answer to the financial-sector question:
  “what evidence is sufficient to allow continued use?”

**Practical implications for financial institutions**

Firms can satisfy process expectations while still having weak substantive
validation. The result is a validation function that approves documentation
rather than testing whether the deployed system remains acceptable.

**Original recommendation**

Build a validation model with three distinct layers:

- **design validation** before deployment
- **production validation** after initial live exposure
- **change-triggered revalidation** for material model, prompt, tool, or data
  changes

This is where the standards should be extended, not merely adopted.

### Reliability Assessment

**Coverage**

- **ISO/IEC 42001:** provides only indirect support by making reliability part
  of governance expectations.
- **ISO/IEC 23894:** helps prioritize reliability as a risk issue.
- **ISO/IEC 5338:** creates lifecycle insertion points for reliability
  activities.
- **ISO/IEC TS 25570:** is the strongest direct source because it focuses on
  reliability assessment as a distinct concern.

**Where standards overlap**

- `23894` and `TS 25570` overlap where risk significance determines what
  reliability evidence matters.
- `5338` and `TS 25570` overlap where lifecycle checkpoints need reliability
  evidence.
- `42001` overlaps with all of them only at the governance layer.

**Gaps, ambiguities, and under-specified areas**

- `TS 25570` is still not enough on its own for financial institutions because
  it does not fully resolve:
  - reliability metrics for adaptive systems
  - thresholds for acceptable degradation
  - relationships between reliability and business continuity
  - reliability evidence after production incidents
- The standards set does not yet distinguish clearly between:
  - prediction reliability
  - workflow reliability
  - operational reliability
  - human-in-the-loop reliability

**Practical implications for financial institutions**

Financial institutions need reliability assessment that can be challenged by
governance forums and translated into intervention decisions. Generic
statements about reliability are not enough when customer outcomes, fraud loss,
or operational resilience are affected.

**Original recommendation**

Define reliability in financial-AI terms as a monitored control outcome with:

- leading indicators
- materiality thresholds
- intervention triggers
- post-incident reassessment rules

That interpretation should sit on top of `TS 25570`, not be expected to emerge
from it automatically.

### Runtime Monitoring

**Coverage**

- **ISO/IEC 42001:** supports monitoring at the management-system level but not
  detailed runtime practice.
- **ISO/IEC 23894:** supports monitoring through risk detection and treatment
  logic.
- **ISO/IEC 5338:** contributes operational checkpoints and maintenance
  discipline.
- **ISO/IEC TS 25570:** contributes to monitoring where runtime evidence is
  needed for reliability assessment.

**Where standards overlap**

- All four standards support the idea that monitoring matters.
- None of them provides a sufficiently concrete runtime monitoring model for
  modern financial AI systems.

**Gaps, ambiguities, and under-specified areas**

- The standards do not adequately distinguish:
  - health monitoring
  - performance monitoring
  - drift monitoring
  - control-effectiveness monitoring
  - workflow monitoring
- There is little guidance on alert design, escalation thresholds, or minimum
  telemetry requirements for vendor AI services.

**Practical implications for financial institutions**

Institutions often end up with dashboards that show movement but do not trigger
decisions. Monitoring becomes observational rather than supervisory. That is
especially weak for systems that can deteriorate before headline metrics fail.

**Original recommendation**

Design runtime monitoring around decisions, not metrics alone. For each
monitored signal, define:

- owner
- review frequency
- escalation threshold
- remediation action
- evidence retention requirement

This is a practical extension that the standards imply but do not specify.

### Concept Drift Management

**Coverage**

- **ISO/IEC 42001:** provides only indirect support because drift is a control
  issue within governance, not a separately treated domain.
- **ISO/IEC 23894:** contributes risk framing for changing conditions.
- **ISO/IEC 5338:** provides limited lifecycle support for maintenance and
  change handling.
- **ISO/IEC TS 25570:** contributes to drift questions where reliability under
  changing operating conditions is central.

**Where standards overlap**

- `23894` and `TS 25570` are the most useful pair here: one frames the risk,
  the other supports assessment thinking.
- `5338` contributes only if firms treat drift as a lifecycle event that
  should reopen review and change processes.

**Gaps, ambiguities, and under-specified areas**

- No standard gives a strong operating model for:
  - detecting concept drift
  - quantifying business impact
  - deciding when drift becomes material
  - distinguishing temporary noise from structural change
  - assigning accountability for drift-triggered intervention
- There is also no sector-specific guidance for market regime changes, fraud
  adaptation, or customer behavior shifts.

**Practical implications for financial institutions**

Drift is one of the most material live risks in finance. If standards do not
translate into intervention rules, firms either react too slowly or overreact
to normal variation. Both create governance problems.

**Original recommendation**

Treat concept drift as a governance event, not just a technical metric. Firms
should define:

- drift types
- drift thresholds
- review triggers
- permitted interim mitigations
- mandatory revalidation conditions

That control model is missing from the standards and must be added locally.

### Retraining Governance

**Coverage**

- **ISO/IEC 42001:** supports change governance and documented control.
- **ISO/IEC 23894:** helps justify retraining decisions through risk treatment.
- **ISO/IEC 5338:** supports retraining as a lifecycle change activity.
- **ISO/IEC TS 25570:** offers only limited support because retraining is not
  principally a reliability framework question, though it affects reliability.

**Where standards overlap**

- `42001`, `23894`, and `5338` all contribute to the idea that retraining must
  be governed, justified, and documented.
- None of them says enough about how to govern frequent or semi-automated
  retraining in a live financial environment.

**Gaps, ambiguities, and under-specified areas**

- No clear standard answer exists for:
  - what counts as a material retraining event
  - when retraining can be pre-approved
  - what evidence is required before promotion
  - how cumulative low-level changes should be governed
  - how retraining interacts with independent validation

**Practical implications for financial institutions**

This is where many firms face real tension between model performance and
governance discipline. Standards support process thinking, but not the
operating thresholds needed for rapid production environments.

**Original recommendation**

Create retraining tiers such as:

- **minor refresh**
- **parameter or data refresh**
- **material model change**
- **architecture or supplier change**

Each tier should have predefined evidence, approval, and rollback
requirements.

### Incident Management

**Coverage**

- **ISO/IEC 42001:** provides the strongest general governance basis for
  corrective action and management review.
- **ISO/IEC 23894:** contributes through severity framing and treatment logic.
- **ISO/IEC 5338:** contributes only indirectly through maintenance and change
  processes.
- **ISO/IEC TS 25570:** contributes only where incident analysis is used to
  reassess reliability.

**Where standards overlap**

- `42001` and `23894` overlap around the need to treat failures as governance
  and risk events.
- All four standards remain weaker on operational incident response than on
  design-time discipline.

**Gaps, ambiguities, and under-specified areas**

- The standards do not sufficiently specify:
  - AI incident categories
  - severity models for degraded behavior
  - customer-impact escalation
  - links to business continuity or operational resilience
  - evidence expectations after incident closure

**Practical implications for financial institutions**

Firms often have strong general incident processes but weak AI-specific
triggering logic. That means AI failures can remain classified as technical
noise even when they should trigger governance escalation.

**Original recommendation**

Define AI incident categories separately from generic technology incidents, for
example:

- performance degradation
- harmful output event
- drift-driven instability
- vendor model regression
- agent action control breach

That taxonomy should determine escalation, remediation, and post-incident
review.

### Audit Evidence

**Coverage**

- **ISO/IEC 42001:** offers the strongest foundation because management systems
  require documented processes, records, and review discipline.
- **ISO/IEC 23894:** contributes risk records and treatment rationale.
- **ISO/IEC 5338:** contributes lifecycle artifacts and change history.
- **ISO/IEC TS 25570:** contributes only limited evidence expectations focused
  on reliability assessment rather than full assurance records.

**Where standards overlap**

- `42001`, `23894`, and `5338` all reinforce that evidence should exist.
- None of them gives a financial institution a concrete audit packet design for
  modern AI services.

**Gaps, ambiguities, and under-specified areas**

- The standards do not specify minimum evidence bundles for:
  - deployment approval
  - retraining approval
  - vendor AI acceptance
  - LLM prompt changes
  - incident closure
- They also do not clarify how long reliability evidence should remain
  decision-usable after system changes.

**Practical implications for financial institutions**

Auditability often fails not because evidence does not exist, but because it is
fragmented across engineering, MLOps, product, and risk tools. Standards
conformance alone will not solve this fragmentation.

**Original recommendation**

Define standard evidence bundles for each control milestone, including:

- system classification record
- validation record
- change approval record
- monitoring thresholds
- incident history
- vendor assurance record

That operating discipline is far more important than generic “retain records”
language.

### Third-Party AI Oversight

**Coverage**

- **ISO/IEC 42001:** supports governance over providers and externally sourced
  systems as part of overall management responsibility.
- **ISO/IEC 23894:** supports assessment of externally introduced risks.
- **ISO/IEC 5338:** supports lifecycle controls where third-party components
  affect development, maintenance, and change.
- **ISO/IEC TS 25570:** is of limited use unless institutions can actually
  obtain reliability evidence from providers.

**Where standards overlap**

- `42001`, `23894`, and `5338` all imply that outsourced AI does not remove
  accountability.
- None of them sufficiently resolves the asymmetry between institution-level
  accountability and provider-level visibility.

**Gaps, ambiguities, and under-specified areas**

- There is limited guidance on:
  - minimum provider evidence
  - update notification expectations
  - black-box reliability assurance
  - shared responsibility models
  - vendor incident notification and joint remediation

**Practical implications for financial institutions**

Third-party AI is often where standards become hardest to operationalize. Firms
remain accountable for outcomes even when they do not control the model, the
training data, or the release cycle.

**Original recommendation**

Create a dedicated vendor-AI assurance standard internally with minimum
requirements for:

- update notice
- validation support
- reliability reporting
- drift-relevant telemetry
- incident escalation
- contractual evidence access

This is a gap that the current standards do not close.

### LLM Governance

**Coverage**

- **ISO/IEC 42001:** offers limited but still useful governance structure.
- **ISO/IEC 23894:** offers limited but useful risk framing.
- **ISO/IEC 5338:** offers limited lifecycle structure.
- **ISO/IEC TS 25570:** has no explicit LLM governance treatment.

**Where standards overlap**

- The three broader standards can all be extended to LLM systems by analogy.
- None of them was built around prompt-based, retrieval-dependent, externally
  updated systems with fluid task boundaries.

**Gaps, ambiguities, and under-specified areas**

- No explicit treatment exists for:
  - prompt governance
  - context-window dependence
  - retrieval quality dependency
  - output grounding expectations
  - hallucination management
  - provider model version changes
- Existing standards help with governance form, but not with LLM-specific
  control content.

**Practical implications for financial institutions**

Firms that treat LLMs as ordinary models will under-govern them. The control
problem is broader because behavior depends on prompt policy, retrieval
quality, tool access, and provider updates, not only model weights.

**Original recommendation**

Add an LLM-specific control layer covering:

- prompt inventory
- prompt change approval
- retrieval-source governance
- response-risk categorization
- human review thresholds
- provider update impact assessment

This is a clear standards gap with immediate sector relevance.

### Agentic AI Governance

**Coverage**

- **ISO/IEC 42001:** offers limited governance support at organizational level.
- **ISO/IEC 23894:** offers limited support through risk framing.
- **ISO/IEC 5338:** offers limited lifecycle structure for composite systems.
- **ISO/IEC TS 25570:** has no explicit coverage of agentic governance.

**Where standards overlap**

- The standards can be extended to agents only at a very high level.
- None directly addresses delegated action authority, tool chaining, or
  workflow emergence.

**Gaps, ambiguities, and under-specified areas**

- No explicit standard answer exists for:
  - bounded action authority
  - tool permission control
  - workflow traceability
  - plan-to-action accountability
  - approval gates for semi-autonomous operations
  - failure handling in multi-step AI actions

**Practical implications for financial institutions**

Agentic systems are not just “stronger models.” They change the control
surface. The governance problem moves from output review to action governance,
execution traceability, and bounded delegation. Current standards are too
general to handle that directly.

**Original recommendation**

Treat agentic systems as a separate governance class with explicit controls
for:

- action authorization
- tool-level permissions
- execution logging
- fail-safe behavior
- human override design
- post-action review

This is one of the most important forward-looking gaps in the current
standards landscape.

## Cross-Standard Synthesis

The comparison shows a consistent pattern:

- **ISO/IEC 42001** is strongest at governance structure and documentary
  accountability
- **ISO/IEC 23894** is strongest at framing risk treatment questions
- **ISO/IEC 5338** is strongest at lifecycle structuring
- **ISO/IEC TS 25570** is strongest at making reliability a distinct subject

The problem for financial institutions is that the real control domains do not
line up neatly with those boundaries. Runtime assurance, drift response,
retraining decisions, vendor oversight, and LLM or agentic control design all
cut across the four standards simultaneously. That is why “adopting a
standard” is not the same thing as having an adequate control framework.

## Key Gaps in Current AI Standards for Financial Services

### 1. Weak integration between governance and runtime assurance

The standards collectively explain how AI should be governed, assessed, and
maintained, but they do not provide an integrated control model for live
systems that degrade, adapt, or depend on changing external services.

**Recommendation**

Financial institutions should define a continuous-assurance layer that links:

- monitoring
- incident thresholds
- drift triggers
- revalidation
- retraining approval

That layer should be treated as a first-class control construct.

### 2. Insufficient treatment of adaptive behavior

The standards are materially stronger for relatively stable systems than for
continually updated, rapidly retrained, or highly context-dependent systems.

**Recommendation**

Create internal control rules that distinguish:

- stable systems
- periodically refreshed systems
- continuously tuned systems
- externally updated systems

Each class should have different approval, evidence, and rollback rules.

### 3. No mature doctrine for LLM and agentic governance

Current standards can be applied to LLMs and agents, but only indirectly. They
do not yet express the distinctive control problems of prompt dependence,
retrieval dependence, tool use, or delegated action.

**Recommendation**

Develop a local policy extension for:

- prompt governance
- retrieval governance
- tool-use control
- action authority
- human override rules
- provider update review

This should be treated as a strategic extension area, not an optional detail.

### 4. Limited operational guidance for third-party AI assurance

The standards recognize organizational responsibility, but they do not solve
the visibility gap between institutions and providers.

**Recommendation**

Financial institutions should define minimum provider evidence requirements and
contractual control expectations before production use. In practice, this is
often more important than the internal standards mapping itself.

### 5. Under-specified evidence expectations for audit and supervision

The standards support record keeping, but do not provide enough detail on what
evidence must exist to defend production decisions in regulated environments.

**Recommendation**

Create predefined evidence bundles for:

- onboarding
- validation
- deployment
- retraining
- incident response
- retirement

Evidence design should be treated as a control architecture problem rather than
an afterthought.

### 6. No clear control model for concept drift in financial environments

Concept drift is a central operational problem in finance, yet the standards do
not define sufficiently concrete intervention models or materiality thresholds.

**Recommendation**

Institutionalize drift governance with named drift categories, thresholds,
review forums, and required actions. Without this, standards compliance will
not produce reliable production control.

## Final View

For financial services, the most important conclusion is that the four
standards are **complementary but not collectively sufficient**. They help
establish governance discipline, risk framing, lifecycle structure, and
reliability attention. They do not yet provide a complete operating model for
adaptive, externally dependent, or semi-autonomous AI systems in regulated
environments.

The main original implication is therefore this: the next frontier is not
another generic AI governance statement. It is a more explicit standards-based
control model for **continuous assurance, live reliability, delegated
autonomy, and evidence-driven financial oversight**.
