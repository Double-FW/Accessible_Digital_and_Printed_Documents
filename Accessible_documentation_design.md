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

# Accessible documentation design

A practical guide for digital documents, screen and print editions, and printed books

Original version 1.0: 28 October 2026. Reconstructed edition: 7 November 2026.

> **Reconstruction note.** This edition restores incomplete passages in the supplied Markdown and repairs its escaping, headings, tables and links. Missing wording has been reconstructed from the surviving context; it is not a verbatim recovery. All twelve sections and their rule IDs are retained. The eleven attachments described in the original source register were not available for inspection during reconstruction. Their descriptions and the reported source comparisons require confirmation against the originals. The technical references in section 12 were checked separately during reconstruction. This edition does not establish what caused the original text loss.

Design for people to find, perceive, understand and use information in their preferred reading mode. Preserve meaning and navigation across visual reading, speech, braille, enlargement and print. Accessible documentation combines clear content, meaningful structure, usable presentation and reliable delivery.

This guide is for document designers, authors, editors, developers, publishers and teams using LLMs to generate documents. The original synthesis drew on eleven supplied sources. This reconstruction preserves its practical framework, distinguishes standards from editorial defaults, and makes the verification and evidence limitations explicit.

The central decision is to maintain one structured content source and create appropriate editions from it. One fixed page layout cannot satisfy every screen, paper size, reading distance or access need. Editions may differ in presentation while preserving substantive information and useful navigation.

## How to use this guide

Read sections 1 to 6 for every document. Apply section 7 to digital editions, section 8 when screen content must print, and section 9 to physical publications and books. Use section 10 before release. Section 11 translates the guidance into requirements for LLM workflows; section 12 explains provenance and the treatment of conflicting advice.

**Requirement language.** MUST and MUST NOT are release requirements within this guide when their stated scope applies. SHOULD means the default practice; a departure needs a recorded reason and review. MAY identifies an option. These terms describe this guide's production policy. They do not make every recommendation a requirement of WCAG or of law.

**Evidence categories.** STANDARD identifies a requirement from a named technical standard within its scope. SOURCE identifies practitioner guidance attributed to the original attachments. SYNTHESIS identifies a practical rule or editorial judgement combining that material. TEST means the choice needs evaluation in the actual context, rather than acceptance as a universal numerical threshold. A source attribution in this reconstructed edition is not evidence that the attachment has been rechecked.

**Scope.** ALL means every edition; DIGITAL means an electronic edition; HYBRID means content offered for both screen and print; PRINT means the physical output; BOOK means sustained reading in a publication. Combined labels apply to the specified combinations. An applicable standard, contract or organisational policy may impose additional requirements.

**Exceptions.** A design preference cannot waive an applicable standard or leave essential information inaccessible. Record the affected rule, context, reason, reader impact, equivalent alternative, evidence, responsible approving role and review date. An internal exception does not establish standards conformance. Record unresolved failures honestly.

## Contents

