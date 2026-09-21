#!/usr/bin/env python3
"""Build each module's single-file snapshot <slug>-complete.md from the
canonical Markdown notes.

The per-chapter folders under notes/<Module>/ are the source of truth; the
complete file is a generated convenience snapshot (whole course in one file)
and is never edited by hand.

Order of the snapshot: module README (course map) -> chapters 01…06 ->
olympiad paper -> solutions.

Usage:
  python3 tools/build-complete.py all
  python3 tools/build-complete.py PnC

A module is any folder under notes/ that has a README.md and at least one
NN-<slug> chapter folder.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(ROOT, 'notes')


def slug(name):
    return re.sub(r'[\s_-]+', '-', name.strip().lower()).strip('-')


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def find_modules():
    out = []
    for d in sorted(os.listdir(NOTES_DIR)):
        p = os.path.join(NOTES_DIR, d)
        if d.startswith('.') or not os.path.isdir(p):
            continue
        has_chapters = any(re.match(r'\d\d-', x) and os.path.isdir(os.path.join(p, x))
                           for x in os.listdir(p))
        if os.path.isfile(os.path.join(p, 'README.md')) and has_chapters:
            out.append(d)
    return out


def build(module):
    base = os.path.join(NOTES_DIR, module)
    parts = [read(os.path.join(base, 'README.md')).rstrip()]
    for d in sorted(os.listdir(base)):
        full = os.path.join(base, d)
        if os.path.isdir(full) and re.match(r'\d\d-', d):
            readme = os.path.join(full, 'README.md')
            if os.path.isfile(readme):
                # Chapter files reference ../assets/ (one level deep); the
                # snapshot lives at module level, so normalise back to assets/.
                parts.append(read(readme).replace('](../assets/', '](assets/').rstrip())
    for name in ('olympiad-paper.md', 'olympiad-paper-solutions.md'):
        p = os.path.join(base, name)
        if os.path.isfile(p):
            parts.append(read(p).rstrip())
    out = '\n\n---\n\n'.join(parts) + '\n'
    dest = os.path.join(base, slug(module) + '-complete.md')
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(out)
    print(f'[{module}] wrote notes/{module}/{slug(module)}-complete.md ({len(out):,} bytes, '
          f'{len(parts)} parts)')


if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    mods = find_modules()
    if which.lower() == 'all':
        targets = mods
    else:
        targets = [m for m in mods if slug(m) == slug(which)]
        if not targets:
            raise SystemExit(f'no module matching {which!r}; found: '
                             + (', '.join(mods) if mods else '(none)'))
    for m in targets:
        build(m)
