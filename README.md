# Maths_JEEAd_notes — an Obsidian vault

Hand-crafted, first-principles maths study notes that walk a student from
board-level basics to **JEE Advanced and Olympiad mathematics** — every formula
*derived from reasoning*, every answer *numerically verified*.

The whole repository **is an [Obsidian](https://obsidian.md) vault** (git-enabled):
one Markdown note per chapter, native Obsidian callouts, YAML frontmatter,
`[[Wikilinks]]`, and Dataview dashboards. Math is real LaTeX (`$…$`, `$$…$$`,
rendered by Obsidian's built-in MathJax).

## Open it in Obsidian

1. Clone / open this folder as a vault: **Obsidian → Open folder as vault** →
   select `Maths_JEEAd_notes`.
2. When prompted, **install the community plugins** listed in
   `.obsidian/community-plugins.json` (**Dataview**, **Templater**,
   **Excalidraw**) — Settings → Community plugins → Turn off restricted mode →
   Browse. The dashboards in [[Home]] need Dataview.
3. Start at **[[Home]]** (or open `Home.md`), then explore the Graph view.

> The core plugins (graph, backlinks, tags, properties, templates, callouts,
> MathJax) are already enabled — no install needed.

## Vault structure

```
Maths_JEEAd_notes/
├── Home.md                      # ★ vault entry point (Dataview dashboards)
├── .obsidian/                   # vault config, enabled plugins, CSS snippet
├── notes/                       # ★ the course — one folder per module
│   └── <Module>/
│       ├── <Module>.md                  # module index / course map
│       ├── 01-<chapter-slug>.md         # ONE note per chapter …
│       ├── … 02-… 03-… 04-… 05-… 06-…   #   (all content in the note)
│       ├── <Module> — Theory.md         # one-page theory reference
│       ├── <Module> — Paper.md          # Olympiad paper (sections A–H)
│       ├── <Module> — Solutions.md      # full worked solutions
│       └── assets/fig-XX.svg            # the module's diagrams
├── docs/                        # ROADMAP · coverage · formatting · diagrams
├── templates/markdown/          # skeletons for a new module (Templater-ready)
├── tools/                       # pure-Python stdlib gates (see below)
└── README.md · CONTRIBUTING.md · AGENTS.md
```

Each module has exactly **six chapter notes** numbered `01`…`06`, following one
arc: **foundations → machinery → core → applications → frontier → synthesis**.

## Modules

| Module | Folder | Chapters | Paper Qs | Index |
|---|---|---|---|---|
| **PnC** · Permutations & Combinations | `notes/PnC` | 6 | 40 | [[PnC]] |
| **Complex Numbers** | `notes/Complex-Numbers` | 6 | 38 | [[Complex-Numbers]] |
| **Binomial Theorem** | `notes/Binomial-Theorem` | 6 | 38 | [[Binomial-Theorem]] |
| **Conic Sections** | `notes/Conic-Sections` | 6 | 38 | [[Conic-Sections]] |

## The notes standard (short version)

Every module is well-ordered **board basics → JEE Main → JEE Advanced →
Olympiad frontier**, and:

- **First principles** — every formula is derived, never memorised; counting
  claims carry a small-case check ($n=3,4$).
- **Callouts** (Obsidian callout types): `[!abstract]` First Principles ·
  `[!tip]` Key Idea · `[!warning]` Common Trap · `[!example]` Olympiad
  Extension · `[!note]`/`[!info]` formulas · `[!quote]` named results.
- **Questions** — `S#` worked example, `P#` practice (woven between theory),
  `Q#` paper (sections A–H, 30–40 questions, answers in `<details>` blocks).
- **Numbering** — continuous per module (except PnC, which numbers P1–P8 within
  each chapter); paper `Q1…Qn` continuous across A–H.

The full rules live in [CONTRIBUTING.md](CONTRIBUTING.md); the machine-checkable
invariants for AI agents are in [AGENTS.md](AGENTS.md).

## Tooling (Python 3, stdlib only)

```bash
python3 tools/verify-md.py          # frontmatter, math balance, blocks, image links
python3 tools/verify-structure.py   # 6 chapters/module, unique names, P/S numbering
```

CI (`.github/workflows/verify.yml`) runs both on every push/PR to `main`.
`tools/migrate-to-obsidian.py` is the one-time script that converted the old
chapter-folder layout into this vault (kept for provenance).

## What's next

[[ROADMAP]] lists the full syllabus and tracks progress. **14 of the 15 planned
modules remain → 84 chapters** still to write from basics to Olympiad level (the
3 already-built extras — PnC, Complex Numbers, Binomial Theorem — sit beyond
that roadmap).

## Contributing

Follow [CONTRIBUTING.md](CONTRIBUTING.md) and the skeletons in
`templates/markdown/`, run the two gates, and open a PR — never push to `main`.
