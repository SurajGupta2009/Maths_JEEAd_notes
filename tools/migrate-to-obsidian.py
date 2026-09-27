#!/usr/bin/env python3
"""One-time migration: legacy chapter-folder notes -> Obsidian single-file vault.

This repo was re-authored from the old "rules" (HTML mindmaps + one folder per
chapter + generated <slug>-complete.md snapshots) into a plain **Obsidian
vault**: one Markdown file per chapter, native Obsidian callouts, YAML
frontmatter and Wikilink navigation.

For each module under notes/ it reads the old layout

    <Module>/README.md                    ->  <Module>/<Module>.md
    <Module>/00-WELL-ORDERED-THEORY.md    ->  <Module>/<Module> — Theory.md
    <Module>/NN-slug/README.md            ->  <Module>/NN-slug.md
    <Module>/olympiad-paper.md            ->  <Module>/<Module> — Paper.md
    <Module>/olympiad-paper-solutions.md  ->  <Module>/<Module> — Solutions.md

and

  * prepends YAML frontmatter (title, module, chapter, level, tags, aliases)
  * rewrites the emoji callout boxes (⛁ 💡 ⚠ ★ 🏛 📌 📦 ƒ ✅ 🌉 🎯 🧮) into
    native Obsidian callouts  `> [!type] Title`
  * normalises image links from `](../assets/…` / `](../<Module>/assets/…`
    down to `](assets/…`
  * wires Wikilink navigation (module home / prev / next / paper / solutions)

It does NOT delete the old files: verify the output first, then remove the old
chapter folders, module README.md, the paper/solutions/theory files and every
*-complete.md with `git rm`. Kept for provenance; the notes are now authored
directly in the new layout. Run from the repo root:

    python3 tools/migrate-to-obsidian.py
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES = os.path.join(ROOT, 'notes')
TODAY = '2026-09-27'

DASH = '\u2014'  # em dash used in note names & titles

# Ordered so longer/compound markers win before their prefixes (⚠️ before ⚠).
EMOJI_CALLOUTS = [
    ('\u26a0\ufe0f', 'warning'),   # ⚠️
    ('\u26a0', 'warning'),         # ⚠
    ('\u26c1', 'abstract'),        # ⛁  First Principles
    ('\U0001f4a1', 'tip'),         # 💡 Key Idea / Method
    ('\u2605', 'example'),         # ★  Olympiad Extension
    ('\U0001f3db', 'example'),     # 🏛 Exam flavor / Olympiad / identity
    ('\U0001f4cc', 'note'),        # 📌 Note / Practice Set
    ('\U0001f4e6', 'info'),        # 📦 formula box
    ('\u0192', 'quote'),           # ƒ  Named Result / Property / Identity / Formula
    ('\u2705', 'success'),         # ✅ checklist
    ('\U0001f309', 'info'),        # 🌉 Bridge
    ('\U0001f3af', 'tip'),         # 🎯 Next
    ('\U0001f9ee', 'quote'),       # 🧮 Identity
]

LEVELS = {1: 'foundations', 2: 'machinery', 3: 'core',
          4: 'applications', 5: 'frontier', 6: 'synthesis'}


def find_modules():
    out = []
    for d in sorted(os.listdir(NOTES)):
        p = os.path.join(NOTES, d)
        if d.startswith('.') or not os.path.isdir(p):
            continue
        chapters = [x for x in sorted(os.listdir(p))
                    if re.match(r'\d\d-', x) and os.path.isdir(os.path.join(p, x))]
        if os.path.isfile(os.path.join(p, 'README.md')) and chapters:
            out.append((d, chapters))
    return out


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def first_h1(text):
    for line in text.split('\n'):
        if line.startswith('# '):
            return line[2:].strip()
    return ''


def chapter_parts(h1):
    m = re.match(r'Chapter\s+(\d+)\s*[\u2014\u2013-]\s*(.+)', h1)
    if m:
        return int(m.group(1)), m.group(2).strip()
    return None, h1


def yq(s):  # yaml-quote a scalar
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def frontmatter(fields):
    lines = ['---']
    for k, v in fields:
        if isinstance(v, list):
            seen, uniq = set(), []
            for item in v:
                if item and item not in seen:
                    seen.add(item)
                    uniq.append(item)
            lines.append('%s:' % k)
            lines += ['  - %s' % item for item in uniq]
        else:
            lines.append('%s: %s' % (k, v))
    lines.append('---')
    return '\n'.join(lines)


def transform_body(text, module):
    """Normalise image links and convert emoji callouts -> Obsidian callouts.

    Fenced code / mermaid blocks are left untouched.
    """
    text = text.replace('](../%s/assets/' % module, '](assets/')
    text = text.replace('](../assets/', '](assets/')

    out = []
    in_fence = False
    for line in text.split('\n'):
        if line.strip().startswith('```'):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence and line.startswith('> **'):
            inner = line[4:]
            if inner.endswith('**'):
                inner = inner[:-2]
            lead = inner.lstrip()
            for marker, typ in EMOJI_CALLOUTS:
                if lead.startswith(marker):
                    title = lead[len(marker):].lstrip()
                    out.append('> [!%s] %s' % (typ, title))
                    break
            else:
                out.append(line)
            continue
        out.append(line)
    return '\n'.join(out)


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def build_chapter(module, module_title, slug, idx, chapters, titles):
    src = os.path.join(NOTES, module, slug, 'README.md')
    body = transform_body(read(src), module)
    h1 = first_h1(body)
    num, title = chapter_parts(h1)
    disp = ('Chapter %d %s %s' % (num, DASH, title)) if num else h1
    prev_slug = chapters[idx - 1] if idx > 0 else None
    next_slug = chapters[idx + 1] if idx + 1 < len(chapters) else None
    prev = ('[[%s|%s]]' % (prev_slug, 'Chapter %d' % (num - 1))) if prev_slug \
        else ('[[%s|%s]]' % (module, module_title))
    nxt = ('[[%s|%s]]' % (next_slug, 'Chapter %d' % (num + 1))) if next_slug \
        else ('[[%s %s Paper|Olympiad Paper]]' % (module, DASH))
    fm = frontmatter([
        ('title', yq(disp)),
        ('aliases', [title, 'Ch %d %s %s' % (num, DASH, title)]),
        ('module', yq(module)),
        ('module_title', yq(module_title)),
        ('chapter', num),
        ('level', LEVELS.get(num, '')),
        ('tags', [module.lower(), 'chapter', LEVELS.get(num, '')]),
        ('created', TODAY),
    ])
    nav = ('> [!info] Navigation\n'
           '> \U0001f4d6 [[%s|%s]] \u00b7 \u2b05 %s \u00b7 %s \u27a1 \u00b7 '
           '\U0001f4dd [[%s %s Paper|Olympiad Paper]] \u00b7 '
           '\u2705 [[%s %s Solutions|Solutions]]'
           % (module, module_title, prev, nxt, module, DASH, module, DASH))
    out = fm + '\n\n' + nav + '\n\n' + body.rstrip() + '\n'
    write(os.path.join(NOTES, module, slug + '.md'), out)
    return disp


def build_theory(module, module_title, chapters):
    src = os.path.join(NOTES, module, '00-WELL-ORDERED-THEORY.md')
    if not os.path.isfile(src):
        return None
    body = transform_body(read(src), module)
    fm = frontmatter([
        ('title', yq('%s %s Well-Ordered Theory Reference' % (module_title, DASH))),
        ('aliases', ['%s Theory Reference' % module, '%s Theory' % module]),
        ('module', yq(module)),
        ('module_title', yq(module_title)),
        ('type', 'reference'),
        ('tags', [module.lower(), 'reference', 'theory']),
        ('created', TODAY),
    ])
    nav = ('> [!info] Navigation\n'
           '> \U0001f4d6 [[%s|%s]] \u00b7 \U0001f9ea [[%s %s Paper|Olympiad Paper]] \u00b7 '
           '\U0001f4da [[%s|First chapter]]'
           % (module, module_title, module, DASH, chapters[0]))
    out = fm + '\n\n' + nav + '\n\n' + body.rstrip() + '\n'
    name = '%s %s Theory.md' % (module, DASH)
    write(os.path.join(NOTES, module, name), out)
    return name


def build_paper(module, module_title, kind, chapters, titles):
    if kind == 'paper':
        src = os.path.join(NOTES, module, 'olympiad-paper.md')
        name = '%s %s Paper.md' % (module, DASH)
        title = '%s %s Olympiad Paper' % (module_title, DASH)
        tags = [module.lower(), 'paper', 'olympiad', 'assessment']
    else:
        src = os.path.join(NOTES, module, 'olympiad-paper-solutions.md')
        name = '%s %s Solutions.md' % (module, DASH)
        title = '%s %s Olympiad Paper Solutions' % (module_title, DASH)
        tags = [module.lower(), 'solutions', 'olympiad']
    if not os.path.isfile(src):
        return None
    body = transform_body(read(src), module)
    fm = frontmatter([
        ('title', yq(title)),
        ('aliases', ['%s %s' % (module, 'Paper' if kind == 'paper' else 'Solutions')]),
        ('module', yq(module)),
        ('module_title', yq(module_title)),
        ('type', kind),
        ('tags', tags),
        ('created', TODAY),
    ])
    if kind == 'paper':
        nav = ('> [!info] Navigation\n'
               '> \u2b05 [[%s|Chapter 6]] \u00b7 \U0001f4d6 [[%s|%s]] \u00b7 '
               '\u2705 [[%s %s Solutions|Solutions]] \u27a1'
               % (chapters[-1], module, module_title, module, DASH))
    else:
        nav = ('> [!info] Navigation\n'
               '> \u2b05 [[%s %s Paper|Paper]] \u00b7 \U0001f4d6 [[%s|%s]]'
               % (module, DASH, module, module_title))
    out = fm + '\n\n' + nav + '\n\n' + body.rstrip() + '\n'
    write(os.path.join(NOTES, module, name), out)
    return name


def transform_index_links(text, module, chapters, titles):
    """Rewrite the course-map links inside the old module README."""
    # [text](#chapter-N) -> [[slug|text]]
    def ch_sub(m):
        n = int(m.group(2))
        slug = chapters[n - 1] if 0 < n <= len(chapters) else chapters[0]
        return '[[%s|%s]]' % (slug, m.group(1))
    text = re.sub(r'\[([^\]]*)\]\(#chapter-(\d+)\)', ch_sub, text)
    text = re.sub(r'\[([^\]]*)\]\(#olympiad-paper\)',
                  lambda m: '[[%s %s Paper|%s]]' % (module, DASH, m.group(1)), text)
    text = re.sub(r'\[([^\]]*)\]\(#solutions\)',
                  lambda m: '[[%s %s Solutions|%s]]' % (module, DASH, m.group(1)), text)
    text = re.sub(r'\[([^\]]*)\]\(#course-map\)', lambda m: m.group(1), text)
    # links to the old single-file snapshot -> the course home
    text = re.sub(r'\[([^\]]*)\]\([\w./-]*-complete\.md\)',
                  lambda m: '[[%s|%s]]' % (module, m.group(1)), text)
    # drop dead links to the legacy HTML mindmap
    text = '\n'.join(l for l in text.split('\n') if 'mindmap.html' not in l)
    # drop inline "One file / whole course (mind map)" HTML-era fragments
    text = re.sub(r'[ \t]*(?:\u26a1[ \t]*)?One file \u00b7 whole course'
                  r'[^\n]*?(?:\*\*open \u2192\*\*|content change\.)', '', text)
    # any remaining folder links like (NN-slug/) -> [[NN-slug]]
    def folder_sub(m):
        target = m.group(2).rstrip('/')
        base = target.split('/')[-1]
        if base in chapters:
            return '[[%s|%s]]' % (base, m.group(1))
        return m.group(0)
    text = re.sub(r'\[([^\]]*)\]\(([\w./-]+/)\)', folder_sub, text)
    return text


def build_index(module, module_title, chapters, titles):
    src = os.path.join(NOTES, module, 'README.md')
    body = transform_body(read(src), module)
    # drop the legacy "one file / whole course (mind map)" HTML-era blurb
    body = re.sub(r'###[^\n]*One file[^\n]*\n\n[^\n]+\n+', '', body)
    body = transform_index_links(body, module, chapters, titles)
    fm = frontmatter([
        ('title', yq('%s %s %s' % (module_title, DASH, 'Course Notes'))),
        ('aliases', [module_title, module]),
        ('module', yq(module)),
        ('type', 'index'),
        ('tags', [module.lower(), 'module', 'index']),
        ('created', TODAY),
    ])
    chap_rows = []
    for i, slug in enumerate(chapters, 1):
        chap_rows.append('%d. [[%s|%s]]' % (i, slug, titles[slug]))
    nav = ('> [!info] Navigation\n'
           '> \U0001f4d6 [[Home|Vault home]] \u00b7 '
           '\U0001f9ea [[%s %s Paper|Olympiad Paper]] \u00b7 '
           '\u2705 [[%s %s Solutions|Solutions]] \u00b7 '
           '\U0001f4d8 [[%s %s Theory|Theory Reference]]'
           % (module, DASH, module, DASH, module, DASH))
    dv = ('\n\n## Chapters\n\n```dataview\n'
          'TABLE chapter AS "Ch", level AS "Level"\n'
          'FROM "notes/%s"\n'
          'WHERE chapter\n'
          'SORT chapter ASC\n```\n' % module)
    out = fm + '\n\n' + nav + '\n\n' + body.rstrip() + '\n' + dv
    write(os.path.join(NOTES, module, module + '.md'), out)


def main():
    mods = find_modules()
    if not mods:
        print('no modules found under notes/')
        return 1
    for module, chapters in mods:
        # module title = display name (folder slug with spaces)
        module_title = module.replace('-', ' ')
        titles = {}
        for slug in chapters:
            h1 = first_h1(read(os.path.join(NOTES, module, slug, 'README.md')))
            _, t = chapter_parts(h1)
            titles[slug] = t or slug
        print('[%s] %d chapters' % (module, len(chapters)))
        for i, slug in enumerate(chapters):
            disp = build_chapter(module, module_title, slug, i, chapters, titles)
            print('   -> %s.md  (%s)' % (slug, disp))
        tn = build_theory(module, module_title, chapters)
        if tn:
            print('   -> %s' % tn)
        pn = build_paper(module, module_title, 'paper', chapters, titles)
        if pn:
            print('   -> %s' % pn)
        sn = build_paper(module, module_title, 'solutions', chapters, titles)
        if sn:
            print('   -> %s' % sn)
        build_index(module, module_title, chapters, titles)
        print('   -> %s.md  (index)' % module)
    return 0


if __name__ == '__main__':
    sys.exit(main())
