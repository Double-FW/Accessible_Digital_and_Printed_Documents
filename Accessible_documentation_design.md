Accessible documentation design

A practical guide for digital documents, screen and print editions, and printed books

Version 1.0 • 28 October 2026

Design for people to find, perceive, understand and use information in their preferred reading mode. Preserve meaning and navigation across visual reading, speech, braille, enlargement and print. A polished page is only one part of an accessible document.

This guide is for document designers, authors, editors, developers, publishers and teams using LLMs to generate documents. It combines the eleven supplied sources, resolves conflicting advice and adds implementation guidance for document structure, exports, physical production and quality assurance. Source IDs appear throughout; the source register explains their status. The guide is not a certification of a font, file format or individual publication.

The central decision is to maintain one structured content source and create appropriate editions from it. One fixed page layout cannot satisfy every screen, paper size, reading distance or access need. Shared content should remain equivalent even when presentation differs.

# How to use this guide

Read sections 1 to 6 for every document. Apply section 7 to digital editions, section 8 when screen content must print, and section 9 to physical publications and books. Use section 10 before release. Sections 11 and 12 explain how to turn the guidance into reliable LLM instructions and how the sources were reconciled.

**Requirement language.** MUST and MUST NOT are release requirements within this guide when their stated scope applies. SHOULD means the default practice; a departure needs a recorded reason and review. MAY identifies an option. These labels express this guide's policy, not a claim that every item is a statutory or WCAG requirement.

**Evidence categories.** STANDARD identifies a requirement from a named technical standard within its scope. SOURCE identifies supplied practitioner guidance. SYNTHESIS identifies a practical rule or starting value developed for this guide. TEST identifies a decision that needs evaluation with intended readers. A rule can combine categories.

**Scope.** ALL means every edition; DIGITAL means an electronic edition; HYBRID means content offered for both screen and print; PRINT means the physical output; BOOK means sustained reading in print or an electronic book. A hybrid publication must satisfy both relevant sets of checks.

**Exceptions.** A design preference cannot waive an applicable standard or leave essential information inaccessible. Record the affected rule, context, reason, reader impact, equivalent alternative, evidence, approving role and review date. An untested requirement remains untested, not passed.

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

**ALL • MUST • SOURCE and SYNTHESIS.** Before styling, record the purpose, intended readers, languages and scripts, expected reading duration, delivery formats, devices or paper sizes, viewing conditions and production constraints. Identify whether readers will scan, compare, complete a task or read continuously. Capture known access needs without assuming that a diagnosis predicts a person's preferences. \[S1, S7, S9, S10\]

Include low vision, nonvisual access, motor access, cognitive and language needs where relevant. A quick-reference safety sheet and a novel need different navigation and reading rhythms. Where information is missing, record reasonable provisional assumptions and proceed with a reversible design. Seek input when the answer materially affects access, such as a requested large-print size or required script.

## PLAN02 Choose formats deliberately

**ALL • SHOULD • SYNTHESIS.** Prefer a reflowable reading edition for screen use. HTML suits online guidance; a structured word-processing file suits editable documents; reflowable EPUB suits books. Use PDF where stable pagination or exact layout matters, and provide appropriate structure and alternatives. No format is accessible merely because of its extension.

A PDF containing page images is a poor primary reading edition. OCR can recover text but still needs correction, structure and reading-order work. A well-tagged PDF can support assistive technology while remaining awkward on small screens. Offer an equivalent reflowable edition when fixed layout prevents comfortable reading.

## PLAN03 Evaluate three separate outcomes

**ALL • MUST • SOURCE.** Assess emotional accessibility, functional accessibility and technical accessibility separately. Emotional accessibility concerns whether the communication feels appropriate, credible and welcoming. Functional accessibility concerns recognition, reading, comprehension and task success. Technical accessibility concerns whether files, fonts, structure and software preserve access. \[S1, S9\]

Brand expression belongs within this evaluation. Expressive typography may suit a short title but should not compromise instructions or body copy. Preference is useful evidence, but it is not a substitute for performance. Legibility means recognising characters accurately; readability means reading connected text with manageable effort. Evaluate comprehension and fatigue as well as reading speed.

# 2 Build structure before appearance

## STRUCT01 Preserve a meaningful sequence

**ALL • MUST • SOURCE and SYNTHESIS.** Write content in a logical order before applying layout. Use real heading levels, paragraphs, lists, captions and table structures. Do not simulate headings with bold text alone, lists with manually typed symbols, or columns with spaces and tabs. \[S3, S6; V3\]

Use a clear title and descriptive headings that explain each section. Nest heading levels consistently; do not choose a heading level for its size. In Word, use the Title style for the title and Heading 1 onwards for the body hierarchy. In HTML, use a logical heading outline with an identifiable main heading. Set presentation through styles.

