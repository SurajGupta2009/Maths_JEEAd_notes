# SCOPE — Chapter 2: Exponents & Logarithms

## Syllabus reading (official JEE Advanced 2026 Mathematics)

- **Algebra** lists **"Logarithms and their properties"**. The syllabus does not spell out "exponents/indices"; the laws of indices, rational exponents and the exponential function are the machinery the logarithm presupposes, so they are treated in Part I as foundation (this is a coverage judgment, recorded in SOURCE-AUDIT.md).
- Nothing in this chapter claims any model "can never appear in JEE". Part II items are labelled as **beyond the current syllabus sentence** or as **specialised/olympiad-standard models that remain derivable from Part I information**.

## Classification rule used

- **Part I (JEE)** — core definitions/laws/monotonicity + every exam model derivable from them: solving equations/inequalities, comparisons, digits/orders of magnitude, growth models $N_0 a^{t}$.
- **Part II (extensions)** — models standard in IOQM/RMO/algebra olympiads or built on extra analysis shapes: $x^{y} = y^{x}$ classification, multi-base systems, tower conventions, growth hierarchy, Legendre's formula, series estimates.

## Sheet → concept map

### Part I — `JEE/` (9 sheets)

| Sheet | Concepts |
|---|---|
| 01 | $a^{x}$ meaning and extension ladder ($a^{0}$, $a^{-p}$, $a^{p/q}$); base convention $a>0$; parity rules for negative bases; laws of indices with hypotheses; $(a^{r})^{s}$ and $(ab)^{r}$ traps; $\sqrt{x^{2}}=\lvert x\rvert$; injectivity $a^{f}=a^{g} \Leftrightarrow f=g$ |
| 02 | Exponential function: domain/range, $f(x+y)=f(x)f(y)$, monotonicity $a>1$ vs $0<a<1$ (with algebraic proof), graphs + asymptote $y=0$; $e$ and $e^{x}$; substitution method ($t=a^{x}>0$); compatibility $2^{x}=c$ solvable iff $c>0$ |
| 03 | Logarithm definition $\log_{a} y = x \Leftrightarrow a^{x}=y$; domain discipline; three laws derived from index laws; change of base, reciprocity, chain rule; inverse pairs; log curves, reflection in $y=x$; sign rule $(x-1)(a-1)>0$; monotonicity flip for bases $<1$ |
| 04 | Simplification patterns (nested logs, mixed bases, fraction sums); digit formula $\lfloor \lg N \rfloor + 1$ derived; comparison moves (take $\ln$; $\frac{\ln t}{t}$ for $a^{b}$ vs $b^{a}$; integer bridges); $e^{\pi}>\pi^{e}$ worked; sign grid; $\log\lvert x\rvert$ vs $\lvert \log x\rvert$ |
| 05 | Equation types 1–4 (common base, quadratic in $a^{x}$, collapse-logs, $x^{\log x}$); domain-first discipline; worked examples with ghost-root filtering; number-line diagram of surviving roots |
| 06 | Inequality protocol (domain, monotone reading, base flip, case splits); parametric sign analysis; digits/order-of-magnitude models; growth models ($N_0 a^{t}$, $N_0 e^{kt}$, doubling time); growth-class ordering; canonical parameter solve $a^{x}=b^{x+c}$ |
| 07–09 | Chapter recap toolkit; five questions; conventions; where the toolkit reappears; final trap sweep |

### Part II — `Olympiad/` (3 sheets, extensions)

| Sheet | Concepts | Status |
|---|---|---|
| 01 | $x^{y}=y^{x}$: reduction to $\frac{\ln x}{x}$, parametrisation $x=t^{1/(t-1)}$, integer pair $(2,4)$; multi-base log systems (reciprocity/chain); tower convention $a^{b^{c}}=a^{(b^{c})}$ | IOQM/RMO-standard; derived from Part I |
| 02 | Growth hierarchy (log $\ll$ power $\ll$ exponential) as ordering; digit engine and base-$p$ digit sums; Legendre's formula $v_{p}(n!)=\frac{n-s_{p}(n)}{p-1}$ with derivation and worked $100!$ | olympiad number theory; floors + geometric counts |
| 03 | Harmonic/log series estimates, truncation bounds $H_n \approx \ln n$ | standard derived models; forward reference to series chapter |

## Prerequisites assumed

Rational/integer exponents (school level); real functions, graphs and monotonicity in elementary form; floor function notation (chapter 1 toolkit). Calculus is referenced only as a forward note (slope of $e^{x}$ at $0$; concavity shapes) and is never required to complete a model on the sheets.

## Out of scope here

Composition/inverse functions (chapter 1 supplies the algebra; inverse *trigonometric* functions are chapter 4); series summation machinery (chapter 7, referenced as forward notes); binomial/P&C counting (chapters 8–9).
