# Accessible documentation design instructions

Version: 1.0 | 2026-10-28

## Purpose and scope

Apply these instructions when designing, generating, editing or exporting documentation for digital reading, screen-and-print use, physical print or sustained book reading. Produce content that people can find, perceive, understand and use through visual reading, enlargement, speech, braille or an appropriate alternative edition.

This file is self-contained operational guidance derived from *Accessible documentation design*, version 1.0. Rule IDs preserve traceability to that guide. Do not require the original guide to carry out these instructions. Do not insert these implementation instructions or validation records into the reader-facing document unless requested.

## Requirement interpretation

- **MUST / MUST NOT:** requirements of this design policy when the stated scope applies. They are not all statutory or WCAG requirements.
- **SHOULD:** default practice. Depart only for a documented contextual reason, with suitable verification.
- **MAY:** an optional technique.
- **ALL:** every edition. **DIGITAL:** electronic editions. **HYBRID:** both screen and print. **PRINT:** physical output. **BOOK:** sustained reading in print or an electronic book.
- Design starting values are adjustable hypotheses. Standard thresholds are requirements within their defined scope. User override values are tolerance tests. Do not substitute one category for another.
- Respect the governing instruction hierarchy. If a task instruction conflicts with an accessibility requirement, identify the conflict, propose a workable resolution and accurately disclose any unmet requirement. Never describe an unmet standard as satisfied because someone approved a deviation.
- Apply only relevant profiles. A digital-only document does not require a physical proof; a printed book does. A hybrid publication requires both digital and print checks.

## Execution sequence

1. Read the task, existing source and applicable project instructions. Identify audience, reading task, languages, output formats, standards and production constraints.
2. Record assumptions. Ask only when missing information materially changes access or blocks a necessary decision. Continue reversible work that does not depend on the answer.
3. Select output profiles below. Maintain one structured content source where practicable; generate equivalent editions with format-appropriate layouts.
4. Create semantic structure and complete content before styling. Apply the common rules and selected profiles.
5. Generate the requested files. Inspect the actual final outputs, not only templates or source code. Render and inspect every page of paginated outputs.
6. Run applicable structural, adaptation, interaction and export checks. Repair defects in the source, regenerate affected editions and retest relevant dependencies.
7. Record completed, failed, untested and inapplicable checks. Deliver requested files with a concise verification summary and material remaining limitations. Do not claim universal accessibility or formal conformance without the evidence needed for that claim.

## Profile selection

| Output | Apply |
| --- | --- |
| HTML or other reflowable screen guidance | Common rules, digital adaptation, relevant interaction and media checks |
| DOCX or equivalent editable document | Common rules, word-processing profile, relevant digital checks |
| PDF for electronic reading | Common rules, PDF profile, relevant digital checks |
| Reflowable EPUB | Common rules, EPUB profile, sustained-reading rules |
| Screen document that can be printed | All relevant digital rules plus hybrid and print rules |
| Printed leaflet, report or form | Common rules, print production and offline-use rules |
| Physical book | Common rules, print production, book composition and sustained-reading rules |
| Fixed-layout digital book | Common rules, relevant PDF or EPUB profile; document the layout need and provide suitable alternatives |

A print-production PDF and an accessible screen-reading PDF may require separate exports. Do not assume that printer requirements preserve reading tags, links or navigation. Keep content equivalent and distinguish the editions clearly.

## Planning and content

### PLAN01 Establish the reading context — ALL MUST

Record purpose, readers, reading duration, task, languages and scripts, formats, devices or paper sizes, viewing conditions, access needs and production constraints. Distinguish scanning, comparison, task completion and continuous reading. Do not infer an individual's preferences from a diagnosis.

### PLAN02 Choose appropriate editions — ALL SHOULD

Prefer reflowable HTML for online guidance, structured editable files for document collaboration and reflowable EPUB for prose books. Use PDF when fixed pagination or layout matters, with accessible structure. Offer an equivalent adaptable edition when fixed layout obstructs comfortable reading. File extensions and OCR alone do not establish accessibility.

### PLAN03 Evaluate distinct outcomes — ALL MUST

Assess separately:

- Emotional suitability: credibility, tone, familiarity and cultural appropriateness.
- Functional performance: character recognition, reading effort, comprehension and task success.
- Technical delivery: structure, fonts, language support, adaptation and assistive access.

