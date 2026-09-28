---
title: "3D Geometry — Olympiad Paper"
aliases: ["3D Geometry Paper", "Three Dimensional Geometry Paper"]
module: "3D-Geometry"
module_title: "3D Geometry"
type: paper
tags: [3d-geometry, paper, olympiad, geometry, sphere, plane]
created: 2026-09-27
---

> [!info] Navigation
> ⬅ [[3D-Geometry|Chapter 6]] · 📖 [[3D-Geometry|Complete Notes]] · ✅ [[3D-Geometry — Solutions|Solutions]] ➡

# 3D Geometry — Olympiad Paper

> **34 questions · Sections A–H · difficulty ramps JEE Main → JEE Advanced → Olympiad.**
> Attempt the whole paper before opening the [[3D-Geometry — Solutions|solutions]].
> Every numeric answer was verified in pure Python before this file was written.

---

## A · Coordinates in space (Q1–Q5)

#### **Q1**[JEE Main][distance]Find the distance between $(1,2,3)$ and $(4,6,9)$.

**Answer:** $\sqrt{61}\approx7.8102$

#### **Q2**[JEE Main][section]Find the point dividing the join of $(1,0,0)$ and $(4,5,6)$ in the ratio $2:3$.

**Answer:** $\left(\dfrac{11}{5},2,\dfrac{12}{5}\right)$

#### **Q3**[JEE Main][reflection]Find the reflection of $(1,2,3)$ in the $xy$-plane, and in the origin.

**Answer:** $(1,2,-3)$ and $(-1,-2,-3)$

#### **Q4**[JEE Main][locus]Find $z$ for a point at distance $5$ from the origin with $x=3$, $y=4$.

**Answer:** $z=0$

#### **Q5**[JEE Main][translation]Shift the origin to $(1,2,3)$. What are the new coordinates of $(4,6,9)$?

**Answer:** $(3,4,6)$

---

## B · Direction cosines and angles (Q6–Q10)

#### **Q6**[JEE Main][dcs]Find the direction cosines of the line with direction ratios $(2,-1,2)$.

**Answer:** $\left(\dfrac23,-\dfrac13,\dfrac23\right)$

#### **Q7**[JEE Main][angle]Find the angle between the lines with direction ratios $(1,2,2)$ and $(2,1,-1)$.

**Answer:** $\cos^{-1}\!\left(\dfrac{2}{3\sqrt6}\right)\approx74.21^\circ$

#### **Q8**[JEE Main][dcs angle]A line has direction cosines $\left(\frac12,\frac1{\sqrt2},\frac12\right)$. What angle does it make with the $z$-axis?

**Answer:** $60^\circ$

#### **Q9**[JEE Adv][projection]Find the projection of the segment from $(1,2,3)$ to $(4,6,9)$ on the line with direction ratios $(2,-1,2)$.

**Answer:** $\dfrac{14}{3}\approx4.6667$

#### **Q10**[JEE Main][perpendicular]Are the lines with direction ratios $(2,3,4)$ and $(4,3,2)$ perpendicular?

**Answer:** no — the dot product is $25\ne0$

---

## C · Straight lines (Q11–Q16)

#### **Q11**[JEE Main][line]Write the line through $(1,2,3)$ and $(4,6,9)$ in symmetric form.

**Answer:** $\dfrac{x-1}{3}=\dfrac{y-2}{4}=\dfrac{z-3}{6}$

#### **Q12**[JEE Adv][angle]Find the angle between $\dfrac{x-1}{2}=\dfrac{y-2}{3}=\dfrac{z-3}{4}$ and $\dfrac{x-1}{4}=\dfrac{y-2}{1}=\dfrac{z-3}{-2}$.

**Answer:** $\cos^{-1}\!\left(\dfrac{3}{\sqrt{609}}\right)\approx83.02^\circ$

#### **Q13**[JEE Adv][foot]Find the foot of the perpendicular from $(1,2,3)$ to the line $\mathbf r=t(2,-1,2)$.

**Answer:** $\left(\dfrac43,-\dfrac23,\dfrac43\right)$

#### **Q14**[JEE Adv][image]Find the image of $(1,2,3)$ in the line $\mathbf r=t(2,-1,2)$.

**Answer:** $\left(\dfrac53,-\dfrac{10}{3},-\dfrac13\right)$

#### **Q15**[Olympiad][skew]Find the shortest distance between $\mathbf r=(1,2,3)+t(2,-1,2)$ and $\mathbf r=(4,5,6)+s(3,1,-1)$.

**Answer:** $\dfrac{12}{\sqrt{10}}\approx3.7947$

#### **Q16**[JEE Adv][coplanar]Are the lines $\mathbf r=t(1,0,0)$ and $\mathbf r=(0,1,0)+s(0,0,1)$ coplanar?

