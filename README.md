---
title: "Accessible digital and printed documents"
version: "1.1.0"
updated: "2026-11-21"
owner: "Double FW Ltd"
license: "MIT"
language: "en-GB"
status: "editorial_guidance_for_local_adoption"
---

# Accessible digital and printed documents

Practical guidance for creating documents people can find, read, navigate, understand and use through visual reading, enlargement, speech, braille and appropriate alternative editions. It covers structured digital documents, screen-and-print publications, physical print and sustained book reading.

Maintain one structured content source where practicable, then produce editions suited to the task and reading context. Equivalent meaning and useful access matter; the same fixed layout need not serve every medium.

## Start here

1. Read the audience, task and format guidance in [Accessible documentation design](Accessible_documentation_design.md), sections 1–6.
2. Apply section 7 for digital delivery, section 8 for hybrid output and section 9 for physical print and books.
3. Use section 10 to plan checks of actual delivered files or proofs. Keep proposed checks distinct from completed evidence.
4. For AI-assisted work, read [AGENTS.md](AGENTS.md), section 11 and the [activity prompts](Accessible_Documents_RAG_and_Prompts/Content_Creation_and_Production_Activities_and_Prompts.md).
5. Use [Terminology alignment](Terminology_Alignment.md) and [Related Double-FW guidance](Related_Double_FW_Guidance.md) for shared meanings and specialist support.

## What is included

| Resource | Purpose |
| --- | --- |
| [Main design guide](Accessible_documentation_design.md) | Twelve sections and stable PLAN, STRUCT, TYPE, VIS, LANG, IMAGE, DATA, FORM, SPECIAL, DIGITAL, HYBRID, PRINT, BOOK, QA and AI rule IDs. |
| [Agent instructions](AGENTS.md) | Metadata, scope, detailed operational rules, authority and privacy boundaries, evidence handling and an illustrative review template. |
| [Terminology alignment](Terminology_Alignment.md) | Experience, equivalence, cognitive identifiers, standards meanings and evidence states. |
| [Related guidance](Related_Double_FW_Guidance.md) | Public Double-FW resources and their relevant uses. |
| [Production workflow and handoff map](Production_Workflow_and_Handoff_Map.md) | Coordinate documents with email and audiovisual assets without confusing their specialist requirements. |
| [RAG and prompt pack](Accessible_Documents_RAG_and_Prompts/README.md) | Maintained retrieval routes, source coverage and eight activities with sixteen example prompts. |
| [Provenance and rights](NOTICE.md) | Reconstruction limitations, historical attachments and external rights. |
| [MIT licence](LICENSE) | Sole project licence and required copyright/permission notice. |

## Scope and limitations

This is documentation guidance, not an installed generation tool, automated checker or complete WCAG, PDF/UA or EPUB conformance checklist. A successful export or checker result cannot establish universal accessibility. Inspect each delivered edition and use appropriate structural, manual and reader checks. Digital contrast calculations do not certify paper, ink or binding.

MUST/SHOULD wording expresses the guide’s production policy when locally adopted; it does not turn every recommendation into law or a WCAG requirement. Identify the applicable standard, edition, level, context and any binding obligations separately. House typography defaults are starting values, not universal minima or clinical claims.

The guide contains reconstructed wording from 7 November 2026. Eleven historical attachments were unavailable for inspection. Their source register is preserved for provenance, not as verified evidence or a dependency on private files. The 21 November editorial revision does not verify those attachments or recreate lost originals. See [section 12](Accessible_documentation_design.md#12-source-reconciliation-and-provenance) and [NOTICE](NOTICE.md).

## Agent and training use

Retrieve maintained source sections with their scope, qualifications and rule IDs. The [RAG reference](Accessible_Documents_RAG_and_Prompts/RAG_Reference.md) is an index, not a complete embedded corpus or functioning retrieval pipeline. Do not ingest navigation, historical duplicates and source content as independent evidence for the same rule. Record the Git revision, path and section for reproducibility; do not silently truncate a rule or table.

Keep source guidance, project evidence, synthetic examples, proposals and authorised decisions distinct. `unknown`, `not_tested` and `not_applicable` are different states; unresolved decisions are separate. A prompt output is not a test result or permission to publish. Exclude confidential, personal or otherwise unauthorised material from public exports.

The [weekly Hugging Face sync](huggingface/SETUP.md) exports the approved source files to [GarethFW/Accessible_Digital_and_Printed_Documents](https://huggingface.co/datasets/GarethFW/Accessible_Digital_and_Printed_Documents). It is scheduled for Mondays at 10:31 UTC and can be run manually. Publishing requires the dataset-scoped HF_TOKEN Actions secret; installing the workflow does not establish that a first sync has succeeded. The exported views overlap and are source guidance, not executed tests or validated answers.

## Maintaining the guidance

Preserve stable rule IDs and update the guide and corresponding agent rules together. Check relative links, public repository routes, metadata, provenance and the retrieval index after changes. Reassess affected output evidence when content, export software, format or reading context changes. Keep actual source checks, test dates and approvals separate; changing an editorial date does not renew them.

## Licence

The repository is MIT licensed, copyright 2026 Double FW Ltd. See [LICENSE](LICENSE). External references retain their own rights; the historical reference register does not add another project licence or relicense third-party material. See [NOTICE](NOTICE.md) before importing external content.