Do not use preference or brand approval as proof of reading performance. Do not use technical conformance as proof of comfortable sustained reading.

### STRUCT01 Encode semantic structure — ALL MUST

Use a meaningful content sequence, descriptive title, correctly nested headings, real paragraphs and lists, captions and table structures. Never simulate structure with bold alone, typed bullets, spaces or tabs. Use styles rather than repeated direct formatting. In DOCX, use Title and Heading styles; in HTML, use a logical heading hierarchy with an identifiable main heading.

### STRUCT02 Provide navigation — ALL SHOULD

For long documents, provide linked digital contents, descriptive chapter names, useful page or location references and, where appropriate, an index, glossary and figure/table lists. Supply hierarchical PDF bookmarks. Use section names or descriptive cross-references instead of spatial directions alone. Update references after layout changes. Provide return navigation for digital notes. Keep essential information in the main reading sequence, not exclusively in headers or footers.

### STRUCT03 Align reading order and layout — DIGITAL MUST, PRINT SHOULD

Prefer one main prose column. Anchor figures near their first reference; keep captions associated. Prefer inline objects when floating objects break reading order. Verify multi-column and sidebar sequences explicitly. Keep essential instructions in the main sequence. Supplementary material needs an identifiable entry and exit point and must not interrupt sentences.

### STRUCT04 Support comprehension — ALL SHOULD

Lead with purpose and actions. Use familiar language, descriptive headings, one main idea per paragraph, concrete examples and explained abbreviations. Number sequential instructions; use bullets for parallel items. Preserve precision and necessary qualifications. Do not infer comprehension from a reading-age score. Treat Easy Read as a separately prepared editorial adaptation, not a font-size setting; keep adapted content aligned with the full edition.

## Typography

### TYPE01 Inspect actual letterforms — ALL MUST

Inspect candidate fonts at intended sizes and weights on the actual output. Include I/l/1, O/0, c/e/o/a, b/d/p/q, rn/m and cl/d, plus punctuation, numerals, accents, names and realistic words. Check open apertures, clear counters, distinctive shapes, spacing and strokes that survive rendering or printing. Consider x-height and perceived size. These are inspection prompts, not automatic font certification.

### TYPE02 Avoid universal font claims — ALL MUST NOT

Do not select or certify a font solely from serif/sans-serif/humanist classification, brand name or “dyslexia-friendly” marketing. Do not present typography as treatment for a reading condition. Compare plausible candidates in context; use extended passages for books. Do not condense essential text merely to meet page limits. Single- and double-storey letterforms require contextual judgement.

### TYPE03 Use size defaults as starting points — ALL SHOULD

| Context | Initial setting | Verify |
| --- | --- | --- |
| Reflowable screen body | 1rem–1.125rem; root at 100% | Reader base size, small screens, enlargement |
| General print or paginated body | 12–14pt; favour the larger end where feasible | Actual perceived size and physical proof |
| Large print | Begin consultation at 16–18pt | Individual needs; larger type may be needed |
| Printed book body | Begin within the general print range | Real chapters, measure, leading, trim and fatigue |
| Captions, notes and tables | Prefer body size | Essential content remains comfortably readable |

Do not treat these values as WCAG minima or accessibility guarantees. A browser's 1rem is often 16 CSS pixels but depends on user settings. Do not equate CSS pixels with printer dots or assume equivalent screen and print readability from unit conversion. Edit, restructure, add pages or create another edition before shrinking essential text.

### TYPE04 Balance line length and leading — ALL SHOULD

For Latin prose, start around 50–70 characters per line including spaces; approximately 65 is a working target. Allow shorter lines on small screens and in enlarged editions without reducing type to force the target. CSS `ch` measures the advance of zero, not average character count: inspect actual lines.

Start body line spacing around 1.5 times font size. Adjust for font metrics, line length, script and evidence. A tested printed book may work around 1.3–1.5; this does not waive an applicable standard. Avoid exact fixed line heights that clip enlarged type, diacritics or equations. Use script-specific judgement outside Latin text.

### TYPE05 Preserve spacing and restrained emphasis — ALL SHOULD

Start with designed font spacing. Correct observed crowding; do not apply negative body tracking, stretched word spacing or wide tracking globally. Allow supported user overrides. Do not insert letter spacing into joining scripts mechanically. Prefer regular body weight; avoid thin strokes or extreme thick-to-thin contrast at small sizes. Use true bold/italic faces where available. Use sentence case, brief emphasis and conventional acronyms. Avoid long italic, bold, underlined or all-capital passages. Underline links; avoid underlining ordinary text as decoration.

