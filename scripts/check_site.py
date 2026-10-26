"""Validate a built bilingual site without a web server: python scripts/check_site.py."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
ORIGIN = 'https://fmi-stochastics.github.io'


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.refs, self.ids, self.lang = [], set(), None
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        attr = 'href' if tag in ('a', 'link') else 'src'
        if tag in ('a', 'link', 'script', 'img') and attrs.get(attr):
            self.refs.append((tag, attrs[attr], attrs))


def main():
    if not SITE.exists():
        sys.exit('Build the site first: python -m mkdocs build --strict')
    errors, pdfs, cache = [], set(), {}
    routes = ['', 'alternative/', 'prob-stat/', 'prob-stat/applied-math/',
              'prob-stat/computer-science-2/', 'prob-stat/software-engineering/']
    for lang in ('bg', 'en'):
        for route in routes:
            prefix = '' if lang == 'bg' else 'en/'
            path = SITE / prefix / route / 'index.html'
            if not path.exists():
                errors.append(f'Missing page: {path.relative_to(SITE)}')
                continue
            text = path.read_text(encoding='utf-8')
            page = Page(text)
            url = ORIGIN + '/' + prefix + route
            if page.lang != lang:
                errors.append(f'{url}: incorrect document language {page.lang!r}')
            switch_match = re.search(r'<nav class="language-switch".*?</nav>', text, re.S)
            if not switch_match:
                errors.append(f'{url}: language switch absent')
            else:
                switch = Page(switch_match[0])
                links = {attrs.get('lang'): urljoin(url, href)
                         for tag, href, attrs in switch.refs if tag == 'a'}
                expected = {'bg': ORIGIN + '/' + route, 'en': ORIGIN + '/en/' + route}
                if links != expected:
                    errors.append(f'{url}: language switch {links}, expected {expected}')
            if lang == 'en' and 'ChatGPT (OpenAI, GPT-6)' not in text:
                errors.append(f'{url}: translation disclosure absent')
            for tag, href, attrs in page.refs:
                target = urlsplit(urljoin(url, href))
                if target.scheme not in ('http', 'https') or target.netloc != urlsplit(ORIGIN).netloc:
                    continue
                target_path = unquote(target.path).lstrip('/')
                destination = SITE / target_path
                if destination.is_dir():
                    destination /= 'index.html'
                if not destination.is_file():
                    errors.append(f'{url}: missing local target {href}')
                    continue
                if lang == 'en' and target_path.endswith('.pdf'):
                    pdfs.add(target_path)
                    if not target_path.startswith('en/'):
                        errors.append(f'{url}: PDF link falls back to Bulgarian: {href}')
                    if re.search(r'(manual|notes)', target_path, re.I):
                        errors.append(f'{url}: excluded manual/notes linked: {href}')
                if target.fragment and destination.suffix == '.html':
                    if destination not in cache:
                        cache[destination] = Page(destination.read_text(encoding='utf-8')).ids
                    if unquote(target.fragment) not in cache[destination]:
                        errors.append(f'{url}: missing anchor {href}')
    for error in sorted(set(errors)):
        print(error)
    print(f'Checked {2*len(routes)} pages; {len(pdfs)} unique English PDF links; '
          f'{len(set(errors))} errors.')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
