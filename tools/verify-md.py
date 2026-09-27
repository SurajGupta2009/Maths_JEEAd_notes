#!/usr/bin/env python3
"""Quality gate for the Obsidian vault notes.

Usage:
  python3 tools/verify-md.py                    # notes/ + docs/ + root docs
  python3 tools/verify-md.py file1.md [file2.md ...]

Checks, per file:
  fm      — (notes/ only) file starts with a YAML frontmatter block that
            defines `title` and at least one of `module` / `type`
  math    — $$ display pairs are balanced; the remaining inline $ count is even
            (fenced code blocks are ignored)
  blocks  — <details>/<summary> pairs are balanced
  assets  — every ![](…svg) image link resolves to a real file, relative to
            the file that references it

Prints one line per file ending in PASS or FAIL; exits non-zero if any file
fails. Pair with tools/verify-structure.py for the whole-vault layout checks.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(ROOT, 'notes')


def check_frontmatter(s):
    if not s.startswith('---\n'):
        return 'missing frontmatter (file must start with ---)'
    end = s.find('\n---', 4)
    if end == -1:
        return 'unterminated frontmatter block'
    fm = s[4:end]
    if not re.search(r'^title:', fm, re.M):
        return 'frontmatter has no title:'
    if not re.search(r'^(module|type):', fm, re.M):
        return 'frontmatter has neither module: nor type:'
    return None


def iter_files():
    """Yield (path, require_frontmatter).

    notes/**/*.md get the full treatment (frontmatter required). docs/ and the
    root-level project docs (README, CONTRIBUTING, AGENTS, Home) get the
    math/block/image checks but are not required to carry frontmatter.
    """
    for dirpath, dirnames, filenames in os.walk(NOTES_DIR):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith('.'))
        for f in sorted(filenames):
            if f.endswith('.md'):
                yield os.path.join(dirpath, f), True
    for base in (os.path.join(ROOT, 'docs'), ROOT):
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = sorted(d for d in dirnames
                                 if not d.startswith('.') and d not in ('notes', 'templates'))
            for f in sorted(filenames):
                if f.endswith('.md'):
                    yield os.path.join(dirpath, f), False


def check(fn, require_fm=True):
    s = open(fn, encoding='utf-8').read()
    problems = []
    if require_fm:
        fm_err = check_frontmatter(s)
        if fm_err:
            problems.append(fm_err)
    t = re.sub(r'```.*?```', '', s, flags=re.S)  # ignore fenced code / mermaid
    t = re.sub(r'`[^`\n]*`', '', t)              # ignore inline code spans
    dollars = t.count('$$')
    if dollars % 2:
        problems.append('odd $$ count (%d)' % dollars)
    else:
        body = re.sub(r'\$\$.*?\$\$', '', t, flags=re.S)
        singles = body.count('$')
        if singles % 2:
            problems.append('odd inline $ count (%d)' % singles)
    d_open, d_close = t.count('<details'), t.count('</details>')
    if d_open != d_close:
        problems.append('unbalanced <details> %d/%d' % (d_open, d_close))
    s_open, s_close = t.count('<summary'), t.count('</summary>')
    if s_open != s_close:
        problems.append('unbalanced <summary> %d/%d' % (s_open, s_close))
    base = os.path.dirname(fn)
    for m in re.finditer(r'!\[[^]]*\]\(([^)]+)\)', t):
        target = os.path.normpath(os.path.join(base, m.group(1)))
        if not os.path.isfile(target):
            problems.append('missing image %s' % m.group(1))
    ok = not problems
    print('%s: %s' % (os.path.relpath(fn, ROOT),
                      'PASS' if ok else 'FAIL — ' + '; '.join(problems)))
    return ok


if __name__ == '__main__':
    args = sys.argv[1:]
    if args:
        files = [(f, f.startswith(NOTES_DIR + os.sep)) for f in args]
    else:
        files = list(iter_files())
    if not files:
        print('no markdown files found')
        sys.exit(1)
    allok = all(check(f, rf) for f, rf in files)
    sys.exit(0 if allok else 1)
