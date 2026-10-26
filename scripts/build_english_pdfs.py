"""Compile the English archive with pdfLaTeX. Run from any directory.

Examples:
    python scripts/build_english_pdfs.py
    python scripts/build_english_pdfs.py --match '*homework-1*'

The PDFs already in docs/ are sufficient to preview the website; this script
is only needed after changing the English TeX sources.
"""
from pathlib import Path
import argparse
import fnmatch
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'tex' / 'en'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--match', default='*', help='Wildcard matched against the TeX filename')
    parser.add_argument('--changed', action='store_true', help='Only compile missing or older PDFs')
    args = parser.parse_args()
    engine = shutil.which('pdflatex')
    if not engine:
        parser.error('pdfLaTeX was not found. Install MiKTeX or TeX Live and restart your terminal.')
    sources = [p for p in sorted(SOURCE.rglob('*.tex'))
               if fnmatch.fnmatch(p.name, args.match)
               and '\\documentclass' in p.read_text(encoding='utf-8-sig')]
    if not sources:
        parser.error('No standalone English TeX documents match this selection.')
    failed = []
    dependencies = [SOURCE / 'preamble.tex'] + list((ROOT / 'tex' / 'assets').rglob('*'))
    dependency_time = max(p.stat().st_mtime for p in dependencies if p.is_file())
    compiled = 0
    for source in sources:
        relative = source.relative_to(SOURCE)
        destination = ROOT / 'docs' / 'en'
        if relative.parts[0] == 'prob-stat':
            destination /= 'files'
        destination = destination / relative.with_suffix('.pdf')
        if (args.changed and destination.exists()
                and destination.stat().st_mtime >= max(source.stat().st_mtime, dependency_time)):
            continue
        compiled += 1
        build = ROOT / '.pdf-build' / relative.parent / source.stem
        build.mkdir(parents=True, exist_ok=True)
        result = None
        for _ in range(2):
            result = subprocess.run(
                [engine, '-interaction=nonstopmode', '-halt-on-error',
                 '-file-line-error', '-no-shell-escape',
                 f'-output-directory={build}', str(source)],
                cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (build / 'console.txt').write_bytes(result.stdout)
            if result.returncode:
                break
        if result.returncode:
            failed.append(str(relative))
            print(f'FAILED {relative}; see {build / "console.txt"}', flush=True)
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(build / source.with_suffix('.pdf').name, destination)
        print(f'OK {relative}', flush=True)
    print(f'{compiled-len(failed)}/{compiled} documents compiled; {len(sources)-compiled} already current.')
    return bool(failed)


if __name__ == '__main__':
    sys.exit(main())
