#!/usr/bin/env python3
"""Verify CN (or PnC) chapter HTML: tag balance + math delimiters/braces."""
import re, sys
from html.parser import HTMLParser

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

def check(fn):
    s = open(fn).read()
    errs, unc = balance(s)
    t = re.sub(r'<script.*?</script>', '', s, flags=re.S)
    t = re.sub(r'<style.*?</style>', '', t, flags=re.S)
    dm = re.findall(r'\\\[.*?\\\]', t, re.S)
    bad = [(k, walk(d), d[:60].replace(chr(10), ' ')) for k, d in enumerate(dm) if walk(d) != 'OK']
    body = re.sub(r'\\\[.*?\\\]', '', t, flags=re.S)
    im = re.findall(r'\\\((.*?)\\\)', body, re.S)
    badi = [(k, walk(d), d[:60]) for k, d in enumerate(im) if walk(d) != 'OK']
    ok = not errs and not unc and not bad and not badi
    print(f'{fn}: balance {"OK" if not errs and not unc else (errs or unc)} | '
          f'math D{len(dm)}/bad{len(bad)} I{len(im)}/bad{len(badi)} -> {"PASS" if ok else "FAIL"}')
    for x in errs[:4]: print('   B', x)
    for x in bad: print('   D', x)
    for x in badi: print('   I', x)
    return ok

if __name__ == '__main__':
    allok = all(check(f) for f in sys.argv[1:])
    sys.exit(0 if allok else 1)