1. [Define the reading experience](#1-define-the-reading-experience)
2. [Build structure before appearance](#2-build-structure-before-appearance)
3. [Select and set type](#3-select-and-set-type)
4. [Use colour and space to support reading](#4-use-colour-and-space-to-support-reading)
5. [Preserve language and information in images](#5-preserve-language-and-information-in-images)
6. [Design tables forms and specialist content](#6-design-tables-forms-and-specialist-content)
7. [Deliver a usable digital edition](#7-deliver-a-usable-digital-edition)
8. [Make screen content work on paper](#8-make-screen-content-work-on-paper)
9. [Design physical documents and books](#9-design-physical-documents-and-books)
10. [Verify the delivered editions](#10-verify-the-delivered-editions)
11. [Translate the guide into LLM instructions](#11-translate-the-guide-into-llm-instructions)
12. [Source reconciliation and provenance](#12-source-reconciliation-and-provenance)

## 1 Define the reading experience

### PLAN01 Establish the audience and task

**ALL • MUST • SOURCE and SYNTHESIS.** Before styling, record the purpose, intended readers, languages and scripts, expected reading duration, delivery formats, devices or paper sizes, viewing conditions and actions the reader needs to complete. Identify which information is essential and which content is supplementary.

Include low vision, nonvisual access, motor access, cognitive and language needs where relevant. A quick-reference safety sheet and a novel need different navigation and reading rhythms. Where information supports urgent, consequential or unfamiliar decisions, make the required action and supporting explanation easy to locate. Do not assume that all readers have the same knowledge, equipment or capacity at the moment of use.

### PLAN02 Choose formats deliberately

**ALL • SHOULD • SYNTHESIS.** Prefer a reflowable reading edition for screen use. HTML suits online guidance; a structured word-processing file suits editable documents; reflowable EPUB suits books and sustained electronic reading. Use PDF when stable pagination or a fixed representation serves a documented need, and plan for its accessibility requirements separately.

A PDF containing page images is a poor primary reading edition. OCR can recover text but still needs correction, structure and reading-order work. A well-tagged PDF can support assistive technology when correctly authored and tested, but remains dependent on reader software and document construction. Where fixed layout prevents effective enlargement or adaptation, provide a suitable reflowable edition.

### PLAN03 Evaluate three separate outcomes

**ALL • MUST • SOURCE.** Assess emotional accessibility, functional accessibility and technical accessibility separately. Emotional accessibility concerns whether the communication feels appropriate, welcoming and credible to its audience. Functional accessibility concerns whether people can read, navigate, understand and use it. Technical accessibility concerns whether formats, encodings, semantics and software preserve access.

Brand expression belongs within this evaluation. Expressive typography may suit a short title but should not compromise instructions or body copy. Preference is useful evidence, but it is not a substitute for task performance or technical checks. Record tensions between these outcomes and resolve them through evidence and reader needs.

## 2 Build structure before appearance

### STRUCT01 Preserve a meaningful sequence

**ALL • MUST • SOURCE and SYNTHESIS.** Write content in a logical order before applying layout. Use real heading levels, paragraphs, lists, captions and table structures. Do not simulate headings with bold text alone, lists with typed symbols and spaces, or columns with repeated tabs.

Use a clear title and descriptive headings that explain each section. Nest heading levels consistently; do not choose a heading level for its size. In Word, use the Title style for the title and Heading styles for the section hierarchy. In HTML, use semantic headings appropriate to the page structure. Confirm that each export preserves the intended hierarchy rather than relying on the source appearance.

### STRUCT02 Make navigation useful

**ALL • SHOULD • SYNTHESIS.** Long documents need a table of contents, informative chapter or section names and predictable page or location references. Digital contents entries should be links. Provide PDF bookmarks and EPUB navigation where appropriate to the edition and its length. Print editions need accurate contents entries and page references.

Use meaningful cross-references such as “See section 6, Design tables forms and specialist content”, rather than “see above” or “the box on the right”. Update references and page numbers after layout changes. Digital links should explain their destination or purpose in context. Give repeated destinations consistent names and provide a clear return route from notes where supported.

### STRUCT03 Keep layout and reading order aligned

**DIGITAL • MUST; PRINT • SHOULD • SOURCE and SYNTHESIS.** The programmatic sequence must preserve the meaning conveyed visually. Anchor figures and their explanations near their first reference. Check the order of floating objects, text boxes, captions, sidebars and notes after export. A plausible visual arrangement does not prove a correct reading sequence.

Use one main text column as the default for guidance and continuous prose. Sidebars must not interrupt a sentence or contain information needed before the main text can be understood. Put essential instructions into the main sequence. Where columns are justified by the task, ensure that readers and software can follow the intended column order without ambiguity.

### STRUCT04 Write for comprehension

**ALL • SHOULD • SYNTHESIS.** State purpose and required actions early. Use familiar words, concrete examples, short informative headings and paragraphs organised around one idea. Explain necessary terminology and abbreviations at first use. Break procedures into ordered steps and state their prerequisites before the reader needs them.

Preserve precision and necessary qualifications. A readability score or “reading age” does not establish comprehension. Do not simplify technical, legal or literary content until its meaning changes. Where a summary helps, distinguish it from the full explanation and provide a direct route to that explanation. Check comprehension using realistic tasks with relevant readers.

## 3 Select and set type

### TYPE01 Evaluate actual letterforms

**ALL • MUST • SOURCE and TEST.** Evaluate each proposed body font at its intended sizes, weights and output conditions. Inspect uppercase I, lowercase l and numeral 1; O and 0; c, e, o and a; b, d, p and q; and combinations such as rn and m or cl and d. Include punctuation, currency signs, mathematical symbols and diacritics used by the content.

Look for distinctive shapes, open apertures, counters that remain clear, adequate spacing and strokes that survive the output process. An aperture is an opening in a letter; a counter is enclosed or partly enclosed space within a letter. Test meaningful words and paragraphs as well as isolated characters. A character comparison alone cannot establish sustained readability.

### TYPE02 Do not select by category or marketing claim alone

**ALL • MUST NOT • SOURCE and TEST.** Do not claim that serif, sans serif, humanist, a particular brand font or a “dyslexia font” is accessible to everyone. Do not present a typeface as a treatment for dyslexia or another condition without appropriate evidence for the specific claim.

A serif face can work well in a book; a sans serif can also work well. A single-storey or double-storey a may have different advantages for different readers. Familiarity, differentiation, language and script support, perceived size and production quality all affect the result. Select a practical default, evaluate it in context and support reader choice where the format allows it.

### TYPE03 Size for the reader and the medium

**ALL • SHOULD • SYNTHESIS and TEST.** Use the starting values below, then assess the actual font and conditions. These are house defaults for this guide, not universal accessibility thresholds. Perceived size varies between fonts at the same nominal point size.

| Context | Starting point | Required judgement |
| --- | --- | --- |
| Reflowable screen body | 1rem to 1.125rem with the root at 100 percent | Respect the reader's base size; test small screens and enlargement |
| General print and paginated documents | 12 to 14pt body | Prefer the larger end where feasible; proof at actual size |
| Large print | Begin discussion at 16 to 18pt | Confirm the reader's needs; larger sizes may be necessary |
| Sustained book reading | Start within the general print range | Compare real chapters, trim size, measure, leading and fatigue |
| Captions notes and tables | Prefer body size | Essential information must not become tiny to save space |

A 1rem setting often corresponds to 16 CSS pixels at a browser's default, but the reader can change that default. CSS pixels are not physical printer dots. Do not convert a web size into a print specification without checking the actual output. If content does not fit, change the layout, pagination or edition before reducing essential text below the agreed reader requirement.

### TYPE04 Balance measure and leading

**ALL • SHOULD • SOURCE and SYNTHESIS.** For Latin-script prose, aim initially for about 50 to 70 characters per line including spaces; around 65 is a useful working target. Shorter lines may be necessary on small screens or with enlarged text. Do not enforce a character target by preventing reflow or reducing the reader's chosen font size.

Start body line spacing around 1.5 times font size. Adjust for x-height, line length, script, reader feedback and output. A carefully tested book may work at roughly 1.3 to 1.5; this is an editorial option, not a universal accessibility guarantee. Ensure that accents, tall characters and lines do not collide. Spacing defaults and the ability to tolerate reader spacing overrides are separate considerations.

### TYPE05 Preserve regular spacing and emphasis

**ALL • SHOULD • SOURCE.** Begin with the font's designed letter spacing. Correct crowding if observed, but do not impose wide tracking everywhere. Avoid negative body tracking and stretched word spacing. Script-specific shaping must take priority over Latin-script spacing conventions.

Use sentence case and moderate emphasis. Reserve sustained italics, all capitals, underlining and heavy bold for contexts where their meaning justifies them. Preserve conventional acronyms and necessary notation. Make links recognisable without requiring colour discrimination, and use emphasis consistently so readers can understand its purpose.

### TYPE06 Use predictable alignment

**ALL • SHOULD • SOURCE and TEST.** Align prose to the reading start edge: left for ordinary left-to-right text, right for ordinary right-to-left text. Avoid centred paragraphs and fully justified body text as the default. Choose alignment by content: numerical columns, for example, may require a different consistent treatment.

If a printed book uses justification, treat it as a reviewed exception: use professional composition, language-aware hyphenation and restrained spacing; inspect every page for rivers, stretched short lines and distracting gaps. Confirm readability with representative passages. Do not reproduce fixed print justification in a reflowable edition when it prevents useful adaptation.

## 4 Use colour and space to support reading

### VIS01 Maintain contrast without relying on colour

**DIGITAL • MUST • STANDARD; PRINT • MUST • SYNTHESIS.** For WCAG 2.2 AA, ordinary text requires 4.5:1 contrast; qualifying large text requires 3:1. Large text means at least 18pt regular or 14pt bold, or an equivalent size. Apply the criterion's stated exceptions and scope. Relevant interface components and meaningful graphical objects have separate 3:1 non-text contrast requirements.

Use text labels, patterns, shapes or direct annotation for chart series, warnings and categories. Check every actual background, including table shading and states. Essential distinctions must survive loss of colour. Avoid placing text over visually variable imagery.

**PRINT.** Proof dark, sufficiently substantial text against a plain light substrate. Digital contrast calculations help select colours but do not certify reflected-light contrast on paper. Inspect production output under expected lighting, including greyscale printing and show-through.

### VIS02 Support personal presentation

**DIGITAL • MUST where supported • SOURCE and SYNTHESIS.** Do not obstruct font replacement, zoom, spacing changes or reader colour preferences. Check the result with alternate fonts, dark or light preferences, and supported reading modes. Preserve visible content, relationships and controls when presentation changes.

Some readers prefer off-white backgrounds or reduced brightness; others require strong contrast. Offer choice where possible, while keeping authored default themes within the selected contrast requirements. Do not prescribe one tint or contrast preference for an entire disability group. Test supported themes and document any limitations of the file format or reading software.

### VIS03 Create clear visual grouping

**ALL • SHOULD • SOURCE.** Use space and alignment to show relationships. Keep a caption with its figure and a heading with the beginning of its section. Use sufficient margins and a restrained hierarchy of sizes and weights. Related items should be closer together than unrelated groups, with enough separation to distinguish them.

Separate paragraphs consistently. Guidance often benefits from space after paragraphs; continuous book prose may use first-line indents. Avoid combining large indents and large gaps without a reason. Use paragraph and style settings rather than repeated spaces or empty paragraphs, so grouping survives editing and export.

## 5 Preserve language and information in images

### LANG01 Support the complete language

**ALL • MUST • SOURCE.** Verify glyph coverage, diacritics, contextual shaping, punctuation, numerals and direction for every supported language. Use meaningful native-language samples and native-language review where needed. Do not infer language support from the presence of a few characters in a font specimen.

Set the document's primary language and mark changes where the format supports this. Set direction separately when needed, including mixed-direction passages, URLs and numbers. Use script-appropriate line breaking, spacing and emphasis. Test selections, navigation and pronunciation in the delivered digital edition.

Font fallback must preserve meaning and remain readable. Check font loading failure, exports, embedded fonts and licensing. Do not convert prose to outlines to avoid embedding problems. Test search, copying and text extraction where these are supported. Fix missing or substituted characters at the source and regenerate affected outputs.

### IMAGE01 Keep text as text

**DIGITAL • MUST • SOURCE and SYNTHESIS.** Use actual text for prose, headings, instructions, labels and data. Do not flatten a page into an image. A screenshot, scanned letter, logo or historical artefact may need its visual appearance preserved, but meaningful information still needs an accessible equivalent. Apply the relevant standard's exceptions for images of text precisely rather than treating all images alike.

For an image of a quotation or message, transcribe the meaningful text accurately. If the exact appearance matters, describe that separately. Do not assume OCR built into a reader will recover the information correctly. Verify names, numbers, punctuation and reading order against the image.

### IMAGE02 Choose alternatives by purpose

**DIGITAL • MUST; PRINT • MUST for essential meaning • SOURCE and SYNTHESIS.** Provide concise alternative text for informative images, describing their information or purpose in context. For a functional image, explain the action or destination. Mark purely decorative images appropriately so they do not create unnecessary spoken output. Avoid repeating adjacent text without a reason.

Complex diagrams need a nearby explanation, extended description or accessible data representation. Short alt text should identify the graphic and point to the detailed equivalent. Do not hide an entire report or a large data table in an image's alternative text. Make extended descriptions easy to find and navigate.

Alt text is normally not printed. Therefore, essential interpretations must also appear in visible captions or body text in the print edition. A caption naming the subject is not necessarily a description of its meaning. Where visual or spatial information requires another format, plan an appropriate equivalent rather than assuming prose always suffices.

### IMAGE03 Handle charts and media explicitly

**ALL • MUST • SYNTHESIS.** Charts need a clear title, labelled axes, units, understandable series identification and a statement of the important finding. Supply underlying data when exact values matter, in a usable structure. Explain uncertainty, scales and exceptions that materially affect interpretation. Essential findings must be recoverable without seeing the chart.

Digital audio and video need alternatives appropriate to their content, including captions, transcripts and description of meaningful visuals. Printed editions need the essential information in text or another suitable static representation. A link or QR code to media alone does not make its meaning available offline.

## 6 Design tables forms and specialist content

### DATA01 Use tables for real relationships

**ALL • SHOULD • SYNTHESIS.** Use a table when readers need to compare repeated attributes, values or records. Use prose or lists for narrative instructions. Keep tables simple, with a clear title or caption and explicit row and column labels. Break an overly complex table into related simpler tables when this preserves the required comparison.

**DIGITAL • MUST.** Encode header relationships using the format's supported structure. Mark and repeat header rows in word-processing tables; verify associations after export. Complex merged headers require particular care and may need redesign or another representation. A shaded or bold row alone does not establish header semantics.

Avoid blank cells used for spacing, unexplained ditto marks and ambiguous empty values. State “not applicable”, “not recorded” or a defined symbol as appropriate. Align numbers consistently, including decimal places where useful, and state units. Do not use tables merely to position page furniture or ordinary prose.

### DATA02 Keep tables readable across pages

**PRINT and HYBRID • MUST • SOURCE and SYNTHESIS.** Repeat column headings on continuation pages and preserve column order. Keep ordinary rows together where possible, but allow a row that exceeds a page to break in a controlled way. Blanket rules preventing every table or row from breaking can crop or displace content.

Keep titles, notes and units associated with the table. Make continuation status clear when needed. Check that rules and shading survive ordinary printers and greyscale. Use sufficient cell padding and readable type. For wide tables, consider landscape pages, fewer columns or multiple related tables before reducing text size.

### FORM01 Make response tasks operable

**DIGITAL • MUST • SYNTHESIS.** Forms need persistent labels, instructions, identified required fields, meaningful field names, logical keyboard order and understandable errors. Do not use placeholder text as the only label. Associate labels and help with their fields using supported semantics. Make focus visible and provide usable selection, correction and submission controls.

**PRINT • MUST.** Provide adequate writing space, clearly labelled options and an obvious selection method. Do not rely on interactive validation or hover help. Preserve necessary instructions, consent information, submission routes and contact details. Where handwriting or physical handling would exclude readers, offer a suitable alternative response route.

### SPECIAL01 Keep specialist notation recoverable

**DIGITAL • SHOULD • SYNTHESIS.** Use structured equations where supported and test how they are spoken or navigated. If a formula must be an image, provide an accurate textual equivalent suited to the audience and task. Keep code as text, identify its language where useful, and make examples easy to select and copy without introducing errors.

Preserve significant whitespace, operators, minus signs and symbols. Explain uncommon notation. For print, test that subscripts, superscripts, punctuation and thin graph lines remain clear at actual size. Give complex scientific, musical or spatial content a specialist review and an appropriate alternative representation when needed.

## 7 Deliver a usable digital edition

### DIGITAL01 Preserve adaptability

**DIGITAL • MUST within the applicable standard scope • STANDARD.** Check WCAG text resizing to 200 percent and reflow at 320 CSS pixels for vertically scrolling web content, applying the criteria's exceptions. Reflow at that width is commonly tested at 400 percent zoom from a 1280 CSS-pixel viewport. Check text-spacing overrides at 1.5 times line height, 2 times font-size paragraph spacing, 0.12em letter spacing and 0.16em word spacing, within the criterion's scope.

Prefer relative web font sizing and flexible containers. Do not disable pinch zoom, fix prose container heights or truncate essential text with ellipses. Text resizing, page zoom and magnification require distinct practical checks. For non-web formats, identify the applicable requirements and use WCAG2ICT guidance rather than assuming identical software behaviour.

### DIGITAL02 Author word-processing documents semantically

**DIGITAL • MUST • SYNTHESIS.** Use named styles, logical headings, real lists, meaningful link text, document language and an informative title property. Provide image alternatives and simple tables with identified headers. Keep essential information in the main reading sequence rather than relying on headers, footers or floating text boxes alone.

Prefer spacing rules, page-break-before and keep-with-next to repeated empty lines. Avoid manual line breaks throughout body paragraphs. Ensure the document remains usable if fonts change. Run the authoring tool's accessibility checker, resolve relevant findings and review what it cannot assess. Test the actual reading and editing tasks in supported software.

### DIGITAL03 Export PDF as a separate quality gate

**DIGITAL PDF • MUST • SYNTHESIS supported by V3.** Use an export route that preserves tags and structure. Inspect the delivered PDF, not only its source. Check title, primary language, heading hierarchy, reading order, lists, table headers, image alternatives, bookmarks, links and form controls where present. Check that decorative material and repeated page furniture do not disrupt the meaningful sequence.

Check text extraction, search, copy and paste, and embedded font behaviour. Correct OCR errors, especially in names, numbers and symbols. Do not use security settings that prevent assistive access. A visually correct PDF can still have missing content, incorrect tags or an unusable keyboard sequence.

A PDF/UA target must specify the intended standard edition and a suitable validation process. Technical validation and human checks are complementary. Do not claim PDF/UA or WCAG conformance from tags alone, a successful export or a single checker result. Record the scope and limitations of the assessment and any alternative edition offered.

### DIGITAL04 Prepare electronic books for reading systems

**DIGITAL BOOK • SHOULD • SYNTHESIS supported by V5.** Prefer reflowable EPUB for continuous prose. Include semantic chapters, navigable contents, image alternatives, language metadata and useful accessibility metadata. Ensure notes, links and supplementary material can be reached and returned from. Preserve meaningful content when readers change type, size, spacing or theme.

Where print-equivalent pagination is supplied, implement appropriate page navigation and identify its source. Use fixed-layout EPUB only where the content requires it, with suitable alternatives. Validate the EPUB and inspect it in representative reading systems and assistive technology. Record metadata accurately, including known limitations; do not describe untested features as verified.

## 8 Make screen content work on paper

### HYBRID01 Keep meaning equivalent across editions

**HYBRID • MUST • SOURCE and SYNTHESIS.** Maintain a shared structured source and compare each output against it. Essential content must survive printing, including expanded disclosures, selected information, data, warnings and instructions. Decide whether the print edition represents the full publication or a clearly identified selection.

Remove purely operational controls, cookie banners, advertisements and redundant navigation. Replace interactions with static information or instructions. For example, print the currently relevant results and their filter criteria, or provide a complete static dataset when that is the intended edition. Do not remove an aside, footer or embedded object solely because its element type is commonly decorative; assess its content first.

### HYBRID02 Make references usable offline

**PRINT and HYBRID • MUST • SOURCE and SYNTHESIS.** Provide a meaningful destination for essential external links: a readable URL, a numbered reference with its URL, or another usable contact route. Use manageable addresses where an authoritative short route exists. Avoid exposing private, temporary, signed or session-specific addresses in print.

Use section names or page references for internal links. A QR code may supplement a short URL or reference but must not be the only route. Check the code at final print size and on the selected stock. If an external destination is necessary to complete a task, explain what readers will find and provide essential offline instructions where needed.

### HYBRID03 Define and test print layout

**HYBRID • SHOULD • SOURCE and SYNTHESIS.** In web publishing, scope print-specific rules to print media. Use physical units for page geometry and print text sizes; relative spacing remains useful within the typographic system. Define sensible page margins and test the actual target browsers and paper sizes.

Remove fixed positioning and screen-only overflow constraints that can crop print content. Size images to the available width. Keep headings with following text and short figures with captions. Let long tables and extended sections paginate naturally. Treat break-avoidance rules as preferences that must yield when a block cannot fit on a page. Verify the result rather than assuming every print rule is supported consistently.

### HYBRID04 Test ordinary printing conditions

**HYBRID • MUST • SOURCE and SYNTHESIS.** Inspect preview and a physical sample with backgrounds disabled, greyscale enabled and normal printer margins. Check duplex output where intended. Verify that text, chart distinctions, links, page numbers and important borders remain usable and that nothing is cropped, hidden or replaced by an empty space.

Test actual size as well as common “fit to page” settings; scaling can make a previously adequate font too small. Document necessary print instructions beside the download or in the publication. A successful preview does not prove that toner, paper, printer settings and binding will preserve the intended result.

## 9 Design physical documents and books

### PRINT01 Specify paper ink and binding together

**PRINT • SHOULD • SYNTHESIS and TEST.** Use a plain, low-glare stock with enough opacity to minimise distracting show-through. Compare physical proofs; paper weight alone does not establish opacity, surface behaviour or readability. Check the production process for faint strokes, ink spread, uneven coverage and loss of detail.

Off-white stock can be comfortable for some readers, but heavily tinted stock can reduce contrast. Avoid gloss, textured backgrounds and large reverse-out passages where they impede reading. Ensure photographs, diagrams, captions and body text remain clear in the same production conditions. Evaluate likely lighting and handling conditions.

Allow enough inner margin for the actual binding so readers do not have to force the book open or lose text in the gutter. Keep text away from trim and folds. Mirror margins correctly for left and right pages. Consider the publication's weight, opening behaviour and ease of holding or placing it on a support.

### BOOK01 Optimise for sustained reading

**BOOK • SHOULD • SOURCE and SYNTHESIS and TEST.** Test a representative chapter or substantial continuous passage, not only a title page or specimen sentence. Look for lost lines, rereading, visual fatigue, navigation difficulties and problems returning to the text after interruption. Gather feedback under realistic reading conditions.

Keep body typography stable across chapters. Use a calm, consistent hierarchy and predictable paragraph treatment. Avoid decorative drop capitals that disrupt word recognition or reading order. Avoid running important text across a spread where the binding obscures it. Readers should be able to identify chapter starts, locate their place and distinguish notes from the main narrative.

Keep notes readable and easy to return from. Where readers must consult a note immediately, do not bury it at the end of the book without a clear reference. Essential explanations belong in the main text when repeated movement between locations would prevent understanding. Preserve meaningful note relationships in alternative editions.

### BOOK02 Control composition without shrinking text

**PRINT BOOK • SHOULD • SYNTHESIS.** Review widows, orphans, isolated headings, awkward page turns and repeated hyphens. Avoid splitting short labels and number-unit combinations. Use language-aware composition and inspect discretionary breaks. Do not solve pagination problems by silently shrinking text or compressing spacing below the agreed reading requirements.

Balance line length, type size, leading, margins and trim size together. Larger type with excessively short lines can become tiring; wider pages with long lines can make return sweeps difficult. Adjust the page design as a system and compare representative passages again. Preserve the distinction between editorial polish and an essential access requirement.

### PRINT02 Offer appropriate alternative editions

**PRINT • MUST where needed to deliver equivalent access • SYNTHESIS.** Plan how readers obtain large print, accessible digital text, audio, braille or other appropriate formats. Do not treat an electronic file as accessible solely because it is digital. Match the edition to the reader's task and the nature of the content, including tables, diagrams and specialist notation.

Alternative editions should preserve substantive content, version and useful navigation. Make the request or download route clear and usable; do not require a reader to decipher inaccessible print to discover it. Agree practical availability and delivery arrangements, including timely access when the information supports a deadline or urgent decision.

## 10 Verify the delivered editions

### QA01 Combine automated manual and reader checks

**ALL • MUST • SOURCE and SYNTHESIS.** Automated tools detect some structural problems. Human review assesses meaning, descriptions, relationships and reading order. Reader testing establishes how well people can use the delivered publication for its intended tasks. Use all three appropriately and do not substitute one for the others.

Compare candidate typography under the same content and conditions. Include readers relevant to the audience, such as people with low vision, people who use screen readers or magnification, people with reading or cognitive access needs, and readers of the supported scripts. Resolve known technical barriers before asking readers to evaluate the overall experience. Record the sample and conditions; a small study cannot establish universal suitability.

### QA02 Apply the release checks

**ALL • MUST • SYNTHESIS.** For each relevant row below, record pass, fail, not tested or not applicable, with evidence and a reviewer. A failed critical requirement or missing essential information blocks release of the affected edition under this guide. A not-tested result is not a pass. Resolve the barrier, provide and verify equivalent access where appropriate, or escalate the release decision with the limitation recorded.

| Check | Method | Passing outcome |
| --- | --- | --- |
| Content and navigation | Compare source with final editions | No lost meaning; contents and references work |
| Structure and order | Inspect outline and semantic structure; read with assistive technology | Meaningful sequence and navigation |
| Typography and language | Inspect actual fonts and script samples | Clear text; correct shaping; no missing glyphs |
| Digital adaptation | Resize, reflow and apply supported overrides | No obscured, clipped or missing content |
| Images and data | Review descriptions and equivalent representations | Essential information is recoverable |
| Keyboard and forms | Traverse and complete real tasks | Controls labelled, reachable and usable |
| Export | Inspect final file and run relevant validation | No conversion defects or unsupported claims |
| Print | Inspect actual-size and greyscale physical proofs | Legible content; sound pagination and binding |
| Sustained reading | Test representative passages with readers | Findings reviewed; barriers addressed |

### QA03 Keep an honest release record

**ALL • MUST • SYNTHESIS.** Record document version, source revision, output files, applicable standard and edition, tested software, devices or print conditions, dates, methods, results, exceptions and unresolved limitations. Identify who reviewed the evidence and who is responsible for follow-up. Keep the record associated with the delivered version.

Use precise language: “heading structure checked” or “tested with the named reader and software”. Do not write “fully accessible” because a checker reported no errors. This reconstructed guide is a Markdown source document; it has not undergone assistive-technology testing, physical proofing, PDF validation or reader testing. Its presence in a repository does not verify editions subsequently generated from it.

## 11 Translate the guide into LLM instructions

### AI01 Preserve scope obligation and evidence

**LLM WORKFLOWS • MUST • SYNTHESIS.** An AGENTS.md version should preserve each stable rule ID, its scope, obligation and test. Do not compress conditional advice into universal rules. Keep numerical defaults, standards thresholds and reader-specific decisions distinguishable. Retain the reconstruction and evidence limitations when passing this material to another agent.

Use the rule IDs already attached to every requirement in sections 1 to 10. Keep a short execution sequence in AGENTS.md and link to a detailed rule register if the complete guide is too long. Instructions should identify what the agent must inspect, change and verify. Do not claim that an instruction file enforces behaviour unless supporting mechanisms exist and have been checked.

### AI02 Use a repeatable execution sequence

**LLM WORKFLOWS • MUST • SYNTHESIS.** The instruction file should require this sequence:

1. Read the task, existing document and project requirements. Identify output profiles, audience, languages, reading duration and applicable standards.
2. Record missing facts and provisional assumptions. Ask only when missing information materially changes access or prevents a necessary decision.
3. Build semantic structure and complete content before decorative styling. Select typography using the relevant scope and evidence.
4. Generate each requested edition from the shared source. Preserve language, headings, links, tables, image alternatives and reading order.
5. Inspect every rendered page for paginated outputs. Run available structural checks and the format-specific tests in this guide.
6. Repair defects and regenerate affected editions. Record unavailable checks as not tested and explain the practical limitation.
7. Deliver the files with a concise verification summary. Escalate unresolved access barriers to the responsible human; never invent approval or test evidence.

### AI03 Make every rule operational

**LLM WORKFLOWS • MUST • SYNTHESIS.** Represent a rule with the fields below. Split a multi-part rule into subordinate checks when implementing automated tests, retaining its parent ID. Do not mark an entire rule as passed because one subcheck succeeded. Distinguish an automated assertion from human or reader review.

| Field | What it must contain |
| --- | --- |
| id and version | Stable rule ID and revision |
| scope and trigger | Edition or element that activates the rule |
| obligation and basis | MUST, SHOULD or MAY; standard, source, synthesis or test |
| instruction | A concrete action or prohibited behaviour |
| parameters | Defaults, units, bounds and permitted context adjustments |
| verification | Method and observable passing outcome |
| evidence and status | Actual result, file or page, tool or reviewer, date and status |
| exception | Reason, impact, equivalent access, approving role and review date |

**Example using TYPE03.** Scope: PRINT body text. Obligation: SHOULD. Action: start at 12 to 14pt and judge perceived size on an actual-size proof. Basis: synthesis, with the original guide attributing background to S1, S3, S7 and V4; V4 specifically supports the large-print context rather than this general-print default. Verification: inspect representative pages, confirm the selected font size and scaling, and review relevant reader feedback. Status remains not tested until evidence exists. If a reader needs 20pt, record and apply that need rather than treating 14pt as a maximum.

### AI04 Set explicit stop and escalation conditions

**LLM WORKFLOWS • MUST • SYNTHESIS.** Flag missing essential content, broken script shaping, unreadable text, absent required alternatives, an unusable form, loss of digital structure or contradictory requirements. Pause release of an affected edition where an unresolved defect prevents essential access. Explain the impact and a concrete repair or alternative; do not invent a responsible person or an approval.

Do not fabricate alt text for an unseen image, infer that OCR is correct, copy source pass/fail font labels as universal facts, reduce text silently to meet a page count, or treat an inaccessible export as acceptable because the source was structured. When recovering truncated text, label reconstructed wording and unresolved provenance instead of presenting it as the lost original.

If an instruction conflicts with a mandatory applicable standard, identify the conflict and propose an accessible resolution. If a SHOULD rule conflicts with an evidenced reader need, record the adaptation and its basis. Work that can proceed independently may continue while an affected decision remains unresolved.

## 12 Source reconciliation and provenance

### Decisions made when combining the guidance

The supplied material was described as a mixture of practical experience, design-system conventions and research interpretations. It is not one normative standard or one peer-reviewed evidence base. This guide retains useful production advice while keeping technical obligations, house defaults and context-dependent judgements separate.

The comparisons below reconstruct the original synthesis's reported decisions. The source attachments were not inspected during reconstruction, so claims about their specific passages remain subject to confirmation. These comparisons must not be quoted as a new independent audit of those sources.

**Typeface categories and named fonts.** The original synthesis reports that S5 favours serif type for print, S8 includes categorical font pass/fail examples and claims about specific styles, and S1 cautions against category-based assumptions. This guide resolves the issue through inspection of actual letterforms, context and reader performance. No font category or commercial label guarantees access for everyone.

**Size and leading.** The original synthesis reports a BBC-specific scale and a 1.375 leading example in S3, discussion of larger spacing in S7, and differing body and paragraph sizes in S5. This guide gives explicit starting points, makes them adjustable and requires evaluation in the delivered medium. It does not present those defaults as WCAG minima.

**Web standards and paper.** The original synthesis reports direct mapping of WCAG concepts to print in S5. This guide distinguishes digital requirements from physical proofing. Numerical contrast in artwork does not establish the contrast or clarity of the printed result under reflected light.

**Print suppression and pagination.** The original synthesis identifies a risk that broad selectors in S5 could remove meaningful asides, footers or embedded information, and that blanket no-break rules could overflow long tables. This guide requires content-aware print selection and pagination checks against actual output.

**Spacing and group relationships.** The original synthesis reports that a sentence in S3 appears to reverse its intended grouping rule, while the heading example clarifies the relationship. This guide uses the operational principle that related items should be grouped more closely than unrelated items. Confirm the reported wording before proposing a correction to S3 itself.

**Contrast and comfort.** The original synthesis associates discussion of softened contrast with S7 and S10. This guide supports reader choice while preserving required authored digital contrast. Reduced contrast is not assumed to help every reader.

**Writing systems and neuroscience.** The original synthesis describes historical, neurological and classification claims in S9 to S11 that are unnecessary for production decisions. This guide does not reproduce those claims as scientific findings. It requires appropriate script support, contextual evaluation and evidence proportionate to any claim made.

### Supplied source register

The original guide states that all eleven attachments informed its synthesis. The records below retain the filenames, credits and roles visible in the supplied truncated text. Their full bibliographic details, page references and any missing qualifications require confirmation against the original attachments. No missing author, URL or publication date has been invented. A link to a similarly named live page would not establish the contents of the supplied version.

**S1 Accessible Typography for UX and Brand Systems.** Reported supplied file: `Accessible_Typography_for_UX_and_Brand_Systems(1).md`; version `1.0-semantic`; processed 18 September 2026. The pasted attribution is incomplete and requires confirmation. Reported role: contextual typography choices, actual letterform inspection and avoiding universal claims based on typeface category.

**S2 BBC GEL Images of text.** Reported supplied file: `BBC GEL _ Images of text.pdf`, particularly pages 1 to 3; article published 30 May 2024. Reported role: contextual image descriptions, transcription and equivalents for meaningful text presented within images.

**S3 GEL Typography.** Reported supplied file: `GEL _ Typography.pdf`; version 0.1.0; particularly pages 2 to 7. Reported role: relative sizing, measure, spacing, alignment, links and adaptability. BBC-specific font choices and scales are contextual examples rather than universal prescriptions.

**S4 BBC Accessibility for Products Images of text.** Reported supplied file: `Images of text - Accessibility for Products - BBC.pdf`, pages 1 to 2. Reported role: actual text and accessible equivalents. Historical product guidance must be interpreted in its original context rather than assumed to define a current standard.

**S5 Print Friendly Style Sheets Accessibility Best Practices.** Reported supplied file: `PRINT_ACCESSIBILITY_BEST_PRACTICES.md`; copyright 2026 Mike Gifford; the original register reports an `AGPL-3.0-or-later` licence statement. Reported role: print adaptation and print stylesheet considerations. Check the actual licence and provenance before redistributing source text or code; this reconstruction does not determine licensing obligations.

**S6 BBC Accessibility for Products Styling and readability.** Reported supplied file: `Styling and readability - Accessibility for Products - BBC.pdf`, pages 1 to 3. Reported role: separation of content and presentation, readable styling and support for adaptation.

**S7 Typography DDP Accessibility.** Reported supplied file: `Typography _ DDP Accessibility.pdf`, particularly pages 1 to 18. Reported role: contextual font selection, measure, resizing, weight, spacing, direction and presentation preferences. The full source title and publication details require confirmation.

**S8 Typeface Accessibility Guide GAAD 2020.** Reported supplied file: `Typeface Accessibility.pdf`. The pasted register credits Bruno Maag, David Bailey, Gareth Ford Williams and Michael Mathews. Reported role: letterform inspection and practical type evaluation. Specific font classifications are not adopted here as universal accessibility pass/fail findings.

**S9 Typographic accessibility in more detail.** Reported supplied file: `[Articles] - Typographic accessibility in more detail.docx`. Reported role: emotional, functional and technical accessibility, perceived size and contextual typography decisions. Scientific explanations require their own evidence before reuse as factual claims.

**S10 About Legibility and Readability.** Reported supplied file: `[Articles] - Legibility and Readability.pdf`. Reported role: distinguishing character recognition from sustained reading and considering typography in context. Reader preferences are not treated as universal prescriptions.

**S11 Writing Systems.** Reported supplied file: `[Articles] - Writing Systems.pdf`, headed “It's all squiggles to me”. Reported role: cultural and script awareness. Simplified classifications and historical or neurological explanations are not reproduced as production requirements.

### Supplementary technical references

The original document claimed a reference check on 28 October 2026. That historical check cannot be independently established from the paste. The primary references below were accessed or located on 7 November 2026 for this reconstruction. This is a selective production guide; a formal conformance assessment must cover every applicable requirement in its chosen standard and edition.

**V1 W3C Web Content Accessibility Guidelines 2.2.** Recommended digital baseline for this guide: Level AA, supplemented by reader-centred practices. Visual Presentation, success criterion 1.4.8, is Level AAA; the measure and presentation defaults in this guide must not be labelled AA requirements on that basis. Consult the full criteria and their exceptions for contrast, resizing, reflow and spacing. See [WCAG 2.2](https://www.w3.org/TR/WCAG22/).

**V2 W3C WCAG2ICT.** Informative guidance for applying WCAG to non-web documents and software; it does not itself create normative requirements. Identify the applicable organisational, contractual or other adopted standard before making a conformance claim. See [Guidance on Applying WCAG 2 to Non-Web Information and Communications Technologies](https://www.w3.org/TR/wcag2ict-22/).

**V3 W3C PDF techniques.** Practical examples for implementing and checking PDF accessibility features. Techniques do not form an exhaustive mandatory checklist, and a particular technique is not the only possible way to satisfy a criterion. See the [PDF section of Techniques for WCAG 2.2](https://www.w3.org/WAI/WCAG22/Techniques/#pdf). The current PDF section was located through W3C's indexed technique material; direct retrieval of a separate PDF-category URL failed during reconstruction. No PDF validation was performed on this Markdown guide.

**V4 RNIB Large and giant print.** RNIB describes large print as generally 16 to 18pt and discusses ways to find a suitable reading format. The 12 to 14pt general-print starting range in this guide is an editorial default, not a minimum established by that page. See [RNIB: Large and giant print](https://www.rnib.org.uk/living-with-sight-loss/independent-living/leisure/reading-and-books/large-and-giant-print/).

**V5 W3C EPUB Accessibility 1.1.** Covers publication accessibility and discoverability metadata. Consult it alongside the relevant EPUB specification and selected WCAG target. Its existence does not establish the accessibility of a generated EPUB; assess the publication and its metadata. See [EPUB Accessibility 1.1](https://www.w3.org/TR/epub-a11y-11/).
