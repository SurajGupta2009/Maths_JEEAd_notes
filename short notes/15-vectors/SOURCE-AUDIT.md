# Source Audit — Chapter 15: Vectors

## Sources reviewed

- `notes/Vectors/Vectors.md` — the 735-line canonical module. Chapters 1–3 supplied the vector algebra, products and geometric applications; Chapter 6 supplied the labelled advanced extensions. Its appendix and mistake checklist were also reviewed.
- `notes/Vectors/Vectors — Paper.md` (250 lines) and `Vectors — Solutions.md` (240 lines) — all 46 companion questions and their solution conventions were inspected for candidate models and independent checks. Numerical answers were not copied uncritically.
- Official JEE Advanced 2026 Mathematics syllabus, Vectors: <https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf>. The official operations and geometrical interpretations are mapped in `SCOPE.md`.

## Scope decisions

Part I covers vector addition, scalar multiplication, dot/cross products, scalar triple products and direct geometric interpretations: section formulas, centroids, angles, projections, areas, dependence, coplanarity and volumes. Vector triple products, Jacobi, scalar quadruple products, barycentrics/Ceva/Routh and Euler-line proofs are clearly separated in Part II.

The source module's Chapters 4–5, **Straight Lines in Space** and **The Plane**, are reserved for Chapter 16 — Three-Dimensional Geometry. Their full line/plane equations, distance formulas and angle theory are not silently included in this chapter. A cross-product normal or triple-product coplanarity test here serves only the vector-product scope.

## Independent verification

`scripts/math_checks.py` contains **204 exact/rational, numerical, visual-lesson and editable-figure checks**. These cover components and direction cosines, displacements, linear combinations, section formulas, centroids, dot/cross identities, Cauchy–Schwarz, projection/rejection, work, areas, scalar triple products, coplanarity, tetrahedra, both vector-triple-product groupings, Jacobi, scalar quadruple products, barycentrics, Ceva, Routh, Varignon and the Euler line.

Fixed families of exact vectors test the general identities beyond the single printed examples. The suite also reads the actual JSON diagram specifications and checks their encoded arrows, points, cross products, signed volumes, rounded intersections and area ratios. These are targeted reproducible checks, not automated proof verification; native-size visual review supplements them.

## Corrections to the source (do not reproduce)

- **P14 / paper Q42, Routh's ratio:** with $x=2$, $y=1/2$ and $z=3$, the cyclic denominators are $xy+x+1=4$, $yz+y+1=3$ and $zx+z+1=10$. Hence
  $$
  \frac{[PQR]}{[ABC]}=\frac{(3-1)^2}{4\cdot3\cdot10}=\frac1{30},
  $$
  not the module and solution's $1/20$. The erroneous calculation replaces the second factor $3$ by $2$ and then claims a matching direct-intersection check. Independent intersections are $P=(7/4,2)$, $Q=(17/6,4/3)$ and $R=(21/10,12/5)$; they give twice-areas $20$ for $ABC$ and $2/3$ for $PQR$, confirming $1/30$. Since $[ABC]=10$, $[PQR]=1/3$.
- **P15 / paper Q44, alleged 3D circumcentre:** the points $A=(2,0,0)$, $B=(0,2,0)$ and $C=(1,1,\sqrt2)$ are indeed distance $2$ from the origin, but their plane is $x+y=2$, which does not contain $O=(0,0,0)$. Thus $O$ is a sphere centre, not the triangle's circumcentre, and the source's orthocentre answer is not valid for a plane triangle. The notes explicitly warn against the equal-distance-only inference. The verified replacement uses $O=(0,0)$, $A=(5,0)$, $B=(0,5)$ and $C=(-4,-3)$, giving $H=(1,2)$, $G=(1/3,2/3)$, three zero altitude dot products and $OG:GH=1:2$.

## Independently confirmed source models

The non-associativity example was recomputed directly and by both BAC–CAB forms: $(a\times b)\times c=(-102,-12,78)$, while $a\times(b\times c)=(-78,-6,66)$. The four-point coplanarity example has edge triple product $12$, so its parallelepiped and tetrahedron volumes are $12$ and $2$. The tetrahedron example from the common tail $D$ has signed triple product $-5$, volume $5/6$ and centroid $(1/2,3/4,1)$. These checks preserve the valid source calculations while testing their hypotheses.

## IOQM boundary

Part II provides vector-related Olympiad and specialised extensions only. It is not a complete IOQM/RMO syllabus, and no extension is claimed to be impossible in JEE. Proof-level identities are distinguished from the targeted numerical evidence in the check suite.
