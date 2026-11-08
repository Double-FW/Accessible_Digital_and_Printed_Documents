# Accessible Digital and Printed Documents: human-managed content creation and production activities and prompts

**Prepared:** 8 November 2026 · **Source revision:** `e3b2694b5a9d92be89ee49c20f0b350b1fd8188c`  
**Source:** [Double-FW/Accessible_Digital_and_Printed_Documents](https://github.com/Double-FW/Accessible_Digital_and_Printed_Documents/tree/e3b2694b5a9d92be89ee49c20f0b350b1fd8188c)  
**Audience:** authors, editors, designers, publishers, communication teams, producers, commissioners, access-service practitioners and technical/quality partners.

## Where the repository is useful

Use the guide’s profile-based method to author one structured source and deliver appropriate digital, hybrid, print and book editions. Stable rule IDs connect reading context, content structure, typography, images/data, formats and real-output verification. It supports authors, document designers, editors, publishers and those commissioning AI-assisted document production.

The main guide is a reconstructed edition dated 7 November 2026: some wording was restored from context, and eleven original attachments were unavailable to its reconstructor. Preserve that limitation rather than claiming verbatim recovery or independently verified source comparisons. MUST/SHOULD language is scoped to this guide’s production policy, not automatically law or WCAG. Separate standards thresholds, house starting values, user-override tolerance tests and actual output evidence.

The activities below are an editorial application of the repository, not a claim that it already contains a complete organisational process. AI can organise material, draft options and scripts, identify inconsistencies and prepare specifications or evidence summaries. Authors and editors preserve factual meaning and editorial intent. Designers and technical practitioners implement and verify delivered formats. Qualified access-service specialists review their work, and affected audiences inform the experience. Accountable publishers/producers retain creative, acceptance, rights and release decisions. Assign these responsibilities to actual people locally; the examples do not establish a new team or approval body.

## How to use the prompts

1. Attach [RAG_Reference.md](RAG_Reference.md). For selective retrieval, use the source routes below and [Source_Coverage.md](Source_Coverage.md).
2. Replace bracketed inputs with the actual project brief, artefacts and evidence. Supply the target task, audience, platform/setting, constraints and intended decision. Treat missing information as unknown.
3. Use either example prompt for the activity. Both refer to this folder’s reference. Supply only appropriate project information; use anonymised research findings where possible.
4. Require source ID, filename and original section citations; distinguish source guidance, local proposal, observed result and uncertainty. Ask for evidence requests where an artefact cannot be inspected.
5. Review the result with the named human roles and record decisions. A prompt output is a draft editorial/production aid, not implementation or evidence that a test ran. Do not defer disabled people’s involvement until final testing.

**Reusable response contract:** “Use the attached RAG_Reference.md as the knowledge source. Cite source IDs, files and sections. Distinguish source statements, project evidence, recommendations and unknowns. Preserve applicable source identifiers. Do not invent research, capability, approvals or test results. Give a concrete content/production artefact, trade-offs, evidence requests and decisions for the human team.”

## Activity map

| Activity | Production stage | Expected output |
| --- | --- | --- |
| 1. Define the reading task and edition strategy | Commissioning and editorial planning | An editorial/production brief and edition matrix. |
| 2. Build semantic structure and clear content | Authoring and content editing | A structured manuscript and semantic/navigation specification. |
| 3. Develop typography and visual reading treatments | Document design and style specification | A typographic/visual style specification and specimen plan. |
| 4. Make images, tables, forms and notation usable | Content production and information design | An image/data/form inventory with alternatives and production annotations. |
| 5. Specify and verify digital export profiles | Digital publishing and production handoff | A digital-production handoff and format-specific test plan. |
| 6. Produce equivalent screen-and-print editions | Hybrid publishing and offline design | A hybrid edition checklist and print-test brief. |
| 7. Plan physical print and sustained book reading | Print commissioning and book production | A print/book production brief and proof-review plan. |
| 8. Review, release and maintain delivered editions | Quality assurance and editorial release | A scoped verification/release record and correction plan. |

## 1. Define the reading task and edition strategy

**Production stage:** Commissioning and editorial planning

**Retrieve:** [S001 — Accessible_documentation_design.md](RAG_Reference.md#s001).

**Relevant source sections:** PLAN01–PLAN03; Profile selection.

### Tasks the repository can support

- Identify audiences, languages, tasks and preferred reading modes.
- Choose digital, hybrid, print and book profiles deliberately.
- Define meaning, navigation and experience outcomes for each edition.

**Expected output:** An editorial/production brief and edition matrix.

**Human review:** The commissioning editor and publisher agree formats, scope and reader evidence needs.

### Example prompt 1

> Use the attached RAG_Reference.md to brief [publication, audience and task]. Apply PLAN01–PLAN03 to select appropriate digital, hybrid, print or book editions. Define substantive content, navigation, interaction and reading outcomes across modes, plus constraints and unknowns. Distinguish source house defaults from applicable standards and cite source IDs and sections.

### Example prompt 2

> Challenge [publication brief] using the RAG. Identify a single fixed layout assumed to meet every need, missing offline actions and claims inherited from uninspected source attachments. Produce an edition strategy and evidence questions.

## 2. Build semantic structure and clear content

**Production stage:** Authoring and content editing

**Retrieve:** [S001 — Accessible_documentation_design.md](RAG_Reference.md#s001).

**Relevant source sections:** STRUCT01–STRUCT04; LANG01.

### Tasks the repository can support

- Outline meaningful headings, sequence, lists and navigation.
- Preserve qualifications and specialist meaning while improving clarity.
- Annotate language, script and intended reading order.

**Expected output:** A structured manuscript and semantic/navigation specification.

**Human review:** The editor verifies meaning; production specialists check that the intended structure survives authoring and export.

### Example prompt 1

> Using the RAG, restructure [manuscript] with meaningful heading levels, lists, navigation and reading sequence. Apply STRUCT01–STRUCT04 and LANG01, retaining facts, qualifications and language needs. Flag ambiguities rather than inventing content; distinguish a semantic specification from verified exported behaviour.

### Example prompt 2

> Review [document outline and sample pages] against the RAG. Find headings simulated by styling, essential sidebars interrupting sequence and simplification that changes meaning. Propose source-level repairs and navigation checks.

## 3. Develop typography and visual reading treatments

**Production stage:** Document design and style specification

**Retrieve:** [S001 — Accessible_documentation_design.md](RAG_Reference.md#s001).

**Relevant source sections:** TYPE01–TYPE06; VIS01–VIS03.

### Tasks the repository can support

- Inspect actual letterforms and contextual readability.
- Set adaptable hierarchy, spacing, alignment and contrast.
- Treat numerical defaults as candidates requiring contextual checks.

**Expected output:** A typographic/visual style specification and specimen plan.

**Human review:** The document designer reviews actual rendering with relevant readers; nominal font size alone does not prove usability.

### Example prompt 1

> Use the RAG to propose typography and visual styles for [publication and editions]. Apply TYPE and VIS rules, with contextual samples for body, headings, captions and notes. State starting values as house defaults or test hypotheses, preserve presentation overrides where supported and avoid universal accessible-font claims.

### Example prompt 2

> Challenge [document style specification] with the RAG. Identify text shrunk to fit, unjustified serif/sans assumptions, colour-only meaning and spacing or alignment choices unsupported by the reading context. Return concrete design revisions and evidence needs.

## 4. Make images, tables, forms and notation usable

**Production stage:** Content production and information design

**Retrieve:** [S001 — Accessible_documentation_design.md](RAG_Reference.md#s001).

**Relevant source sections:** IMAGE01–IMAGE03; DATA01–DATA02; FORM01; SPECIAL01.

### Tasks the repository can support

- Choose purpose-based alternatives and preserve essential visual relationships.
- Specify real table headers, pagination and response tasks.
- Retain specialist notation through appropriate formats and alternatives.

**Expected output:** An image/data/form inventory with alternatives and production annotations.

**Human review:** Subject experts verify facts and notation; designers and technical reviewers check relationships and operation.

### Example prompt 1

> Using the RAG and [document assets], create an inventory for images, charts, tables, forms and specialist notation. Apply the IMAGE, DATA, FORM and SPECIAL IDs with exact purpose, essential meaning, alternative route, semantic structure and edition-specific checks. Do not describe unseen graphics or invent data.

### Example prompt 2

> Review [table, chart, form and notation treatment] using the RAG. Identify image-only text, missing relationships, split tables losing headers and completion tasks unusable on paper or screen. Propose source repairs and evidence requests.

## 5. Specify and verify digital export profiles

**Production stage:** Digital publishing and production handoff

**Retrieve:** [S001 — Accessible_documentation_design.md](RAG_Reference.md#s001).

**Relevant source sections:** DIGITAL01–DIGITAL04.

### Tasks the repository can support

- Specify semantic word-processing, PDF and EPUB/reflow requirements.
- Treat each export as a separate output needing inspection.
- Plan adaptation, navigation and interaction tests in actual reading software.

**Expected output:** A digital-production handoff and format-specific test plan.

**Human review:** Production specialists inspect delivered files; format checkers and visual checks establish different evidence.

### Example prompt 1

> Use the RAG’s DIGITAL profiles to specify [DOCX, PDF, EPUB or HTML deliverables]. Map source structure, export settings, reading order, tags/navigation, adaptation and interaction to actual output checks. Identify tools and environments to confirm; do not claim accessible PDF from appearance or a successful export alone.

### Example prompt 2

> Challenge [digital export plan] against the RAG. Identify a print-production PDF reused without screen checks, flattened semantics and a source-template review substituted for final-file inspection. Return specific export and retest actions.

## 6. Produce equivalent screen-and-print editions

**Production stage:** Hybrid publishing and offline design

**Retrieve:** [S001 — Accessible_documentation_design.md](RAG_Reference.md#s001).

**Relevant source sections:** HYBRID01–HYBRID04; DATA02.

### Tasks the repository can support

- Preserve substantive meaning and actions across editions.
- Make links, references and instructions usable offline.
- Test ordinary printing and pagination without shrinking essential content.

**Expected output:** A hybrid edition checklist and print-test brief.

**Human review:** Editors verify content parity; production staff inspect actual screen and ordinary printed outputs.

### Example prompt 1

> Using the RAG, adapt [screen document] for ordinary printing. Apply HYBRID01–HYBRID04 and table pagination rules. Preserve content and action equivalence, make references usable offline and specify print layout, pagination and proof checks. Mark untested printer and paper conditions explicitly.

### Example prompt 2

> Review [screen/print edition pair] using the RAG. Find essential links lost on paper, omitted content, broken cross-references or print fixes that damage digital reading. Produce an edition-parity repair plan.

## 7. Plan physical print and sustained book reading

**Production stage:** Print commissioning and book production

**Retrieve:** [S001 — Accessible_documentation_design.md](RAG_Reference.md#s001).

**Relevant source sections:** PRINT01–PRINT02; BOOK01–BOOK02.

### Tasks the repository can support

- Specify paper, ink, binding and handling as a system.
- Review sustained-reading composition and reader alternatives.
- Use physical proofs and reader evidence for relevant choices.

**Expected output:** A print/book production brief and proof-review plan.

**Human review:** Publishers, printers and book designers validate physical samples and appropriate alternative editions.

### Example prompt 1

> Use the RAG to commission [printed publication or book]. Specify paper/ink/binding, opening and handling, contrast/glare, composition and sustained-reading considerations. Apply PRINT/BOOK rules, choose relevant alternatives and propose physical proof and reader checks rather than universal material or type-size guarantees.

### Example prompt 2

> Challenge [book or print specification] against the RAG. Identify binding that prevents practical use, compositional fixes that shrink essential text and assumptions that a print-ready PDF proves physical readability. Return proof questions and feasible alternatives.

## 8. Review, release and maintain delivered editions

**Production stage:** Quality assurance and editorial release

**Retrieve:** [S001 — Accessible_documentation_design.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** QA01–QA03; AI01–AI04.

### Tasks the repository can support

- Combine structural, automated, manual and reader checks as appropriate.
- Tie findings to exact edition/version and repair the source.
- Separate checked, failed, untested and inapplicable items honestly.

**Expected output:** A scoped verification/release record and correction plan.

**Human review:** The accountable publisher/editor decides release on actual evidence; internal exceptions do not make unmet standards satisfied.

### Example prompt 1

> Use the RAG to create a verification plan and release-record draft for [edition set]. Preserve QA and relevant rule IDs, specify final-file/page inspection, semantic/adaptation checks and reader evaluation. Record actual evidence or Not tested, limitations, residual issues, owner and review trigger; do not claim checks have run.

### Example prompt 2

> Audit [document release evidence] with the RAG. Identify a changed file carrying stale acceptance, visual inspection treated as semantic proof and an approved deviation presented as conformance. Produce corrections and retest scope.

## Editorial and production decision record

For each adopted result, record the project/task, source revision and sections used, observed editorial/production issue, barrier or opportunity, chosen option and rejected alternatives, expected outcome, evidence available, assumptions, unresolved constraints, accountable person, next check and review trigger. Use actual names and dates when agreed; leave them unassigned when unknown. Record acceptance and residual risk only when the accountable person has made the decision.

Revisit the reference when repository sources change, a new platform or context is introduced, implementation changes invalidate assumptions, or user feedback exposes a barrier. Compare changed sources rather than silently replacing the basis of existing decisions.
