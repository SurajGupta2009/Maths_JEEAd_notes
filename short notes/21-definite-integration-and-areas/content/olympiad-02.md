---
id: olympiad-02
part: olympiad
title: "Beta and Gamma Functions, Reflection and Duplication"
---

## Two convergent parameter integrals and their bridge

For $z>0$, the Gamma function is
$$
\Gamma(z)=\int_0^\infty t^{z-1}e^{-t}dt,
\qquad \Gamma(z+1)=z\Gamma(z),
$$
with $\Gamma(1)=1$ and $\Gamma(n+1)=n!$. For $p,q>0$,
$$
B(p,q)=\int_0^1t^{p-1}(1-t)^{q-1}dt
=\frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}.
$$
The product identity follows from a double integral and a factorising change of variables. The substitution $t=\sin^2\theta$ gives
$$
B(p,q)=2\int_0^{\pi/2}\sin^{2p-1}\theta\cos^{2q-1}\theta\,d\theta.
$$

:::example title="S18 and Q39: the base Beta value"
$$
B\left(\frac{1}{2},\frac{1}{2}\right)
=2\int_0^{\pi/2}1\,d\theta=\pi
=\frac{\Gamma(1/2)^2}{\Gamma(1)}.
$$
Since $\Gamma(1/2)>0$, this also gives $\Gamma(1/2)=\sqrt{\pi}$.
:::

## The same Beta formula evaluates Q40 and S19/Q43

For $p>-1$, putting $q=1/2$ in the trigonometric Beta form gives
$$
\int_0^{\pi/2}\sin^p x\,dx
=\frac{1}{2} B\left(\frac{p+1}{2},\frac{1}{2}\right)
=\frac{\sqrt{\pi}}{2}\frac{\Gamma((p+1)/2)}{\Gamma((p+2)/2)}.
$$

For Q40, first use $\sin x\cos x=\sin(2x)/2$. With $u=2x$ and sine symmetry on $[0,\pi]$,
$$
A=\frac{1}{\sqrt{2}}\int_0^{\pi/2}\sqrt{\sin(2x)}dx
=\frac{1}{2\sqrt{2}}\int_0^\pi\sqrt{\sin u}\,du
=\frac{1}{\sqrt{2}}\int_0^{\pi/2}\sqrt{\sin u}\,du.
$$
Now put $p=1/2$ in the Beta formula:
$$
A=\frac{1}{\sqrt{2}}\frac{\sqrt{\pi}}{2}
\frac{\Gamma(3/4)}{\Gamma(5/4)}
\approx0.8472130848.
$$

For S19/Q43, put $p=6$:
$$
\int_0^{\pi/2}\sin^6x\,dx
=\frac{\sqrt{\pi}}{2}\frac{\Gamma(7/2)}{\Gamma(4)}
=\frac{5\pi}{32},
$$
using $\Gamma(7/2)=15\sqrt{\pi}/8$ and $\Gamma(4)=6$.

## Q42 and Q44: reflection and duplication

For $0<z<1$ in the real-integral setting, Euler's reflection formula is
$$
\Gamma(z)\Gamma(1-z)=\frac{\pi}{\sin(\pi z)}.
$$
Analytic continuation extends it to nonintegral complex values and explains Gamma's poles at the nonpositive integers.

Legendre's duplication formula, for $z>0$, is
$$
\Gamma(z)\Gamma\left(z+\frac{1}{2}\right)
=2^{1-2z}\sqrt{\pi}\,\Gamma(2z).
$$
At $z=1/2$, it reduces to $\Gamma(1/2)=\sqrt{\pi}$, not $\pi=2\sqrt{\pi}$; the source's substitution at that point is corrected. For P18/Q41, $z=1/4$ gives
$$
\Gamma\left(\frac{1}{4}\right)\Gamma\left(\frac{3}{4}\right)
=2^{1/2}\sqrt{\pi}\,\Gamma\left(\frac{1}{2}\right)
=\sqrt{2}\pi,
$$
in agreement with Q42's reflection formula.

:::diagram
{
  "type": "table",
  "title": "Parameter identities must be checked at the substituted value",
  "columns": ["Source item", "Parameter choice", "Conclusion"],
  "rows": [
    ["S18 / Q39", "p=q=1/2", "B=pi and Gamma(1/2)=sqrt(pi)"],
    ["Q40", "p=1/2 after u=2x", "0.8472130848 approximately"],
    ["S19 / Q43", "p=6", "5 pi/32"],
    ["Q42 / Q44", "reflection and duplication", "identities with stated domains"],
    ["P18 / Q41", "z=1/4", "product=sqrt(2) pi"]
  ],
  "col_widths": [0.24, 0.36, 0.40],
  "caption": "The z=1/2 duplication step is only a consistency check. The z=1/4 evaluation is the nontrivial product and agrees with reflection."
}
:::

:::warn title="Parameter restrictions are convergence restrictions"
The stated real-integral definitions require $z>0$ and $p,q>0$. Analytic continuation extends Gamma to other complex values, but it does not make the original real integral converge there.
:::