**Answer:** no — they are skew; the triple product is $-1$

---

## D · The plane (Q17–Q23)

#### **Q17**[JEE Main][plane]Find the plane through $(1,2,3)$ with normal $(2,-3,4)$.

**Answer:** $2x-3y+4z=8$

#### **Q18**[JEE Main][three points]Find the plane through $(1,0,0)$, $(0,2,0)$, $(0,0,3)$.

**Answer:** $6x+3y+2z=6$

#### **Q19**[JEE Main][distance]Find the distance from $(1,1,1)$ to $2x-3y+4z-5=0$.

**Answer:** $\dfrac{2}{\sqrt{29}}\approx0.3714$

#### **Q20**[JEE Main][angle planes]Find the angle between the planes with normals $(1,2,2)$ and $(2,1,-1)$.

**Answer:** $\cos^{-1}\!\left(\dfrac{2}{3\sqrt6}\right)\approx74.21^\circ$

#### **Q21**[JEE Adv][image]Find the image of $(1,2,3)$ in the plane $x+y+z=1$.

**Answer:** $\left(-\dfrac73,-\dfrac43,-\dfrac13\right)$

#### **Q22**[JEE Adv][foot]Find the foot of the perpendicular from $(1,2,3)$ to $2x-3y+4z-5=0$, and the distance.

**Answer:** $\left(\dfrac{23}{29},\dfrac{67}{29},\dfrac{75}{29}\right)$; distance $\dfrac3{\sqrt{29}}\approx0.5571$

#### **Q23**[JEE Adv][pencil]Find the plane through the intersection of $x+y+z=1$ and $2x-3y+4z=5$ that passes through the origin.

**Answer:** $3x+8y+z=0$

---

## E · The sphere (Q24–Q29)

#### **Q24**[JEE Main][sphere]Find the centre and radius of $x^2+y^2+z^2+2x-4y+6z-11=0$.

**Answer:** centre $(-1,2,-3)$, radius $5$

#### **Q25**[JEE Main][diameter]Find the sphere on the join of $(1,0,0)$ and $(0,2,0)$ as diameter.

**Answer:** centre $\left(\dfrac12,1,0\right)$, radius $\dfrac{\sqrt5}{2}\approx1.1180$

#### **Q26**[JEE Adv][section]The plane $2x-3y+4z=20$ cuts the sphere $x^2+y^2+z^2=25$. Find the centre and radius of the circle of intersection.

**Answer:** centre $\left(\dfrac{40}{29},-\dfrac{60}{29},\dfrac{80}{29}\right)$, radius $\sqrt{\dfrac{325}{29}}\approx3.3477$

#### **Q27**[JEE Adv][radical]Find the radical plane of $x^2+y^2+z^2=25$ and $(x-3)^2+y^2+z^2=16$.

**Answer:** $x=3$

#### **Q28**[JEE Adv][orthogonal]Do $x^2+y^2+z^2=1$ and $(x-1)^2+(y-2)^2+(z-3)^2=1$ cut orthogonally?

**Answer:** no — $0\ne12$

#### **Q29**[JEE Main][sphere]Find the radius of the sphere with centre $(1,2,3)$ passing through the origin.

**Answer:** $\sqrt{14}\approx3.7417$

---

## F · Olympiad frontier (Q30–Q34)

#### **Q30**[Olympiad][tangent cone]Find the semi-vertical angle of the cone of tangents from $(13,0,0)$ to $x^2+y^2+z^2=25$, and the plane and radius of the circle of contact.

**Answer:** $\alpha=\sin^{-1}\!\left(\dfrac5{13}\right)\approx22.62^\circ$; plane $x=\dfrac{25}{13}$, radius $\dfrac{60}{13}\approx4.6154$

#### **Q31**[Olympiad][insphere]Find the inradius of the tetrahedron with vertices $(0,0,0)$, $(4,0,0)$, $(0,4,0)$, $(0,0,3)$.

**Answer:** $\dfrac{24}{20+\frac12\sqrt{544}}\approx0.7580$

#### **Q32**[Olympiad][polar]Find the polar plane of $(1,2,3)$ with respect to $x^2+y^2+z^2=25$.

**Answer:** $x+2y+3z=25$

#### **Q33**[Olympiad][radical axis]Find the radical axis of $x^2+y^2+z^2=14$, $(x-5)^2+y^2+z^2=29$ and $x^2+(y-5)^2+z^2=19$.

**Answer:** the line $x=1$, $y=2$

#### **Q34**[Olympiad][Monge]State Monge's theorem for a tetrahedron and prove that the six midplanes are concurrent.

**Answer:** the six planes through the midpoints of the edges, each perpendicular to the opposite edge, meet at the Monge point, the reflection of the circumcentre in the centroid

