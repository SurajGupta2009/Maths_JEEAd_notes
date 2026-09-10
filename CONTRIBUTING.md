# Contributing

This repo is hand-crafted HTML notes (JEE Advanced → Olympiad). Two modules —
`PnC/` and `Complex Numbers/` — are **golden references**: when in doubt, copy
what they do. Everything here exists to keep new files consistent with them.

## File layout rules

- **One chapter = one single large HTML file**, named `NN-slug.html`
  (`03-combinations.html`). **Never** bifurcate a chapter into multiple files.
- A module folder holds exactly: `index.html`, chapters `01-…`…`06-…`,
  `olympiad-paper.html`, `olympiad-paper-solutions.html`,
  the generated `*-mindmap.html`, and `assets/notes.css`.
- `assets/notes.css` is a per-module copy (no cross-folder links; folders must
  open standalone from disk).
- Mind maps are **generated** by `tools/build-mindmap.py` — never hand-written.

## Naming

- New module folders are kebab-case-ish slugs: `Quadratic-Equations/`,
  `Sequences-and-Series/`. The existing `Complex Numbers/` folder keeps its
  space — do not rename it.
- Mind-map file = the folder name lowercased with spaces/hyphens normalized to
  single hyphens plus `-mindmap.html` (`Quadratic-Equations/` →
  `quadratic-equations-mindmap.html`); the builder creates/reuses exactly that
  name (existing modules keep their current file names, e.g. `cn-mindmap.html`).
- Chapter files: `NN-short-kebab-title.html`, `NN` = chapter number.

## Math rendering (exact head)

Every page carries this `<head>` (only `<title>` varies):

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PAGE TITLE — {{MODULE}} Notes</title>
<link rel="stylesheet" href="assets/notes.css">
<script>
window.MathJax = {
  tex: { inlineMath: [['\\(', '\\)']], displayMath: [['$$', '$$'], ['\\[', '\\]']] },
  svg: { fontCache: 'global' }
};
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
```

Real math only: inline `\( … \)`, display `\[ … \]` or `$$ … $$`. **Never**
fake math with Unicode glyphs (`x²`, `√`, `≤`) — MathJax or nothing.

## Page skeleton

```html
<body>
<nav class="topnav">
  <div class="inner">
    <span class="brand">{{MODULE}} · Notes</span>
    <a href="index.html">Home</a><span class="sep">|</span>
    <a href="01-first-chapter.html">1 · First</a>
    <a href="02-second-chapter.html">2 · Second</a>
    <!-- … one link per chapter … -->
    <span style="color:var(--teal);font-weight:700;">3 · Current</span><!-- current page = span, highlighted -->
    <a href="olympiad-paper.html" style="color:var(--violet);font-weight:700;">Olympiad Paper</a>
    <a href="olympiad-paper-solutions.html" style="color:var(--violet);">Solutions</a>
  </div>
</nav>
<div class="page">
  <header class="ch-head">
    <div class="ch-kicker">Chapter 3 of 6</div>
    <h1>Chapter Title</h1>
    <p class="ch-sub">Two to four sentences of motivation.</p>
  </header>

  <!-- content lives in <div class="card"> blocks -->

  <div class="foot">
    <span>{{MODULE}} · Chapter 3</span>
    <span><a href="index.html">← Home</a> · <a href="04-next-chapter.html">Next →</a></span>
  </div>
</div>
</body>
```

## Theory card

```html
<div class="card">
  <h2><span class="no">3.1</span> Section Title</h2>
  <p>Prose. Inline math: \( n! = 1\cdot 2 \cdots n \).</p>
  <div class="formula"><span class="label">label</span>
    \[ \binom{n}{k} = \frac{n!}{k!\,(n-k)!} \]</div>
  <h3>Optional sub-heading</h3>
  <p>More prose…</p>
</div>
```

## Callout box

`div.box` + one modifier class, always with a `.box-title` line:

```html
<div class="box box-first">
  <div class="box-title">⛁ First Principles — why it is true</div>
  <p>The actual reasoning.</p>
</div>
```

Modifiers: `box-first` (teal, first principles) · `box-idea` (green, key idea) ·
`box-note` (slate, note/practice-set header) · `box-warn` (amber, common trap) ·
`box-check` (verification habit) · `box-bridge` (link to next chapter) ·
`box-identity` (named identity) · `box-olymp` (violet, olympiad extension).

## Practice question (inside a theory card, between sections)

```html
<div class="q">
  <div class="q-head"><span class="q-id">P23</span><span class="badge b-adv">JEE Adv</span><span class="badge b-pract">practice</span><span class="badge b-concept">stars &amp; bars</span></div>
  <p>The problem statement, with \( \mathrm{math} \) as usual.</p>
  <details class="ans"><summary>Answer + reasoning</summary><div class="ans-body">
    <p><strong>Method: bijection to bit-strings.</strong> Worked derivation…</p>
    <p>Answer: <strong>24</strong>. (Small-case check: \(n=3\) lists 6 ✓.)</p>
  </div></details>
</div>
```

Difficulty badges: `b-main` (JEE Main) · `b-adv` (JEE Advanced) · `b-olymp`
(Olympiad — the styled class in `notes.css`; older CN files use `b-oly`, prefer
`b-olymp`). Tags: `b-pract`, `b-concept`, `b-solved`. Worked examples are
`div.q.solved` with `q-id` `S#` and a `div.solution` + `sol-title` instead of
`details.ans`. **Solutions state the method first, then the derivation, then a
check.**

## Paper question (olympiad-paper.html)

```html
<div class="card">
  <h2>A · Arrangements (Q1–Q8)</h2>
  <div class="q">
    <div class="q-head"><span class="q-id">Q1</span><span class="badge b-main">JEE Main</span></div>
    <p>Find the principal argument of \(1 - i\sqrt3\).</p>
    <p class="answer-pill">Answer: \(-\dfrac{\pi}{3}\)</p>
  </div>
  <!-- more questions… -->
</div>
```

The paper file ends with a `box-warn` "📝 Exam technique notes" card.

## Numbering rules

- **Practice P1…Pn**: numbered continuously per module, unique across the whole
  module, woven between theory sections (not dumped at the end of a chapter).
- **Worked examples S1…Sn**: continuous per module like P.
- **Paper Q1…Qn**: continuous across the paper, grouped into lettered sections
  A–H, difficulty ramping Main → Advanced → Olympiad. Aim 38–40 questions
  (minimum 30). The solutions file reuses the same Q-ids verbatim.

## Verify before you commit

```bash
python3 tools/verify-math.py PnC/*.html "Complex Numbers/"*.html templates/*.html
python3 tools/verify-mindmap.py all          # after any mind-map rebuild
python3 tools/build-mindmap.py all           # mind maps must regenerate unchanged
```

Every paper answer must be verified **numerically in pure Python** (stdlib
only) before the solutions file is written — keep the throwaway script out of
the repo, keep its verdict in the PR description.

## Hard rules

1. One chapter = one HTML file; never split.
2. Real MathJax delimiters only (`\(…\)`, `\[…\]`, `$$…$$`); never Unicode math.
3. No new dependencies: pure stdlib Python, no build system, no images unless
   the maintainer asks.
4. Do not alter existing note files in `PnC/` or `Complex Numbers/`; the only
   permitted change there is tooling moves, and only with byte-identical mind
   maps and PASS verification afterwards.
5. `tools/verify-math.py` must report PASS for every HTML file — CI enforces it.
6. Mind maps: generate, never hand-edit.

Adding a whole module? Follow [templates/CHECKLIST.md](templates/CHECKLIST.md)
end to end, then open a PR — do not push to `main`.
