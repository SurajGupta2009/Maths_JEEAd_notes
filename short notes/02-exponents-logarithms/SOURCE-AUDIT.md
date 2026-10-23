# SOURCE-AUDIT — Chapter 2: Exponents & Logarithms

## Sources reviewed

- **Vault (`notes/`): no dedicated Exponents/Logarithms module exists.** A repo-wide search for logarithm material found only *incidental uses* (inside `Complex-Numbers`, `Sequences-and-Series`, `Differentiation-and-Methods`, `Integration`, `Limits-and-Continuity` worked solutions) — no exponents/logarithms theory chapter to draw from. Like chapter 1 (Sets), this chapter's content was therefore **authored fresh** against the official syllabus sentence, and the gap is disclosed here rather than papered over.
- **Official JEE Advanced 2026 Mathematics syllabus (jeeadv.ac.in PDF, fetched and reviewed earlier in this build):** Algebra lists **"Logarithms and their properties"**; no separate "exponents" entry. Classification decisions below follow that sentence.
- Chapter 1 of this short-notes series (`01-sets-relations-functions`) supplied the conventions register (notably the $0^{0}$ convention) kept consistent here.

## Coverage gap (disclosed)

The vault cannot supply prose for this chapter. What is written in `content/` is original exposition, checked against the standing requirement of the syllabus sentence and by the independent numeric checks in `scripts/math_checks.py` (163/163 PASS). Readers who want the vault's multi-module treatment of logarithms *in context* should see the uses inside `Complex-Numbers` and `Sequences-and-Series` (series bounds) — those are applications of this chapter's toolkit, not a source for it.

## Corrections and authoring decisions (not source-error reproductions — there is no source)

1. **$(a^{r})^{s} = a^{rs}$ on negative bases** is stated with its hypothesis ($a>0$, or integer exponents) and the counterexample $\left((-2)^{2}\right)^{1/2} \ne (-2)^{2 \cdot 1/2}$ — many popular treatments state the law bare; here the hypothesis is part of the formula.
2. **$x^{2/3} = 8$ solved as $x = \pm 16\sqrt{2}$** with the lowest-terms parity rule ($q$ odd after reduction) stated first; both roots verified in the independent checks.
3. **$100^{n}$ vs $n^{100}$ crossover**: a first draft said "$100^{n}$ wins for $n \geq 100$"; the independent numeric check caught that at $n = 100$ the two are **equal** (and $n^{100}$ is larger for $e < n < 100$). The sheet now states the precise crossover (where $\frac{\ln n}{n} = \frac{\ln 100}{100}$).
4. **Ghost-root hygiene in worked examples**: $\log_{2}(x-3)+\log_{2}(x+1)=3$ is solved with the domain $x>3$ fixed first and the algebra-generated root $1-2\sqrt{3}$ explicitly rejected; $x^{\lg x}=10^{4}$ is shown to have **two** valid roots.
5. **Notation fixed for the whole set**: $\lg = \log_{10}$, $\ln = \log_{e}$, "$\log$" without base = statement for every legal base; $\log$ arguments positive, bases $>0$ and $\ne 1$ stated once in an ASSUMPTIONS box and enforced throughout.

## Unresolved assumptions (logged)

- **Base convention**: $a^{x}$ is real-valued for $a>0$; negative bases only through integer exponents or odd roots (rational exponents reduced to lowest terms first). Stated on sheet 01.
- **$0^{0} = 1$** kept as the empty-product convention, consistent with chapter 1's logged convention.
- **Shape of $f(t) = \frac{\ln t}{t}$** (increasing to $t=e$, then decreasing) is quoted as the known shape of the standard curve; its calculus proof is deferred (noted as a forward reference). The $x^{y}=y^{x}$ classification and $a^{b}$ vs $b^{a}$ comparisons rely on this shape — flagged on the sheets.
- **Harmonic estimates** $\ln(n+1) \leq H_{n} \leq 1 + \ln n$ and $\frac{1}{k+1} \leq \ln(1+\frac{1}{k}) \leq \frac{1}{k}$ are quoted as standard derived models (checked numerically for $n=100$ on the sheet).
- **Discontinuous solutions of $f(x+y)=f(x)f(y)$** exist (Hamel-basis style constructions) but are excluded as exam material; the sheet says the exponential law plus continuity pins down $a^{x}$ and flags the caveat.
- **Growth models** ($N_0 a^{t}$, $N_0 e^{kt}$) are treated as applied *models built from the supplied function $a^{x}$*, not as additional theory.

## Verification record

- `scripts/math_checks.py` — 163/163 numeric checks PASS (laws, parity, every worked example re-substituted, log identities at random bases, digit counts, comparisons, parametrisation, Legendre, harmonic bounds).
- `scripts/check.py` — deliverable/render checks PASS (formula parsing, fonts, margins, ZIP/PDF integrity, gallery links).
- Visual: all 24 sheets reviewed at contact-sheet resolution; both diagrams (exponential family, log curves) inspected at full resolution and label positions corrected.
- No claim of exhaustive mathematical verification beyond the above is made.