### TYPE06 Align to the reading start edge — ALL SHOULD

Use left alignment for ordinary left-to-right prose and right alignment for ordinary right-to-left prose. Avoid centred paragraphs and full justification by default.

For a justified printed book, record the exception, use professional composition and language-aware hyphenation, inspect every page for rivers, stretched gaps and repeated hyphens, compare ragged-edge samples and evaluate sustained reading. Preserve an adaptable digital edition. Do not incorrectly label justification alone as a universal WCAG AA failure.

## Visual presentation and language

### VIS01 Maintain contrast and redundant meaning — DIGITAL MUST, PRINT MUST

For the selected WCAG AA digital baseline:

- Text contrast: at least 4.5:1; large text at least 3:1. Large means at least 18pt regular or 14pt bold, or equivalent size. Apply the standard's defined exceptions.
- Relevant graphical objects and interface visuals: at least 3:1 against adjacent colours, within the scope and exceptions of non-text contrast requirements.
- Never use colour alone to convey essential meaning. Add labels, patterns, shapes or direct annotation.

Check actual backgrounds and states. Avoid text over photography or texture. For print, proof dark, substantial text on a plain light substrate in realistic lighting and greyscale. Digital colour ratios do not certify contrast on physical paper; account for ink, glare and show-through.

### VIS02 Respect reader presentation — DIGITAL MUST where supported

Preserve font replacement, zoom, spacing and colour preferences. Test alternate fonts, themes and relevant high-contrast settings. Keep essential boundaries, labels and focus indicators visible. Keep authored default themes within the selected standard; do not override a reader's own preferences merely to restore the default. Do not assume grey text, cream paper or dark mode is universally beneficial.

### VIS03 Group through space and alignment — ALL SHOULD

Keep related elements closer than unrelated groups. Keep headings with following content and captions with figures. Use sufficient margins and a consistent hierarchy. Avoid clutter, decorative watermarks and crowded boxes. Use paragraph spacing or book-style first-line indents deliberately; usually omit an indent after a heading. Do not create layout through repeated empty paragraphs.

### LANG01 Support language and script — ALL MUST

Set primary language and language changes where supported. Set direction separately where needed. Verify glyphs, accents, shaping, conjuncts, punctuation, numerals, mixed-direction content and script-appropriate breaks. Use meaningful native-language samples and native-reader review. Do not replace a script with transliteration or omit accents to fit a font.

Check font fallback, loading failure, export, embedding permission and text mapping. Preserve searchable, copyable text. Do not convert prose to outlines to solve font problems. A visually correct page can still contain incorrect underlying text.

## Images data and interaction

### IMAGE01 Preserve actual text — DIGITAL MUST

Use real text for prose, headings, instructions, labels and data. Do not flatten documents into page images. Necessary screenshots, logos and facsimiles need suitable equivalents. Transcribe meaningful embedded text accurately; describe appearance separately when relevant. Vector artwork and OCR are not automatic substitutes for accessible text. Graphic headings also need structural headings.

### IMAGE02 Supply purpose-based alternatives — DIGITAL MUST, PRINT MUST for essential meaning

Inspect the image before writing its alternative. Describe informative content in context; name the action or destination for functional images; mark decorative images appropriately. For complex graphics, provide a short identification plus a nearby extended explanation or accessible data representation. Do not bury long articles or datasets in alt-text fields. Avoid unnecessary repetition while preserving necessary meaning.

Alt text is normally absent from physical print. Put essential interpretation into visible captions or body text in the printed edition. Do not assume a subject label supplies a complete explanation.

### IMAGE03 Explain charts and media — ALL MUST

Give charts descriptive titles, appropriate axes and units, identifiable series and the important finding. Provide accessible data when exact values matter. Do not rely on colour or position alone. Provide captions, transcripts and descriptions of meaningful visual media content as applicable. Printed editions need essential media information in text or figures and a usable reference to optional media; an empty player is not an equivalent.

### DATA01 Encode simple real tables — ALL SHOULD, DIGITAL header relationships MUST

Use tables for comparisons and records, not page layout or narrative instructions. Supply clear headers, units and an introduction or caption. Encode header associations using the format's capabilities; mark repeating DOCX headers and verify export semantics. Simplify merged structures where possible. Bold cells alone are not headers.

