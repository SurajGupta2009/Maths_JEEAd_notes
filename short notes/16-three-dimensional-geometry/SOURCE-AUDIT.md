# Source Audit — Chapter 16: Three-Dimensional Geometry

## Sources reviewed

- `notes/3D-Geometry/3D-Geometry.md` — the 1,066-line canonical module covering coordinates, directions, lines, planes, spheres and labelled advanced topics.
- `notes/3D-Geometry/3D-Geometry — Paper.md` and `3D-Geometry — Solutions.md` — all 46 companion question/answer pairs were inspected for candidate models, conventions and independent checks. Numerical answers were not copied uncritically.
- Official JEE Advanced 2026 Mathematics syllabus, Three-Dimensional Geometry: <https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf>. The official line/plane scope is mapped in `SCOPE.md`.

## Scope decisions

Part I contains the complete official line/plane core and directly supporting coordinates, projections, feet/images, parallel-plane distances, pencils and bisector planes. Sphere equations, sphere sections, radical/polar geometry, tetrahedron centres and spherical geometry are explicitly separated into Part II. The visual lab is an exact problem-solving supplement, not a replacement for derivations.

The source's Dandelin-sphere remark is not developed here: its main purpose is the focal theory of conics, while this chapter's extension sequence remains focused on spatial metric geometry. No extension is claimed to be impossible in JEE.

## Independent verification

`scripts/math_checks.py` contains **200 exact/rational, numerical, visual-lab and editable-figure checks**. It recomputes the displayed answers, tests general hypotheses and degenerate cases, verifies all six Monge midplanes, and reads the actual JSON diagram specifications. Selected checks cover plane-patch incidence, sphere distances, circle bases, rounded inradius data and the regular-tetrahedron drawing.

These are targeted reproducible checks, not automated proof verification. Native-size visual inspection supplements them, including label placement, transparent sphere visibility, plane-patch orientation, safe margins and continuation-page flow.

## Corrections to the source (do not reproduce)

- **S16, completing squares:** the source contains contradictory scratch prose claiming $C=(1,-2,3)$. For
  $$
  x^2+y^2+z^2+2x-4y+6z-11=0,
  $$
  the correct completed form is $(x+1)^2+(y-2)^2+(z-3)^2=25$, so $C=(-1,2,-3)$ and $R=5$.
- **S18, four-point sphere:** the centre $(-13/10,1/10,9/10)$ and radius $\sqrt{611}/10$ are correct. However, the general-form constant is
  $$
  d=|C|^2-R^2=\frac{251-611}{100}=-\frac{18}{5},
  $$
  not $-611/100$. The notes verify all four squared distances and the cleared equation $5(x^2+y^2+z^2)+13x-y-9z-18=0$.
- **P6, allegedly parallel but distinct lines:** $L_1:t(1,2,3)$ and $L_2:(1,2,3)+s(1,2,3)$ **coincide**, because the second base point lies on $L_1$ at $t=1$. The notes state this correction and use $(1,0,0)+s(1,2,3)$ for a genuinely distinct parallel variant.
- **Tetrahedron inradius volume check:** for vertices $(0,0,0),(4,0,0),(0,4,0),(0,0,3)$, the coordinate-face areas are $8,6,6$, the slant-face area is $2\sqrt{34}$, and
  $$
  V=8,\qquad S=20+2\sqrt{34},\qquad r=\frac{12}{10+\sqrt{34}}\approx0.7580087464.
  $$
  The source's surrounding volume-check prose is malformed; the bounding box volume is $48$, not the tetrahedron volume.
- **Paper Q46, centroid and Monge point:** for $(1,0,0),(0,2,0),(0,0,3),(2,1,4)$, the correct values are
  $$
  G=\left(\frac34,\frac34,\frac74\right),\quad
  O=\left(\frac{47}{34},\frac{49}{34},\frac{61}{34}\right),\quad
  M=2G-O=\left(\frac2{17},\frac1{17},\frac{29}{17}\right).
  $$
  The paper answer uses a wrong centroid and Monge $x$-coordinate. The solutions' approximate final point agrees with the exact value above. The new notes test all six midplanes exactly.
- **S28, tetrahedron wording:** “opposite faces are parallel” is invalid for a tetrahedron. Monge's construction instead pairs an edge with its opposite edge; the notes use that correct formulation.
- **Regular-tetrahedron solid angle:** the spherical triangle at a vertex has **dihedral angles** $\theta=\arccos(1/3)$, not $60^\circ$ face angles. Hence
  $$
  \Omega=3\arccos(1/3)-\pi\approx0.5512855984\ \mathrm{sr},
  $$
  with dihedral angle $70.5287793655^\circ$. The $60^\circ$ face angles are the spherical triangle's sides.

## Independently confirmed and completed source models

For the skew-line example, the common normal is $(-1,8,5)$, the signed numerator is $36$, and $d=12/\sqrt{10}$. Solving both perpendicularity equations gives $t=4/5$, $s=-3/5$ and
$$
F_1=(13/5,6/5,23/5),\qquad F_2=(11/5,22/5,33/5),
$$
so $F_2-F_1=(2/5)(-1,8,5)$. This independently confirms both the distance and the common-perpendicular construction.

The tangent-cone example has $D=13$, $R=5$, tangent length $12$, semi-vertical angle $22.6198649480^\circ$, contact plane $x=25/13$ and contact-circle radius $60/13$. The sphere-section example has $r^2=325/29$ and $r\approx3.3476703171$. The finite-pencil omission of $P_2=0$ is stated explicitly, with the complete homogeneous pencil supplied.

## IOQM boundary

Part II provides spatial-geometry Olympiad and specialised extensions only. It is not a complete IOQM/RMO syllabus. Proof-level concurrence and spherical results are distinguished from numerical evidence in the check suite.
