---
title: "Accessible documentation design"
subtitle: "A practical guide for digital documents, screen and print editions, and printed books"
version: "1.0"
date: "2026-10-28"
status: "active"
document_type: "accessibility guidance"
category:
  - documentation design
  - digital accessibility
  - print accessibility
  - inclusive publishing
  - llm-generated-document guidance
intended_audience:
  - document designers
  - authors
  - editors
  - developers
  - publishers
  - teams using LLMs to generate documents
language: "en"
reading_modes:
  - visual
  - speech
  - braille
  - enlarged text
  - print
  - screen
summary: "A practical framework for designing accessible documents across digital, hybrid, and print editions while preserving meaning, navigation, and usability for diverse readers."
keywords:
  - accessibility
  - documentation design
  - inclusive design
  - print accessibility
  - digital accessibility
  - information architecture
  - typography
  - document structure
  - llm instructions
  - WCAG
source_scope: "This guide synthesises supplied practitioner guidance and technical references into operational rules for document production and verification."
---

Accessible documentation design

A practical guide for digital documents, screen and print editions, and printed books

Version 1.0 • 28 October 2026

Design for people to find, perceive, understand and use information in their preferred reading mode. Preserve meaning and navigation across visual reading, speech, braille, enlargement and print. A[...]

This guide is for document designers, authors, editors, developers, publishers and teams using LLMs to generate documents. It combines the eleven supplied sources, resolves conflicting advice and adds[...]

The central decision is to maintain one structured content source and create appropriate editions from it. One fixed page layout cannot satisfy every screen, paper size, reading distance or access[...]

# How to use this guide

Read sections 1 to 6 for every document. Apply section 7 to digital editions, section 8 when screen content must print, and section 9 to physical publications and books. Use section 10 before rele[...]

**Requirement language.** MUST and MUST NOT are release requirements within this guide when their stated scope applies. SHOULD means the default practice; a departure needs a recorded reason and revie[...]

**Evidence categories.** STANDARD identifies a requirement from a named technical standard within its scope. SOURCE identifies supplied practitioner guidance. SYNTHESIS identifies a practical rule or [...]

**Scope.** ALL means every edition; DIGITAL means an electronic edition; HYBRID means content offered for both screen and print; PRINT means the physical output; BOOK means sustained reading in print [...]

**Exceptions.** A design preference cannot waive an applicable standard or leave essential information inaccessible. Record the affected rule, context, reason, reader impact, equivalent alternative, e[...]

# Contents