---

## G · Orthogonality, spherical excess & the regular tetrahedron (Q35–Q40)

#### **Q35**[Olympiad][orthogonal]Do the spheres $x^{2}+y^{2}+z^{2}=25$ and $(x-4)^{2}+(y-3)^{2}+z^{2}=16$ cut orthogonally?

**Answer:** no — the centre distance is $5$, so $d^{2}=25\ne41=r_1^{2}+r_2^{2}$

#### **Q36**[Olympiad][orthogonal]Find the locus of the centres of spheres of radius $3$ that cut $x^{2}+y^{2}+z^{2}=16$ orthogonally.

**Answer:** $x^{2}+y^{2}+z^{2}=25$ (centre at distance $\sqrt{16+9}=5$ from the origin)

#### **Q37**[JEE Adv][orthogonal]State the condition for two spheres of radii $r_1,r_2$ whose centres are distance $d$ apart to cut orthogonally.

**Answer:** $d^{2}=r_{1}^{2}+r_{2}^{2}$

#### **Q38**[Olympiad][Girard]A spherical triangle on the unit sphere has angles $80^{\circ}$, $70^{\circ}$ and $60^{\circ}$. Find its area and the fraction of the sphere it covers.

**Answer:** excess $30^{\circ}=\frac\pi6$, area $\frac\pi6\approx0.5236$, fraction $\frac1{24}$

#### **Q39**[Olympiad][Girard]A spherical triangle on a sphere of radius $2$ has area $1$. Find its spherical excess.

**Answer:** $E=\text{area}/R^{2}=\frac14$ radian $\approx14.32^{\circ}$

#### **Q40**[Olympiad][regular]A regular tetrahedron has inradius $1$. Find its edge, circumradius and volume.

**Answer:** edge $2\sqrt6\approx4.8990$, circumradius $3$, volume $8\sqrt3\approx13.8564$

---

## H · Olympiad synthesis (Q41–Q46)

#### **Q41**[Olympiad][regular]For a regular tetrahedron of edge $a$, prove $R=3r$ and find the dihedral angle between two faces.

**Answer:** $R=\frac{a\sqrt6}{4}$, $r=\frac{a\sqrt6}{12}$, so $R=3r$; dihedral angle $\cos^{-1}\!\frac13\approx70.53^{\circ}$

#### **Q42**[Olympiad][regular]Find the solid angle subtended at a vertex of a regular tetrahedron by the opposite face.

**Answer:** $\Omega=3\cos^{-1}\!\frac13-\pi\approx0.5513$ steradians

#### **Q43**[Olympiad][spherical]The three coordinate planes cut the unit sphere into eight congruent spherical triangles. Find the area of one of them, and check it against Girard's theorem.

**Answer:** each has angles $\frac\pi2,\frac\pi2,\frac\pi2$, excess $\frac\pi2$, area $\frac\pi2$ — exactly $\frac18$ of $4\pi$ ✓

#### **Q44**[Olympiad][Dandelin]Explain why the Dandelin spheres prove that a plane section of a cone is an ellipse with the tangency points as foci.

**Answer:** the two tangent segments from a point on the section to each sphere are equal, so $PF_1+PF_2$ equals the constant distance between the contact circles along a generator

#### **Q45**[Olympiad][coaxal]A sphere is orthogonal to two given spheres. What can you say about it and the coaxal pencil they generate?

**Answer:** it is orthogonal to **every** member of the coaxal pencil, and its centre lies on their radical plane

#### **Q46**[Olympiad][Monge]For the tetrahedron $(1,0,0)$, $(0,2,0)$, $(0,0,3)$, $(2,1,4)$, locate the Monge point.

**Answer:** the centroid is $\mathbf g=\frac14(5,3,7)=(1.25,0.75,1.75)$; with the circumcentre $\mathbf O\approx(1.382,1.441,1.794)$ the Monge point is $\mathbf m=2\mathbf g-\mathbf O\approx(1.118,0.059,1.706)$

---

> [!note] Exam technique notes
> - Decide first *what kind* of answer is wanted: an angle (dot product), a
>   distance (cross product or point–plane formula), a foot (projection), an
>   image (reflect), or a locus (equation).
> - When a plane must pass through an extra condition, reach for the pencil
>   $P_1+\lambda P_2=0$ before writing simultaneous equations.
> - For anything involving a sphere, complete the square first — it converts the
>   general equation into a centre and a radius you can reason about.
> - For a plane–sphere question, always compare the centre–plane distance with
>   the radius before computing the section.
> - Orthogonality of two spheres is a statement about three lengths only:
>   check $d^{2}=r_1^{2}+r_2^{2}$ before doing anything else.
> - In a spherical problem, convert degrees to radians before applying Girard.