## STRUCT02 Make navigation useful

**ALL • SHOULD • SYNTHESIS.** Long documents need a table of contents, informative chapter or section names and predictable page or location references. Digital contents entries should be links. PDF bookmarks should reflect the hierarchy. Printed books and reference works may also need an index, glossary and lists of figures or tables.

Use meaningful cross-references such as "See section 6, Tables and complex information", rather than "see above" or "the box on the right". Update references and page numbers after layout changes. Digital notes should provide a usable return route. Never make essential context available only through a header, footer or marginal note.

## STRUCT03 Keep layout and reading order aligned

**DIGITAL • MUST; PRINT • SHOULD • SOURCE and SYNTHESIS.** The programmatic sequence must preserve the meaning conveyed visually. Anchor figures and their explanations near their first reference. Prefer inline objects to floating text boxes when the latter disrupt reading order. Multi-column pages need explicit checking; a screen reader must not alternate accidentally between columns. \[S6; V3\]

Use one main text column as the default for guidance and continuous prose. Sidebars must not interrupt a sentence or contain information needed before the main text can be understood. Put essential instructions into the main sequence. Give supplementary material a heading and a clear entry and exit point.

## STRUCT04 Write for comprehension

**ALL • SHOULD • SYNTHESIS.** State purpose and required actions early. Use familiar words, concrete examples, short informative headings and paragraphs organised around one idea. Explain necessary specialist terms and abbreviations on first use. Use numbered lists for sequences and bullets for parallel items.

Preserve precision and necessary qualifications. A readability score or "reading age" does not establish comprehension. Do not simplify technical, legal or literary content until its meaning changes. Use reader testing and, where needed, separately prepared Easy Read or plain-language editions. Easy Read is a distinct editorial approach, not just large text and pictures. Label adaptations and keep them aligned with the full edition.

# 3 Select and set type

## TYPE01 Evaluate actual letterforms

**ALL • MUST • SOURCE and TEST.** Evaluate each proposed body font at its intended sizes, weights and output conditions. Inspect uppercase I, lowercase l and numeral 1; O and 0; c, e, o and a; b, d, p and q; and combinations such as rn, m, cl and d. Include punctuation, numerals, accents, names, symbols and realistic words. \[S1, S7, S8\]

Look for distinctive shapes, open apertures, counters that remain clear, adequate spacing and strokes that survive the output process. An aperture is an opening in a letter; a counter is enclosed or partly enclosed space. X-height is the height of the main lowercase body. These features affect perceived size and recognition. They are selection criteria, not an automatic pass or fail certification.

## TYPE02 Do not select by category or marketing claim alone

**ALL • MUST NOT • SOURCE and TEST.** Do not claim that serif, sans serif, humanist, a particular brand font or a "dyslexia font" is accessible to everyone. Do not present a typeface as a treatment for a reading condition. Compare plausible candidates in the intended context, including long passages where sustained reading matters. \[S1, S7, S8\]

A serif face can work well in a book; a sans serif can also work well. A single-storey or double-storey a may have different advantages for different readers. Familiarity, differentiation, language and reading experience matter. Use expressive or highly condensed designs sparingly, and do not condense essential text merely to fit a page.

## TYPE03 Size for the reader and the medium

**ALL • SHOULD • SYNTHESIS and TEST.** Use the starting values below, then assess the actual font and conditions. These are house defaults for this guide, not universal accessibility thresholds. Point size alone does not establish perceived size. \[S1, S3, S7; V4\]

| **Context**                           | **Starting point**                            | **Required judgement**                                             |
| ------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------ |
| Reflowable screen body                | 1rem to 1.125rem with the root at 100 percent | Respect the reader's base size; test small screens and enlargement |
| General print and paginated documents | 12 to 14pt body                               | Prefer the larger end where feasible; proof at actual size         |
| Large print                           | Begin discussion at 16 to 18pt                | Confirm the reader's needs; larger sizes may be necessary          |
| Sustained book reading                | Start within the general print range          | Compare real chapters, trim size, measure, leading and fatigue     |
| Captions notes and tables             | Prefer body size                              | Essential information must not become tiny to save space           |

A 1rem setting often corresponds to 16 CSS pixels at a browser's default, but the reader can change that default. CSS pixels are not physical printer dots. Do not convert a web size into a print size and assume equivalent readability. If a page becomes crowded, edit or restructure it, increase the page count or create another edition before shrinking essential text.

## TYPE04 Balance measure and leading

**ALL • SHOULD • SOURCE and SYNTHESIS.** For Latin-script prose, aim initially for about 50 to 70 characters per line including spaces; around 65 is a useful working target. Shorter lines may be necessary on small screens or in enlarged editions. Do not reduce text size to force this range. A CSS ch unit measures the advance of zero, not the average character, so verify rendered lines. \[S3, S7\]

