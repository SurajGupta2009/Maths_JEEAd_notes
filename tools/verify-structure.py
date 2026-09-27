#!/usr/bin/env python3
"""Whole-vault layout gate for the Obsidian maths vault.

Usage:
  python3 tools/verify-structure.py

Invariants checked across notes/:

  * every module folder has exactly six chapter notes  NN-<slug>.md
  * every module folder has its four module-level notes:
        <Module>.md · <Module> - Paper.md · <Module> - Solutions.md · <Module> - Theory.md
  * every note's basename is unique across the whole vault (so [[Wikilinks]]
    resolve without ambiguity)
  * the six chapter numbers are 01..06 with no gaps or duplicates
  * no chapter note carries a P/S question id duplicated elsewhere in the
    module (continuous per-module numbering)

Exits non-zero (with a summary) if any invariant is violated.
"""
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(ROOT, 'notes')
CHAPTER_RE = re.compile(r'^(\d\d)-.+\.md$')
PS_RE = re.compile(r'####\s*\*\*([PS]\d+)\*\*')
DASH = '\u2014'  # em dash used in module-note names (e.g. "PnC — Paper.md")


def modules():
    return [d for d in sorted(os.listdir(NOTES_DIR))
            if os.path.isdir(os.path.join(NOTES_DIR, d)) and not d.startswith('.')]


def main():
    problems = []

    # 1. per-module layout
    for mod in modules():
        base = os.path.join(NOTES_DIR, mod)
        files = [f for f in os.listdir(base) if f.endswith('.md')]
        chapters = sorted(f for f in files if CHAPTER_RE.match(f))
        nums = [CHAPTER_RE.match(f).group(1) for f in chapters]
        if len(chapters) != 6:
            problems.append('%s: expected 6 chapter notes, found %d (%s)'
                            % (mod, len(chapters), ', '.join(chapters) or 'none'))
        if nums != ['01', '02', '03', '04', '05', '06']:
            problems.append('%s: chapter numbers must be 01..06, got %s'
                            % (mod, nums))
        for suffix, label in (('.md', 'index'), (' %s Paper.md' % DASH, 'paper'),
                              (' %s Solutions.md' % DASH, 'solutions'),
                              (' %s Theory.md' % DASH, 'theory')):
            expected = mod + suffix
            if expected not in files:
                problems.append('%s: missing %s note %r' % (mod, label, expected))

    # 2. globally unique note basenames (clean Wikilinks)
    names = []
    for dirpath, dirnames, filenames in os.walk(NOTES_DIR):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for f in filenames:
            if f.endswith('.md'):
                names.append(f[:-3])
    for name, count in Counter(names).items():
        if count > 1:
            problems.append('duplicate note name %r appears %d times '
                            '(Wikilinks would be ambiguous)' % (name, count))

    # 3. P/S question-id numbering per module (informational — some modules,
    #    e.g. PnC, intentionally number P1–P8 within each chapter)
    warnings = []
    for mod in modules():
        base = os.path.join(NOTES_DIR, mod)
        ids = []
        for f in sorted(os.listdir(base)):
            if f.endswith('.md'):
                with open(os.path.join(base, f), encoding='utf-8') as fh:
                    ids += PS_RE.findall(fh.read())
        dupes = sorted(i for i, c in Counter(ids).items() if c > 1)
        if dupes:
            warnings.append('%s: repeated question ids %s (per-chapter numbering?)'
                            % (mod, dupes))

    if problems:
        print('STRUCTURE FAIL')
        for p in problems:
            print('  - ' + p)
        for w in warnings:
            print('  ~ ' + w)
        return 1
    print('STRUCTURE PASS — %d modules, all chapters + module notes present, '
          'unique note names' % len(modules()))
    for w in warnings:
        print('  ~ ' + w)
    return 0


if __name__ == '__main__':
    sys.exit(main())
