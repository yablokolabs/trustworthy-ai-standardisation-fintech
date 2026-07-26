# Trustworthy AI Standardisation for Financial Services

## Project Overview

This repository is a public technical artifact for practical work on
trustworthy AI standardisation in financial services. It consolidates
implementation guidance, standards mappings, gap analysis, and
recommendations that can be reused across fellowship reporting, technical
engagement, and open-source dissemination.

The central objective is to translate high-level AI standardisation work into
concrete engineering, governance, and assurance practices that are useful for
financial institutions, fintech companies, supervisors, auditors, and
standards participants.

## StandICT.eu 2029 Fellowship Context

This repository supports the StandICT.eu 2029 Fellowship project
**AI Standardisation for Trustworthy ML Systems in FinTech**.

It is designed as a living project record that can capture:

- standards reviews and structured observations
- technical interpretations relevant to financial services
- gap analysis for emerging AI system types
- recommendations for future standardisation work
- evidence supporting final fellowship reporting and dissemination

## Why Trustworthy AI Matters

Financial services use AI in environments where model outputs can influence
credit decisions, fraud controls, market behavior, customer treatment,
capital allocation, and operational resilience. Trustworthy AI therefore
requires more than model accuracy.

Practical assurance in this sector depends on:

- clear accountability across the model lifecycle
- reliable behavior under data, market, and policy change
- traceable controls for monitoring, escalation, and remediation
- proportionate governance for high-impact use cases
- defensible evidence for internal oversight and external scrutiny

## Standards Landscape

The repository focuses on a set of standards and initiatives that are highly
relevant to trustworthy AI implementation:

- **ISO/IEC 42001** for AI management systems and organizational governance
- **ISO/IEC 23894** for AI risk management concepts and processes
- **ISO/IEC 5338** for AI system life cycle processes
- **ISO/IEC TS 25570** for reliability assessment of AI systems
- AI quality model initiatives relevant to measurable assurance
- green and sustainable AI initiatives relevant to operational design choices

The analysis does not reproduce copyrighted standards text. It uses publicly
available scope descriptions and develops original implementation guidance.

## Financial Services Focus

The financial sector raises a specific set of challenges for AI
standardisation:

- regulated decision environments with strong audit expectations
- frequent concept drift driven by markets, customer behavior, and fraud
- portfolios of interconnected models rather than isolated systems
- growing use of LLMs, copilots, and agentic workflows in operations
- high dependence on evidence, governance, and incident response discipline

The repository therefore emphasizes operational controls that can be
implemented within risk, compliance, engineering, and model governance
functions.

## Repository Structure

```text
trustworthy-ai-standardisation-fintech/
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   └── fellowship-overview.md
├── proposals/
│   └── continuous-reliability-assurance-for-financial-ai.md
├── mappings/
│   ├── ai-standards-landscape.md
│   ├── financial-ai-controls-gap-matrix.md
│   └── fintech-controls-mapping.md
├── gap-analysis/
│   └── reliability-gaps.md
├── recommendations/
│   └── future-standardisation-directions.md
├── examples/
│   ├── README.md
│   ├── schema/
│   │   └── cra-evidence-bundle.schema.json
│   ├── python/
│   │   └── cra_eval.py
│   └── samples/
├── notes/
│   ├── standards-review-log.md
│   └── dissemination-log.md
├── evidence/
│   ├── README.md
│   └── index.md
└── assets/
```

### Key documents

- [Continuous Reliability Assurance proposal](proposals/continuous-reliability-assurance-for-financial-ai.md)
  — the central original contribution: a trigger taxonomy, evidence bundle,
  escalation model, and ownership split for live financial AI supervision
- [Financial AI controls gap matrix](mappings/financial-ai-controls-gap-matrix.md)
  — cross-standard coverage assessment against financial AI control domains
- [Reliability gap analysis](gap-analysis/reliability-gaps.md)
  — targeted gaps for adaptive, LLM-based, and agentic system forms