Start body line spacing around 1.5 times font size. Adjust for x-height, line length, script, reader feedback and output. A carefully tested book may work at roughly 1.3 to 1.5; this is an editorial option, not an automatic exception to a separately required standard. Avoid rigid "exactly" line heights that clip accents, equations or enlarged text. Keep headings closer to the material they introduce than to the preceding section.

## TYPE05 Preserve regular spacing and emphasis

**ALL • SHOULD • SOURCE.** Begin with the font's designed letter spacing. Correct crowding if observed, but do not impose wide tracking everywhere. Avoid negative body tracking and stretched word spacing. Allow user overrides in digital formats that support them. Do not apply Latin tracking rules mechanically to joining scripts. \[S1, S3, S7\]

Use sentence case and moderate emphasis. Reserve sustained italics, all capitals, underlining and heavy bold for contexts where their meaning justifies them. Preserve conventional acronyms and necessary italic conventions. Use true bold and italic faces where available. Underline links rather than using underlining as general decoration. Avoid thin body weights and extreme thick-to-thin stroke contrast at reading sizes.

## TYPE06 Use predictable alignment

**ALL • SHOULD • SOURCE and TEST.** Align prose to the reading start edge: left for ordinary left-to-right text, right for ordinary right-to-left text. Avoid centred paragraphs and fully justified prose as defaults. Uneven word gaps and rivers can make line tracking harder. \[S3, S7\]

If a printed book uses justification, treat it as a reviewed exception: use professional composition, language-aware hyphenation and restrained spacing; inspect every page for rivers, stretched short lines and repeated hyphens. Compare with ragged-edge samples and test sustained reading. Preserve an adaptable digital edition. Do not imply that justification alone fails every WCAG AA assessment; the stronger visual-presentation criterion is at AAA.

# 4 Use colour and space to support reading

## VIS01 Maintain contrast without relying on colour

**DIGITAL • MUST • STANDARD; PRINT • MUST • SYNTHESIS.** For the selected WCAG AA digital baseline, text contrast is at least 4.5:1, or 3:1 for large text: 18pt regular or 14pt bold and above. Relevant graphical objects and interface boundaries need 3:1 against adjacent colours, subject to the standard's exceptions. Colour must not be the only carrier of meaning. \[V1\]

Use text labels, patterns, shapes or direct annotation for chart series, warnings and categories. Check text on every actual background, including shaded table rows and selected states. Avoid text over photography or texture; a numerically sufficient pair of sampled colours does not remove visual interference. \[S3, S7\]

**PRINT.** Proof dark, sufficiently substantial text against a plain light substrate. Digital contrast calculations are useful when choosing artwork colours, but do not certify reflected-light contrast on paper. Ink, paper, glare, show-through and printer settings change the result. Check physical samples, including greyscale output. Do not use pale grey text simply because it appears elegant on a bright monitor.

## VIS02 Support personal presentation

**DIGITAL • MUST where supported • SOURCE and SYNTHESIS.** Do not obstruct font replacement, zoom, spacing changes or reader colour preferences. Check the result with alternate fonts, dark or light themes and high-contrast settings where available. Essential borders, labels and focus indicators must remain perceivable. \[S1, S6, S7\]

Some readers prefer off-white backgrounds or reduced brightness; others require strong contrast. Offer choice where possible, while keeping authored default themes within the selected contrast requirements. Do not assert that cream paper, grey text or dark mode is best for everyone. In print, choose paper and ink through proofing rather than translating a screen theme directly.

## VIS03 Create clear visual grouping

**ALL • SHOULD • SOURCE.** Use space and alignment to show relationships. Keep a caption with its figure and a heading with the beginning of its section. Use sufficient margins and a restrained hierarchy; avoid excessive decoration, watermarks through text and crowded boxes. \[S3, S7\]

Separate paragraphs consistently. Guidance often benefits from space after paragraphs; continuous book prose may use first-line indents. Avoid combining large indents and large gaps without a reason. Usually omit a first-line indent after a heading. Do not insert empty paragraphs to manufacture vertical spacing. Use paragraph styles and deliberate breaks.

# 5 Preserve language and information in images

## LANG01 Support the complete language

**ALL • MUST • SOURCE.** Verify glyph coverage, diacritics, contextual shaping, punctuation, numerals and direction for every supported language. Use meaningful native-language samples and native-reader review. Correctly joined Arabic and correctly formed Indic conjuncts matter as much as Latin character differentiation. \[S1, S7, S9, S11\]

Set the document's primary language and mark changes where the format supports this. Set direction separately when needed, including mixed-direction passages, URLs and numbers. Use script-appropriate line breaking and spacing. Do not substitute transliteration, remove accents or distort a script to match a Latin brand aesthetic.

