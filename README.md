# FMI probability teaching site

The Bulgarian site is served at `/` and the English site at `/en/`. The BG / EN links in the upper-right corner switch to the corresponding page. The alternative exercises are available only through direct links at `/alternative/` and `/en/alternative/`; they are omitted from the main navigation.

## Preview with Anaconda on Windows

Open **Anaconda Prompt**, then run:

```bat
cd /d C:\GitHub\fmi-stochastics.github.io
conda activate fmi-site
python -m pip install -r requirements.txt
python -m mkdocs serve --dev-addr 127.0.0.1:8000
```

Keep that window open. Visit:

- Bulgarian: <http://127.0.0.1:8000/>
- English: <http://127.0.0.1:8000/en/>
- English alternative exercises: <http://127.0.0.1:8000/en/alternative/>

Press **Ctrl+C** in Anaconda Prompt to stop the preview. Changes to pages are automatically rebuilt while the preview is running.

If the `fmi-site` environment does not exist on another computer, create it once with `conda create -n fmi-site python=3.12`, then use the commands above. If port 8000 is in use, change `8000` to `8001` in both the command and browser address.

The compiled PDFs are included. Previewing the site does not require LaTeX.

## Files to edit

| Content | Location |
|---|---|
| Bulgarian pages | `docs/` |
| English pages | `docs/en/` |
| English archive PDFs | `docs/en/files/prob-stat/` |
| English alternative PDF | `docs/en/alternative/exercises.pdf` |
| Active Bulgarian alternative PDF | `docs/alternative/informatics-2026-2027.pdf` |
| English TeX sources | `tex/en/` |
| Supplied Bulgarian alternative TeX | `tex/bg/alternative/exercises.tex` |
| Shared TeX graphics and style file | `tex/assets/` |
| Languages and navigation | `mkdocs.yml` |
| Language switch | `overrides/partials/alternate.html` |
| English translation disclosure | `overrides/main.html`, `tex/en/preamble.tex` |

The English version omits the manual and lecture notes. Existing Bulgarian materials remain available. The alternative collection is the supplied 2026/2027 version; its complete English source is `tex/en/alternative/exercises.tex`. For weekly Bulgarian updates, replace `docs/alternative/informatics-2026-2027.pdf` in place so the page and download URLs stay the same. The older Bulgarian PDF remains unlinked for compatibility with previously shared URLs.

## Check a build

From the repository folder with the Anaconda environment active:

```bat
python -m mkdocs build --strict
python scripts\check_site.py
```

The second command checks local page, PDF and anchor links and verifies that BG / EN points to the corresponding page in each language.

## Rebuild English PDFs after editing TeX

Install MiKTeX or TeX Live with `pdflatex` available on PATH. Then run:

```bat
python scripts\build_english_pdfs.py
```

To rebuild a selection:

```bat
python scripts\build_english_pdfs.py --match "*2024-homework-1.tex"
```

The script compiles twice, writes temporary files into `.pdf-build/`, and replaces the corresponding English PDFs in `docs/en/`. It does not compile the Bulgarian originals. The existing English Cambridge homework handout is retained directly from its original PDF and has no translated TeX source.

Translation provenance and university disclosure references are in [TRANSLATION.md](TRANSLATION.md).