Explain empty values and symbols. Avoid spacing cells and unexplained ditto marks. Align prose to its start edge and numbers consistently. For wide tables, restructure, split logically with identifying columns, use an appropriate landscape page or provide an accessible alternative. Do not shrink until unreadable.

### DATA02 Paginate tables sensibly — PRINT and HYBRID MUST

Repeat headings and preserve column order across pages. Keep ordinary rows together where practical, but allow oversized rows or long tables to continue without overflow. Keep units, captions and notes associated. Use adequate padding and flexible heights. Check rules and shading in greyscale. Do not apply “never split” indiscriminately.

### FORM01 Support completion — DIGITAL and PRINT MUST

Digital: persistent labels, instructions, identified required fields, meaningful accessible names, logical keyboard order, visible focus and understandable errors. Test real completion, saving and submission. Do not rely on placeholders or hover-only help. Apply relevant interaction requirements of the selected standard.

Print: clear labels/options, an obvious selection method, sufficient writing space, necessary consent/instructions and return details. Provide an appropriate alternative when handwriting or signing creates a barrier.

### SPECIAL01 Preserve specialist notation — DIGITAL SHOULD, PRINT verification required

Use structured equations where supported and test their spoken/navigation behaviour. Necessary formula images need accurate equivalents. Keep code selectable and significant whitespace intact; wrap or provide usable horizontal navigation without clipping. Explain unfamiliar notation. Verify operators, punctuation, subscripts, superscripts and fine lines at final print size. Never simplify away technical meaning.

## Digital profiles

### DIGITAL01 Test adaptation — DIGITAL MUST within applicable scope

- Test text enlargement to 200% without loss of content or functionality within the applicable criterion's scope.
- For vertically scrolling reflowable web content, test a width equivalent to 320 CSS pixels, including a 1280px starting viewport at 400% zoom. Do not require two-dimensional scrolling except for content covered by the standard's exceptions. For horizontal writing flow, apply the corresponding 256 CSS pixel height test.
- Where supported, apply these spacing overrides together without changing other styles: line height 1.5, spacing after paragraphs 2, letter spacing 0.12 and word spacing 0.16 times font size. Content and function must survive. Apply language/script exceptions where a spacing property is not used.

These are tolerance tests, not compulsory authored settings. Prefer relative web text sizes and flexible containers. Do not disable pinch zoom, crop text in fixed heights or truncate essential prose. Test text-only enlargement, page zoom and magnification as distinct modes where relevant. Evaluate fixed-layout formats using suitable reader software and provide equivalent adaptable editions where necessary.

### DIGITAL02 Word-processing profile — MUST

Use named styles, semantic headings and lists, document language, meaningful links and title metadata. Use image alternatives, marked table headers and a logical main flow. Check navigation and keyboard traversal. Prefer style-based spacing and pagination over blank lines and manual line breaks. Check fallback fonts. Run the application's accessibility checker and review its findings manually; a clean report does not prove meaningful alternatives or readable prose.

### DIGITAL03 PDF profile — MUST

Export with structure preserved. Inspect the delivered PDF for tags, heading hierarchy, lists, table associations, alternatives, language, title, bookmarks, links, reading order and form tab order. Mark decorative/repetitive furniture as artefacts where appropriate. Verify search, text extraction, copying and fonts. Correct OCR, especially names, numbers and symbols. Do not impose assistive-access restrictions.

Do not assume print-to-PDF preserves accessibility. If PDF/UA is a target, identify its edition and use suitable validation plus human checks. Tags, screenshots and generic checker passes cannot independently establish PDF/UA or WCAG conformance.

### DIGITAL04 EPUB profile — SHOULD

Prefer reflowable EPUB for continuous prose. Include semantic chapters, navigable contents, alternatives, language metadata and return navigation for notes. Test reader styling, enlargement, text-to-speech, sequence and multiple reading systems. Provide accurate accessibility metadata. Implement appropriate page navigation when print-equivalent pagination is supplied and identify its source. Validate the package separately from assessing reading accessibility. Justify fixed layout and provide suitable alternatives.

## Hybrid and offline profiles

### HYBRID01 Preserve content equivalence — HYBRID MUST

