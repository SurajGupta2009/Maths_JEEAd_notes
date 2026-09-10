import re, html as H
from html.parser import HTMLParser

s = open('pnc-mindmap.html', encoding='utf-8').read()
srcs = ['index.html', '01-counting-basics.html', '02-permutations.html', '03-combinations.html',
        '04-binomial-and-identities.html', '05-advanced-methods.html', '06-olympiad-theory.html',
        'olympiad-paper.html', 'olympiad-paper-solutions.html']
non_idx = [f for f in srcs if f != 'index.html']

def tot(files, pat, flags=0):
    return sum(len(re.findall(pat, open(x, encoding='utf-8').read(), flags)) for x in files)

B = chr(92)
NQ, VQ, NB, VB = '<details class="q ', '<div class="q ', '<details class="box ', '<div class="box '
NQ2, VQ2 = '<details class="q solved', '<div class="q solved'
SUB, H3 = '<details class="mm-sub"', '<h3>'
SEC, CARD = '<details class="mm-sec"', '<div class="card">'
ANS = '<details class="ans"'
FIG, TAB, FMO = '<div class="figure">', '<table class="data">', '<div class="formula">'

so, sc = s.count(B + '('), s.count(B + ')')
ok = so == sc == tot(srcs, B + '(') and so == tot(srcs, B + ')')
print("math delims:", "OK" if ok else "FAIL", f"(src \\(={tot(srcs, B + '(')} out \\(={so})")

dq, vq = len(re.findall(NQ, s)) + s.count(NQ2), len(re.findall(VQ, s)) + s.count(VQ2)
print("q nodes:    details=", dq, " raw=", vq, " src=", tot(non_idx, VQ) + tot(non_idx, VQ2),
      "OK" if dq == tot(non_idx, VQ) + tot(non_idx, VQ2) and vq == 0 else "FAIL")

db, vb = len(re.findall(NB, s)), s.count(VB)
print("box nodes:  details=", db, " raw=", vb, " src=", tot(non_idx, VB),
      "OK" if db == tot(non_idx, VB) and vb == 0 else "FAIL")

print("sub nodes:  mm-sub=", s.count(SUB), " raw h3=", s.count(H3), " src h3=", tot(srcs, H3),
      "OK" if s.count(SUB) == tot(srcs, H3) and s.count(H3) == 0 else "FAIL")

n_cards = tot(non_idx, CARD) + tot(['index.html'], CARD) - 1  # minus skipped toc card
print("sec nodes:  mm-sec=", s.count(SEC), " raw card=", s.count(CARD), " src=", n_cards,
      "OK" if s.count(SEC) == n_cards and s.count(CARD) == 0 else "FAIL")

print("answers:    out=", s.count(ANS), " src=", tot(non_idx, ANS),
      "OK" if s.count(ANS) == tot(non_idx, ANS) else "FAIL")
print("figures:    out=", s.count(FIG), " src=", tot(non_idx, FIG),
      "OK" if s.count(FIG) == tot(non_idx, FIG) else "FAIL")
print("tables:     out=", s.count(TAB), " src=", tot(non_idx, TAB),
      "OK" if s.count(TAB) == tot(non_idx, TAB) else "FAIL")
print("formulas:   out=", s.count(FMO), " src=", tot(non_idx, FMO),
      "OK" if s.count(FMO) == tot(non_idx, FMO) else "FAIL")

qids = []
for f in non_idx:
    qids += re.findall(r'class="q-id">([^<]+)<', open(f, encoding='utf-8').read())
s_plain = H.unescape(s)
missing = sorted(set(q for q in qids if (q + ')</span>') not in s_plain))
print("q-ids:      src=", len(qids), " unique=", len(set(qids)), " missing=", missing)

h2s = []
for f in srcs:
    h2s += [re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).strip()
            for h in re.findall(r'<h2>.*?</h2>', open(f, encoding='utf-8').read(), re.S)]
s_norm = re.sub(r'\s+', ' ', s_plain)
miss = [t for t in h2s if t not in s_norm]
print("h2 titles:  src=", len(h2s), " missing=", miss)

class Checker(HTMLParser):
    VOID = {'meta', 'link', 'br', 'img', 'hr', 'input', 'circle', 'rect', 'line',
            'polyline', 'path', 'text', 'ellipse', 'polygon', 'use', 'stop'}
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID:
            self.stack.append((tag, self.getpos()))
    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if not self.stack:
            self.errors.append("unexpected </%s> at %s" % (tag, self.getpos()))
            return
        if self.stack[-1][0] != tag:
            names = [t for t, _ in self.stack]
            if tag in names:
                while self.stack and self.stack[-1][0] != tag:
                    t, p = self.stack.pop()
                    self.errors.append("unclosed <%s> at %s" % (t, p))
                self.stack.pop()
            else:
                self.errors.append("stray </%s> at %s" % (tag, self.getpos()))
        else:
            self.stack.pop()

c = Checker()
c.feed(s)
leftover = [(t, p) for t, p in c.stack if t not in ('html', 'body')]
print("tag balance:", "OK" if not c.errors and not leftover else "FAIL %s %s" % (c.errors[:4], leftover[:4]))

depth, neg, i = 0, False, 0
while i < len(s) - 1:
    if s[i] == B and s[i + 1] == '(':
        depth += 1; i += 2; continue
    if s[i] == B and s[i + 1] == ')':
        depth -= 1
        neg = neg or depth < 0
        depth = max(0, depth); i += 2; continue
    i += 1
print("math walk:  ", "OK" if depth == 0 and not neg else "FAIL depth=%d neg=%s" % (depth, neg))