Font fallback must preserve meaning and remain readable. Check font loading failure, exports, embedded fonts and licensing. Do not convert prose to outlines to avoid embedding problems. Test search, copying and text extraction as well as appearance; a visually correct glyph may still have an incorrect text mapping.

## IMAGE01 Keep text as text

**DIGITAL • MUST • SOURCE and SYNTHESIS.** Use actual text for prose, headings, instructions, labels and data. Do not flatten a page into an image. A screenshot, scanned letter, logo or historical facsimile can be necessary, but must have an appropriate accessible equivalent. Vector artwork is not automatically accessible text. \[S2, S4, S6\]

For an image of a quotation or message, transcribe the meaningful text accurately. If the exact appearance matters, describe that separately. Do not assume OCR built into a reader will recover the information. A graphic used as a heading also needs a real heading in the document structure.

## IMAGE02 Choose alternatives by purpose

**DIGITAL • MUST; PRINT • MUST for essential meaning • SOURCE and SYNTHESIS.** Provide concise alternative text for informative images, describing the information or purpose in context. For a functional image, convey the action or destination. Mark purely decorative images as decorative using the format's mechanism. \[S2, S4; V3\]

Complex diagrams need a nearby explanation, extended description or accessible data representation. Short alt text should identify the graphic and point to the detailed equivalent. Do not hide an entire chart or article inside a long alt-text field. Avoid unnecessary repetition between alt text, captions and adjacent prose, but retain all necessary information.

Alt text is normally not printed. Therefore, essential interpretations must also appear in visible captions or body text in the print edition. A caption naming the subject is not necessarily a description of what the image communicates. Remove decorative details from descriptions unless they contribute to the meaning.

## IMAGE03 Handle charts and media explicitly

**ALL • MUST • SYNTHESIS.** Charts need a clear title, labelled axes, units, understandable series identification and a statement of the important finding. Supply the underlying data when exact values matter. Do not use position or colour alone to explain a diagram; name the relevant elements.

Digital audio and video need the alternatives appropriate to their content, including captions, transcripts and description of meaningful visuals. Printed editions need the essential information in text or figures plus a usable reference to optional media. Do not print an empty player rectangle and treat the content as preserved.

# 6 Design tables forms and specialist content

## DATA01 Use tables for real relationships

**ALL • SHOULD • SYNTHESIS.** Use a table when readers need to compare repeated attributes, values or records. Use prose or lists for narrative instructions. Keep tables simple, with a clear title or introduction, explicit units and unambiguous row and column headings.

**DIGITAL • MUST.** Encode header relationships using the format's supported structure. Mark and repeat header rows in word-processing tables; verify associations after export. Complex merged headers often need more explicit structure or redesign. Do not assume that bold cells establish headers. \[V3\]

Avoid blank cells used for spacing, unexplained ditto marks and ambiguous empty values. State "not applicable", "not recorded" or a defined symbol as appropriate. Align numbers consistently, including decimal alignment where useful; align prose to the reading start edge. Do not shrink a wide table until it fits. Split it logically with repeated identifying columns, provide a landscape page, or offer a more suitable accessible representation.

## DATA02 Keep tables readable across pages

**PRINT and HYBRID • MUST • SOURCE and SYNTHESIS.** Repeat column headings on continuation pages and preserve column order. Keep ordinary rows together where possible, but allow a row that exceeds a page to split with clear continuation. A blanket "never split any table" rule can create overflow or blank pages. \[S5\]

Keep titles, notes and units associated with the table. Make continuation status clear when needed. Check that table rules and shading survive ordinary printers and greyscale. Use sufficient cell padding; do not use fixed heights that crop text.

## FORM01 Make response tasks operable

**DIGITAL • MUST • SYNTHESIS.** Forms need persistent labels, instructions, identified required fields, meaningful field names, logical keyboard order and understandable errors. Do not use placeholder text as the only label. Check keyboard operation, visible focus, screen-reader labels and saving or submitting completed responses. Apply the relevant interaction requirements of the selected standard. \[V1, V3\]

**PRINT • MUST.** Provide adequate writing space, clearly labelled options and an obvious selection method. Do not rely on interactive validation or hover help. Preserve necessary instructions, consent wording and return details. Where handwriting or signing is a barrier, provide an appropriate alternative completion route.

## SPECIAL01 Keep specialist notation recoverable

**DIGITAL • SHOULD • SYNTHESIS.** Use structured equations where supported and test how they are spoken or navigated. If a formula must be an image, provide an accurate textual equivalent suited to the audience. Keep code selectable, use a readable monospaced face where useful, and wrap or provide accessible horizontal navigation without cutting off content.

Preserve significant whitespace, operators, minus signs and symbols. Explain uncommon notation. For print, test that subscripts, superscripts, punctuation and thin graph lines remain clear at actual size. Do not solve a notation problem with a description that changes its mathematical or technical meaning.

