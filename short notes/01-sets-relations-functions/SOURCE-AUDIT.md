# SOURCE-AUDIT — Chapter 1: Sets, Relations and Functions

## Sources reviewed

1. **Primary source — repository notes** (`notes/` vault): the vault contains
   18 modules, each with six chapters + paper + solutions. **There is no
   "Sets, Relations and Functions" module and no standalone sets/relations/
   functions chapter anywhere in the vault** — closest neighbours are
   `notes/PnC/` (counting, sets-as-language only incidentally) and
   `notes/Inequalities/`. **Gap disclosed:** for this chapter the repo source
   material is *unavailable*, so the sheets were authored from the official
   syllabus text (below) and standard theory; the vault's *format and pedagogy
   standard* (first-principles derivations, small-case checks, common-trap
   callouts) was followed, but no vault content was copied because none exists
   for this chapter. No vault file was modified or deleted.
2. **Official syllabus** — JEE (Advanced) 2026 Syllabus, MATHEMATICS unit
   "Sets, Relations and Functions", retrieved from
   `jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf` on 2026-10-22. All
   bullets are mapped to sheets in `SCOPE.md`. The same PDF is the authority
   for the 22-chapter master list.
3. **Independent authoring** — theory, derivations and worked examples were
   written from first principles and re-derived during review (see below).

## Independent checks performed (and their limits)

- **Derivations re-derived line by line**: $|\mathcal{P}(A)| = 2^n$ (product
  rule + binary strings); De Morgan (element chase, and $n$-set form);
  inclusion–exclusion for 2 and 3 sets (disjoint-region partition);
  $n(A \times B) = n(A)n(B)$; relation counts $2^{n^2}, 2^{n^2-n},
  2^{n(n+1)/2}, 2^{n}3^{n(n-1)/2}, 2^{n(n-1)/2}$; functions $|B|^{|A|}$;
  injections $P(|B|,|A|)$; surjections by inclusion–exclusion
  $\sum_i (-1)^i \binom{m}{i}(m-i)^n$; even/odd split; $(g \circ f)^{-1} =
  f^{-1} \circ g^{-1}$; rational linearity of Cauchy; Hermite's identity
  (full proof on the sheet); "increasing involution is the identity".
- **Brute-force numerical checks** (`scripts/math_checks.py`, pure stdlib):
  67 checks, all passing — relation-type counts enumerated for $n = 1,2,3$
  ($2^{9} = 512$ relations for $n = 3$), Bell numbers $B_3 = 5$, $B_4 = 15$,
  $B_5 = 52$ by partition enumeration, function/injection/surjection counts
  for six $(n,m)$ pairs against closed forms and IE, De Morgan +
  inclusion–exclusion + difference/symmetric-difference identities on
  generated set triples, floor sandwich/sum bounds on a $800 \times 41$ grid,
  Hermite's identity for $n = 1..8$ on two grids (including integer and
  half-integer boundary points), and every worked example replayed with its
  boundary cases (domain endpoints $x = 1, 3, 5$; range $[0,1)$; $|x-1| +
  |x-3| = 4$; $\lfloor x^2 \rfloor = 2$ solution set incl. endpoints;
  $f(f^{-1}(3)) = 3$, $f^{-1}(f(2)) = 2$; involution grids).
- **Boundary/example review**: open/closed brackets tested at every endpoint
  in the domain/range worked examples; $\varnothing$ vs $\{0\}$ vs
  $\{\varnothing\}$ enumerated; $n = 0$ conventions flagged where IE is used.
- **Not done / limits**: this is *not* exhaustive mathematical verification.
  Prose claims without finite checkable content (e.g. "Hamel-basis solutions
  of Cauchy exist", "Pexider solutions are affine") are stated as standard
  theory with hypotheses spelled out; they were not formally re-proven here.
  Diagrams were reviewed visually at full resolution; they are schematic
  (not to scale unless labelled).

## Corrections made during authoring (do not reproduce the earlier drafts)

1. The first draft of the Cartesian-product worked example contained a
   self-contradictory pair-checking narrative; replaced by the $y - x \ge 3$
   example with all six pairs checked (boundary $y - x = 3$ included).
2. A draft trap bullet claimed "periodic + additive forces $f \equiv 0$"
   unconditionally — **false without regularity** (wild additive $T$-periodic
   solutions exist on a Hamel basis). Corrected on `olympiad-02` to state the
   continuity hypothesis explicitly.
3. The $\lfloor x^2 \rfloor = 2$ model draft contained an in-line correction
   stutter; rewritten with the final solution set
   $[-\sqrt3, -\sqrt2] \cup [\sqrt2, \sqrt3)$ and the integer-quantifier
   variant (no integer solutions).
4. The inclusion–exclusion $0^0$ warning was reworded: the correct statement
   is the empty-domain convention $m^{0} = 1$ (including $0^{0} = 1$ in this
   counting context), not "$0^n$ with $n = 0$".
5. Engine-level rendering fixes found in review (affect presentation, not
   mathematics): inline-math spacing at run boundaries, bold spans swallowing
   `$…$` (earlier prints showed raw `$\mathbb{R}$`), mathtext macro set
   (`\iff`, `\le`→`\leq`, `\pmod`→`\ (\mathrm{mod}\ n)`, `\underbrace`
   avoided), display-math auto-fit for the 3-set formula.

## Unresolved assumptions & conventions (open to revision)

1. **"…etc." in the official special-functions list** is open-ended. We read
   it as including $\operatorname{sgn} x$ and the fractional part $\{x\}$;
   a stricter reading could exclude $\operatorname{sgn}$. Neither the
   derivatives nor the models depend on that choice.
2. **$\subset$ notation**: we use $\subset$ = *proper* subset, $\subseteq$ =
   subset (possibly equal). Some textbooks use $\subset$ loosely for
   $\subseteq$; the sheets state the convention explicitly but a student's
   exam paper may mix conventions.
3. **"Into"** is read as "not onto" (modern usage). The legacy "every
   function is into some codomain" phrasing is flagged in-line; exam wording
   decides the reading.
4. **Bell numbers / Stirling numbers** (Part II) are named vocabulary beyond
   the official list; counts themselves are derivable and were brute-force
   checked. If a future official syllabus change drops "equivalence relation"
   counts from papers, Part II still stands as extension material.
5. **Congruence classes** are presented on $\mathbb{Z}$; the sheet notes class
   labels are cosmetic. No unresolved issue.
6. The vault's own extended modules (e.g. `notes/PnC`, `notes/Inequalities`)
   contain deeper olympiad machinery that *could* be woven into Part II of
   later chapters (e.g. chapters 6–9); for Chapter 1 the vault supplied
   nothing, as stated above.

## Vault integrity

No file under `notes/`, `docs/`, `templates/`, `tools/` or `.obsidian/` was
created, edited, renamed or deleted for this chapter. All new artefacts live
under `short notes/`. Repo verifiers (`python3 tools/verify-md.py`,
`python3 tools/verify-structure.py`) were run after authoring: **STRUCTURE
PASS** (18 modules unchanged) and verify-md **PASS** on all notes — it also
accepts the new `short notes/**/content/*.md` files (frontmatter + balanced
math), so the vault gates remain green.
