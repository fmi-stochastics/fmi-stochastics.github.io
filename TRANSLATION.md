# English translation record

Date: 26 October 2026.

System and model: **ChatGPT (OpenAI, GPT-6)**. The model name is the one supplied by the course owner for this chat.

## Request and scope

The course owner requested an English version of the existing Bulgarian teaching site, the full available archive, BG / EN links in the upper-right corner, and the new alternative exercise collection. The manual and lecture notes were explicitly excluded from the English version. This is a summary of the instructions, not an export of the complete conversation.

The site pages link to 92 distinct archive PDFs and one alternative exercise PDF. Material already written in English is reused: `prob-stat-applied-math-tvms-2024-homework-4-5.pdf` (Cambridge Statistics examples). The new Bulgarian alternative PDF is added alongside the older Bulgarian alternative PDF.

Source material:

- The existing Bulgarian pages and PDFs in this repository.
- TeX files supplied under `C:\Users\Lenovo\OneDrive - Sofia University\Teaching\site\fmi_stochastics (1)`.
- The pasted alternative-exercise TeX supplied in the conversation.
- `informatics_2026 (3).pdf`, supplied by the course owner.

AI assistance was used to translate Bulgarian prose into English, transcribe handwritten solution scans into English LaTeX, format the translated documents, and implement the bilingual website. The mathematical notation, exercise structure, dates and original solution arguments were retained. Translation does not establish that the source mathematics is correct. Apparent inconsistencies identified during transcription are recorded in the affected documents or accompanying source notes.

See [SOURCE_REVIEW.md](SOURCE_REVIEW.md) for the collected source issues and edition choices to review before teaching from the translated materials.

The common exercise bank uses the newer supplied TeX edition (179 exercises), rather than the older published PDF (171 exercises). The alternative collection contains all 69 exercise and research-task environments from the supplied TeX.

## Validation

The finished English collection contains **93 PDF files and 220 pages**: 92 translated documents with editable TeX sources and one existing English handout retained unchanged. The per-file source mapping, page counts and checksums are in [translation-inventory.csv](translation-inventory.csv).

All translated PDFs were compiled and visually inspected. The final LaTeX logs contain no overfull boxes or undefined commands. Extracted English PDF text contains no Cyrillic text, and all translated PDFs contain the ChatGPT/GPT-6 disclosure. A strict MkDocs build and checks of all 12 Bulgarian/English pages, language counterparts, local anchors and 93 distinct English PDF links passed.

The app's browser policy blocked the local website preview. Website checks used the generated HTML and links; no browser-based visual verification is claimed. The local preview instructions in README.md allow the course owner to inspect the website in a normal browser.

## Published disclosure

English pages and translated PDFs use the following disclosure:

> English translation prepared with ChatGPT (OpenAI, GPT-6), 26 October 2026, for translation of the Bulgarian text into English and LaTeX formatting. The Bulgarian originals remain the reference; translation may contain errors.

The original alternative collection also contains its author's earlier AI-use note. That note is translated as part of the source content and is distinct from the disclosure of this translation.

## Sofia University references

The university's [regulations index](https://www.uni-sofia.bg/index.php/bul/universitet_t/administrativna_struktura/pravilnici_na_su) links to the September 2026 AI rules and guidance:

- [Rules for the use of AI, 24 September 2026](https://www.uni-sofia.bg/index.php/bul/content/download/363036/2325663/version/3/file/%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0%2B%D0%B7%D0%B0%2B%D0%B8%D0%B7%D0%BF%D0%BE%D0%BB%D0%B7%D0%B2%D0%B0%D0%BD%D0%B5%2B%D0%BD%D0%B0%2B%D0%98%D0%98_%D0%A1%D0%A3_24.09.2026.pdf): Article 27 calls for the system/model/version, purpose, and nature and scope of AI-generated or transformed content to be disclosed. Article 24 addresses critical verification; Article 26 addresses retention of prompts, results and intermediate versions, including at least one academic year for teaching activity.
- [Guidance for the use of AI systems, 23 September 2026](https://www.uni-sofia.bg/index.php/bul/content/download/363037/2325667/version/3/file/%D0%9D%D0%B0%D1%81%D0%BE%D0%BA%D0%B8%2B%D0%B7%D0%B0%2B%D0%B8%D0%B7%D0%BF%D0%BE%D0%BB%D0%B7%D0%B2%D0%B0%D0%BD%D0%B5%2B%D0%BD%D0%B0%2B%D0%A1%D0%98%D0%98%2B%D0%B2%2B%D0%A1%D0%A3%2B23.09.2026.pdf): section 1.5.3 addresses identification of AI-assisted teaching materials.

The disclosure records the assistance used. It does not certify completion of academic review or replace the instructor's responsibility to check the translated teaching materials. Retain this conversation and the original and translated source versions with the course records; this file is only a provenance summary.
