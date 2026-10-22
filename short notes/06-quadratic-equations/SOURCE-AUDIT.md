# Source Audit — Chapter 6: Quadratic Equations

## Sources

- `notes/Quadratic-Equations/Quadratic-Equations.md` — the repository's own
  module (834 lines, 6 chapters + appendix). **Read in full before
  authoring.** The accompanying Paper/Solutions files are practice sets;
  the main markdown is the complete theory source used.
- Official JEE Advanced 2026 syllabus (jeeadv.ac.in PDF), Algebra unit —
  used to set the Part I / Part II boundary.
- Supplementation: the source module treats root location only through one
  practice problem (both roots $> 1$). The full location-of-roots toolkit
  (sheet 04) and the discriminant range method (sheet 07) are standard JEE
  Advanced material authored for these sheets and verified independently;
  this supplementation is disclosed here rather than silently implied to
  come from the source.

## Independent verification performed

`scripts/math_checks.py`: **281/281 assertions pass**, covering the
discriminant cases (including conjugate roots of $2x^{2}-3x+5$); the whole
Vieta toolkit on four quadratics; squared/shifted/reciprocal transformed
equations; vertex and sign facts; the location claims by brute force over
parameter grids (both roots $>1$ iff $k>2$; exactly one root of
$x^{2}-3x+k$ in $(0,2)$ iff $0<k\leq 2$); opposite-sign criterion;
all reducible-equation solution sets including extraneous-root rejection;
common-root examples; the range $\left[\frac17, 7\right]$ of
$\frac{x^{2}-3x+4}{x^{2}+3x+4}$ by dense sampling with endpoints attained
at $x=-2$ ($y=7$) and $x=2$ ($y=\frac17$); Newton's recurrence against
direct root powers for $n \le 8$; Fibonacci/Lucas/Binet identities;
rational-root perfect-square criterion for $k \in [-10, 10]$;
IMO 1988/6 by brute force over $1 \le a, b < 300$ and the $k=9$ chain.

## Corrections (source or draft defects not reproduced)

- **Root-location endpoint case (found by our own checks on these
  sheets):** for $x^{2}-3x+k$ with exactly one root in $(0,2)$, the
  endpoint $k=2$ gives roots $1, 2$ — one root inside — so the correct
  answer is $0 < k \leq 2$, not $0 < k < 2$. Mechanical exclusion of both
  endpoints is wrong; each endpoint must be checked with its *other* root.
- **IMO 1988/6 brute-force range (source claim narrowed):** the source
  states admissible quotients for $a,b<300$ are only $\{1,4,9,16,25\}$.
  Our brute force also finds $36$ (e.g. $(a,b)=(6,216)$:
  $\frac{36+46656}{1297}=36$). The sheets state only the correct claim:
  every admissible quotient is a perfect square.
- The source's common-root condition is printed in two different pairings
  in different places ($(bc'-b'c)^{2}=(ab'-a'b)(ac'-a'c)$ in §5.1 vs
  $(ca'-c'a)^{2}=(ab'-a'b)(bc'-b'c)$ in the appendix). The sheets avoid
  the trap by teaching subtraction/elimination as the primary method and
  flagging the memorised condition as error-prone.

## Assumptions and conventions

- Real coefficients unless stated; roots counted with multiplicity;
  repeated root still counts twice in Vieta.
- Location-of-roots conditions assume real roots; the $D \geq 0$
  ingredient is omitted only where $a f(k) < 0$ forces it.
- Lagrange resolvent cube roots must satisfy $uv = -P/3$; stated
  explicitly wherever the method is used.