# 7 Deliver a usable digital edition

## DIGITAL01 Preserve adaptability

**DIGITAL • MUST within the applicable standard scope • STANDARD.** Test text enlargement to 200 percent without loss. For reflowing web content, test at 320 CSS pixels wide, equivalent to a 1280px viewport at 400 percent zoom; two-dimensional content has defined exceptions. Test supported spacing overrides together: line height 1.5, paragraph spacing 2, letter spacing 0.12 and word spacing 0.16 times font size. These are tolerance tests, not compulsory default settings. \[V1\]

Prefer relative web font sizing and flexible containers. Do not disable pinch zoom, fix text container heights or truncate essential prose with ellipses. Text-only resizing, page zoom and screen magnification are different conditions: test the relevant ones. Fixed-layout documents need an evaluation suited to their reader software and an equivalent adaptable edition when necessary. \[S3, S7; V2\]

## DIGITAL02 Author word-processing documents semantically

**DIGITAL • MUST • SYNTHESIS.** Use named styles, logical headings, real lists, meaningful link text, document language and an informative title property. Provide image alternatives and simple tables with marked headings. Keep essential content in the main document flow. Check the navigation pane and keyboard traversal.

Prefer spacing rules, page-break-before and keep-with-next to repeated empty lines. Avoid manual line breaks throughout body paragraphs. Ensure the document remains usable if fonts change. Run the authoring application's accessibility checker, then review warnings and perform manual checks. A checker cannot establish whether a description is accurate or a chapter is easy to read.

## DIGITAL03 Export PDF as a separate quality gate

**DIGITAL PDF • MUST • SYNTHESIS supported by V3.** Use an export route that preserves tags and structure. Inspect the delivered PDF, not only its source. Check the title, primary language, headings, lists, table semantics, image alternatives, links, bookmarks, reading order and form tab order. Mark decorative or repetitive page furniture as artefacts where appropriate.

Check text extraction, search, copy and paste, and embedded font behaviour. Correct OCR errors, especially in names, numbers and symbols. Do not use security settings that prevent assistive access. A print-to-PDF route may discard semantics; never assume its output is an accessible reading edition.

A PDF/UA target must specify the intended edition and a suitable validation process. Technical validation and human checks are complementary. Do not claim PDF/UA or WCAG conformance from tags alone, a visual proof or a generic "passed" message. The checks here are not a complete conformance assessment.

## DIGITAL04 Prepare electronic books for reading systems

**DIGITAL BOOK • SHOULD • SYNTHESIS supported by V5.** Prefer reflowable EPUB for continuous prose. Include semantic chapters, navigable contents, image alternatives, language metadata and useful note navigation. Verify reading order, reader styling, text-to-speech, enlargement and different screen sizes. Describe accessibility features and limitations accurately in publication metadata.

Where print-equivalent pagination is supplied, implement appropriate page navigation and identify its source. Use fixed-layout EPUB only where the content requires it, with suitable alternatives. Validate the package and perform reading-system and assistive-technology checks; packaging validity alone does not demonstrate accessibility.

# 8 Make screen content work on paper

## HYBRID01 Keep meaning equivalent across editions

**HYBRID • MUST • SOURCE and SYNTHESIS.** Maintain a shared structured source and compare each output against it. Essential content must survive printing, including expanded disclosures, selected filters, chart context, footnotes and media equivalents. Do not hide all sidebars, footers, forms or embedded content indiscriminately: any of them may contain necessary information. \[S5, S6\]

Remove purely operational controls, cookie banners, advertisements and redundant navigation. Replace interactions with static information or instructions. For example, print the currently relevant results and identify the filter used; do not print an empty interactive chart. Ensure a useful fallback when print styles fail.

## HYBRID02 Make references usable offline

**PRINT and HYBRID • MUST • SOURCE and SYNTHESIS.** Provide a meaningful destination for essential external links: a readable URL, a numbered reference with its URL, or another usable contact route. Avoid appending long tracking URLs to every link. Resolve relative URLs and remove unnecessary tracking parameters where the destination remains correct. \[S5\]

Use section names or page references for internal links. A QR code may supplement a short URL or reference but must not be the only route. Check the code at final print size and on the selected stock. A link to an online alternative does not make inaccessible print itself usable for every reader.

## HYBRID03 Define and test print layout

**HYBRID • SHOULD • SOURCE and SYNTHESIS.** In web publishing, scope print-specific rules to print media. Use physical units for page geometry and print text sizes; relative spacing remains useful. Retain genuine heading and table structure. Set margins and page size for the intended output, then test likely alternatives such as A4 and Letter. \[S5\]

