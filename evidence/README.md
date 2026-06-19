# Evidence Management

## Purpose

This directory supports evidence collection for the fellowship's technical
outputs. The goal is to keep analytical claims, engagement activity, and
public dissemination artifacts traceable enough to support final reporting and
future reuse.

## What Counts as Evidence

Relevant evidence can include:

- public agendas, programs, and workshop descriptions
- public scope summaries for standards and technical specifications
- meeting notes from standards engagement activities
- presentations, blog posts, and dissemination materials
- correspondence summaries where publication is permitted
- screenshots or exported metadata that confirm public outputs
- internal analysis notes that explain how conclusions were formed

## Current Evidence Set

The public repository should not contain authenticated BSI portal screenshots
or other portal captures that may expose account, session, or redistribution
risk.

Working evidence may still be retained privately where appropriate. At
repository level, that evidence should be referenced through
`evidence/index.md` using metadata notes rather than committing the underlying
screenshots themselves.

The currently referenced privately retained evidence covers scope and purpose
material for:

- ISO/IEC TS 25570
- ISO/IEC 5338
- AI quality model work in SC 42
- green and sustainable AI work relevant to the repository analysis

These privately retained captures are useful as working evidence for standards
review and fellowship traceability, especially where they preserve proposal
titles, scope summaries, purpose statements, committees, and timeline context.

## Screenshot-Specific Handling

Screenshots require more care than plain notes or exported metadata.

When retaining screenshots privately for fellowship evidence:

- record what page or view was captured
- record the capture date
- state why the screenshot matters to the repository analysis
- note whether the screenshot reflects a public page, member portal, or
  authenticated workspace
- note any restrictions on redistribution or publication

If a screenshot includes visible account names, session indicators, internal
navigation, or other portal-specific metadata, create a companion note in the
repository that explains:

- source location
- capture context
- relevance to a specific repository document
- whether redaction is required before public publication

## Publication and Redaction Considerations

Because this repository is public, screenshot evidence should be reviewed for
publication suitability before being committed or cited directly in public
outputs.

In particular:

- redact personal names, account details, or session indicators where needed
- avoid publishing screenshots that may expose non-public portal context unless
  publication rights are clear
- prefer short metadata notes plus analytical references when the screenshot is
  useful for working evidence but not ideal for public redistribution
- do not rely on screenshots as the sole evidence for an analytical claim when
  a stable public source description can also be recorded

## Evidence Handling Principles

Evidence stored or referenced here should follow four principles:

- **Traceability:** each item should support a specific claim, activity, or
  deliverable
- **Provenance:** the source, date, and collector should be obvious
- **Reusability:** references should be understandable during final reporting
  without reconstructing context from memory
- **Appropriate disclosure:** do not store confidential material unless
  handling permissions are clear and the storage approach is appropriate

## Recommended Storage Practice

Use stable filenames that make items easy to cite. A practical naming pattern
is:

`YYYY-MM-DD_source_topic_short-description.ext`

Examples:

- `2026-06-19_sc42_public-workshop_agenda.pdf`
- `2026-07-02_bsi_meeting-notes_reliability-assessment.md`
- `2026-08-14_blog-draft_financial-ai-governance.md`

When a source cannot be stored directly, create a markdown note that captures:

- source title
- URL or location
- access date
- reason it matters
- any constraints on redistribution

For screenshot evidence, a companion note is recommended even when the image is
retained privately. That note should identify the private evidence item and
clarify the page context and publication status.

## Referencing in Fellowship Outputs

Each analytical document should reference evidence in a way that is stable
enough for later reporting. Useful patterns include:

- linking to a file stored in this directory when it is suitable for public
  publication
- linking to `evidence/index.md` when the underlying evidence is privately
  retained
- linking to a note in `notes/` that summarizes the source and observation
- recording evidence identifiers in standards review entries

## Minimal Metadata for Each Item

Every evidence item or evidence note should, at minimum, capture:

- date collected
- source or event name
- collector or author
- short summary of relevance
- related repository document or deliverable
- publication suitability or redaction status for screenshots

## Relationship to Final Reporting

The repository is intended to serve as a living fellowship artifact. Evidence
stored or referenced here should make it easier to produce:

- final report narratives
- standards engagement summaries
- dissemination logs
- citations supporting recommendations and observed gaps
