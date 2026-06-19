# AI Standards Landscape

## Purpose of This Document

This document summarizes a selected set of AI standards and initiatives that
are relevant to trustworthy AI implementation in financial services. The
analysis is based on publicly visible descriptions and original interpretation
for sector use.

## ISO/IEC 42001

### Purpose

ISO/IEC 42001 provides an organizational management system framework for AI.
Its practical value lies in defining how responsibility, policy, oversight,
and continual improvement can be organized at enterprise level.

### Scope

The standard addresses governance structures, documented processes, and
control expectations for organizations that develop, provide, or use AI
systems.

### Relationship to Trustworthy AI

Trustworthy AI depends on accountability and repeatable governance. ISO/IEC
42001 is important because it frames those foundations. It supports
trustworthy AI indirectly by establishing management discipline rather than by
specifying detailed technical metrics.

### Relevance to Financial Services

Financial firms need a consistent governance layer across many models,
suppliers, business units, and risk owners. ISO/IEC 42001 is therefore
relevant as a common operating framework for AI ownership, decision rights,
documentation, internal review, and escalation.

### Relationship with Other Standards

ISO/IEC 42001 works best as the top-level organizational framework that is
paired with more specialized standards:

- with ISO/IEC 23894 for structured AI risk treatment
- with ISO/IEC 5338 for lifecycle process definition
- with ISO/IEC TS 25570 for reliability-oriented evaluation questions

## ISO/IEC 23894

### Purpose

ISO/IEC 23894 addresses AI risk management. It helps organizations identify,
analyze, evaluate, and treat AI-related risks in a systematic way.

### Scope

Its scope is risk-oriented rather than sector-specific. It frames categories
of AI risk and risk process expectations, but does not attempt to define
complete operational controls for every deployment context.

### Relationship to Trustworthy AI

Trustworthy AI requires explicit treatment of safety, fairness, reliability,
security, and governance risks. ISO/IEC 23894 is directly relevant because it
encourages structured identification of those issues and supports clear
decision-making around residual risk.

### Relevance to Financial Services

Financial institutions face model risk, customer impact, fraud pressure,
market volatility, and regulatory scrutiny. ISO/IEC 23894 provides a useful
bridge between enterprise risk management and AI-specific risk assessment,
especially when aligning technical findings with governance decisions.

### Relationship with Other Standards

ISO/IEC 23894 complements:

- ISO/IEC 42001 by supplying risk-oriented content within a management system
- ISO/IEC 5338 by informing risk checkpoints across the lifecycle
- reliability-oriented work by helping determine what must be monitored and
  escalated in production

## ISO/IEC 5338

### Purpose

ISO/IEC 5338 focuses on AI system life cycle processes. It is relevant where
organizations need disciplined transitions from design through deployment,
operation, maintenance, and retirement.

### Scope

The standard addresses lifecycle activities, process interfaces, and
engineering discipline for AI systems. It does not replace governance or risk
frameworks, but provides structure for execution.

### Relationship to Trustworthy AI

Many trust failures arise at lifecycle boundaries: unclear data ownership,
weak validation handoffs, poor deployment controls, or unmanaged changes.
ISO/IEC 5338 supports trustworthy AI by improving process integrity across
those boundaries.

### Relevance to Financial Services

Financial-sector ML systems often have long operational lives, recurring model
refreshes, layered approvals, and strong expectations for change control.
Lifecycle clarity is therefore essential for reproducibility, auditability,
and incident investigation.

### Relationship with Other Standards

ISO/IEC 5338 links naturally to:

- ISO/IEC 42001 for governance and management accountability
- ISO/IEC 23894 for lifecycle risk assessment and treatment
- reliability assessment work for determining what evidence should be produced
  at deployment and operation stages

## ISO/IEC TS 25570

### Purpose

ISO/IEC TS 25570 addresses reliability assessment of AI systems. Its value is
in focusing attention on whether AI systems behave dependably under intended
and changing operational conditions.

### Scope

The technical specification addresses reliability-related assessment ideas for
AI systems. It is particularly relevant where static model evaluation is not
enough and production behavior must be examined more carefully.

### Relationship to Trustworthy AI

Reliability is one of the most practical dimensions of trustworthy AI because
it shapes whether systems continue to operate within expected bounds.
Trustworthy AI claims are weak if organizations cannot define, measure, and
review reliability over time.

### Relevance to Financial Services

This is highly relevant to finance because production environments change
rapidly. Fraud patterns evolve, market conditions shift, customer populations
move, and operational dependencies fail in combination. Reliability assessment
must therefore be dynamic, not only pre-deployment.

### Relationship with Other Standards

ISO/IEC TS 25570 can be seen as an operational deepening layer:

- under ISO/IEC 42001 governance expectations
- informed by ISO/IEC 23894 risk prioritization
- embedded into ISO/IEC 5338 lifecycle checkpoints

## AI Quality Model Initiatives

### Purpose

AI quality model initiatives attempt to make AI assurance more measurable by
defining characteristics such as robustness, explainability, maintainability,
data quality, or usability in a structured way.

### Scope

These initiatives are typically cross-cutting. They do not replace management
or lifecycle standards, but provide quality dimensions that can shape metrics
and evaluation plans.

### Relationship to Trustworthy AI

Trustworthy AI needs operational definitions. Quality models help translate
abstract trust properties into characteristics that can be measured, reviewed,
and improved.

### Relevance to Financial Services

Financial firms need quality characteristics that map to business materiality.
Examples include input data integrity, output stability, calibration quality,
human review usability, and evidence completeness for audit.

### Relationship with Other Standards

Quality models can strengthen:

- ISO/IEC 42001 control design by clarifying what must be governed
- ISO/IEC 23894 risk treatment by making risk indicators more concrete
- ISO/IEC TS 25570 reliability assessment by supporting measurable attributes

## Green and Sustainable AI Initiatives

### Purpose

Green and sustainable AI initiatives focus on energy efficiency, hardware
usage, carbon impact, and resource-aware system design.

### Scope

The scope is broader than climate reporting alone. It includes design choices
that affect operational efficiency, deployment architecture, model size, and
lifecycle maintenance burden.

### Relationship to Trustworthy AI

Sustainability is not separate from trust. Inefficient systems can create
operational fragility, excessive infrastructure dependence, and poor scaling
decisions. Sustainable design can therefore support resilience and governance
quality.

### Relevance to Financial Services

Financial institutions increasingly run large inference estates, vendor model
services, and latency-sensitive decision pipelines. Sustainable AI matters in
cost control, operational resilience, vendor oversight, and procurement
choices.

### Relationship with Other Standards

Sustainability initiatives intersect with the other standards by influencing:

- governance decisions about acceptable deployment patterns
- lifecycle decisions about retraining and infrastructure design
- reliability tradeoffs where efficiency, latency, and resilience interact

## Cross-Cutting Interpretation

The selected standards and initiatives are complementary rather than
interchangeable:

- ISO/IEC 42001 answers how the organization governs AI
- ISO/IEC 23894 answers how AI risk is framed and treated
- ISO/IEC 5338 answers how lifecycle processes are structured
- ISO/IEC TS 25570 helps answer how reliability is assessed in operation
- quality and sustainability initiatives help answer what should be measured
  and optimized

For financial services, the main implementation challenge is integration. The
technical problem is not choosing one standard, but constructing a coherent
control system from several partial viewpoints.

