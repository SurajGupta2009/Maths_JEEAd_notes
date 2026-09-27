---
title: "3D Geometry — Solutions"
aliases: ["3D Geometry Solutions", "Three Dimensional Geometry Solutions"]
module: "3D-Geometry"
module_title: "3D Geometry"
type: solutions
tags: [3d-geometry, solutions, olympiad, geometry, sphere, plane]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[3D-Geometry — Paper|Paper]] · 📖 [[3D-Geometry|Complete Notes]]

# 3D Geometry — Solutions

> Full solutions to all 34 questions, same Q-ids as the [[3D-Geometry — Paper|paper]].
> Every solution: **method first → derivation → a check.** Every numeric answer was
> verified in pure Python (stdlib only) before this file was written.

---

## A · Coordinates in space

#### **Q1**
**Method: Pythagoras in three dimensions.** $(4-1)^2+(6-2)^2+(9-3)^2=9+16+36=61$.
**Answer:** $\sqrt{61}\approx7.8102$.

#### **Q2**
**Method: section formula $\frac{n\mathbf a+m\mathbf b}{m+n}$.** $\frac{3(1,0,0)+2(4,5,6)}{5}=\frac{(11,10,12)}{5}$.
**Answer:** $\left(\dfrac{11}{5},2,\dfrac{12}{5}\right)$.

#### **Q3**
**Method: reflect by flipping the sign of the coordinate(s) perpendicular to the mirror.** In the $xy$-plane only $z$ flips; in the origin all three flip.
**Answer:** $(1,2,-3)$ and $(-1,-2,-3)$.

#### **Q4**
**Method: substitute into the locus $x^2+y^2+z^2=25$.** $9+16+z^2=25\Rightarrow z^2=0$.
**Answer:** $z=0$.

#### **Q5**
**Method: new coordinates = old $-$ new origin.**
**Answer:** $(3,4,6)$.

---

## B · Direction cosines and angles

#### **Q6**
**Method: divide the ratios by their magnitude.** $\lvert(2,-1,2)\rvert=3$.
**Answer:** $\left(\dfrac23,-\dfrac13,\dfrac23\right)$. (Check: $\frac49+\frac19+\frac49=1$ ✓.)

#### **Q7**
**Method: $\cos\theta=\frac{\mathbf b_1\cdot\mathbf b_2}{\lvert\mathbf b_1\rvert\lvert\mathbf b_2\rvert}$.** $\frac{2+2-2}{3\sqrt6}=\frac{2}{3\sqrt6}$.
**Answer:** $\theta\approx74.21^\circ$.

#### **Q8**
**Method: the angle with the $z$-axis has cosine $n$, the third direction cosine.** Here $n=\frac12$.
**Answer:** $60^\circ$. (Check: $\frac14+\frac12+\frac14=1$ ✓.)

#### **Q9**
**Method: $(\mathbf b-\mathbf a)\cdot\hat{\mathbf d}$.** $\hat{\mathbf d}=\frac{(2,-1,2)}{3}$ and $\mathbf b-\mathbf a=(3,4,6)$, so $\frac{6-4+12}{3}=\frac{14}{3}$.
**Answer:** $\dfrac{14}{3}\approx4.6667$.

#### **Q10**
**Method: perpendicular lines have a zero dot product of their ratios.** $2\cdot4+3\cdot3+4\cdot2=8+9+8=25$.
**Answer:** no — they are not perpendicular.

---

## C · Straight lines

#### **Q11**
**Method: two-point form; the direction ratios are the coordinate differences.** $(4-1,6-2,9-3)=(3,4,6)$.
**Answer:** $\dfrac{x-1}{3}=\dfrac{y-2}{4}=\dfrac{z-3}{6}$.

#### **Q12**
**Method: the cosine formula.** $\frac{\lvert2\cdot4+3\cdot1+4(-2)\rvert}{\sqrt{4+9+16}\sqrt{16+1+4}}=\frac{3}{\sqrt{29}\sqrt{21}}=\frac{3}{\sqrt{609}}$.
**Answer:** $\theta\approx83.02^\circ$.

