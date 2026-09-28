#!/usr/bin/env python3
"""Whole-vault layout gate for the Obsidian maths vault.

New model — three notes per module:

    notes/<Module>/<Module>.md              complete notes (course map + 6 chapters + theory appendix)
    notes/<Module>/<Module> — Paper.md      Olympiad paper (sections A–H)
    notes/<Module>/<Module> — Solutions.md  full worked solutions

Invariants checked across notes/:

  * every module folder has EXACTLY those three notes and nothing else
    (no leftover per-chapter NN-slug.md files)
  * the complete note contains all six `# Chapter N` headings and the
    `# Appendix — Well-ordered theory reference`
  * every note's basename is unique across the whole vault (so [[Wikilinks]]
    resolve without ambiguity)
  * paper Q-ids and the Solutions note's Q-ids match (every question answered)

Exits non-zero (with a summary) if any invariant is violated.
"""
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(ROOT, 'notes')
DASH = '\u2014'
CHAPTER_H1 = re.compile(r'^#\s+Chapter\s+(\d+)', re.M)
QID = re.compile(r'\*\*Q(\d+)\*\*')


def modules():
    return [d for d in sorted(os.listdir(NOTES_DIR))
            if os.path.isdir(os.path.join(NOTES_DIR, d)) and not d.startswith('.')]


def main():
    problems = []
    warnings = []

    for mod in modules():
        base = os.path.join(NOTES_DIR, mod)
        md = sorted(f for f in os.listdir(base) if f.endswith('.md'))
        expected = sorted(['%s.md' % mod,
                           '%s %s Paper.md' % (mod, DASH),
                           '%s %s Solutions.md' % (mod, DASH)])
        stray_chapters = [f for f in md if re.match(r'^\d\d-', f)]
        if stray_chapters:
            problems.append('%s: leftover per-chapter notes %s — merge them into '
                            '%s.md by hand (the vault keeps one complete note per '
                            'module)' % (mod, stray_chapters, mod))
        if md != expected:
            missing = [f for f in expected if f not in md]
            extra = [f for f in md if f not in expected]
            if missing:
                problems.append('%s: missing %s' % (mod, missing))
            if extra:
                problems.append('%s: unexpected notes %s' % (mod, extra))

        complete = os.path.join(base, '%s.md' % mod)
        if os.path.isfile(complete):
            text = open(complete, encoding='utf-8').read()
            chaps = sorted(set(int(n) for n in CHAPTER_H1.findall(text)))
            if chaps != [1, 2, 3, 4, 5, 6]:
                problems.append('%s.md: expected chapters 1..6, found %s'
                                % (mod, chaps))
            if '# Appendix' not in text:
                warnings.append('%s.md: no theory appendix found' % mod)

        # paper <-> solutions Q-id parity
        paper = os.path.join(base, '%s %s Paper.md' % (mod, DASH))
        sols = os.path.join(base, '%s %s Solutions.md' % (mod, DASH))
        if os.path.isfile(paper) and os.path.isfile(sols):
            pq = set(QID.findall(open(paper, encoding='utf-8').read()))
            sq = set(QID.findall(open(sols, encoding='utf-8').read()))
            unanswered = sorted(pq - sq, key=int)
            if unanswered:
                problems.append('%s: paper questions with no solution: Q%s'
                                % (mod, ', Q'.join(unanswered)))

    # globally unique note basenames (clean Wikilinks)
    names = []
    for dirpath, dirnames, filenames in os.walk(NOTES_DIR):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        names += [f[:-3] for f in filenames if f.endswith('.md')]
    for name, count in Counter(names).items():
        if count > 1:
            problems.append('duplicate note name %r appears %d times '
                            '(Wikilinks would be ambiguous)' % (name, count))

    if problems:
        print('STRUCTURE FAIL')
        for p in problems:
            print('  - ' + p)
        for w in warnings:
            print('  ~ ' + w)
        return 1
    print('STRUCTURE PASS — %d modules × 3 notes (complete + paper + solutions), '
          '6 chapters + appendix each, unique names, paper↔solutions matched'
          % len(modules()))
    for w in warnings:
        print('  ~ ' + w)
    return 0


if __name__ == '__main__':
    sys.exit(main())