Compare each edition with the structured source. Preserve essential expanded disclosures, selected results and filters, chart context, notes and media equivalents. Remove only genuinely operational or decorative material. Do not blanket-hide asides, footers, forms or embedded content. Replace essential interactions with static information or instructions. Confirm useful fallback content when styles fail.

### HYBRID02 Make references usable offline — PRINT and HYBRID MUST

Provide readable destinations for essential external links through URLs, numbered references or appropriate contact details. Resolve relative links; omit unnecessary tracking without changing the destination. Avoid dumping long URLs after every link. Replace internal links with useful section or page references. QR codes may supplement, never replace, a usable route; test at final size on the selected stock.

### HYBRID03 Set print-specific layout — HYBRID SHOULD

Scope web print rules to print media. Use physical units for page geometry and print type; relative spacing is permitted. Choose paper size and margins deliberately and test likely alternatives such as A4 and Letter. Remove fixed positioning and overflow constraints that clip printed content. Fit images to the page. Keep headings and short captioned figures together; let long tables and text paginate. Control widows/orphans without excessive gaps. Verify renderer support for page counters and running furniture.

### HYBRID04 Test ordinary printing — HYBRID MUST

Inspect preview and a physical sample with background printing off, greyscale on and ordinary printer margins. Check duplex output where intended. Check actual size and common fit-to-page scaling. Ensure all labels, references and meaningful lines survive. Provide necessary print instructions. If a browser-generated PDF is distributed digitally, validate it separately under the PDF profile.

## Physical print and books

### PRINT01 Specify production as a system — PRINT SHOULD

Evaluate paper, ink and binding together. Prefer plain low-glare stock with sufficient opacity; paper weight does not prove opacity. Physically proof ink density, stroke survival, colour, glare, show-through and reverse-side interference in realistic light. Do not assume off-white or tinted stock suits everyone. Avoid textures, gloss and large reverse-out passages where they obstruct reading.

Allow a binding-appropriate inner margin. Keep text clear of trim and folds; mirror margins correctly. Verify content is visible without forcing the book open. Consider weight, thickness, opening resistance, page turning, stands and magnifiers. Consider lay-flat binding where feasible. Follow the printer's actual trim, bleed and binding specifications; do not invent universal production values.

### BOOK01 Test sustained reading — BOOK SHOULD

Evaluate a representative chapter or substantial passage using the intended device or paper and realistic lighting. Look for lost lines, rereading, discomfort, fatigue and reduced comprehension. Keep body typography, hierarchy and paragraph treatment stable. Avoid disruptive drop capitals, repeated pull quotes and arbitrary chapter page limits. Put essential explanations in the main text. Make notes readable, easy to find and easy to return from; select footnotes/endnotes according to the task.

### BOOK02 Review composition — PRINT BOOK SHOULD

Inspect every page for widows, orphans, isolated headings, difficult page turns, rivers and repeated hyphens. Use language-aware hyphenation; check names and unfamiliar words. Avoid separating short labels and number–unit combinations. Do not insert hard hyphens into shared source solely to fix one layout.

Balance type size, leading, line length, margins and trim together. Larger type with excessively short lines can impede flow. Change composition or pagination before shrinking essential text. Reject physical proofs with text lost in gutters or illegible fine detail.

### PRINT02 Plan equivalent access — PRINT MUST where needed

Provide an appropriate route to large print, accessible digital text, audio, braille or other needed formats. Recompose large print rather than merely enlarging photocopies; reconsider tables, navigation and line lengths. Confirm individual preferences where relevant. Keep substantive content and versions aligned. Make alternative-format access discoverable without requiring readers to decipher inaccessible print. Physical print alone cannot provide nonvisual access.

## Validation and release

### QA01 Separate evidence types — ALL MUST

Use automated checks for detectable defects, manual review for meaning and sequence, and reader testing for actual experience. Never report one as another. Compare typography under equivalent content and conditions. Include relevant readers and familiar assistive technology. Record comprehension, accuracy, task success, effort, fatigue and preference separately. Do not generalise small-sample findings to everyone.

### QA02 Apply scoped release gates — ALL MUST

