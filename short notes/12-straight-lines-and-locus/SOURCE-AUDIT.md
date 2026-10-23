# Source Audit — Chapter 12: Straight Lines & Locus

## Sources reviewed

- `notes/Coordinate-Geometry-Lines-and-Circles/Coordinate-Geometry-Lines-and-Circles.md` — all 827 lines reviewed, including the six chapters and theory appendix.
- The companion 249-line Olympiad paper and 238-line solutions were read in full; they contain 46 questions. The sheets use the theory source as the primary source and independently recheck selected examples rather than copying the mixed-level paper.
- Official JEE Advanced 2026 Mathematics syllabus, Analytical Geometry (two dimensions), retrieved from the official PDF at <https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf>. The precise coordinate/line/triangle-centre bullets are mapped in `SCOPE.md`.

## Scope decisions

The official list explicitly includes coordinates, distance/section/origin shift, line forms, angle/distance, pencil through an intersection, angle bisectors, concurrency and the four named triangle centres. Locus techniques, determinant area and homogeneous pairs of lines are retained as useful derivable tools, but not mislabelled as separate quoted syllabus bullets. Olympiad extensions are isolated in Part II.

## Independent verification

`scripts/math_checks.py` contains **40 exact/rational checks**: distance and section ratios (internal and external), coordinate translation, signed area/collinearity, point-to-line projection and scale invariance, line parallel/perpendicular tests, normalized bisectors, line pencils, the four 3–4–5 triangle centres, the Euler-line ratio, Apollonius circle/line cases, a homogeneous pair and all nine points of a non-right nine-point-circle example. Checks support the worked values; they do not prove every general theorem.

## Corrections and source limitations

- The source's Euler-line extension mixes the four points' parameter positions with segment lengths. The correct order is $O,G,N,H$, with parameter positions $0,1/3,1/2,1$ and segment ratio $OG:GN:NH=2:1:3$; the equilateral case has all centres coincident.
- The source's nine-point discussion lists the altitude-foot case but its one-line midpoint argument does not establish that case. Part II now supplies a coordinate proof, rather than treating a numerical check as proof.
- The source's external-division wording is not used as a shortcut. The notes state the coordinate formula and the $m\ne n$ condition explicitly.
- The source module's pair-of-lines treatment is useful but not separately named in the quoted official line syllabus; it is marked as a derived model.
- No full synthetic proof of every triangle-centre theorem is claimed; the core uses their definitions, equations and independent coordinate examples.
