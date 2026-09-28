---
title: "Vectors — Olympiad Paper"
aliases: ["Vectors Paper", "Vector Algebra Paper"]
module: "Vectors"
module_title: "Vectors"
type: paper
tags: [vectors, paper, olympiad, geometry, linear-algebra]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Vectors|Chapter 6]] · 📖 [[Vectors|Complete Notes]] · ✅ [[Vectors — Solutions|Solutions]] ➡

# Vectors — Olympiad Paper

> **34 questions · Sections A–H · difficulty ramps JEE Main → JEE Advanced → Olympiad.**
> Attempt the whole paper before opening the [[Vectors — Solutions|solutions]].
> Every numeric answer was verified in pure Python before this file was written.

---

## A · Vector algebra (Q1–Q5)

#### **Q1**[JEE Main][magnitude]Find $\lvert\mathbf a\rvert$ and the unit vector for $\mathbf a=(1,2,3)$.

**Answer:** $\sqrt{14}\approx3.7417$; $\hat{\mathbf a}=\big(\tfrac1{\sqrt{14}},\tfrac2{\sqrt{14}},\tfrac3{\sqrt{14}}\big)$

#### **Q2**[JEE Main][dot]Find $\mathbf a\cdot\mathbf b$ for $\mathbf a=(1,2,3)$, $\mathbf b=(4,5,6)$.

**Answer:** $32$

#### **Q3**[JEE Main][cross]Compute $\mathbf a\times\mathbf b$ for $\mathbf a=(1,2,3)$, $\mathbf b=(4,5,6)$, and its magnitude.

**Answer:** $(-3,6,-3)$; $\lvert\mathbf a\times\mathbf b\rvert=3\sqrt6\approx7.3485$

#### **Q4**[JEE Main][angle]Find the angle between $\mathbf a=(1,2,3)$ and $\mathbf b=(4,5,6)$.

**Answer:** $\cos^{-1}\!\left(\dfrac{32}{\sqrt{1078}}\right)\approx12.93^\circ$

#### **Q5**[JEE Main][section]Find the point dividing the join of $(1,0,0)$ and $(4,5,6)$ in the ratio $2:3$.

**Answer:** $\left(\dfrac{11}{5},2,\dfrac{12}{5}\right)$

---

## B · The two products (Q6–Q10)

#### **Q6**[JEE Main][perpendicular]Show that $(1,2,2)$ and $(2,-2,1)$ are perpendicular.

**Answer:** dot product $=0$

#### **Q7**[JEE Adv][Lagrange]Verify $\lvert\mathbf a\times\mathbf b\rvert^2+(\mathbf a\cdot\mathbf b)^2=\lvert\mathbf a\rvert^2\lvert\mathbf b\rvert^2$ for $\mathbf a=(1,2,3)$, $\mathbf b=(4,5,6)$.

**Answer:** both sides $1078$

#### **Q8**[JEE Adv][triple]Evaluate $\big[(1,2,3)\,(4,5,6)\,(-1,0,2)\big]$.

**Answer:** $-3$

#### **Q9**[JEE Main][self cross]Show that $\mathbf a\times\mathbf a=\mathbf 0$ and explain why.

**Answer:** $\sin 0=0$, so the length is zero

#### **Q10**[JEE Adv][identity]Verify that $(\mathbf a\times\mathbf b)\cdot\mathbf a=0$ for any $\mathbf a,\mathbf b$.

**Answer:** $\mathbf a\times\mathbf b\perp\mathbf a$, so the dot product vanishes

---

## C · Geometry of points (Q11–Q15)

#### **Q11**[JEE Main][distance]Find the distance between $(1,2,3)$ and $(4,6,9)$.

**Answer:** $\sqrt{61}\approx7.8102$

#### **Q12**[JEE Main][area]Find the area of the triangle with vertices $(0,0,0)$, $(3,0,0)$, $(0,4,0)$.

**Answer:** $6$

#### **Q13**[JEE Main][centroid]Find the centroid of the triangle with vertices $(1,0,0)$, $(4,5,6)$, $(7,8,9)$.

**Answer:** $(4,\tfrac{13}{3},5)$

#### **Q14**[JEE Adv][volume]Find the volume of the parallelepiped on $(1,0,0)$, $(0,2,0)$, $(0,0,3)$.

**Answer:** $6$

#### **Q15**[JEE Adv][tetrahedron]Find the volume of the tetrahedron on the same three vectors and the origin.

**Answer:** $1$

---

## D · Straight lines (Q16–Q21)

#### **Q16**[JEE Main][line]Write the line through $(1,2,3)$ with direction $(2,-1,4)$, and find the point at $t=2$.

**Answer:** $\dfrac{x-1}{2}=\dfrac{y-2}{-1}=\dfrac{z-3}{4}$; point $(5,0,11)$