[1 Define the reading experience](#1-define-the-reading-experience)

[2 Build structure before appearance](#2-build-structure-before-appearance)

[3 Select and set type](#3-select-and-set-type)

[4 Use colour and space to support reading](#4-use-colour-and-space-to-support-reading)

[5 Preserve language and information in images](#5-preserve-language-and-information-in-images)

[6 Design tables forms and specialist content](#6-design-tables-forms-and-specialist-content)

[7 Deliver a usable digital edition](#7-deliver-a-usable-digital-edition)

[8 Make screen content work on paper](#8-make-screen-content-work-on-paper)

[9 Design physical documents and books](#9-design-physical-documents-and-books)

[10 Verify the delivered editions](#10-verify-the-delivered-editions)

[11 Translate the guide into LLM instructions](#11-translate-the-guide-into-llm-instructions)

[12 Source reconciliation and provenance](#12-source-reconciliation-and-provenance)

# 1 Define the reading experience

## PLAN01 Establish the audience and task

**ALL • MUST • SOURCE and SYNTHESIS.** Before styling, record the purpose, intended readers, languages and scripts, expected reading duration, delivery formats, devices or paper sizes, viewing con[...]

Include low vision, nonvisual access, motor access, cognitive and language needs where relevant. A quick-reference safety sheet and a novel need different navigation and reading rhythms. Where informa[...]

## PLAN02 Choose formats deliberately

**ALL • SHOULD • SYNTHESIS.** Prefer a reflowable reading edition for screen use. HTML suits online guidance; a structured word-processing file suits editable documents; reflowable EPUB suits book[...]

A PDF containing page images is a poor primary reading edition. OCR can recover text but still needs correction, structure and reading-order work. A well-tagged PDF can support assistive technology wh[...]

## PLAN03 Evaluate three separate outcomes

**ALL • MUST • SOURCE.** Assess emotional accessibility, functional accessibility and technical accessibility separately. Emotional accessibility concerns whether the communication feels appropria[...]

Brand expression belongs within this evaluation. Expressive typography may suit a short title but should not compromise instructions or body copy. Preference is useful evidence, but it is not a substi[...]

# 2 Build structure before appearance

## STRUCT01 Preserve a meaningful sequence

**ALL • MUST • SOURCE and SYNTHESIS.** Write content in a logical order before applying layout. Use real heading levels, paragraphs, lists, captions and table structures. Do not simulate headings [...]

Use a clear title and descriptive headings that explain each section. Nest heading levels consistently; do not choose a heading level for its size. In Word, use the Title style for the title and Headi[...]

## STRUCT02 Make navigation useful

**ALL • SHOULD • SYNTHESIS.** Long documents need a table of contents, informative chapter or section names and predictable page or location references. Digital contents entries should be links. P[...]

Use meaningful cross-references such as "See section 6, Tables and complex information", rather than "see above" or "the box on the right". Update references and page numbers after layout changes. Dig[...]

## STRUCT03 Keep layout and reading order aligned

**DIGITAL • MUST; PRINT • SHOULD • SOURCE and SYNTHESIS.** The programmatic sequence must preserve the meaning conveyed visually. Anchor figures and their explanations near their first reference[...]

Use one main text column as the default for guidance and continuous prose. Sidebars must not interrupt a sentence or contain information needed before the main text can be understood. Put essential in[...]

## STRUCT04 Write for comprehension

**ALL • SHOULD • SYNTHESIS.** State purpose and required actions early. Use familiar words, concrete examples, short informative headings and paragraphs organised around one idea. Explain necessar[...]

Preserve precision and necessary qualifications. A readability score or "reading age" does not establish comprehension. Do not simplify technical, legal or literary content until its meaning changes. [...]

# 3 Select and set type

## TYPE01 Evaluate actual letterforms

**ALL • MUST • SOURCE and TEST.** Evaluate each proposed body font at its intended sizes, weights and output conditions. Inspect uppercase I, lowercase l and numeral 1; O and 0; c, e, o and a; b, [...]

Look for distinctive shapes, open apertures, counters that remain clear, adequate spacing and strokes that survive the output process. An aperture is an opening in a letter; a counter is enclosed or p[...]

## TYPE02 Do not select by category or marketing claim alone

**ALL • MUST NOT • SOURCE and TEST.** Do not claim that serif, sans serif, humanist, a particular brand font or a "dyslexia font" is accessible to everyone. Do not present a typeface as a treatmen[...]

A serif face can work well in a book; a sans serif can also work well. A single-storey or double-storey a may have different advantages for different readers. Familiarity, differentiation, language an[...]

## TYPE03 Size for the reader and the medium

**ALL • SHOULD • SYNTHESIS and TEST.** Use the starting values below, then assess the actual font and conditions. These are house defaults for this guide, not universal accessibility thresholds. P[...]

| **Context**                           | **Starting point**                            | **Required judgement**                                             |
| ------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------ |
| Reflowable screen body                | 1rem to 1.125rem with the root at 100 percent | Respect the reader's base size; test small screens and enlargement |
| General print and paginated documents | 12 to 14pt body                               | Prefer the larger end where feasible; proof at actual size         |
| Large print                           | Begin discussion at 16 to 18pt                | Confirm the reader's needs; larger sizes may be necessary          |
| Sustained book reading                | Start within the general print range          | Compare real chapters, trim size, measure, leading and fatigue     |
| Captions notes and tables             | Prefer body size                              | Essential information must not become tiny to save space           |

A 1rem setting often corresponds to 16 CSS pixels at a browser's default, but the reader can change that default. CSS pixels are not physical printer dots. Do not convert a web size into a print [...]

## TYPE04 Balance measure and leading

**ALL • SHOULD • SOURCE and SYNTHESIS.** For Latin-script prose, aim initially for about 50 to 70 characters per line including spaces; around 65 is a useful working target. Shorter lines may be n[...]

Start body line spacing around 1.5 times font size. Adjust for x-height, line length, script, reader feedback and output. A carefully tested book may work at roughly 1.3 to 1.5; this is an editorial o[...]

## TYPE05 Preserve regular spacing and emphasis

**ALL • SHOULD • SOURCE.** Begin with the font's designed letter spacing. Correct crowding if observed, but do not impose wide tracking everywhere. Avoid negative body tracking and stretched word [...]

Use sentence case and moderate emphasis. Reserve sustained italics, all capitals, underlining and heavy bold for contexts where their meaning justifies them. Preserve conventional acronyms and necessa[...]

## TYPE06 Use predictable alignment

**ALL • SHOULD • SOURCE and TEST.** Align prose to the reading start edge: left for ordinary left-to-right text, right for ordinary right-to-left text. Avoid centred paragraphs and fully justified[...]

If a printed book uses justification, treat it as a reviewed exception: use professional composition, language-aware hyphenation and restrained spacing; inspect every page for rivers, stretched short [...]

# 4 Use colour and space to support reading

## VIS01 Maintain contrast without relying on colour

**DIGITAL • MUST • STANDARD; PRINT • MUST • SYNTHESIS.** For the selected WCAG AA digital baseline, text contrast is at least 4.5:1, or 3:1 for large text: 18pt regular or 14pt bold and above.[...]

Use text labels, patterns, shapes or direct annotation for chart series, warnings and categories. Check text on every actual background, including shaded table rows and selected states. Avoid text ove[...]

**PRINT.** Proof dark, sufficiently substantial text against a plain light substrate. Digital contrast calculations are useful when choosing artwork colours, but do not certify reflected-light contras[...]

## VIS02 Support personal presentation

**DIGITAL • MUST where supported • SOURCE and SYNTHESIS.** Do not obstruct font replacement, zoom, spacing changes or reader colour preferences. Check the result with alternate fonts, dark or ligh[...]

Some readers prefer off-white backgrounds or reduced brightness; others require strong contrast. Offer choice where possible, while keeping authored default themes within the selected contrast require[...]

## VIS03 Create clear visual grouping

**ALL • SHOULD • SOURCE.** Use space and alignment to show relationships. Keep a caption with its figure and a heading with the beginning of its section. Use sufficient margins and a restrained hi[...]

Separate paragraphs consistently. Guidance often benefits from space after paragraphs; continuous book prose may use first-line indents. Avoid combining large indents and large gaps without a reason. [...]

# 5 Preserve language and information in images

## LANG01 Support the complete language

**ALL • MUST • SOURCE.** Verify glyph coverage, diacritics, contextual shaping, punctuation, numerals and direction for every supported language. Use meaningful native-language samples and native-[...]

Set the document's primary language and mark changes where the format supports this. Set direction separately when needed, including mixed-direction passages, URLs and numbers. Use script-appropriate [...]

Font fallback must preserve meaning and remain readable. Check font loading failure, exports, embedded fonts and licensing. Do not convert prose to outlines to avoid embedding problems. Test search, c[...]

## IMAGE01 Keep text as text

**DIGITAL • MUST • SOURCE and SYNTHESIS.** Use actual text for prose, headings, instructions, labels and data. Do not flatten a page into an image. A screenshot, scanned letter, logo or historical[...]

For an image of a quotation or message, transcribe the meaningful text accurately. If the exact appearance matters, describe that separately. Do not assume OCR built into a reader will recover the inf[...]

## IMAGE02 Choose alternatives by purpose

**DIGITAL • MUST; PRINT • MUST for essential meaning • SOURCE and SYNTHESIS.** Provide concise alternative text for informative images, describing the information or purpose in context. For a fu[...]

Complex diagrams need a nearby explanation, extended description or accessible data representation. Short alt text should identify the graphic and point to the detailed equivalent. Do not hide an enti[...]

Alt text is normally not printed. Therefore, essential interpretations must also appear in visible captions or body text in the print edition. A caption naming the subject is not necessarily a descrip[...]

## IMAGE03 Handle charts and media explicitly

**ALL • MUST • SYNTHESIS.** Charts need a clear title, labelled axes, units, understandable series identification and a statement of the important finding. Supply the underlying data when exact va[...]

Digital audio and video need the alternatives appropriate to their content, including captions, transcripts and description of meaningful visuals. Printed editions need the essential information in te[...]

# 6 Design tables forms and specialist content

## DATA01 Use tables for real relationships

**ALL • SHOULD • SYNTHESIS.** Use a table when readers need to compare repeated attributes, values or records. Use prose or lists for narrative instructions. Keep tables simple, with a clear title[...]

**DIGITAL • MUST.** Encode header relationships using the format's supported structure. Mark and repeat header rows in word-processing tables; verify associations after export. Complex merged header[...]

Avoid blank cells used for spacing, unexplained ditto marks and ambiguous empty values. State "not applicable", "not recorded" or a defined symbol as appropriate. Align numbers consistently, including[...]

## DATA02 Keep tables readable across pages

**PRINT and HYBRID • MUST • SOURCE and SYNTHESIS.** Repeat column headings on continuation pages and preserve column order. Keep ordinary rows together where possible, but allow a row that exceeds[...]

Keep titles, notes and units associated with the table. Make continuation status clear when needed. Check that table rules and shading survive ordinary printers and greyscale. Use sufficient cell padd[...]

## FORM01 Make response tasks operable

**DIGITAL • MUST • SYNTHESIS.** Forms need persistent labels, instructions, identified required fields, meaningful field names, logical keyboard order and understandable errors. Do not use placeho[...]

**PRINT • MUST.** Provide adequate writing space, clearly labelled options and an obvious selection method. Do not rely on interactive validation or hover help. Preserve necessary instructions, cons[...]

## SPECIAL01 Keep specialist notation recoverable

**DIGITAL • SHOULD • SYNTHESIS.** Use structured equations where supported and test how they are spoken or navigated. If a formula must be an image, provide an accurate textual equivalent suited t[...]

Preserve significant whitespace, operators, minus signs and symbols. Explain uncommon notation. For print, test that subscripts, superscripts, punctuation and thin graph lines remain clear at actual s[...]

# 7 Deliver a usable digital edition

## DIGITAL01 Preserve adaptability

**DIGITAL • MUST within the applicable standard scope • STANDARD.** Test text enlargement to 200 percent without loss. For reflowing web content, test at 320 CSS pixels wide, equivalent to a [...]

Prefer relative web font sizing and flexible containers. Do not disable pinch zoom, fix text container heights or truncate essential prose with ellipses. Text-only resizing, page zoom and screen magni[...]

## DIGITAL02 Author word-processing documents semantically

**DIGITAL • MUST • SYNTHESIS.** Use named styles, logical headings, real lists, meaningful link text, document language and an informative title property. Provide image alternatives and simple tab[...]

Prefer spacing rules, page-break-before and keep-with-next to repeated empty lines. Avoid manual line breaks throughout body paragraphs. Ensure the document remains usable if fonts change. Run the aut[...]

## DIGITAL03 Export PDF as a separate quality gate

**DIGITAL PDF • MUST • SYNTHESIS supported by V3.** Use an export route that preserves tags and structure. Inspect the delivered PDF, not only its source. Check the title, primary language, headin[...]

Check text extraction, search, copy and paste, and embedded font behaviour. Correct OCR errors, especially in names, numbers and symbols. Do not use security settings that prevent assistive access. A [...]

A PDF/UA target must specify the intended edition and a suitable validation process. Technical validation and human checks are complementary. Do not claim PDF/UA or WCAG conformance from tags alone, a[...]

## DIGITAL04 Prepare electronic books for reading systems

**DIGITAL BOOK • SHOULD • SYNTHESIS supported by V5.** Prefer reflowable EPUB for continuous prose. Include semantic chapters, navigable contents, image alternatives, language metadata and useful [...]

Where print-equivalent pagination is supplied, implement appropriate page navigation and identify its source. Use fixed-layout EPUB only where the content requires it, with suitable alternatives. Vali[...]

# 8 Make screen content work on paper

## HYBRID01 Keep meaning equivalent across editions

**HYBRID • MUST • SOURCE and SYNTHESIS.** Maintain a shared structured source and compare each output against it. Essential content must survive printing, including expanded disclosures, sele[...]

Remove purely operational controls, cookie banners, advertisements and redundant navigation. Replace interactions with static information or instructions. For example, print the currently relevant res[...]

## HYBRID02 Make references usable offline

**PRINT and HYBRID • MUST • SOURCE and SYNTHESIS.** Provide a meaningful destination for essential external links: a readable URL, a numbered reference with its URL, or another usable contact rout[...]

Use section names or page references for internal links. A QR code may supplement a short URL or reference but must not be the only route. Check the code at final print size and on the selected stock.[...]

## HYBRID03 Define and test print layout

**HYBRID • SHOULD • SOURCE and SYNTHESIS.** In web publishing, scope print-specific rules to print media. Use physical units for page geometry and print text sizes; relative spacing remains useful[...]

Remove fixed positioning and screen-only overflow constraints that can crop print content. Size images to the available width. Keep headings with following text and short figures with captions. Let lo[...]

## HYBRID04 Test ordinary printing conditions

**HYBRID • MUST • SOURCE and SYNTHESIS.** Inspect preview and a physical sample with backgrounds disabled, greyscale enabled and normal printer margins. Check duplex output where intended. Verify [...]

Test actual size as well as common "fit to page" settings; scaling can make a previously adequate font too small. Document any necessary print instructions beside the download or in the publication. A[...]

# 9 Design physical documents and books

## PRINT01 Specify paper ink and binding together

**PRINT • SHOULD • SYNTHESIS and TEST.** Use a plain, low-glare stock with enough opacity to minimise distracting show-through. Compare physical proofs; paper weight alone does not establish opaci[...]

Off-white stock can be comfortable for some readers, but heavily tinted stock can reduce contrast. Avoid gloss, textured backgrounds and large reverse-out passages where they impede reading. Ensure ph[...]

Allow enough inner margin for the actual binding so readers do not have to force the book open or lose text in the gutter. Keep text away from trim and folds. Mirror margins correctly for left and rig[...]

## BOOK01 Optimise for sustained reading

**BOOK • SHOULD • SOURCE and SYNTHESIS and TEST.** Test a representative chapter or substantial continuous passage, not only a title page or specimen sentence. Look for lost lines, rereading, visu[...]

Keep the body typography stable across chapters. Use a calm, consistent hierarchy and predictable paragraph treatment. Avoid decorative drop capitals that disrupt word recognition or reading order. Av[...]

Keep notes readable and easy to return from. Where readers must consult a note immediately, do not bury it at the end of the book without a clear reference. Essential explanations belong in the main t[...]

## BOOK02 Control composition without shrinking text

**PRINT BOOK • SHOULD • SYNTHESIS.** Review widows, orphans, isolated headings, awkward page turns and repeated hyphens. Avoid splitting short labels and number-unit combinations. Use language-awa[...]

Balance line length, type size, leading, margins and trim size together. Larger type with excessively short lines can become tiring; wider pages with long lines can make return sweeps difficult. Adjus[...]

## PRINT02 Offer appropriate alternative editions

**PRINT • MUST where needed to deliver equivalent access • SYNTHESIS.** Plan how readers obtain large print, accessible digital text, audio, braille or other appropriate formats. Do not treat an e[...]

Alternative editions should preserve substantive content, version and useful navigation. Make the request or download route clear and usable; do not require a reader to decipher inaccessible print to [...]

# 10 Verify the delivered editions

## QA01 Combine automated manual and reader checks

**ALL • MUST • SOURCE and SYNTHESIS.** Automated tools detect some structural problems. Human review assesses meaning, descriptions, relationships and reading order. Reader testing establishes how[...]

Compare candidate typography under the same content and conditions. Include readers relevant to the audience, such as people with low vision, people who use screen readers or magnification, peopl[...]

## QA02 Apply the release checks

**ALL • MUST • SYNTHESIS.** For each relevant row below, record pass, fail, not tested or not applicable, with evidence and a reviewer. A failed critical requirement or missing essential informati[...]

| **Check**               | **Method**                                                             | **Passing outcome**                            |
| ----------------------- | ---------------------------------------------------------------------- | ---------------------------------------------- |
| Content and navigation  | Compare source with final editions                                     | No lost meaning; contents and references work  |
| Structure and order     | Inspect outline and semantic structure; read with assistive technology | Meaningful sequence and navigation             |
| Typography and language | Inspect actual fonts and script samples                                | Clear text; correct shaping; no missing glyphs |
| Digital adaptation      | Resize, reflow and apply supported overrides                           | No obscured, clipped or missing content        |
| Images and data         | Review descriptions and equivalent representations                     | Essential information is recoverable           |
| Keyboard and forms      | Traverse and complete real tasks                                       | Controls labelled, reachable and usable        |
| Export                  | Inspect final file and run relevant validation                         | No conversion defects or unsupported claims    |
| Print                   | Inspect actual-size and greyscale physical proofs                      | Legible content; sound pagination and binding  |
| Sustained reading       | Test representative passages with readers                              | Findings reviewed; barriers addressed          |

## QA03 Keep an honest release record

**ALL • MUST • SYNTHESIS.** Record the document version, source revision, output files, applicable standard and edition, tested software, devices or print conditions, dates, methods, results, exce[...]

Use precise language: "heading structure checked" or "tested with the named reader and software". Do not write "fully accessible" because a checker reported no errors. This guide itself has been prepa[...]

# 11 Translate the guide into LLM instructions

## AI01 Preserve scope obligation and evidence

**LLM WORKFLOWS • MUST • SYNTHESIS.** An AGENTS.md version should preserve each stable rule ID, its scope, obligation and test. Do not compress conditional advice into universal rules. Keep numeri[...]

Use the rule IDs already attached to every requirement in sections 1 to 10. Keep a short execution sequence in AGENTS.md and link to a detailed rule register if the complete guide is too long. Instruc[...]

## AI02 Use a repeatable execution sequence

**LLM WORKFLOWS • MUST • SYNTHESIS.** The instruction file should require this sequence:

1. Read the task, existing document and project requirements. Identify output profiles, audience, languages, reading duration and applicable standards.
2. Record missing facts and provisional assumptions. Ask only when missing information materially changes access or prevents a necessary decision.
3. Build semantic structure and complete content before decorative styling. Select typography using the relevant scope and evidence.
4. Generate each requested edition from the shared source. Preserve language, headings, links, tables, image alternatives and reading order.
5. Inspect every rendered page for paginated outputs. Run available structural checks and the format-specific tests in this guide.
6. Repair defects and regenerate affected editions. Record unavailable checks as not tested and explain the practical limitation.
7. Deliver the files with a concise verification summary. Escalate unresolved access barriers to the responsible human; never invent approval or test evidence.

## AI03 Make every rule operational

**LLM WORKFLOWS • MUST • SYNTHESIS.** Represent a rule with the fields below. Split a multi-part rule into subordinate checks when implementing automated tests, retaining its parent ID. Do not mar[...]

| **Field**            | **What it must contain**                                          |
| -------------------- | ----------------------------------------------------------------- |
| id and version       | Stable rule ID and revision                                       |
| scope and trigger    | Edition or element that activates the rule                        |
| obligation and basis | MUST, SHOULD or MAY; standard, source, synthesis or test          |
| instruction          | A concrete action or prohibited behaviour                         |
| parameters           | Defaults, units, bounds and permitted context adjustments         |
| verification         | Method and observable passing outcome                             |
| evidence and status  | Actual result, file or page, tool or reviewer, date and status    |
| exception            | Reason, impact, equivalent access, approving role and review date |

**Example using TYPE03.** Scope: PRINT body text. Obligation: SHOULD. Action: start at 12 to 14pt and judge perceived size on an actual-size proof. Basis: synthesis informed by S1, S3, S7 and V4. Veri[...]

## AI04 Set explicit stop and escalation conditions

**LLM WORKFLOWS • MUST • SYNTHESIS.** Flag missing essential content, broken script shaping, unreadable text, absent required alternatives, an unusable form, loss of digital structure or contradic[...]

Do not fabricate alt text for an unseen image, infer that OCR is correct, copy source pass/fail font labels as universal facts, reduce text silently to meet a page count, or treat an inaccessible expo[...]

If an instruction conflicts with a mandatory applicable standard, identify the conflict and propose an accessible resolution. If a SHOULD rule conflicts with an evidenced reader need, record the adapt[...]

# 12 Source reconciliation and provenance

## Decisions made when combining the guidance

The supplied material contains practical experience, design-system conventions and research interpretations. It is not one normative standard or one peer-reviewed evidence base. This guide retains use[...]

**Typeface categories and named fonts.** S5 favours serif type for print, while S8 includes categorical font pass/fail examples and claims about specific styles. S1 explicitly cautions against th[...]

**Size and leading.** S3 uses a BBC-specific scale and a 1.375 leading example; S7 discusses larger spacing; S5 sets 12pt body but overrides paragraphs to 11pt. This guide makes practical startin[...]

**Web standards and paper.** S5 maps WCAG concepts directly to print. This guide distinguishes digital requirements from physical proofing. The numerical contrast of artwork does not prove contra[...]

**Print suppression and pagination.** S5's broad selectors could remove meaningful asides, footers or embedded information, and blanket no-break rules can overflow long tables. This guide require[...]

**Spacing and group relationships.** A sentence in S3 appears to reverse the intended grouping rule; its heading example makes the intended relationship clear. This guide keeps related items clos[...]

**Contrast and comfort.** S7 and S10 discuss softened contrast. This guide supports personal choice but does not trade away required default digital contrast or assume reduced contrast helps ever[...]

**Writing systems and neuroscience.** S9 to S11 contain explanatory historical, neurological and classification claims that are unnecessary for document production. This guide does not reproduce [...]

## Supplied source register

All eleven attachments informed this synthesis. References below identify the supplied versions, not a claim that their linked pages remain unchanged. Page references refer to the supplied PDF pa[...]

**S1 Accessible Typography for UX and Brand Systems.** Supplied file Accessible_Typography_for_UX_and_Brand_Systems(1).md, version 1.0-semantic, processed 18 September 2026. Attributed in the file to [...]

**S2 BBC GEL Images of text.** Supplied BBC GEL _ Images of text.pdf, particularly pages 1 to 3; article published 30 May 2024. Basis for contextual descriptions, transcription and body-text equi[...]

**S3 GEL Typography.** Supplied GEL _ Typography.pdf, version 0.1.0, particularly pages 2 to 7. Basis for relative sizing, measure, spacing, alignment, links and adaptability. BBC-specific font c[...]

**S4 BBC Accessibility for Products Images of text.** Supplied Images of text - Accessibility for Products - BBC.pdf, pages 1 to 2. Basis for using actual text and accessible equivalents. Histori[...]

**S5 Print Friendly Style Sheets Accessibility Best Practices.** Supplied PRINT_ACCESSIBILITY_BEST_PRACTICES.md, copyright 2026 Mike Gifford; file states AGPL-3.0-or-later. Basis for print adapta[...]

**S6 BBC Accessibility for Products Styling and readability.** Supplied Styling and readability - Accessibility for Products - BBC.pdf, pages 1 to 3. Basis for separating content and presentation[...]

**S7 Typography DDP Accessibility.** Supplied Typography _ DDP Accessibility.pdf, particularly pages 1 to 18. Basis for contextual font selection, measure, resizing, weight, spacing, direction an[...]

**S8 Typeface Accessibility Guide GAAD 2020.** Supplied Typeface Accessibility.pdf. Credits Bruno Maag, David Bailey, Gareth Ford Williams and Michael Mathews. Basis for letterform inspection and[...]

**S9 Typographic accessibility in more detail.** Supplied \[Articles\] - Typographic accessibility in more detail.docx. Basis for emotional, functional and technical accessibility, perceived size[...]

**S10 About Legibility and Readability.** Supplied \[Articles\] - Legibility and Readability.pdf. Basis for distinguishing character recognition from sustained reading and considering typography [...]

**S11 Writing Systems.** Supplied \[Articles\] - Writing Systems.pdf, headed "It's all squiggles to me". Basis for cultural and script awareness. The guide does not reproduce its simplified classi[...]

## Supplementary technical references

These primary references were checked on 28 October 2026 to clarify technical requirements and fill gaps beyond the attachments. The checklist in this guide is selective; a formal conformance assessme[...]

**V1 W3C Web Content Accessibility Guidelines 2.2.** Recommended digital baseline for this guide: Level AA, with additional reader-centred practices. Visual Presentation 1.4.8 is AAA; do not labe[...]

**V2 W3C WCAG2ICT.** Informative guidance for applying WCAG to non-web documents and software; it does not itself create normative requirements. Use the applicable procurement, organisational or [...]

**V3 W3C PDF techniques.** Practical techniques for alternatives, headings, tables, bookmarks, language, links, OCR and reading order. Techniques are examples, not a complete mandatory checklist. See [...]

**V4 RNIB Large and giant print.** Supports the common 16 to 18pt description of large print and the need to find a suitable reading format. The 12 to 14pt general starting range in this guide is an e[...]

**V5 W3C EPUB Accessibility 1.1.** Covers publication accessibility and discoverability metadata. Consult it alongside the relevant EPUB specification and selected WCAG target. See <https://www.w[...]