#### **Q13**
**Method: $F=\mathbf a+t_0\mathbf b$ with $t_0=\frac{\mathbf p\cdot\mathbf b}{\mathbf b\cdot\mathbf b}$ and $\mathbf a=\mathbf 0$.** $t_0=\frac{2-2+6}{9}=\frac23$, so $F=\frac23(2,-1,2)$.
**Answer:** $\left(\dfrac43,-\dfrac23,\dfrac43\right)$. (Check: $(P-F)\cdot(2,-1,2)=0$ ✓.)

#### **Q14**
**Method: reflect the point in its foot, $I=2F-P$.** $2F=\left(\frac83,-\frac43,\frac83\right)$ and $2F-P=\left(\frac53,-\frac{10}{3},-\frac13\right)$.
**Answer:** $\left(\dfrac53,-\dfrac{10}{3},-\dfrac13\right)$. (Check: $F$ is the midpoint of $P$ and $I$ ✓.)

#### **Q15**
**Method: the skew-line distance formula.** $\mathbf b_1\times\mathbf b_2=(2,-1,2)\times(3,1,-1)=(-1,8,5)$; $\mathbf a_2-\mathbf a_1=(3,3,3)$; numerator $\lvert-3+24+15\rvert=36$, denominator $\sqrt{90}$.
**Answer:** $\dfrac{36}{\sqrt{90}}=\dfrac{12}{\sqrt{10}}\approx3.7947$. (Check: $\lvert\mathbf b_1\times\mathbf b_2\rvert\ne0$ and the numerator $\ne0$, so the lines are genuinely skew ✓.)

#### **Q16**
**Method: the coplanarity triple product.** $(0,1,0)\cdot\big((1,0,0)\times(0,0,1)\big)=(0,1,0)\cdot(0,-1,0)=-1$.
**Answer:** not coplanar — skew.

---

## D · The plane

#### **Q17**
**Method: $d=\mathbf a\cdot\mathbf n$.** $(2,-3,4)\cdot(1,2,3)=2-6+12=8$.
**Answer:** $2x-3y+4z=8$.

#### **Q18**
**Method: normal $=(\mathbf b-\mathbf a)\times(\mathbf c-\mathbf a)$.** $(-1,2,0)\times(-1,0,3)=(6,3,2)$; $d=(6,3,2)\cdot(1,0,0)=6$.
**Answer:** $6x+3y+2z=6$. (Equivalently $\frac x1+\frac y2+\frac z3=1$ ✓.)

#### **Q19**
**Method: point–plane distance.** $\frac{\lvert2-3+4-5\rvert}{\sqrt{4+9+16}}=\frac{2}{\sqrt{29}}$.
**Answer:** $\dfrac{2}{\sqrt{29}}\approx0.3714$.

#### **Q20**
**Method: angle between the normals.** $\frac{\lvert2-2-2\rvert}{3\sqrt6}$ — precisely $\frac{(1,2,2)\cdot(2,1,-1)}{3\sqrt6}=\frac{2}{3\sqrt6}$.
**Answer:** $\theta\approx74.21^\circ$.

#### **Q21**
**Method: $F=P-\frac{\mathbf p\cdot\mathbf n-d}{\lvert\mathbf n\rvert^2}\mathbf n$, then $I=2F-P$.** $\frac{1+2+3-1}{3}=\frac53$; $F=(1,2,3)-\frac53(1,1,1)=\left(-\frac23,\frac13,\frac43\right)$; $I=\left(-\frac73,-\frac43,-\frac13\right)$.
**Answer:** $\left(-\dfrac73,-\dfrac43,-\dfrac13\right)$. (Check: $F$ lies on $x+y+z=1$ ✓ and is the midpoint of $P$ and $I$ ✓.)

#### **Q22**
**Method: the same projection, with $\mathbf n=(2,-3,4)$, $d=5$.** $\frac{2-6+12-5}{29}=\frac3{29}$; $F=(1,2,3)-\frac3{29}(2,-3,4)=\left(\frac{23}{29},\frac{67}{29},\frac{75}{29}\right)$.
**Answer:** foot $\left(\dfrac{23}{29},\dfrac{67}{29},\dfrac{75}{29}\right)$; distance $\dfrac3{\sqrt{29}}\approx0.5571$. (Check: $2\cdot\frac{23}{29}-3\cdot\frac{67}{29}+4\cdot\frac{75}{29}=\frac{145}{29}=5$ ✓.)