Remove fixed positioning and screen-only overflow constraints that can crop print content. Size images to the available width. Keep headings with following text and short figures with captions. Let long tables and text blocks paginate. Apply widow and orphan controls without creating excessive gaps. Printed page numbering and running headers depend on the actual renderer; verify their output rather than assuming CSS support.

## HYBRID04 Test ordinary printing conditions

**HYBRID • MUST • SOURCE and SYNTHESIS.** Inspect preview and a physical sample with backgrounds disabled, greyscale enabled and normal printer margins. Check duplex output where intended. Verify that text, chart labels, borders and references remain visible. Do not depend on a browser printing background colours. \[S5\]

Test actual size as well as common "fit to page" settings; scaling can make a previously adequate font too small. Document any necessary print instructions beside the download or in the publication. A browser's saved PDF must pass the digital checks separately if it is distributed as a reading edition.

# 9 Design physical documents and books

## PRINT01 Specify paper ink and binding together

**PRINT • SHOULD • SYNTHESIS and TEST.** Use a plain, low-glare stock with enough opacity to minimise distracting show-through. Compare physical proofs; paper weight alone does not establish opacity. Check ink density, fine strokes, colour reproduction, reverse-side interference and reflected light under realistic conditions.

Off-white stock can be comfortable for some readers, but heavily tinted stock can reduce contrast. Avoid gloss, textured backgrounds and large reverse-out passages where they impede reading. Ensure photographs or heavy ink on the reverse do not intrude through the text page. These are production decisions to test, not universal paper specifications.

Allow enough inner margin for the actual binding so readers do not have to force the book open or lose text in the gutter. Keep text away from trim and folds. Mirror margins correctly for left and right pages. Consider book weight, thickness, opening resistance, page turning and use with a stand or magnifier. A lay-flat binding may help where feasible.

## BOOK01 Optimise for sustained reading

**BOOK • SHOULD • SOURCE and SYNTHESIS and TEST.** Test a representative chapter or substantial continuous passage, not only a title page or specimen sentence. Look for lost lines, rereading, visual discomfort, fatigue and falling comprehension. Use the intended paper or reading device and realistic lighting. \[S1, S8, S9, S10\]

Keep the body typography stable across chapters. Use a calm, consistent hierarchy and predictable paragraph treatment. Avoid decorative drop capitals that disrupt word recognition or reading order. Avoid forcing every chapter into the same page count. Page rhythm should support reading, not repeatedly interrupt it with pull quotes or large decorative elements.

Keep notes readable and easy to return from. Where readers must consult a note immediately, do not bury it at the end of the book without a clear reference. Essential explanations belong in the main text. Choose footnotes or endnotes according to the reading task and test the arrangement.

## BOOK02 Control composition without shrinking text

**PRINT BOOK • SHOULD • SYNTHESIS.** Review widows, orphans, isolated headings, awkward page turns and repeated hyphens. Avoid splitting short labels and number-unit combinations. Use language-aware hyphenation, and inspect proper names, unfamiliar words and line-end punctuation. Do not manually insert hard hyphens into reusable source text to repair one edition.

Balance line length, type size, leading, margins and trim size together. Larger type with excessively short lines can become tiring; wider pages with long lines can make return sweeps difficult. Adjust the page design and pagination before reducing readability. Reject binding proofs where text disappears into the gutter.

## PRINT02 Offer appropriate alternative editions

**PRINT • MUST where needed to deliver equivalent access • SYNTHESIS.** Plan how readers obtain large print, accessible digital text, audio, braille or other appropriate formats. Do not treat an enlarged photocopy as the default large-print solution: recompose the layout, line lengths, tables and navigation. Confirm preferred sizes where serving an individual reader. \[V4\]

Alternative editions should preserve substantive content, version and useful navigation. Make the request or download route clear and usable; do not require a reader to decipher inaccessible print to discover it. Physical print cannot by itself provide nonvisual access. The publication plan must account for that limitation.

# 10 Verify the delivered editions

## QA01 Combine automated manual and reader checks

**ALL • MUST • SOURCE and SYNTHESIS.** Automated tools detect some structural problems. Human review assesses meaning, descriptions, relationships and reading order. Reader testing establishes how the experience works in practice. Keep these evidence types separate; none substitutes for all the others. \[S1, S7, S8\]

Compare candidate typography under the same content and conditions. Include readers relevant to the audience, such as people with low vision, people who use screen readers or magnification, people with reading difficulties and native readers of supported scripts. Offer participants their familiar technology. Record accuracy, comprehension, task completion, effort and fatigue separately from preference. Do not claim population-wide results from a small convenience sample.

## QA02 Apply the release checks

**ALL • MUST • SYNTHESIS.** For each relevant row below, record pass, fail, not tested or not applicable, with evidence and a reviewer. A failed critical requirement or missing essential information blocks an accessibility release claim. Resolve defects in the source where possible, regenerate all affected editions and retest the changed areas and their dependencies.

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