| Gate | Required evidence |
| --- | --- |
| Content | Final editions retain all substantive information and correct references |
| Semantics | Heading/list/table structures, language, alternatives and reading sequence checked |
| Typography | Final glyphs, size, spacing, shaping and fallback inspected |
| Adaptation | Applicable resizing/reflow/spacing/theme checks completed without loss |
| Interaction | Relevant controls and forms tested through keyboard and assistive access |
| Export | Final files inspected independently; relevant validation completed |
| Pagination | Every rendered page inspected for clipping, overlap, glyph defects and broken relationships |
| Physical production | Actual-size and greyscale proofs checked; stock/binding inspected where relevant |
| Sustained reading | Relevant reader evaluation completed or explicitly recorded as untested |

Use `pass`, `fail`, `not_tested` or `not_applicable`. Give a reason for `not_applicable`. Record tool/version or reviewer, output version, date and relevant conditions. A pass applies only to the tested scope. If screen-reader access, physical proofs or reader testing is unavailable, say so; do not fabricate results or block safe draft creation unnecessarily.

### QA03 Maintain a truthful release record — ALL MUST

Keep a lightweight record outside the publication unless requested. Use this schema when a structured record is useful; replace sample values with actual evidence:

```yaml
accessibility_review:
  source_revision: null
  output_files: []
  profiles: []
  audience_and_tasks: []
  languages_and_scripts: []
  standards: [] # Name, edition, level, applicability
  assumptions: []
  checks:
    - rule_id: STRUCT01
      output: null
      method: null
      environment: null
      result: not_tested
      evidence: null
      reviewer: null
      date: null
  exceptions: [] # Rule, reason, reader impact, equivalent access,
                 # evidence, approving role and review date
  unresolved_barriers: []
  release_status: draft # draft | ready_with_disclosed_limits | verified_in_scope
```

A failed critical requirement blocks release as an accessible edition. Continue independent safe work, fix defects and retest. Deliver an explicitly labelled draft when appropriate. Do not use an exception or alternative-format link to conceal a barrier or claim conformance for a failing edition. Never label a publication “fully accessible” from a checker result.

## Agent guardrails

- **AI01:** Preserve rule scope, obligation, evidence category and numerical meaning when adapting these instructions. Keep IDs stable; version substantive changes.
- **AI02:** Follow the execution sequence. Use existing project conventions when they preserve access; do not request permission for routine reversible design choices already within scope.
- **AI03:** Turn multi-part rules into subordinate checks when automating them. A partial automated check cannot pass the entire parent rule. Keep evidence tied to the actual output.
- **AI04:** Flag missing content, broken shaping, unreadable text, absent necessary alternatives, unusable forms and lost export structure. Do not invent alt text for unseen images, trust unreviewed OCR, silently shrink text, copy universal font pass/fail labels, or treat screenshots as semantic validation.

## Standards and evidence handling

The defaults and production practices here are editorial design policy, not universal scientific thresholds. The original guide reconciles supplied BBC, DDP, Readability Group and print-style guidance. Retain these decisions:

- No universal serif/sans-serif winner, accessible-font whitelist or clinical benefit claim.
- Digital contrast calculations do not certify paper, and alt attributes do not normally print.
- Related items belong closer together; do not reverse the grouping rule.
- Print suppression and no-break rules must be content-aware.
- WCAG text-spacing values test tolerance; they are not compulsory starting typography.
- WCAG Visual Presentation 1.4.8 is AAA; do not label every associated recommendation AA.
- Avoid unsupported neurological, historical or writing-system generalisations; verify rendering with native readers.

For a formal conformance decision, consult the exact applicable standard and all relevant criteria. This file is not a complete WCAG, PDF/UA or EPUB conformance checklist. Verify current requirements, tool capabilities and version-specific behaviour before relying on them; do not repeatedly retrieve standards for routine editorial changes that make no new conformance claim.

Primary references:

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): selected digital baseline is Level AA unless the project specifies otherwise.
- [WCAG2ICT](https://www.w3.org/WAI/standards-guidelines/wcag/non-web-ict/): informative interpretation for non-web documents and software; not itself a normative requirement.
- [W3C PDF techniques](https://www.w3.org/TR/WCAG20-TECHS/pdf) and [PDF reading order](https://www.w3.org/WAI/WCAG22/Techniques/pdf/PDF3.html): implementation guidance, not a complete certification process.
- [EPUB Accessibility 1.1](https://www.w3.org/TR/epub-a11y-11/): publication accessibility and discoverability requirements.
- [RNIB large and giant print](https://www.rnib.org.uk/living-with-sight-loss/independent-living/leisure/reading-and-books/large-and-giant-print/): context for large-print options; no single size suits everyone.