#### **Q17**[JEE Main][angle]Find the angle between the lines with directions $(1,2,2)$ and $(2,1,-1)$.

**Answer:** $\cos^{-1}\!\left(\dfrac{2}{3\sqrt6}\right)\approx74.21^\circ$

#### **Q18**[JEE Adv][distance]Find the distance from $(1,2,3)$ to the line $\mathbf r=t(2,-1,2)$.

**Answer:** $\sqrt{10}\approx3.1623$

#### **Q19**[Olympiad][skew]Find the shortest distance between $\mathbf r=t(1,2,2)$ and $\mathbf r=(1,0,0)+s(2,-1,2)$.

**Answer:** $\dfrac{6}{\sqrt{65}}\approx0.7442$

#### **Q20**[JEE Adv][parallel lines]Find the distance between the parallel lines $\mathbf r=t(2,-1,2)$ and $\mathbf r=(4,5,6)+t(2,-1,2)$.

**Answer:** $\dfrac{\lvert(4,5,6)\times(2,-1,2)\rvert}{3}=2\sqrt{13}\approx7.2111$

#### **Q21**[JEE Main][direction cosines]Find the direction cosines of the line with direction ratios $(2,-1,2)$.

**Answer:** $\left(\dfrac23,-\dfrac13,\dfrac23\right)$

---

## E · The plane (Q22–Q27)

#### **Q22**[JEE Main][plane]Find the plane through $(1,2,3)$ with normal $(2,-3,4)$.

**Answer:** $2x-3y+4z=8$

#### **Q23**[JEE Main][distance]Find the distance from $(1,1,1)$ to $2x-3y+4z-5=0$.

**Answer:** $\dfrac{2}{\sqrt{29}}\approx0.3714$

#### **Q24**[JEE Adv][angle planes]Find the angle between the planes with normals $(1,2,2)$ and $(2,1,-1)$.

**Answer:** $\cos^{-1}\!\left(\dfrac{2}{3\sqrt6}\right)\approx74.21^\circ$

#### **Q25**[JEE Adv][line-plane]Find the angle between the line with direction $(3,-1,2)$ and the plane $x+2y+2z=7$.

**Answer:** $\sin^{-1}\!\left(\dfrac{5}{3\sqrt{14}}\right)\approx26.4^\circ$

#### **Q26**[JEE Adv][parallel]Is the line with direction $(2,-1,2)$ parallel to the plane $x+2y+2z=7$? Justify.

**Answer:** no — $(2,-1,2)\cdot(1,2,2)=4\ne0$

#### **Q27**[JEE Adv][intercept]Find the normal to the plane with intercept form $\dfrac x2+\dfrac y3+\dfrac z6=1$.

**Answer:** $\left(\dfrac12,\dfrac13,\dfrac16\right)$, i.e. $(3,2,1)$

---

## F · Scalar triple & volumes (Q28–Q30)

#### **Q28**[JEE Adv][coplanar]Are $(1,2,3)$, $(4,5,6)$, $(-1,0,2)$, $(2,-1,4)$ coplanar?

**Answer:** no — the triple product is non-zero

#### **Q29**[JEE Main][coplanar]Show that $(1,1,1)$, $(2,2,2)$, $(3,3,3)$ are coplanar.

**Answer:** the triple product is $0$

#### **Q30**[Olympiad][tetrahedron]Find the volume of the tetrahedron with vertices $(1,0,0)$, $(0,2,0)$, $(0,0,3)$, $(1,1,1)$.

**Answer:** $\dfrac56\approx0.8333$

---

## G · Applications & synthesis (Q31–Q36)

#### **Q31**[JEE Main][work]Find the work done by $\mathbf F=(3,4,5)$ over a displacement $(1,0,2)$.

**Answer:** $13$

#### **Q32**[JEE Main][torque]Find the magnitude of the torque $\mathbf r\times\mathbf F$ for $\mathbf r=(1,0,0)$, $\mathbf F=(0,3,4)$.

**Answer:** $5$

#### **Q33**[JEE Adv][Lagrange]Verify Lagrange's identity for $\mathbf a=(3,-1,2)$ and $\mathbf b=(1,4,-2)$.

**Answer:** $\lvert\mathbf a\times\mathbf b\rvert^{2}=269$, $(\mathbf a\cdot\mathbf b)^{2}=25$, $\lvert\mathbf a\rvert^{2}\lvert\mathbf b\rvert^{2}=294$; $269+25=294$ ✓

#### **Q34**[JEE Adv][Lagrange]If $\lvert\mathbf a\rvert=\lvert\mathbf b\rvert=1$ and $\mathbf a\cdot\mathbf b=\frac12$, find $\lvert\mathbf a\times\mathbf b\rvert$.

**Answer:** $\dfrac{\sqrt3}{2}$

