"""Extract prompt-box texts from workshop.html as the Copy button would (innerText-like)."""
import html, json, re, sys
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.cur, self.depth = {}, None, 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.cur is None and tag == 'div' and 'prompt-box' in (a.get('class') or '').split():
            self.cur, self.depth, self.buf = a['id'], 1, []
        elif self.cur is not None:
            if tag == 'div': self.depth += 1
            if tag == 'br': self.buf.append('\n')
    def handle_endtag(self, tag):
        if self.cur is not None and tag == 'div':
            self.depth -= 1
            if self.depth == 0:
                self.out[self.cur] = ''.join(self.buf).strip()
                self.cur = None
    def handle_data(self, d):
        if self.cur is not None: self.buf.append(d)

p = P(); p.feed(open(sys.argv[1], encoding='utf-8').read())
json.dump(p.out, sys.stdout, ensure_ascii=False, indent=1)