#### **Q23**
**Method: the pencil $(x+y+z-1)+\lambda(2x-3y+4z-5)=0$; substitute the origin.** $-1-5\lambda=0\Rightarrow\lambda=-\frac15$. Multiplying by $5$: $(5x+5y+5z-5)+(-2x+3y-4z+5)=0$, i.e. $3x+8y+z=0$.
**Answer:** $3x+8y+z=0$.

---

## E · The sphere

#### **Q24**
**Method: compare with $x^2+y^2+z^2+2ux+2vy+2wz+d=0$; then $C=(-u,-v,-w)$ and $R^2=u^2+v^2+w^2-d$.** Here $u=1,v=-2,w=3,d=-11$.
**Answer:** centre $(-1,2,-3)$, radius $\sqrt{1+4+9+11}=5$.

#### **Q25**
**Method: centre = midpoint, radius = half the distance.** $C=\left(\frac12,1,0\right)$; $R=\frac12\sqrt{1+4}=\frac{\sqrt5}{2}$.
**Answer:** centre $\left(\dfrac12,1,0\right)$, radius $\dfrac{\sqrt5}{2}\approx1.1180$.

#### **Q26**
**Method: compare the centre–plane distance with the radius, then $r^2=R^2-d^2$.** $d=\frac{20}{\sqrt{29}}\approx3.7139<5$, so the plane cuts the sphere. The foot of the perpendicular from the origin is $\frac{20}{29}(2,-3,4)$ and $r^2=25-\frac{400}{29}=\frac{325}{29}$.
**Answer:** centre $\left(\dfrac{40}{29},-\dfrac{60}{29},\dfrac{80}{29}\right)$, radius $\sqrt{\dfrac{325}{29}}\approx3.3477$.

#### **Q27**
**Method: subtract the two sphere equations.** $(x^2+y^2+z^2-25)-(x^2+y^2+z^2-6x-7)=6x-18=0$.
**Answer:** $x=3$. (Check with $(3,1,2)$: both powers equal $-11$ ✓.)

#### **Q28**
**Method: orthogonality condition $2(u_1u_2+v_1v_2+w_1w_2)=d_1+d_2$.** $S_1$: $u=v=w=0$, $d=-1$. $S_2$: $(x-1)^2+(y-2)^2+(z-3)^2=1\Rightarrow u=-1,v=-2,w=-3$, $d=1+4+9-1=13$. LHS $=2(0)=0$, RHS $=-1+13=12$.
**Answer:** not orthogonal ($0\ne12$).

#### **Q29**
**Method: radius = distance from the centre to the given point.** $\lvert(1,2,3)\rvert=\sqrt{14}$.
**Answer:** $\sqrt{14}\approx3.7417$.

---

## F · Olympiad frontier

#### **Q30**
**Method: $\sin\alpha=R/\lvert PC\rvert$; the contact circle lies at distance $R^2/\lvert PC\rvert$ from $C$ along $PC$, with radius $R\sqrt{1-R^2/\lvert PC\rvert^2}$.** With $C=(0,0,0)$, $R=5$, $P=(13,0,0)$: $\lvert PC\rvert=13$.
$$\sin\alpha=\frac5{13},\qquad \alpha\approx22.62^\circ.$$
The contact circle is in the plane $x=\frac{25}{13}$ with radius $5\sqrt{1-\frac{25}{169}}=\frac{60}{13}$.
**Answer:** $\alpha=\sin^{-1}\!\left(\dfrac5{13}\right)\approx22.62^\circ$; plane $x=\dfrac{25}{13}$, radius $\dfrac{60}{13}\approx4.6154$. (Check: the slant height from $P$ to the circle is $\sqrt{13^2-5^2}=12$, giving the $5$-$12$-$13$ triangle ✓.)

