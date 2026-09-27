#!/usr/bin/env python3
"""Merge each module's separate chapter notes into ONE complete-notes file.

New vault model — one Markdown file per module holds the *complete* notes
(module course map + all six chapters + the theory-reference appendix), and the
Olympiad paper and its solutions stay as two separate files:

    notes/<Module>/<Module>.md              <- complete notes (this script builds it)
    notes/<Module>/<Module> — Paper.md      <- hand-authored
    notes/<Module>/<Module> — Solutions.md  <- hand-authored

This is a ONE-TIME migration from the earlier one-file-per-chapter layout. After
it runs, `<Module>.md` is the canonical, hand-edited note — so the script is a
safe no-op once the chapter notes are gone (it refuses to overwrite an existing
complete file unless the per-chapter sources are still present).

Usage:
  python3 tools/build-complete.py            # every module that still has chapter notes
  python3 tools/build-complete.py PnC        # one module
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES = os.path.join(ROOT, 'notes')
DASH = '\u2014'
TODAY = '2026-09-27'
CHAPTER_RE = re.compile(r'^\d\d-.+\.md$')


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def write(p, s):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


def strip_frontmatter(text):
    if text.startswith('---\n'):
        end = text.find('\n---', 4)
        if end != -1:
            return text[end + 4:].lstrip('\n')
    return text


def strip_nav(text):
    lines = text.split('\n')
    i = 0
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    if i < len(lines) and lines[i].strip() == '> [!info] Navigation':
        i += 1
        while i < len(lines) and lines[i].lstrip().startswith('>'):
            i += 1
        while i < len(lines) and lines[i].strip() == '':
            i += 1
    return '\n'.join(lines[i:])


def drop_first_h1(text):
    lines = text.split('\n')
    if lines and lines[0].startswith('# '):
        lines = lines[1:]
        while lines and lines[0].strip() == '':
            lines = lines[1:]
    return '\n'.join(lines)


def remove_dataview_block(text):
    return re.sub(r'\n*## Chapters\n\n```dataview.*?```\s*$', '', text, flags=re.S)


def remove_section(text, heading_substr):
    """Drop the section introduced by a heading containing heading_substr,
    up to (not including) the next heading of any level."""
    lines = text.split('\n')
    out, skipping = [], False
    for line in lines:
        if not skipping and re.match(r'^#{1,6}\s', line) and heading_substr in line:
            skipping = True
            continue
        if skipping and re.match(r'^#{1,6}\s', line):
            skipping = False
        if not skipping:
            out.append(line)
    return '\n'.join(out)


def chapter_titles(text):
    hs = []
    for line in text.split('\n'):
        m = re.match(r'^#\s+Chapter\s+(\d+)\s*[\u2014\u2013-]\s*(.+)$', line)
        if m:
            hs.append((int(m.group(1)), m.group(2).strip()))
    return hs


def yq(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def frontmatter(module, module_title):
    return '\n'.join([
        '---',
        'title: %s' % yq('%s %s Complete Notes' % (module_title, DASH)),
        'aliases:',
        '  - %s' % module_title,
        '  - %s' % module,
        'module: %s' % yq(module),
        'type: notes',
        'tags:',
        '  - %s' % module.lower(),
        '  - module',
        '  - complete',
        'created: %s' % TODAY,
        '---',
    ])


def build(module):
    base = os.path.join(NOTES, module)
    chapter_files = sorted(f for f in os.listdir(base) if CHAPTER_RE.match(f))
    if not chapter_files:
        print('[%s] no per-chapter notes found — already merged, leaving %s.md '
              'untouched' % (module, module))
        return False
    module_title = module.replace('-', ' ')

    index_body = strip_nav(strip_frontmatter(read(os.path.join(base, module + '.md'))))
    index_body = remove_dataview_block(index_body)
    index_body = remove_section(index_body, 'Chapters')  # drop the "### 1–6 Chapters" mega-line

    ch_bodies, h1s = [], []
    for f in chapter_files:
        t = strip_nav(strip_frontmatter(read(os.path.join(base, f))))
        ch_bodies.append(t.rstrip())
        h1s += chapter_titles(t)

    theory_path = os.path.join(base, '%s %s Theory.md' % (module, DASH))
    appendix = ''
    if os.path.isfile(theory_path):
        appendix = ('# Appendix %s Well-Ordered Theory Reference\n\n'
                    % DASH + drop_first_h1(strip_nav(strip_frontmatter(read(theory_path)))).rstrip())

    toc = '## Contents\n\n' + '\n'.join(
        '%d. Chapter %d %s %s' % (i, n, DASH, title) for i, (n, title) in enumerate(h1s, 1))

    nav = ('> [!info] Navigation\n'
           '> \U0001f4d6 [[Home|Vault home]] \u00b7 \U0001f4dd [[%s %s Paper|Olympiad Paper]] '
           '\u00b7 \u2705 [[%s %s Solutions|Solutions]]' % (module, DASH, module, DASH))

    parts = [index_body.rstrip(), toc] + ch_bodies
    if appendix:
        parts.append(appendix)
    body = '\n\n---\n\n'.join(parts)
    out = frontmatter(module, module_title) + '\n\n' + nav + '\n\n' + body + '\n'
    write(os.path.join(base, module + '.md'), out)
    print('[%s] merged %d chapters%s into %s.md (%s bytes)'
          % (module, len(chapter_files), ' + theory' if appendix else '',
             module, format(len(out), ',')))
    return True


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    mods = [d for d in sorted(os.listdir(NOTES))
            if os.path.isdir(os.path.join(NOTES, d)) and not d.startswith('.')]
    if which.lower() != 'all':
        mods = [m for m in mods if m.lower() == which.lower()]
    for m in mods:
        build(m)
    return 0


if __name__ == '__main__':
    sys.exit(main())