**ALL • MUST • SYNTHESIS.** Record the document version, source revision, output files, applicable standard and edition, tested software, devices or print conditions, dates, methods, results, exceptions and remaining limitations. Assign an owner for corrections and an accessible feedback route.

Use precise language: "heading structure checked" or "tested with the named reader and software". Do not write "fully accessible" because a checker reported no errors. This guide itself has been prepared with structured headings and tables and checked for visual layout; it has not undergone representative-reader testing or a formal conformance assessment.

# 11 Translate the guide into LLM instructions

## AI01 Preserve scope obligation and evidence

**LLM WORKFLOWS • MUST • SYNTHESIS.** An AGENTS.md version should preserve each stable rule ID, its scope, obligation and test. Do not compress conditional advice into universal rules. Keep numerical defaults distinct from standard thresholds and from user override tests. Preserve the source register and conflict decisions so later updates remain traceable.

Use the rule IDs already attached to every requirement in sections 1 to 10. Keep a short execution sequence in AGENTS.md and link to a detailed rule register if the complete guide is too long. Instructions must tell the model how to select applicable rules, make reversible decisions and report incomplete tests.

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

**LLM WORKFLOWS • MUST • SYNTHESIS.** Represent a rule with the fields below. Split a multi-part rule into subordinate checks when implementing automated tests, retaining its parent ID. Do not mark a whole rule passed when only its automated portion was checked.

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

**Example using TYPE03.** Scope: PRINT body text. Obligation: SHOULD. Action: start at 12 to 14pt and judge perceived size on an actual-size proof. Basis: synthesis informed by S1, S3, S7 and V4. Verification: inspect the final type, measure the output size and test relevant readers. Status without a physical proof: not tested for print suitability. A small font is not automatically acceptable because it helped meet a page limit.

## AI04 Set explicit stop and escalation conditions

**LLM WORKFLOWS • MUST • SYNTHESIS.** Flag missing essential content, broken script shaping, unreadable text, absent required alternatives, an unusable form, loss of digital structure or contradictory accessibility requirements. Continue safe preparatory work where possible, but do not present the affected edition as ready or conformant until the barrier is resolved or accurately disclosed.

Do not fabricate alt text for an unseen image, infer that OCR is correct, copy source pass/fail font labels as universal facts, reduce text silently to meet a page count, or treat an inaccessible export as acceptable because its source was structured. Do not substitute a visual screenshot check for semantic or assistive-technology testing.

If an instruction conflicts with a mandatory applicable standard, identify the conflict and propose an accessible resolution. If a SHOULD rule conflicts with an evidenced reader need, record the adaptation and verify it. Human approval cannot turn an unmet standard into conformance.

# 12 Source reconciliation and provenance

## Decisions made when combining the guidance

The supplied material contains practical experience, design-system conventions and research interpretations. It is not one normative standard or one peer-reviewed evidence base. This guide retains useful design principles while qualifying broad claims and repairing examples that would otherwise become unsafe automated rules.

**Typeface categories and named fonts.** S5 favours serif type for print, while S8 includes categorical font pass/fail examples and claims about specific styles. S1 explicitly cautions against these generalisations. This guide uses the examples as prompts for inspection and comparative testing, not a whitelist or blacklist.

**Size and leading.** S3 uses a BBC-specific scale and a 1.375 leading example; S7 discusses larger spacing; S5 sets 12pt body but overrides paragraphs to 11pt. This guide makes practical starting values explicit and avoids that hidden size reduction. No starting value guarantees accessibility.

**Web standards and paper.** S5 maps WCAG concepts directly to print. This guide distinguishes digital requirements from physical proofing. The numerical contrast of artwork does not prove contrast on paper, and alt attributes do not normally provide a printed explanation.

**Print suppression and pagination.** S5's broad selectors could remove meaningful asides, footers or embedded information, and blanket no-break rules can overflow long tables. This guide requires content-aware suppression, explicit replacements and break rules appropriate to the element's length.

**Spacing and group relationships.** A sentence in S3 appears to reverse the intended grouping rule; its heading example makes the intended relationship clear. This guide keeps related items closer together and allows more space between distinct groups. Spacing overrides are tolerance tests, not a demand that every design start with those values.

**Contrast and comfort.** S7 and S10 discuss softened contrast. This guide supports personal choice but does not trade away required default digital contrast or assume reduced contrast helps everyone. Stroke contrast within a letter is different from foreground-background colour contrast.

**Writing systems and neuroscience.** S9 to S11 contain explanatory historical, neurological and classification claims that are unnecessary for document production. This guide does not reproduce them as design evidence. It retains the actionable requirement for script-specific shaping, layout, language support and native-reader review. It does not infer a universal reading mechanism or clinical effect from typography examples.

## Supplied source register

