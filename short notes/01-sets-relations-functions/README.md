# Short Notes — Chapter 1: Sets, Relations and Functions

Handwritten-style, dense **teacher-style explanatory sheets** (not a formula
dump) for the first chapter of the complete JEE Advanced Mathematics syllabus,
with a separate Olympiad/extension part. Rendered as exact-A4 PNG sheets
(2480×3508 px, 300 DPI) plus bookmarked A4 PDFs and ZIP archives.

- **Part I — JEE Main + Advanced** (`JEE/`, 12 sheets): core theory, derivable
  applications, standard JEE models, common traps — concepts classified by
  relevance and prerequisites, with symbols, domains, ranges and conventions
  defined where they first appear.
- **Part II — Olympiad / extensions** (`Olympiad/`, 6 sheets): IOQM/RMO-style
  additional theory (counting catalogue, functional equations, floor toolkit,
  fixed points). Extra theory is labelled as such; every model shown is solved
  with tools a diligent student can derive from Part I — nothing here is
  declared "impossible in JEE".

## Downloads

| Artifact | File |
|---|---|
| **Combined PNG ZIP (JEE first)** | [`exports/01-sets-relations-functions-combined-sheets.zip`](exports/01-sets-relations-functions-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/01-sets-relations-functions-JEE-sheets.zip`](exports/01-sets-relations-functions-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/01-sets-relations-functions-Olympiad-sheets.zip`](exports/01-sets-relations-functions-Olympiad-sheets.zip) |
| **Combined PDF (bookmarked, JEE first)** | [`exports/01-sets-relations-functions-combined.pdf`](exports/01-sets-relations-functions-combined.pdf) |
| JEE PDF (bookmarked) | [`exports/01-sets-relations-functions-JEE.pdf`](exports/01-sets-relations-functions-JEE.pdf) |
| Olympiad extensions PDF (bookmarked) | [`exports/01-sets-relations-functions-Olympiad-extensions.pdf`](exports/01-sets-relations-functions-Olympiad-extensions.pdf) |
| **Gallery** | [`index.html`](index.html) |
| Scope & full JEE Advanced chapter list | [`SCOPE.md`](SCOPE.md) |
| Source audit, corrections, open assumptions | [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) |
| Printing instructions | [`PRINTING.txt`](PRINTING.txt) |

## What is on the sheets

Part I (JEE) — 12 sheets, independently numbered `JEE/01.png … JEE/12.png`:

1. Sets — language, representation (roster/set-builder/interval), the
   $\varnothing$ vs $\{0\}$ vs $\{\varnothing\}$ family of traps
2. Subsets, power set, $2^{n}$ count (derived), worked boundary example
3. Operations — union, intersection, difference, complement, $\Delta$; De
   Morgan (element-chasing derivation); Venn language
4. Algebraic laws + inclusion–exclusion for 2 and 3 sets (derived); Venn-3
   diagram; cricket/neither model
5. Cartesian products (ordered pairs, $n(A\times B)$, distributive facts),
   relations, domain/range/codomain; mapping diagram; relation counting
6. Reflexive/symmetric/transitive with counterexamples; how many relations
   (derived); worked six-pair check
7. Equivalence relations (congruence mod $n$ proved), partitions, Bell
   numbers with listings; equivalence-class diagram
8. The JEE counting models (reflexive & symmetric $=2^{n(n-1)/2}$ derived);
   traps (empty relation, partial symmetry)
9. Functions as special relations; domain rule stack; image/preimage;
   worked domain with endpoint tests
10. Range techniques (square, monotone pieces, discriminant solve); worked
    $[0,1)$ range; $f(A\cap B)$ pitfalls
11. Special functions $|x|$, $\operatorname{sgn}$, $[x]$, $\{x\}$ with
    graphs (jump conventions); transformations; $|x^2-3x+2|$ cusp graph
12. One-one/onto tests; counts $|B|^{|A|}$, injections, small-case onto;
    even/odd split (derived); periods; composition/inverse; chapter recap

Part II (Olympiad) — 6 sheets, independently numbered `Olympiad/01.png …
Olympiad/06.png`:

1. The full relation/function counting catalogue incl. antisymmetric and
   surjections by inclusion–exclusion (derived, cross-checked by Stirling)
2. Bell numbers by listing; trap sheet; conventions
3. Cauchy's equation — rational linearity derived, regularity upgrades,
   worked models
4. Multiplicative cousins, Pexider, Jensen; involution $f\circ f=\mathrm{id}$;
   increasing-involution proof; decreasing case
5. Hermite's identity with proof; floor identities; $\lfloor x^2\rfloor = 2$
   model (with integer-quantifier variant)
6. Fixed points vs 2-cycles; worked involutions; trap sheet; assumptions

## Editable content

Everything on the sheets is authored in [`content/*.md`](content/) — a small
Markdown dialect (frontmatter + `##` sections + `$math$` + `:::key|warn|
intuition|derive|example|app|assume` boxes + `:::diagram {json}` figures).
Edit the Markdown, re-run the scripts below, and the set re-paginates itself:
**prose is never shrunk to fit a page — the set expands instead.**

## Reproducible build & checks

```bash
pip install -r ../_engine/requirements.txt   # once (Python 3.11+)
python3 scripts/render.py      # content/*.md -> JEE/*.png + Olympiad/*.png + manifest.json
python3 scripts/export.py      # 3 ZIPs + 3 bookmarked A4 PDFs + index.html
python3 scripts/check.py       # delivery checks (dimensions, DPI, margins, glyphs,
                               # math parsing, ZIP/PDF integrity & order, links, docs)
python3 scripts/math_checks.py # 67 brute-force mathematical checks (pure stdlib)
```

`math_checks.py` enumerates the counting formulas on $n \le 5$ sets, checks
De Morgan / inclusion–exclusion on generated set triples, validates the floor
identities and Hermite's identity on grids, and replays every worked example
with its boundary cases. This is **not** exhaustive mathematical verification
of the notes — see `SOURCE-AUDIT.md` for exactly what was checked.

## Sheet format

2480×3508 px (A4 portrait, 210×297 mm at nominal 300 DPI), 10 mm safe
margins, faint ruled paper, two text columns. Navy prose (Kalam), teal
headings/explanations, yellow key results, red common traps; mathematics set
in a proper math font (matplotlib mathtext); diagrams drawn programmatically
(vector construction, rasterised at 300 DPI) with labelled axes, asymptotes,
intercepts and region names. Every sheet carries visible part + page labels
(`PART I — JEE MAIN + ADVANCED · SHEET k / n`, footer `JEE-0k` / `OLY-0k`).

## Fonts

Body/heading handwriting: **Kalam** (OFL, via Fontsource; TTFs in
[`../_assets/fonts/`](../_assets/fonts/)) with **DejaVu Sans** glyph fallback
for symbols Kalam lacks ($\varnothing$, arrows). Math: matplotlib mathtext
(DejaVu/CM glyphs). Both fonts are libre; keep the OFL attribution when
redistributing.
