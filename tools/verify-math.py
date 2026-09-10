#!/usr/bin/env python3
"""Quality gate for note HTML: tag balance + MathJax delimiter balance.

Usage:
  python3 tools/verify-math.py file1.html [file2.html ...]
  python3 tools/verify-math.py                 # every *.html in the repo

Checks, per file:
  balance  — HTML tags open/close in proper nesting (VOID/SVG tags exempt)
  math D*  — every \\[ ... \\] display span has balanced braces/brackets/parens
  math I*  — the same for every \\( ... \\) inline span
  $$       — display-math $$ pairs are even in count outside script/style

Prints one line per file ending in PASS or FAIL; exits non-zero if any file
fails. This is the gate CI runs — see .github/workflows/verify.yml.
"""
import os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root

VOID = {'area','base','br','col','embed','hr','img','input','link','meta',
        'source','track','wbr','circle','rect','line','path','ellipse',
        'polygon','polyline','stop','use','text','tspan'}
PAIRS = {'\\{':'\\}', '[':']', '(':')', '\\[':'\\]'}

def walk(s):
    i, n, stack = 0, len(s), []
    opens, closes = set(PAIRS), set(PAIRS.values())
    while i < n:
        c = s[i]
        if c == '\\':
            if i+1 >= n: return f'dangling backslash @{i}'
            nx = s[i+1]
            if nx == '\\': i += 2; continue
            if nx in '{[':
                stack.append(PAIRS['\\'+nx]); i += 2; continue
            if nx == '}':
                if stack and stack[-1] == '\\}': stack.pop()
                i += 2; continue
            if nx == ']':
                if stack and stack[-1] == '\\]': stack.pop()
                i += 2; continue
            if re.match(r'[a-zA-Z]', nx):
                i += len(re.match(r'[a-zA-Z]+', s[i+1:]).group()) + 1; continue
            i += 2; continue
        if c in opens:
            if c == '[' and i > 0 and s[i-1] == '\\': i += 1; continue
            stack.append(PAIRS[c]); i += 1; continue
        if c in closes:
            if not stack: return f'bad close {c!r} @{i}'
            if stack[-1] == c:
                stack.pop(); i += 1; continue
            if (c == ']' and stack[-1] == ')') or (c == ')' and stack[-1] == ']'):
                stack.pop(); i += 1; continue   # interval notation (a, b] / [a, b)
            return f'bad close {c!r} @{i} top={stack[-3:]}'
        i += 1
    if stack: return f'unclosed {stack[-4:]}'
    return 'OK'

def balance(s):
    class P(HTMLParser):
        def __init__(s):
            super().__init__(); s.st = []; s.err = []
        def handle_starttag(s, t, a):
            if t not in VOID: s.st.append((t, s.getpos()))
        def handle_endtag(s, t):
            if t in VOID: return
            if not s.st: s.err.append(f'extra </{t}> {s.getpos()}'); return
            if s.st[-1][0] != t: s.err.append(f'mismatch </{t}> at {s.getpos()} top={s.st[-3:]}')
            else: s.st.pop()
    p = P(); p.feed(s); p.close()
    return p.err, p.st

def all_html():
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith('.')
                             and d not in ('node_modules', '__pycache__', '.venv'))
        out += [os.path.join(dirpath, f) for f in sorted(filenames) if f.endswith('.html')]
    return out

def check(fn):
    s = open(fn, encoding='utf-8').read()
    errs, unc = balance(s)
    t = re.sub(r'<script.*?</script>', '', s, flags=re.S)
    t = re.sub(r'<style.*?</style>', '', t, flags=re.S)
    dm = re.findall(r'\\\[.*?\\\]', t, re.S)
    bad = [(k, walk(d), d[:60].replace(chr(10), ' ')) for k, d in enumerate(dm) if walk(d) != 'OK']
    body = re.sub(r'\\\[.*?\\\]', '', t, flags=re.S)
    im = re.findall(r'\\\((.*?)\\\)', body, re.S)
    badi = [(k, walk(d), d[:60]) for k, d in enumerate(im) if walk(d) != 'OK']
    rest = re.sub(r'\\\((.*?)\\\)', '', body, flags=re.S)
    n_dollars = rest.count('$$')
    odd_dollars = n_dollars % 2
    ok = not errs and not unc and not bad and not badi and not odd_dollars
    print(f'{fn}: balance {"OK" if not errs and not unc else (errs or unc)} | '
          f'math D{len(dm)}/bad{len(bad)} I{len(im)}/bad{len(badi)} '
          f'$${n_dollars // 2}/bad{odd_dollars} -> {"PASS" if ok else "FAIL"}')
    for x in errs[:4]: print('   B', x)
    for x in bad: print('   D', x)
    for x in badi: print('   I', x)
    if odd_dollars:
        k = rest.rfind('$$')
        print('   $ unpaired $$ outside script/style, near byte', k)
    return ok

if __name__ == '__main__':
    files = sys.argv[1:] or all_html()
    if not files:
        print('no html files found')
        sys.exit(1)
    allok = all(check(f) for f in files)
    sys.exit(0 if allok else 1)
