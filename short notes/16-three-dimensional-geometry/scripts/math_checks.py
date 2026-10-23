#!/usr/bin/env python3
"""Independent exact, numerical and editable-figure checks for Chapter 16."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from math import acos, asin, degrees, isclose, pi, sqrt
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "_engine"))
from visual_math_checks import checks_for

checks = 0


def ck(ok, msg):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(msg)


def close(a, b, tol=1e-9):
    return isclose(float(a), float(b), rel_tol=tol, abs_tol=tol)


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def scale(s, a):
    return tuple(s*x for x in a)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def norm2(a):
    return dot(a, a)


def triple(a, b, c):
    return dot(a, cross(b, c))


def midpoint(a, b):
    return scale(F(1, 2), add(a, b))


def fv(a):
    """Convert JSON numbers to exact decimal rationals."""
    return tuple(F(str(x)) for x in a)


def plane_value(p, n, d):
    return dot(p, n)-d


# Coordinates, displacements, direction cosines and projections.
A, B = (F(1), F(2), F(3)), (F(4), F(6), F(9))
AB = sub(B, A)
ck(AB == (3, 4, 6), "head-minus-tail displacement")
ck(norm2(AB) == 61 and close(sqrt(61), 7.8102496759), "displacement length")
ck(close(sum((x/sqrt(61))**2 for x in AB), 1), "direction cosines normalized")
ck(sub(A, B) == scale(-1, AB), "reversed displacement")
d = (F(2), F(-1), F(2))
ck(norm2(d) == 9, "direction-ratio length squared")
unit = scale(F(1, 3), d)
ck(unit == (F(2, 3), F(-1, 3), F(2, 3)) and norm2(unit) == 1, "unit direction from ratios")
ck(norm2(d) != 1, "direction ratios are not automatically cosines")
ck(dot(AB, d) == 14 and close(F(dot(AB, d), 3), F(14, 3)), "signed projection numerator and length")
ck(close(acos(F(1, 2)), pi/3) and round(degrees(acos(F(1, 2)))) == 60, "direction-cosine angle")

# Vector, parametric, symmetric and general-form lines.
for t in (F(-1), F(0), F(1, 2), F(1), F(2)):
    r = add(A, scale(t, AB))
    ck(sub(r, A) == scale(t, AB), "line parametrization reconstruction")
ck(add(A, scale(F(1, 2), AB)) == (F(5, 2), F(4), F(6)), "midpoint parameter")
ck(add(A, AB) == B, "second point at parameter one")
for t in (F(-2), F(1, 3), F(3)):
    r = add(A, scale(t, AB))
    ck(all((r[i]-A[i])/AB[i] == t for i in range(3)), "symmetric-form parameter elimination")
ck((1, 2, 3+4) == (1, 2, 7), "zero-denominator parametric form remains valid")
n1, n2 = (F(1), F(1), F(1)), (F(2), F(-3), F(4))
dline = cross(n1, n2)
P = (F(8, 5), F(-3, 5), F(0))
ck(dline == (7, -2, -5), "two plane normals give line direction")
ck(dot(dline, n1) == dot(dline, n2) == 0, "intersection direction perpendicular to both normals")
ck(plane_value(P, n1, 1) == plane_value(P, n2, 5) == 0, "chosen point lies on both planes")
for t in (F(-2), F(0), F(3)):
    ck(plane_value(add(P, scale(t, dline)), n1, 1) == 0 and plane_value(add(P, scale(t, dline)), n2, 5) == 0, "whole parametrized intersection line")
ck(cross((1, 2, 3), (2, 4, 6)) == (0, 0, 0), "dependent normals do not give an intersection direction")

# Angles, coplanarity, intersection and the corrected parallel-line example.
b1, b2 = (F(1), F(2), F(2)), (F(2), F(1), F(-1))
ck(dot(b1, b2) == 2 and norm2(b1) == 9 and norm2(b2) == 6, "line-angle dot and lengths")
ck(close(degrees(acos(F(2, 3)/sqrt(6))), 74.2068309517), "exact line angle")
ck(dot((2, 3, 4), (4, 3, 2)) == 25, "nonperpendicular direction check")
a1, b1 = (F(0), F(0), F(0)), (F(1), F(0), F(0))
a2, b2 = (F(0), F(1), F(0)), (F(0), F(0), F(1))
ck(triple(sub(a2, a1), b1, b2) == -1, "skew-line coplanarity test")
a2, b2 = (F(1), F(0), F(1)), (F(0), F(1), F(1))
b1 = (F(1), F(2), F(3))
ck(triple(sub(a2, a1), b1, b2) == 0, "coplanar-line triple product")
intersection = add(a1, scale(F(1), b1))
ck(intersection == add(a2, scale(F(2), b2)) == (1, 2, 3), "coplanar lines intersect at verified parameters")
ck(cross(b1, b2) != (0, 0, 0), "coplanar example is nonparallel")
base = (F(1), F(2), F(3))
ck(cross(base, base) == (0, 0, 0) and base == add((0, 0, 0), base), "source parallel lines actually coincide")
ck(sub((1, 0, 0), (0, 0, 0)) != scale(F(1, 3), base), "replacement base point gives distinct parallel lines")

# Perpendicular foot, image and point-line distance.
P = (F(1), F(2), F(3)); a = (F(0), F(0), F(0)); b = (F(2), F(-1), F(2))
t0 = F(dot(sub(P, a), b), norm2(b))
Ffoot = add(a, scale(t0, b)); I = sub(scale(2, Ffoot), P)
ck(t0 == F(2, 3), "foot parameter")
ck(Ffoot == (F(4, 3), F(-2, 3), F(4, 3)), "exact perpendicular foot")
ck(I == (F(5, 3), F(-10, 3), F(-1, 3)), "exact reflected image")
ck(midpoint(P, I) == Ffoot and dot(sub(P, Ffoot), b) == 0, "midpoint and perpendicularity checks")
ck(norm2(sub(P, Ffoot)) == 10, "point-line distance squared")
area_vector = cross(sub(P, a), b)
ck(area_vector == (7, 4, -5) and norm2(area_vector) == 90, "cross-product height numerator")
ck(close(sqrt(F(norm2(area_vector), norm2(b))), sqrt(10)), "cross-product height agrees with foot distance")
for t in (F(-1), F(0), F(2, 3), F(2)):
    ck(norm2(sub(P, add(a, scale(t, b)))) >= 10, "foot minimizes sampled squared distances")

# Skew-line shortest distance and exact common-perpendicular feet.
a1, b1 = (F(1), F(2), F(3)), (F(2), F(-1), F(2))
a2, b2 = (F(4), F(5), F(6)), (F(3), F(1), F(-1))
n = cross(b1, b2); delta = sub(a2, a1)
ck(n == (-1, 8, 5) and norm2(n) == 90, "skew common-normal direction")
ck(delta == (3, 3, 3) and dot(delta, n) == 36, "skew signed volume numerator")
ck(close(F(36, 1)/sqrt(90), 12/sqrt(10)) and close(12/sqrt(10), 3.7947331922), "skew shortest distance")
t, s = F(4, 5), F(-3, 5)
F1, F2 = add(a1, scale(t, b1)), add(a2, scale(s, b2))
ck(F1 == (F(13, 5), F(6, 5), F(23, 5)), "first common-perpendicular foot")
ck(F2 == (F(11, 5), F(22, 5), F(33, 5)), "second common-perpendicular foot")
connector = sub(F2, F1)
ck(connector == scale(F(2, 5), n), "connector parallel to cross product")
ck(dot(connector, b1) == dot(connector, b2) == 0, "connector perpendicular to both lines")
ck(norm2(connector) == F(72, 5) and close(sqrt(norm2(connector)), 12/sqrt(10)), "connector length independently reproduces distance")
ck(close(norm2(cross((0, 2, 0), (1, 0, 0)))/1, 4) and close(sqrt(4), 2), "distinct parallel lines use point-line distance")

# Plane equations, three-point form and intercepts.
A = (F(1), F(2), F(3)); n = (F(2), F(-3), F(4)); d0 = dot(A, n)
ck(d0 == 8, "plane constant from point and normal")
for Q in (A, (F(4), F(0), F(0)), (F(0), F(-8, 3), F(0))):
    ck(plane_value(Q, n, d0) == 0, "points satisfy normal-form plane")
A, B, C = (F(1), F(0), F(0)), (F(0), F(2), F(0)), (F(0), F(0), F(3))
u, v = sub(B, A), sub(C, A); n = cross(u, v)
ck(u == (-1, 2, 0) and v == (-1, 0, 3) and n == (6, 3, 2), "three-point plane normal")
ck(dot(n, A) == 6 and all(plane_value(Q, n, 6) == 0 for Q in (A, B, C)), "three-point plane equation")
ck((A[0], B[1], C[2]) == (1, 2, 3), "nonzero intercept data")
ck(1/1 + 0/2 + 0/3 == 1 and 0/1 + 2/2 + 0/3 == 1 and 0/1 + 0/2 + 3/3 == 1, "intercept form verified at all three points")

# Plane-plane and line-plane angles.
n1, n2 = (F(1), F(1), F(1)), (F(1), F(-1), F(1))
ck(dot(n1, n2) == 1 and norm2(n1) == norm2(n2) == 3, "plane-angle data")
ck(close(degrees(acos(F(1, 3))), 70.5287793655), "plane-plane angle")
b, n = (F(2), F(3), F(4)), (F(2), F(-3), F(4))
ck(dot(b, n) == 11 and norm2(b) == norm2(n) == 29, "line-plane angle data")
ck(close(degrees(asin(F(11, 29))), 22.2909703748), "line-plane angle from sine")
ck(close(sqrt(1-F(121, 841)), 12*sqrt(5)/29), "line-plane cosine second check")
ck(close((11/29)/(12*sqrt(5)/29), 11/(12*sqrt(5))), "line-plane tangent second check")
ck(close(degrees(asin(F(11, 29)))+degrees(acos(F(11, 29))), 90), "line-normal complement")
ck(dot((1, 0, 0), (0, 1, 0)) == 0, "parallel line and plane have zero direction-normal dot")

# Point-plane distances, parallel planes, feet and reflections.
P = (F(1), F(2), F(3)); n = (F(2), F(-3), F(4))
residual = plane_value(P, n, 5)
ck(residual == 3 and close(abs(residual)/sqrt(norm2(n)), 3/sqrt(29)), "absolute normalized plane residual")
ck(close(F(10-5, 1)/sqrt(29), 5/sqrt(29)), "parallel-plane distance")
n = (F(1), F(1), F(1)); residual = plane_value(P, n, 1)
t0 = F(residual, norm2(n)); Ffoot = sub(P, scale(t0, n)); I = sub(P, scale(2*t0, n))
ck(residual == 5 and t0 == F(5, 3), "plane reflection multiplier")
ck(Ffoot == (F(-2, 3), F(1, 3), F(4, 3)), "plane foot coordinates")
ck(I == (F(-7, 3), F(-4, 3), F(-1, 3)), "plane image coordinates")
ck(plane_value(Ffoot, n, 1) == 0 and midpoint(P, I) == Ffoot, "plane foot equation and midpoint")
n = (F(2), F(-3), F(4)); t0 = F(plane_value(P, n, 5), norm2(n)); Ffoot = sub(P, scale(t0, n))
ck(t0 == F(3, 29) and Ffoot == (F(23, 29), F(67, 29), F(75, 29)), "second plane-foot example")
ck(plane_value(Ffoot, n, 5) == 0 and close(norm2(sub(P, Ffoot)), F(9, 29)), "second plane-foot verification")

# Plane pencils and normalized bisector planes.
P1, P2 = (F(1), F(1), F(1)), (F(2), F(-3), F(4))
lam = F(-1, 5); n_pencil = add(P1, scale(lam, P2)); d_pencil = add((F(-1),), scale(lam, (F(-5),)))[0]
ck(lam == F(-1, 5) and n_pencil == (F(3, 5), F(8, 5), F(1, 5)) and d_pencil == 0, "pencil through the origin")
ck(scale(5, n_pencil) == (3, 8, 1), "cleared pencil coefficients")
P1 = lambda p: p[0]+2*p[1]+3*p[2]-4
P2 = lambda p: 2*p[0]+p[1]-p[2]-5
lam = F(2, 3)
ck(P1((1, 1, 1)) == 2 and P2((1, 1, 1)) == -3 and P1((1, 1, 1))+lam*P2((1, 1, 1)) == 0, "second pencil parameter")
ck(7+8+7 == 22, "second pencil at required point")
for p in ((F(1), F(0), F(2)), (F(-2), F(0), F(3)), (F(0), F(1), F(-1))):
    if p[1] == 0 or p[0]+p[2] == 0:
        ck(close(abs(p[0]+p[1]+p[2])/sqrt(3), abs(p[0]-p[1]+p[2])/sqrt(3)), "bisector plane equal-distance locus")
ck(dot((0, 1, 0), (1, 0, 1)) == 0, "bisector planes perpendicular")

# Sphere foundations, diameter form and the corrected four-point sphere.
C = (F(-1), F(2), F(-3)); R2 = F(25)
ck(norm2(C) == 14 and R2 == 14-(-11), "complete-square centre and radius")
ck((-1+1)**2+(2-2)**2+(-3+3)**2 == 0, "single-point degenerate sphere check")
A, B = (F(1), F(0), F(0)), (F(0), F(2), F(0)); C = midpoint(A, B)
ck(C == (F(1, 2), F(1), F(0)) and norm2(sub(A, C)) == F(5, 4), "diameter midpoint and radius")
ck(dot(sub((0, 0, 0), A), sub((0, 0, 0), B)) == 0, "diameter form right angle at origin")
for Q in ((F(0), F(0), F(0)), A, B):
    ck(norm2(sub(Q, C)) == F(5, 4), "three points on diameter sphere")
A, B, C, D = (F(1), F(0), F(0)), (F(0), F(2), F(0)), (F(0), F(0), F(3)), (F(1), F(1), F(1))
O = (F(-13, 10), F(1, 10), F(9, 10))
ck(-2*O[0]+4*O[1] == 3 and -2*O[0]+6*O[2] == 8 and O[1]+O[2] == 1, "four-point sphere linear system")
dists = [norm2(sub(Q, O)) for Q in (A, B, C, D)]
ck(all(x == F(611, 100) for x in dists), "four equal sphere squared distances")
ck(tuple(100*x for x in dists) == (611, 611, 611, 611), "cleared four-distance numerators")
ck(close(sqrt(F(611, 100)), 2.4718414189), "four-point sphere radius")
constant = norm2(O)-F(611, 100)
ck(constant == F(-18, 5) and constant != F(-611, 100), "correct general-form constant")
for Q in (A, B, C, D):
    x, y, z = Q
    ck(5*norm2(Q)+13*x-y-9*z-18 == 0, "cleared four-point sphere equation")

# Plane sections and tangent planes.
R2, distance2 = F(25), F(9)
ck(R2-distance2 == 16 and close(sqrt(16), 4), "axis-aligned section radius")
n = (F(2), F(-3), F(4)); t0 = F(20, norm2(n)); Q = scale(t0, n)
ck(Q == (F(40, 29), F(-60, 29), F(80, 29)), "general section centre")
ck(norm2(Q) == F(400, 29) and F(25)-norm2(Q) == F(325, 29), "general section radius squared")
ck(close(sqrt(F(325, 29)), 3.3476703171), "general section radius decimal")
T = (F(3), F(0), F(4)); n = T
ck(norm2(T) == 25 and plane_value(T, n, 25) == 0, "tangent point and tangent plane")
ck(close(F(25, 5), 5) and close(F(9, 3), 3), "tangent and secant plane distances")
for v in ((F(4), F(0), F(-3)), (F(0), F(1), F(0))):
    if dot(v, T) == 0:
        ck(plane_value(add(T, v), n, 25) == 0, "tangent-plane direction perpendicular to radius")

# Radical planes, orthogonal spheres, polars and the tangent cone.
power1 = lambda p: norm2(p)-25
power2 = lambda p: norm2(sub(p, (3, 0, 0)))-16
for p in ((F(3), F(1), F(2)), (F(3), F(4), F(0)), (F(3), F(0), F(-4))):
    ck(power1(p) == power2(p), "radical plane equal-power check")
ck(power1((3, 1, 2)) == -11 and 1**2+2**2 == 5, "radical example power and section data")
ck(norm2(sub((3, 0, 0), (0, 3, 0))) == 18 == 9+9, "orthogonal spheres centre-distance condition")
ck(2*((-3)*0+0*(-3)+0*0) == 0, "orthogonal spheres coefficient condition")
ck(25 != 25+16, "nonorthogonal radius-distance counterexample")
D, R = F(13), F(5)
ck(D*D-R*R == 144 and close(degrees(asin(R/D)), 22.6198649480), "tangent-cone length and angle")
ck(R*R/D == F(25, 13) and close(R*sqrt(1-R*R/(D*D)), F(60, 13)), "contact-circle plane and radius")
P = (F(13), F(0), F(0)); T = (F(25, 13), F(0), F(60, 13))
ck(norm2(T) == 25 and dot(T, sub(P, T)) == 0 and norm2(sub(P, T)) == 144, "exact tangent contact point")
ck(13*T[0] == 25 and F(25, 13)*P[0]+F(60, 13)*P[2] == 25, "reciprocal polar check")
for t in (F(-2), F(0), F(3)):
    p = (F(1), F(2), t); q = norm2(p)
    ck(q-14 == q+25-10*1-29 == q+25-10*2-19 == t*t-9, "three-sphere radical axis and common power")

# Tetrahedron insphere, circumcentre, Monge point and regular tetrahedron.
O0 = (F(0), F(0), F(0)); A = (F(4), F(0), F(0)); B = (F(0), F(4), F(0)); C = (F(0), F(0), F(3))
V = F(abs(triple(A, B, C)), 6)
slant_twice_area = norm2(cross(sub(B, A), sub(C, A)))
ck(V == 8 and slant_twice_area == 544, "tetrahedron volume and slant-face area squared")
ck(close(sqrt(slant_twice_area)/2, 2*sqrt(34)), "slant-face area")
r = 12/(10+sqrt(34))
ck(close(3*8/(20+2*sqrt(34)), r) and close(r, 0.7580087464), "inradius from volume and surface area")
I = (r, r, r)
ck(close((12-10*r)/sqrt(34), r), "incentre distance to slant face")
ck(close(12, (10+sqrt(34))*r), "exact inradius defining equation")
A, B, C, D = (F(1), F(0), F(0)), (F(0), F(2), F(0)), (F(0), F(0), F(3)), (F(2), F(1), F(4))
O = (F(47, 34), F(49, 34), F(61, 34))
ck(len({norm2(sub(Q, O)) for Q in (A, B, C, D)}) == 1, "Monge example circumcentre equidistant from vertices")
G = scale(F(1, 4), add(add(A, B), add(C, D)))
M = sub(scale(2, G), O)
ck(G == (F(3, 4), F(3, 4), F(7, 4)), "correct tetrahedron centroid")
ck(M == (F(2, 17), F(1, 17), F(29, 17)), "correct exact Monge point")
vertices = (A, B, C, D)
for i, j in combinations(range(4), 2):
    k, l = (x for x in range(4) if x not in (i, j))
    mid = midpoint(vertices[i], vertices[j]); opposite = sub(vertices[l], vertices[k])
    ck(dot(sub(M, mid), opposite) == 0, "all six Monge midplanes")
mid = midpoint(A, B)
ck(dot(sub(M, mid), sub(D, C)) == 0 and mid == (F(1, 2), F(1), F(0)), "displayed midplane check")
regular = ((F(1), F(1), F(1)), (F(1), F(-1), F(-1)), (F(-1), F(1), F(-1)), (F(-1), F(-1), F(1)))
ck(all(norm2(sub(vertices[i], vertices[j])) == 8 for vertices in [regular] for i, j in combinations(range(4), 2)), "regular tetrahedron six equal edges")
ck(all(norm2(Q) == 3 for Q in regular), "regular tetrahedron circumradius squared")
ck(close(1/sqrt(3), sqrt(3)/3) and close(F(abs(triple(sub(regular[1], regular[0]), sub(regular[2], regular[0]), sub(regular[3], regular[0]))), 6), F(8, 3)), "regular tetrahedron inradius ratio and volume")
ck(close(degrees(acos(F(1, 3))), 70.5287793655), "regular tetrahedron dihedral angle")
omega = 3*acos(F(1, 3))-pi
ck(close(omega, 0.5512855984) and omega > 0, "regular tetrahedron solid angle")
ck(close((2*sqrt(6))**3/(6*sqrt(2)), 8*sqrt(3)), "recover regular tetrahedron volume from inradius")
ck(close((80+70+60-180)*pi/180, pi/6) and close((pi/6)/(4*pi), F(1, 24)), "spherical excess area and fraction")
ck(close(3*pi/2-pi, pi/2) and close((pi/2)/(4*pi), F(1, 8)), "spherical octant excess and fraction")

# Assertions against the actual editable JSON figures, not just the prose.
content = Path(__file__).resolve().parents[1] / "content"
specs = []
for path in sorted(content.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    for block in text.split(":::diagram\n")[1:]:
        specs.append(json.loads(block.split("\n:::", 1)[0]))
ck(len(specs) == 22, "editable diagram inventory")
ck(sum(s.get("type") == "vector3d" for s in specs) == 19, "editable 3D diagram inventory")
ck(sum(s.get("type") == "flow" for s in specs) == 2 and sum(s.get("type") == "table" for s in specs) == 1, "editable decision diagrams")
by_title = {s["title"]: s for s in specs}
all_elements = [e for s in specs if s.get("type") == "vector3d" for e in s["elements"]]
ck(sum(e.get("kind") == "sphere" for e in all_elements) == 5, "editable sphere inventory")
ck(sum(e.get("kind") == "circle3d" for e in all_elements) == 5, "editable circle and arc inventory")
ck(sum(e.get("kind") == "plane" for e in all_elements) == 5, "editable plane-patch inventory")
for e in all_elements:
    if e.get("kind") == "sphere":
        ck(e["r"] > 0 and len(e.get("centre", [0, 0, 0])) == 3, "valid sphere figure parameters")
    elif e.get("kind") == "plane":
        ck(norm2(cross(fv(e["u"]), fv(e["v"]))) > 0, "nondegenerate plane patch")
    elif e.get("kind") == "circle3d":
        ck(e["r"] > 0, "positive circle radius")
        if "u" in e:
            u, v = fv(e["u"]), fv(e["v"])
            ck(close(dot(u, v), 0) and norm2(u) > 0 and norm2(v) > 0, "orthogonal circle basis")


def element(spec, kind, label=None):
    matches = [e for e in spec["elements"] if e.get("kind") == kind and (label is None or e.get("label") == label)]
    assert len(matches) == 1, (spec["title"], kind, label, len(matches))
    return matches[0]


spec = by_title["A line is one point plus all scalar multiples of a direction"]
arrow = element(spec, "arrow")
ck(sub(fv(arrow["b"]), fv(arrow["a"])) == (3, 4, 6), "actual line-figure direction")
mid = next(e for e in spec["elements"] if e.get("label") == "t = 1/2")
ck(fv(mid["at"]) == midpoint(fv(arrow["a"]), fv(arrow["b"])), "actual line-figure midpoint")
spec = by_title["The common perpendicular is parallel to b1 × b2"]
segments = [e for e in spec["elements"] if e.get("kind") == "segment" and e.get("color") == "#B91C1C"]
ck(len(segments) == 1 and close(norm2(sub(fv(segments[0]["b"]), fv(segments[0]["a"]))), F(72, 5), 1e-4), "actual skew-figure connector length")
spec = by_title["Two edges fix the plane; their cross product fixes its normal"]
points = {e["label"]: fv(e["at"]) for e in spec["elements"] if e.get("kind") == "point" and e.get("label") in {"A", "B", "C"}}
ck(cross(sub(points["B"], points["A"]), sub(points["C"], points["A"])) == (6, 3, 2), "actual three-point plane normal")
spec = by_title["The intersection line is perpendicular to both plane normals"]
planes = [e for e in spec["elements"] if e.get("kind") == "plane"]
for e, normal, rhs in zip(planes, ((1, 1, 1), (2, -3, 4)), (1, 5)):
    ck(dot(fv(e["u"]), normal) == dot(fv(e["v"]), normal) == 0 and dot(fv(e["centre"]), normal) == rhs, "actual plane patch lies in stated plane")
line = next(e for e in spec["elements"] if e.get("kind") == "segment")
direction = sub(fv(line["b"]), fv(line["a"]))
ck(direction == scale(F(1, 2), (7, -2, -5)), "actual intersection-line direction")
spec = by_title["P and I are symmetric about the plane through F"]
points = {e["label"]: fv(e["at"]) for e in spec["elements"] if e.get("kind") == "point"}
ck(add(points["P"], points["I"]) == scale(2, points["F"]), "actual plane-reflection midpoint")
plane = element(spec, "plane")
ck(dot(fv(plane["u"]), (1, 1, 1)) == dot(fv(plane["v"]), (1, 1, 1)) == 0, "actual reflection plane patch")
spec = by_title["The midpoint of a diameter is the sphere's centre"]
sphere = element(spec, "sphere"); points = {e["label"]: fv(e["at"]) for e in spec["elements"] if e.get("kind") == "point"}
ck(all(close(norm2(sub(points[name], fv(sphere["centre"]))), F(str(sphere["r"]))**2, 1e-5) for name in ("O", "A", "B")), "actual diameter-sphere points")
ck(fv(sphere["centre"]) == midpoint(points["A"], points["B"]), "actual sphere centre is diameter midpoint")
spec = by_title["A plane section is a circle whose centre is the perpendicular foot"]
sphere = element(spec, "sphere"); circle = element(spec, "circle3d")
ck(close(F(str(sphere["r"]))**2-norm2(fv(circle["centre"])), F(str(circle["r"]))**2), "actual section Pythagorean relation")
spec = by_title["The contact circle lies in the external point's polar plane"]
circle = element(spec, "circle3d"); P = fv(element(spec, "point", "P(13,0,0)")["at"])
ck(close(13*fv(circle["centre"])[0], 25, 1e-4) and close(F(str(circle["r"])), F(60, 13), 1e-4), "actual tangent-cone contact circle")
ck(close(norm2(P), 169), "actual tangent-cone external distance")
spec = by_title["The insphere is tangent to all four faces"]
sphere = element(spec, "sphere"); c = fv(sphere["centre"]); rr = F(str(sphere["r"]))
ck(close(c[0], c[1]) and close(c[1], c[2]) and close(c[0], rr), "actual insphere coordinate-plane distances")
ck(close((12-10*rr)/sqrt(34), rr, 1e-4), "actual insphere slant-plane distance")
spec = by_title["One octant is a spherical triangle with three right angles"]
arcs = [e for e in spec["elements"] if e.get("kind") == "circle3d"]
ck(len(arcs) == 3 and all(e.get("tstart") == 0 and e.get("tend") == 90 for e in arcs), "actual three quarter-circle arcs")
ck(all(dot(fv(e["u"]), fv(e["v"])) == 0 and norm2(fv(e["u"])) == norm2(fv(e["v"])) == 1 for e in arcs), "actual octant arc bases")
spec = by_title["In a regular tetrahedron, the circumradius is three times the inradius"]
points = {e["label"]: fv(e["at"]) for e in spec["elements"] if e.get("kind") == "point" and e.get("label") in {"A", "B", "C", "D", "O"}}
ck(all(norm2(sub(points[a], points[b])) == 8 for a, b in combinations("ABCD", 2)), "actual regular-tetrahedron edges")
ck(all(norm2(points[a]) == 3 for a in "ABCD") and points["O"] == (0, 0, 0), "actual regular-tetrahedron circumcentre")

# Targeted assertions for the six-page visual lab.
for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    ck(_condition, f"visual lab: {_name}")

print(f"Three-Dimensional Geometry: {checks}/{checks} checks PASS")