#### **Q31**
**Method: $r=\frac{3V}{S}$ with $V=\frac16\lvert[\mathbf a\,\mathbf b\,\mathbf c]\rvert$.** With $\mathbf a=(4,0,0)$, $\mathbf b=(0,4,0)$, $\mathbf c=(0,0,3)$:
$$V=\frac16\big\lvert(4,0,0)\cdot\big((0,4,0)\times(0,0,3)\big)\big\rvert=\frac16\lvert(4,0,0)\cdot(12,0,0)\rvert=8.$$
The four faces: $8$, $6$, $6$, and $\frac12\lvert(0,-4,-3)\times(-4,0,-3)\rvert=\frac12\sqrt{544}$, so $S=20+\frac12\sqrt{544}\approx31.6619$.
**Answer:** $r=\dfrac{24}{20+\frac12\sqrt{544}}\approx0.7580$. (Check the volume independently: the tetrahedron is $\frac16$ of the box $\frac14\cdot4\cdot4\cdot3=8$ ✓.)

#### **Q32**
**Method: the polar plane of $(x_1,y_1,z_1)$ wrt $x^2+y^2+z^2=R^2$ is $xx_1+yy_1+zz_1=R^2$.**
**Answer:** $x+2y+3z=25$. (Note: $\lvert P\rvert=\sqrt{14}<5$, so $P$ is inside the sphere and no real tangent cone exists — the polar plane is still well defined, at distance $\frac{25}{\sqrt{14}}\approx6.68$ from the centre.)

#### **Q33**
**Method: subtract the equations pairwise.** With $S_1=x^2+y^2+z^2-14$, $S_2=x^2+y^2+z^2-10x-4$, $S_3=x^2+y^2+z^2-10y+6$:
$$S_1-S_2=10x-10=0,\quad S_1-S_3=10y-20=0,\quad S_2-S_3=-10x+10y-10=0.$$
All three planes contain the line $x=1$, $y=2$, so that line is the radical axis.
**Answer:** the radical axis is the line $x=1$, $y=2$. (Check with $(1,2,0)$, $(1,2,5)$ and $(1,2,-7)$: the three powers are equal at each point — $-9$, $16$ and $40$ respectively ✓. The axis is parallel to the $z$-axis, which is perpendicular to the plane $z=0$ containing the three centres ✓.)

#### **Q34**
**Method: put the circumcentre at the origin.** Let the vertices be $\mathbf a,\mathbf b,\mathbf c,\mathbf d$, and since the origin is the circumcentre,
$$\lvert\mathbf a\rvert=\lvert\mathbf b\rvert=\lvert\mathbf c\rvert=\lvert\mathbf d\rvert=R.$$
Consider the edge $AB$. Its midpoint is $\frac{\mathbf a+\mathbf b}{2}$ and the *opposite* edge is $CD$, whose direction is $\mathbf d-\mathbf c$. The **midplane** of $AB$ is therefore
$$\left(\mathbf r-\frac{\mathbf a+\mathbf b}{2}\right)\cdot(\mathbf d-\mathbf c)=0.$$
Now set $\mathbf m=\frac12(\mathbf a+\mathbf b+\mathbf c+\mathbf d)$ and substitute $\mathbf r=\mathbf m$:
$$\left(\frac{\mathbf a+\mathbf b+\mathbf c+\mathbf d}{2}-\frac{\mathbf a+\mathbf b}{2}\right)\cdot(\mathbf d-\mathbf c)
=\frac{\mathbf c+\mathbf d}{2}\cdot(\mathbf d-\mathbf c)
=\frac{\lvert\mathbf d\rvert^2-\lvert\mathbf c\rvert^2}{2}=0,$$
because both vertices lie on the circumsphere. The same computation works for each of the six edges (replacing the pair $(C,D)$ by whichever edge is opposite), so **all six midplanes pass through $\mathbf m$**.

Finally, the centroid is $\mathbf g=\frac14(\mathbf a+\mathbf b+\mathbf c+\mathbf d)$, so $\mathbf m=2\mathbf g$ — that is, $\mathbf m$ is the reflection of the circumcentre (the origin) in the centroid.
**Answer:** the six midplanes are concurrent at the **Monge point** $\mathbf m$, which is the reflection of the circumcentre in the centroid. (Verified numerically: for the tetrahedron $(1,0,0)$, $(0,2,0)$, $(0,0,3)$, $(2,1,4)$, the circumcentre is $(1.382,1.441,1.794)$, the centroid $(0.75,0.75,1.75)$, and $\mathbf m=2\mathbf g-\mathbf O=(0.118,0.059,1.706)$ satisfies all six midplane equations to machine precision ✓.)