- [CRA reference implementation](examples/README.md)
  — the proposal expressed as a JSON Schema and a runnable evaluator
- [Standards review log](notes/standards-review-log.md) and
  [dissemination log](notes/dissemination-log.md) — the working project record

## Deliverables

The repository contents provide:

- a fellowship overview and dissemination framing
- a standards landscape assessment for selected AI standards
- a controls mapping for financial services implementation
- a targeted reliability gap analysis for newer AI system forms
- the Continuous Reliability Assurance proposal as an original contribution
- a runnable reference implementation of that proposal
- future standardisation recommendations with actionable work items
- an evidence management note and private evidence index for reporting
- a reusable standards review log and a dissemination log

## Reference Implementation

The CRA proposal is accompanied by a small, dependency-free reference
implementation in [`examples/`](examples/README.md) so the model can be
executed and tested rather than only read:

- a [JSON Schema](examples/schema/cra-evidence-bundle.schema.json) for the
  minimum CRA evidence bundle, encoding the A-E trigger taxonomy, materiality
  classes, and required ownership split
- an [evaluator](examples/python/cra_eval.py) that scores the six threshold
  design factors, recommends an escalation level from 1 to 5, and reports
  conformance findings such as collapsed ownership or an understated level
- five [sample bundles](examples/samples) covering credit decisioning, fraud
  detection, LLM assistants, and agentic payment workflows, one of which is
  deliberately non-conformant to demonstrate the checks

```bash
cd examples/python
python3 cra_eval.py ../samples/*.json
python3 cra_eval.py --selftest
```

The scoring weights are an inspectable default rather than a recommendation,
and the [known limitations](examples/README.md#known-limitations) are stated
explicitly. Python 3.8+, standard library only.

## Dissemination

Primary article, published 22 Jul 2026:

- [Four ISO Standards, One Missing Layer: Trustworthy AI in Financial
  Services](https://medium.com/@santhosh.kbr/four-iso-standards-one-missing-layer-trustworthy-ai-in-financial-services-7ec5d1f58845)
  on Medium, cross-posted to
  [dev.to](https://dev.to/sbalasa/four-iso-standards-one-missing-layer-trustworthy-ai-in-financial-services-2km),
  Reddit r/artificial, and the Yabloko Labs LinkedIn company page, and
  submitted to KDnuggets for editorial review.

Standards engagement:

- Technical input submitted to BSI ART/1, the UK national mirror committee to
  ISO/IEC JTC 1/SC 42 (22 Jul 2026): the [CRA
  proposal](proposals/continuous-reliability-assurance-for-financial-ai.md) and
  the [financial-AI controls gap
  matrix](mappings/financial-ai-controls-gap-matrix.md), with StandICT.eu 2029
  fellowship funding declared to the committee.
- BSI Standards Maker application submitted 22 Jul 2026. BSI acknowledged the
  committee message the same day and confirmed an application backlog, with a
  substantive decision not expected until later in 2026.

Channel-by-channel status, dates, and evidence references are recorded in the
[dissemination log](notes/dissemination-log.md).

## Contribution Areas

Relevant future contributions include:

- additional standards review notes and cross-standard comparisons
- BSI, SC 42, and European standardisation engagement observations
- financial-sector case studies and implementation patterns
- control evidence examples for audit and assurance teams
- blog posts, presentation notes, and dissemination artifacts
- final report references and structured evidence links

## How To Contribute

Contributions should improve analytical quality, traceability, or practical
utility. Good contributions usually:

1. identify a concrete standards, governance, or assurance question
2. document sources and assumptions clearly
3. add original analysis rather than copied material
4. explain sector relevance for financial services
5. link claims to evidence stored or referenced in this repository

Issues and pull requests should state the problem addressed, the rationale for
the proposed change, and any evidence or references that support it.

## Disclaimer

This repository contains independent technical analysis and implementation
guidance. The views expressed are those of the author and do not represent
StandICT.eu, BSI, ISO, IEC, CEN, CENELEC, the European Commission, or any
standards body.

