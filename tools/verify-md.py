#!/usr/bin/env python3
"""Quality gate for the canonical Markdown notes under notes/.

Usage:
  python3 tools/verify-md.py                    # every *.md under notes/
  python3 tools/verify-md.py file1.md [file2.md ...]

Checks, per file:
  math   — $$ display pairs are balanced; the remaining inline $ count is even
           (fenced code blocks are ignored)
  blocks — <details>/<summary> pairs are balanced
  assets — every ![](…svg) image link resolves to a real file, relative to
           the file that references it

Prints one line per file ending in PASS or FAIL; exits non-zero if any file
fails. This is the Markdown counterpart of tools/verify-math.py (HTML gate).
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(ROOT, 'notes')


def all_md():
    out = []
    for dirpath, dirnames, filenames in os.walk(NOTES_DIR):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith('.'))
        out += [os.path.join(dirpath, f) for f in sorted(filenames) if f.endswith('.md')]
    return out


def check(fn):
    s = open(fn, encoding='utf-8').read()
    problems = []
    t = re.sub(r'```.*?```', '', s, flags=re.S)  # ignore fenced code / mermaid
    t = re.sub(r'`[^`\n]*`', '', t)              # ignore inline code spans
    dollars = t.count('$$')
    if dollars % 2:
        problems.append(f"odd $$ count ({dollars})")
    else:
        body = re.sub(r'\$\$.*?\$\$', '', t, flags=re.S)
        singles = body.count('$')
        if singles % 2:
            problems.append(f"odd inline $ count ({singles})")
    d_open, d_close = t.count('<details'), t.count('</details>')
    if d_open != d_close:
        problems.append(f"unbalanced <details> {d_open}/{d_close}")
    s_open, s_close = t.count('<summary'), t.count('</summary>')
    if s_open != s_close:
        problems.append(f"unbalanced <summary> {s_open}/{s_close}")
    base = os.path.dirname(fn)
    for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', s):
        target = os.path.normpath(os.path.join(base, m.group(1)))
        if not os.path.isfile(target):
            problems.append(f"missing image {m.group(1)}")
    ok = not problems
    print(f'{os.path.relpath(fn, ROOT)}: '
          f'{"PASS" if ok else "FAIL — " + "; ".join(problems)}')
    return ok


if __name__ == '__main__':
    files = sys.argv[1:] or all_md()
    if not files:
        print('no markdown files found under notes/')
        sys.exit(1)
    allok = all(check(f) for f in files)
    sys.exit(0 if allok else 1)