All eleven attachments informed this synthesis. References below identify the supplied versions, not a claim that their linked pages remain unchanged. Page references refer to the supplied PDF page sequence where useful.

**S1 Accessible Typography for UX and Brand Systems.** Supplied file Accessible_Typography_for_UX_and_Brand_Systems(1).md, version 1.0-semantic, processed 18 September 2026. Attributed in the file to Gareth Ford Williams, Bruno Maag, David Bailey and Michael Mathews. Main basis for contextual typography, three accessibility outcomes, user testing and AI governance; itself an editorial synthesis.

**S2 BBC GEL Images of text.** Supplied BBC GEL _ Images of text.pdf, particularly pages 1 to 3; article published 30 May 2024. Basis for contextual descriptions, transcription and body-text equivalents for complex material.

**S3 GEL Typography.** Supplied GEL _ Typography.pdf, version 0.1.0, particularly pages 2 to 7. Basis for relative sizing, measure, spacing, alignment, links and adaptability. BBC-specific font choices and examples are not universal requirements.

**S4 BBC Accessibility for Products Images of text.** Supplied Images of text - Accessibility for Products - BBC.pdf, pages 1 to 2. Basis for using actual text and accessible equivalents. Historical platform code is not reproduced as current implementation guidance.

**S5 Print Friendly Style Sheets Accessibility Best Practices.** Supplied PRINT_ACCESSIBILITY_BEST_PRACTICES.md, copyright 2026 Mike Gifford; file states AGPL-3.0-or-later. Basis for print adaptation, references, pagination and greyscale testing. This guide paraphrases its principles and does not reproduce its code. Review the stated licence before reusing its code in an implementation.

**S6 BBC Accessibility for Products Styling and readability.** Supplied Styling and readability - Accessibility for Products - BBC.pdf, pages 1 to 3. Basis for separating content and presentation and retaining core meaning when styles are unavailable.

**S7 Typography DDP Accessibility.** Supplied Typography _ DDP Accessibility.pdf, particularly pages 1 to 18. Basis for contextual font selection, measure, resizing, weight, spacing, direction and reader preferences. Font-category rules and browser-specific statements are treated cautiously.

**S8 Typeface Accessibility Guide GAAD 2020.** Supplied Typeface Accessibility.pdf. Credits Bruno Maag, David Bailey, Gareth Ford Williams and Michael Mathews. Basis for letterform inspection and comparative in-context testing. Font pass/fail illustrations are not general conformance tests.

**S9 Typographic accessibility in more detail.** Supplied \[Articles\] - Typographic accessibility in more detail.docx. Basis for emotional, functional and technical accessibility, perceived size, crowding and language support. Broader physiological and historical claims are not adopted as requirements.

**S10 About Legibility and Readability.** Supplied \[Articles\] - Legibility and Readability.pdf. Basis for distinguishing character recognition from sustained reading and considering typography in context. Does not establish a universal paper, ink or contrast prescription.

**S11 Writing Systems.** Supplied \[Articles\] - Writing Systems.pdf, headed "It's all squiggles to me". Basis for cultural and script awareness. The guide does not reproduce its simplified classifications or historical assertions.

## Supplementary technical references

These primary references were checked on 28 October 2026 to clarify technical requirements and fill gaps beyond the attachments. The checklist in this guide is selective; a formal conformance assessment must examine every applicable requirement, not only the examples here.

**V1 W3C Web Content Accessibility Guidelines 2.2.** Recommended digital baseline for this guide: Level AA, with additional reader-centred practices. Visual Presentation 1.4.8 is AAA; do not label all its advice as AA. See <https://www.w3.org/TR/WCAG22/>

**V2 W3C WCAG2ICT.** Informative guidance for applying WCAG to non-web documents and software; it does not itself create normative requirements. Use the applicable procurement, organisational or legal standard for the actual obligation. See <https://www.w3.org/WAI/standards-guidelines/wcag/non-web-ict/>

**V3 W3C PDF techniques.** Practical techniques for alternatives, headings, tables, bookmarks, language, links, OCR and reading order. Techniques are examples, not a complete mandatory checklist. See <https://www.w3.org/TR/WCAG20-TECHS/pdf> and <https://www.w3.org/WAI/WCAG22/Techniques/pdf/PDF3.html>

**V4 RNIB Large and giant print.** Supports the common 16 to 18pt description of large print and the need to find a suitable reading format. The 12 to 14pt general starting range in this guide is an editorial synthesis, not an RNIB certification. See <https://www.rnib.org.uk/living-with-sight-loss/independent-living/leisure/reading-and-books/large-and-giant-print/>

**V5 W3C EPUB Accessibility 1.1.** Covers publication accessibility and discoverability metadata. Consult it alongside the relevant EPUB specification and selected WCAG target. See <https://www.w3.org/TR/epub-a11y-11/>