#### **Q35**[Olympiad][vector area]Show that the four vector areas of the faces of a tetrahedron sum to $\mathbf 0$.

**Answer:** with consistently oriented outward normals, $\sum\frac12(\mathbf q-\mathbf p)\times(\mathbf r-\mathbf p)=\mathbf0$ over the four faces

#### **Q36**[JEE Adv][tetrahedron]Find the centroid of the tetrahedron with vertices $(0,0,0)$, $(1,0,0)$, $(0,2,0)$, $(0,0,3)$.

**Answer:** $\left(\dfrac14,\dfrac12,\dfrac34\right)$

---

## H · Olympiad frontier (Q37–Q46)

#### **Q37**[Olympiad][Jacobi]Verify Jacobi's identity $\mathbf a\times(\mathbf b\times\mathbf c)+\mathbf b\times(\mathbf c\times\mathbf a)+\mathbf c\times(\mathbf a\times\mathbf b)=\mathbf 0$ for $\mathbf a=(7,8,9)$, $\mathbf b=(1,2,3)$, $\mathbf c=(4,5,6)$.

**Answer:** the sum is $\mathbf 0$

#### **Q38**[Olympiad][median]Prove that the medians of a triangle are concurrent and that the centroid divides each median in the ratio $2:1$.

**Answer:** concurrent at $\frac{\mathbf b+\mathbf c}{3}$ with $A$ at the origin; ratio $2:1$

#### **Q39**[Olympiad][barycentric]In triangle $A(0,0)$, $B(4,0)$, $C(0,3)$, find the barycentric coordinates of $P(1,1)$.

**Answer:** $(5,3,4)$ up to scale, so $[PBC]:[PCA]:[PAB]=5:3:4$

#### **Q40**[Olympiad][barycentric]A point $P$ has barycentric coordinates $(2,5,3)$ relative to triangle $ABC$. What fraction of $[ABC]$ is $[PAB]$?

**Answer:** $\dfrac{3}{10}$

#### **Q41**[Olympiad][Ceva]In triangle $ABC$, $X\in BC$ with $BX:XC=2:1$, $Y\in CA$ with $CY:YA=3:1$, $Z\in AB$ with $AZ:ZB=1:6$. Show the cevians are concurrent.

**Answer:** $xyz=2\cdot3\cdot\frac16=1$, so Ceva applies — concurrent

#### **Q42**[Olympiad][Routh]For $A(0,0)$, $B(5,0)$, $C(1,4)$ and $x=2$, $y=\frac12$, $z=3$, find $\frac{[PQR]}{[ABC]}$ where $PQR$ is bounded by the three cevians.

**Answer:** $\dfrac{(3-1)^{2}}{(1+2+1)(\frac12+\frac12+1)(6+3+1)}=\dfrac{1}{20}$

#### **Q43**[Olympiad][Euler line]Prove that the circumcentre $O$, the centroid $G$ and the orthocentre $H$ of a triangle are collinear, and find $OG:GH$.

**Answer:** collinear (the **Euler line**); $OG:GH=1:2$

#### **Q44**[Olympiad][Euler line]A triangle has circumcentre at the origin, with $A=(2,0,0)$, $B=(0,2,0)$ and $C=(1,1,\sqrt2)$. Find its orthocentre.

**Answer:** $H=A+B+C=(3,3,\sqrt2)$

#### **Q45**[Olympiad][non-associative]Show that $(\mathbf a\times\mathbf b)\times\mathbf c\ne\mathbf a\times(\mathbf b\times\mathbf c)$ for $\mathbf a=(7,8,9)$, $\mathbf b=(1,2,3)$, $\mathbf c=(4,5,6)$.

**Answer:** not equal — the cross product is not associative

#### **Q46**[Olympiad][midpoint]Show that the diagonals of a parallelogram bisect each other.

**Answer:** vertices $0,\mathbf a,\mathbf b,\mathbf a+\mathbf b$; both diagonals share the midpoint $\frac{\mathbf a+\mathbf b}{2}$

---

> [!note] Exam technique notes
> - Put one vertex at the origin whenever the problem allows it — the algebra
>   collapses and no generality is lost.
> - Decide which product you need: an **angle** or a **projection** calls for the
>   dot product; an **area**, a **perpendicular direction** or a **volume** calls
>   for the cross product or the scalar triple.
> - For a distance, ask whether it is point-to-point, point-to-line,
>   point-to-plane, line-to-line (parallel) or skew — each has its own formula.
> - Translate the circumcentre to the origin before any Euler-line problem: with
>   $\lvert A\rvert=\lvert B\rvert=\lvert C\rvert$ the orthocentre becomes $A+B+C$.
> - In any area-ratio problem, write the point in barycentric form first — the
>   coefficients *are* the ratios.
> - Check every identity on a concrete triple of vectors before trusting it.
