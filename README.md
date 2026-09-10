# Maths_JEEAd_notes

Hand-crafted, self-contained HTML study notes that walk a JEE aspirant from
board-level basics to JEE Advanced and Olympiad mathematics — every formula
*derived from reasoning*, every answer numerically verified, one single HTML
file per chapter.

[![verify](https://img.shields.io/github/actions/workflow/status/SurajGupta2009/Maths_JEEAd_notes/verify.yml?branch=main&style=flat-square&label=verify)](https://github.com/SurajGupta2009/Maths_JEEAd_notes/actions/workflows/verify.yml)

## Modules

| Module | Status | Chapters | Practice Qs | Paper Qs | Mind map | Open |
|---|---|---|---|---|---|---|
| **PnC** · Permutations & Combinations | ✅ complete | 6 | 47 (P1–P8 per chapter) | 40 (A–G + stretch) | [pnc-mindmap.html](PnC/pnc-mindmap.html) | [index.html](PnC/index.html) |
| **Complex Numbers** | ✅ complete | 6 | 50 (P1–P51, continuous) | 38 (A–H) | [cn-mindmap.html](Complex%20Numbers/cn-mindmap.html) | [index.html](Complex%20Numbers/index.html) |
| **Binomial Theorem** | ✅ complete | 6 | 47 (P1–P47, continuous) | 38 (A–H) | [binomial-theorem-mindmap.html](Binomial-Theorem/binomial-theorem-mindmap.html) | [index.html](Binomial-Theorem/index.html) |

Each module ships: a chapter-per-file course (`01-…`–`06-…`), an
Olympiad-level paper with per-question answer pills, a full worked-solutions
file, and a generated single-file recursive mind map.

## Planned modules (roadmap)

Ordered draft — **curation of the final list and order is on hold for review**.
Proposed folder slugs follow the naming rule (see [CONTRIBUTING.md](CONTRIBUTING.md)).

| # | Module | Proposed folder |
|---|---|---|
| 1 | Quadratic Equations | `Quadratic-Equations/` |
| 2 | Inequalities | `Inequalities/` |
| 3 | Trigonometry | `Trigonometry/` |
| 4 | Sequences & Series | `Sequences-and-Series/` |
| 5 | Limits & Continuity | `Limits-and-Continuity/` |
| 6 | Differentiation | `Differentiation/` |
| 7 | Applications of Derivatives | `Applications-of-Derivatives/` |
| 8 | Integration | `Integration/` |
| 9 | Differential Equations | `Differential-Equations/` |
| 10 | Coordinate Geometry — Lines & Circles | `Coordinate-Geometry-Lines-and-Circles/` |
| 11 | Conic Sections | `Conic-Sections/` |
| 12 | 3D Geometry | `3D-Geometry/` |
| 13 | Vectors | `Vectors/` |
| 14 | Matrices & Determinants | `Matrices-and-Determinants/` |
| 15 | Probability | `Probability/` |

## Quick start

No build step, no dependencies — just open a module home in a browser:

- `PnC/index.html`
- `Complex Numbers/index.html`

Internet **is** required for the MathJax CDN (formulas render via jsdelivr;
everything else works offline). To check tooling: Python 3, stdlib only.

## Repo structure

```
Maths_JEEAd_notes/
├── .github/workflows/verify.yml    CI: runs the verifier over every *.html + mind-map checks
├── PnC/                            module: Permutations & Combinations (golden reference)
│   ├── index.html                  module home: banner, chips, roadmap SVG, chapter TOC
│   ├── 01-counting-basics.html       one big file per chapter (01…06)
│   ├── … 02-permutations.html … 06-olympiad-theory.html
│   ├── olympiad-paper.html         40 Q, sections A–H, answer pills
│   ├── olympiad-paper-solutions.html  full worked solutions (method-first)
│   ├── pnc-mindmap.html            GENERATED — single-file recursive mind map
│   └── assets/notes.css            shared stylesheet (copied per module)
├── Complex Numbers/                module: same shape (folder keeps its space — intentional)
│   ├── …
│   └── cn-mindmap.html             GENERATED
├── templates/                      skeletons for new modules
│   ├── module-index.html           module home (chips, roadmap SVG, chapter cards)
│   ├── chapter.html                chapter page (topnav → ch-head → cards → q → foot)
│   ├── olympiad-paper.html         paper page (section card, Q + answer pill, technique box)
│   ├── olympiad-paper-solutions.html  method-first solved-question page
│   └── CHECKLIST.md                the ordered 10-step procedure for a new module
├── tools/
│   ├── build-mindmap.py            mind-map builder (auto-discovers any module folder)
│   ├── verify-mindmap.py           mind map ↔ source completeness check
│   ├── verify-math.py              quality gate: HTML tag + MathJax delimiter balance
│   └── mindmap-overrides.json      per-module label pins & CLI aliases
├── README.md · CONTRIBUTING.md · AGENTS.md · .gitignore
```

## Tooling

```bash
# regenerate the mind map for one module, or every module (idempotent):
python3 tools/build-mindmap.py PnC
python3 tools/build-mindmap.py cn          # alias for 'Complex Numbers'
python3 tools/build-mindmap.py all

# quality gate — HTML tag balance + MathJax delimiter balance, every file must PASS:
python3 tools/verify-math.py                       # all *.html in the repo
python3 tools/verify-math.py PnC/01-counting-basics.html "Complex Numbers/index.html"

# mind-map completeness (q/box/section/answer counts match the source pages):
python3 tools/verify-mindmap.py all
```

Mind maps are **generated artifacts**: never hand-edit them — the CI checks
that a rebuild is a no-op. New chapters need no builder config: any top-level
folder containing an `index.html` is auto-discovered.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) (humans) or [AGENTS.md](AGENTS.md)
(AI agents) — both state the file-layout rules, the exact MathJax head, the
question/box markup, the numbering rules, and the verify commands. Follow
[templates/CHECKLIST.md](templates/CHECKLIST.md) when adding a module.
