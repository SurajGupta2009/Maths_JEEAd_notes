#!/usr/bin/env python3
"""Independent exact, numerical and editable-figure checks for Chapter 15 vectors."""
from pathlib import Path
from fractions import Fraction as F
from math import acos, degrees, isclose, sqrt
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


def close(a, b, tol=1e-10):
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


def det2(a, b):
    return a[0]*b[1]-a[1]*b[0]


def twice_area(a, b, c):
    return det2(sub(b, a), sub(c, a))


def midpoint(a, b):
    return scale(F(1, 2), add(a, b))


# Components, direction cosines, displacement and translation.
a = (F(2), F(-1), F(2))
ck(norm2(a) == 9, "magnitude squared of (2,-1,2)")
unit = scale(F(1, 3), a)
ck(unit == (F(2, 3), F(-1, 3), F(2, 3)) and norm2(unit) == 1, "unit vector and direction cosines")
ck(a != unit and norm2(a) != 1, "direction ratios are not direction cosines")
A, B = (F(1), F(-2), F(3)), (F(4), F(2), F(-1))
AB = sub(B, A)
ck(AB == (3, 4, -4) and norm2(AB) == 41, "head-minus-tail displacement")
ck(sub(A, B) == scale(-1, AB), "reversing a displacement")
ck(sub((6, 2), (3, 0)) == sub((3, 2), (0, 0)) == (3, 2), "free-vector translation invariance")
ck(norm2((0, 0, 0)) == 0, "zero-vector magnitude")

# Addition, scalar multiplication and the exact structural identities.
a, b = (F(3), F(1)), (F(-1), F(2))
ck(add(a, b) == (2, 3) and sub(a, b) == (4, -1), "component addition and subtraction")
ck(sub(scale(2, a), scale(3, b)) == (9, -4), "linear combination example")
ck(norm2(add(a, b))+norm2(sub(a, b)) == 30 == 2*(norm2(a)+norm2(b)), "parallelogram-law numerical example")
ck(scale(2, (2, 1)) == (4, 2) and scale(-1, (2, 1)) == (-2, -1), "scalar multiplication diagram vectors")
ck(close(sqrt(norm2(scale(2, (2, 1)))), 2*sqrt(5)), "positive scalar scales magnitude")
ck(close(sqrt(norm2(scale(-1, (2, 1)))), sqrt(5)), "negative scalar preserves magnitude")

pairs = [
    ((F(1), F(2), F(3)), (F(4), F(5), F(6))),
    ((F(3), F(-1), F(2)), (F(1), F(4), F(-2))),
    ((F(2), F(-1), F(2)), (F(1), F(0), F(-1))),
    ((F(0), F(2), F(-1)), (F(3), F(1), F(4))),
    ((F(2), F(0), F(0)), (F(1), F(2), F(0))),
    ((F(1), F(1), F(0)), (F(1), F(0), F(1))),
]
for u, v in pairs:
    ck(norm2(add(u, v)) == norm2(u)+2*dot(u, v)+norm2(v), "plus-expansion identity")
    ck(norm2(add(u, v))+norm2(sub(u, v)) == 2*(norm2(u)+norm2(v)), "parallelogram identity")
    ck(cross(u, v) == scale(-1, cross(v, u)), "cross-product anti-commutativity")
    ck(dot(cross(u, v), u) == 0 and dot(cross(u, v), v) == 0, "cross-product perpendicularities")
    ck(norm2(cross(u, v))+dot(u, v)**2 == norm2(u)*norm2(v), "Lagrange identity")
    nu, nv = sqrt(norm2(u)), sqrt(norm2(v))
    nplus, nminus = sqrt(norm2(add(u, v))), sqrt(norm2(sub(u, v)))
    ck(abs(nu-nv)-1e-10 <= nplus <= nu+nv+1e-10 and abs(nu-nv)-1e-10 <= nminus <= nu+nv+1e-10, "triangle inequalities for both diagonals")

# Internal/external section formulas, centroids and medians.
A, B = (F(1), F(0), F(0)), (F(4), F(5), F(6))
P = scale(F(1, 5), add(scale(3, A), scale(2, B)))
ck(P == (F(11, 5), F(2), F(12, 5)), "internal section coordinates")
ck(sub(P, A) == scale(F(2, 3), sub(B, P)), "internal section directed ratio")
ck(P == add(A, scale(F(2, 5), sub(B, A))), "section formula as affine interpolation")
A, B = (F(1), F(-1), F(2)), (F(3), F(3), F(-2))
P = sub(scale(2, B), A)
ck(P == (5, 7, -6), "external section coordinates")
ck(norm2(sub(P, A)) == 4*norm2(sub(B, P)), "external section length ratio")
ck(P == add(A, scale(2, sub(B, A))), "external point beyond B")
A2, B2, C2 = (F(0), F(0)), (F(6), F(0)), (F(2), F(4))
G = scale(F(1, 3), add(add(A2, B2), C2))
D = midpoint(B2, C2)
ck(G == (F(8, 3), F(4, 3)) and D == (4, 2), "triangle centroid and median midpoint")
ck(sub(G, A2) == scale(2, sub(D, G)), "centroid divides median two to one")
ck(twice_area(A2, B2, D) == twice_area(A2, D, C2) == 12, "median gives equal areas")
T = (F(1), F(1), F(1))
ck(scale(F(1, 4), add(add(A, B), add((0, 0, 0), T))) == (F(5, 4), F(3, 4), F(1, 4)), "tetrahedron centroid arithmetic")

# Dot products, angles, Cauchy-Schwarz and projections.
a, b = (F(1), F(2), F(2)), (F(2), F(-2), F(1))
ck(dot(a, b) == 0 and norm2(a) == norm2(b) == 9, "exact perpendicular pair")
a2, b2 = (F(3), F(1)), (F(1), F(2))
ck(dot(a2, b2) == 5 and norm2(a2) == 10 and norm2(b2) == 5, "two-dimensional angle data")
ck(close(dot(a2, b2)/sqrt(norm2(a2)*norm2(b2)), 1/sqrt(2)), "exact 45-degree cosine")
a, b = (F(1), F(2), F(3)), (F(4), F(5), F(6))
ck(dot(a, b) == 32 and norm2(a) == 14 and norm2(b) == 77, "numerical angle components")
ck(dot(a, b)**2 == 1024 < 1078 == norm2(a)*norm2(b), "strict Cauchy-Schwarz example")
ck(round(degrees(acos(32/sqrt(1078))), 2) == 12.93, "numerical angle in degrees")
for u, v in pairs:
    ck(dot(u, v)**2 <= norm2(u)*norm2(v), "Cauchy-Schwarz over vector family")
u = (F(1), F(2), F(3))
ck(dot(u, scale(2, u))**2 == norm2(u)*norm2(scale(2, u)), "Cauchy-Schwarz equality under dependence")

a, b = (F(2), F(2), F(1)), (F(1), F(2), F(2))
projection = scale(F(8, 9), b)
rejection = sub(a, projection)
ck(projection == (F(8, 9), F(16, 9), F(16, 9)), "3D vector projection")
ck(rejection == (F(10, 9), F(2, 9), F(-7, 9)), "3D rejection")
ck(add(projection, rejection) == a and dot(rejection, b) == 0, "projection reconstruction and perpendicularity")
ck(close(dot(a, b)/sqrt(norm2(b)), F(8, 3)), "signed scalar projection")
ck(norm2(projection)+norm2(rejection) == norm2(a), "projection Pythagorean identity")
ck(add((1, 0, 0), (0, 1, 0)) == (1, 1, 0) and sub((1, 0, 0), (0, 1, 0)) == (1, -1, 0), "unit-vector angle bisectors")
ck(dot((1, 1, 0), (1, -1, 0)) == 0, "internal and external bisectors perpendicular")
ck(dot((3, 4, 5), (1, 0, 2)) == 13, "work as a dot product")
ck(scale(F(dot(a, b), norm2(b)), b) != scale(F(dot(a, b), norm2(a)), a), "projection onto different directions differs")

# Cross products, oriented area and the angle-bisector theorem.
a, b = (F(1), F(2), F(3)), (F(4), F(5), F(6))
n = cross(a, b)
ck(n == (-3, 6, -3) and cross(b, a) == (3, -6, 3), "cross-product components and order")
ck(dot(n, a) == dot(n, b) == 0 and norm2(n) == 54, "cross-product checks and area squared")
ck(close(norm2(scale(1/sqrt(6), (-1, 2, -1))), 1), "unit normal from cross product")
u, v = (F(3), F(-1), F(2)), (F(1), F(4), F(-2))
ck(cross(u, v) == (-6, 8, 13) and dot(u, v) == -5, "second Lagrange example")
ck(norm2(cross(u, v)) == 269 and 269+25 == 294 == norm2(u)*norm2(v), "second Lagrange numerical identity")
ck(close(dot(u, v)/sqrt(norm2(u)*norm2(v)), -5/(7*sqrt(6))), "obtuse-angle cosine")
ck(close(F(269, 294), 1-F(25, 294)), "sine-squared from Lagrange")
ck(cross((1, 0, 0), (0, 1, 0)) == (0, 0, 1), "right-handed basis orientation")
ck(cross((1, 2, 3), (2, 4, 6)) == (0, 0, 0), "parallel vectors have zero cross product")
ck(cross(a, add(b, u)) == add(cross(a, b), cross(a, u)), "cross-product distributivity")

A, B, C = (F(1), F(0), F(0)), (F(0), F(2), F(0)), (F(0), F(0), F(3))
u, v = sub(B, A), sub(C, A)
ck(u == (-1, 2, 0) and v == (-1, 0, 3) and cross(u, v) == (6, 3, 2), "3D triangle edge and normal vectors")
ck(norm2(cross(u, v)) == 49, "3D parallelogram area is seven")
ck(scale(F(1, 2), cross(u, v)) == (3, F(3, 2), 1), "oriented vector area of ordered triangle")
for u, v in pairs:
    ck(cross(add(u, v), sub(u, v)) == scale(-2, cross(u, v)), "diagonal parallelogram area identity")
A0, B0, C0 = (F(0), F(0)), (F(4), F(0)), (F(0), F(3))
D0 = scale(F(1, 7), add(scale(3, B0), scale(4, C0)))
ck(D0 == (F(12, 7), F(12, 7)) and sub(D0, B0) == scale(F(4, 3), sub(C0, D0)), "angle-bisector theorem section weights")
ck(det2(D0, (1, 1)) == 0, "angle bisector follows sum of unit directions")

# Scalar triple products, permutations, coplanarity and tetrahedra.
a, b, c = (F(1), F(2), F(3)), (F(4), F(5), F(6)), (F(-1), F(0), F(2))
ck(cross(b, c) == (10, -14, 5) and triple(a, b, c) == -3, "signed triple-product example")
ck(triple(b, c, a) == triple(c, a, b) == -3 and triple(b, a, c) == 3, "triple-product permutation signs")
ck(triple(a, b, c) == dot(cross(a, b), c), "two scalar-triple-product forms")
A, B, C, D = (F(1), F(2), F(3)), (F(4), F(5), F(6)), (F(-1), F(0), F(2)), (F(2), F(-1), F(4))
u, v, w = sub(B, A), sub(C, A), sub(D, A)
ck((u, v, w) == ((3, 3, 3), (-2, -2, -1), (1, -3, 1)), "four-point edge vectors")
ck(cross(v, w) == (-5, 1, 8) and triple(u, v, w) == 12, "four-point noncoplanarity test")
ck(F(abs(triple(u, v, w)), 6) == 2, "tetrahedron volume from four-point test")
for lam in (F(-2), F(0), F(1), F(2), F(5)):
    cc = (F(-1), F(0), lam)
    ck(cross(b, cc) == (5*lam, -6-4*lam, 5), "parameter cross product")
    ck(triple(a, b, cc) == 3*(1-lam), "parameter triple product")
ck(triple(a, b, (-1, 0, 1)) == 0 and triple(a, b, (-1, 0, 2)) == -3, "coplanar and noncoplanar parameter values")
ck(triple(a, a, c) == 0 and triple(a, b, (0, 0, 0)) == 0, "repeated and zero factors imply dependence")
ck(triple((2, 0, 0), (1, 2, 0), (1, 1, 2)) == 8 and norm2(cross((2, 0, 0), (1, 2, 0))) == 16, "volume base area and height figure")

A, B, C, D = (F(1), F(0), F(0)), (F(0), F(2), F(0)), (F(0), F(0), F(3)), (F(1), F(1), F(1))
u, v, w = sub(A, D), sub(B, D), sub(C, D)
ck((u, v, w) == ((0, -1, -1), (-1, 1, -1), (-1, -1, 2)), "tetrahedron edges from D")
ck(cross(v, w) == (1, 3, 2) and triple(u, v, w) == -5, "tetrahedron signed triple product")
ck(F(abs(triple(u, v, w)), 6) == F(5, 6), "tetrahedron exact volume")
G4 = scale(F(1, 4), add(add(A, B), add(C, D)))
ck(G4 == (F(1, 2), F(3, 4), F(1)), "tetrahedron exact centroid")
ck(abs(triple(sub(B, A), sub(C, A), sub(D, A))) == abs(triple(u, v, w)) == 5, "volume independent of common-tail choice")

# Vector triple products, Jacobi and the scalar quadruple product.
a, b, c = (F(7), F(8), F(9)), (F(1), F(2), F(3)), (F(4), F(5), F(6))
ck((dot(a, c), dot(a, b), dot(b, c)) == (122, 50, 32), "vector-triple-product dot data")
left1 = cross(a, cross(b, c))
left2 = cross(cross(a, b), c)
ck(left1 == (-78, -6, 66) and left2 == (-102, -12, 78), "two direct vector triple products")
ck(left1 == sub(scale(dot(a, c), b), scale(dot(a, b), c)), "BAC-CAB numerical identity")
ck(left2 == sub(scale(dot(a, c), b), scale(dot(b, c), a)), "other grouping numerical identity")
ck(left1 != left2, "cross product is not associative in general")
ck(add(add(cross(a, cross(b, c)), cross(b, cross(c, a))), cross(c, cross(a, b))) == (0, 0, 0), "Jacobi numerical cancellation")
triples = [
    ((F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1))),
    ((F(1), F(2), F(3)), (F(4), F(5), F(6)), (F(-1), F(0), F(2))),
    ((F(2), F(-1), F(0)), (F(1), F(3), F(2)), (F(-2), F(1), F(4))),
    ((F(0), F(2), F(1)), (F(3), F(0), F(-1)), (F(2), F(2), F(2))),
    ((F(1), F(1), F(0)), (F(1), F(0), F(1)), (F(0), F(1), F(1))),
]
for x, y, z in triples:
    ck(cross(x, cross(y, z)) == sub(scale(dot(x, z), y), scale(dot(x, y), z)), "BAC-CAB identity family")
    ck(cross(cross(x, y), z) == sub(scale(dot(x, z), y), scale(dot(y, z), x)), "second triple-product identity family")
    ck(add(add(cross(x, cross(y, z)), cross(y, cross(z, x))), cross(z, cross(x, y))) == (0, 0, 0), "Jacobi identity family")
    ck(triple(x, y, z) == triple(y, z, x) == -triple(y, x, z), "scalar triple permutation family")
    d = (F(2), F(-1), F(3))
    ck(dot(cross(x, y), cross(z, d)) == dot(x, z)*dot(y, d)-dot(x, d)*dot(y, z), "scalar quadruple-product family")
a, b, c, d = (F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(1), F(1), F(0)), (F(0), F(1), F(1))
ck(cross(c, d) == (1, -1, 1) and dot(cross(a, b), cross(c, d)) == 1, "scalar quadruple direct example")
ck(dot(a, c)*dot(b, d)-dot(a, d)*dot(b, c) == 1, "scalar quadruple determinant example")

# Barycentric coordinates, Ceva, Routh and exact intersections.
A, B, C, P = (F(0), F(0)), (F(4), F(0)), (F(0), F(3)), (F(1), F(1))
weights = (F(5, 12), F(1, 4), F(1, 3))
reconstructed = add(add(scale(weights[0], A), scale(weights[1], B)), scale(weights[2], C))
ck(sum(weights) == 1 and reconstructed == P, "normalized barycentric reconstruction")
ck(tuple(12*w for w in weights) == (5, 3, 4), "unnormalized barycentric coordinates")
ck(twice_area(A, B, C) == 12 and twice_area(P, B, C) == 5, "barycentric total and first subtriangle area")
ck(tuple(F(twice_area(*args), 12) for args in [(P, B, C), (P, C, A), (P, A, B)]) == weights, "all barycentric area ratios")
x, y, z = F(2), F(3), F(1, 6)
ck(x*y*z == 1, "Ceva concurrent product")
x, y, z = F(2), F(1, 2), F(3)
factors = (x*y+x+1, y*z+y+1, z*x+z+1)
ck(x*y*z == 3 and factors == (4, 3, 10), "Routh cyclic denominator factors")
routh = F((x*y*z-1)**2, factors[0]*factors[1]*factors[2])
ck(routh == F(1, 30) and routh != F(1, 20), "corrected Routh area ratio")
A, B, C = (F(0), F(0)), (F(5), F(0)), (F(1), F(4))
P, Q, R = (F(7, 4), F(2)), (F(17, 6), F(4, 3)), (F(21, 10), F(12, 5))
X, Y, Z = (F(7, 3), F(8, 3)), (F(2, 3), F(8, 3)), (F(15, 4), F(0))
ck(det2(sub(C, B), sub(X, B)) == 0 and det2(sub(A, C), sub(Y, C)) == 0 and det2(sub(B, A), sub(Z, A)) == 0, "Routh points on their assigned sides")
collinear = lambda p, u, v: det2(sub(v, u), sub(p, u)) == 0
ck(collinear(P, A, X) and collinear(P, B, Y) and collinear(Q, B, Y) and collinear(Q, C, Z) and collinear(R, C, Z) and collinear(R, A, X), "Routh pairwise cevian intersections")
ck(F(twice_area(P, Q, R), twice_area(A, B, C)) == routh, "Routh ratio from direct intersections")
ck(twice_area(A, B, C) == 20 and twice_area(P, Q, R) == F(2, 3), "Routh absolute areas")

# Varignon, the Euler line and the invalid 3D source counterexample.
A, B, C, D = (F(0), F(0)), (F(5), F(1)), (F(4), F(4)), (F(-1), F(3))
P, Q, R, S = midpoint(A, B), midpoint(B, C), midpoint(C, D), midpoint(D, A)
ck(sub(Q, P) == sub(R, S) == scale(F(1, 2), sub(C, A)), "Varignon opposite sides")
ck(sub(R, Q) == sub(S, P) == scale(F(1, 2), sub(D, B)), "Varignon other opposite sides")
A, B, C = (F(5), F(0)), (F(0), F(5)), (F(-4), F(-3))
H = add(add(A, B), C)
G = scale(F(1, 3), H)
ck(H == (1, 2) and G == (F(1, 3), F(2, 3)), "Euler-line H and G coordinates")
ck(norm2(A) == norm2(B) == norm2(C) == 25, "Euler example circumcircle")
ck(dot(sub(H, A), sub(C, B)) == 0 and dot(sub(H, B), sub(A, C)) == 0 and dot(sub(H, C), sub(B, A)) == 0, "all three Euler-example altitudes")
ck(norm2(G) == F(5, 9) and norm2(sub(H, G)) == F(20, 9) == 4*norm2(G), "Euler OG to GH ratio")
O = (F(2), F(-1))
At, Bt, Ct = add(A, O), add(B, O), add(C, O)
Ht = sub(add(add(At, Bt), Ct), scale(2, O))
Gt = scale(F(1, 3), add(add(At, Bt), Ct))
ck(Ht == add(H, O) and sub(Gt, O) == scale(F(1, 3), sub(Ht, O)), "translated circumcentre formula")
A3, B3, C3 = (F(2), F(0), F(0)), (F(0), F(2), F(0)), (F(1), F(1), sqrt(2))
ck(all(norm2(V) == 4 and V[0]+V[1] == 2 for V in (A3, B3, C3)) and 0 != 2, "source 3D circumcentre rejected: origin absent from triangle plane")

# Assertions against the actual editable JSON figures, not just prose examples.
content = Path(__file__).resolve().parents[1] / "content"
specs = []
for path in sorted(content.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    for block in text.split(":::diagram\n")[1:]:
        specs.append(json.loads(block.split("\n:::", 1)[0]))
ck(len(specs) == 22, "editable diagram inventory")
ck(sum(s.get("type") == "vector3d" for s in specs) == 6, "editable 3D diagram inventory")
by_title = {s["title"]: s for s in specs}


def element(spec, kind, label=None):
    matches = [e for e in spec["elements"] if e.get("kind") == kind and (label is None or e.get("label") == label)]
    assert len(matches) == 1, (spec["title"], kind, label, len(matches))
    return matches[0]


def arrow_delta(e):
    return sub(tuple(e["b"]), tuple(e["a"]))


spec = by_title["A free vector can be translated without changing it"]
arrows = [e for e in spec["elements"] if e.get("kind") == "arrow"]
ck(arrow_delta(arrows[0]) == arrow_delta(arrows[1]) == (3, 2), "actual free-vector figure translations")
spec = by_title["AP:PB = 2:1 means P is two-thirds of the way"]
Af = tuple(element(spec, "point", "A")["at"]); Bf = tuple(element(spec, "point", "B")["at"])
Pf = tuple(next(e for e in spec["elements"] if e.get("kind") == "point" and str(e.get("label", "")).startswith("P ="))["at"])
ck(Pf == scale(F(1, 3), add(Af, scale(2, Bf))), "actual section-figure point")
spec = by_title["The centroid lies two-thirds along every median"]
Gf = tuple(element(spec, "point", "G")["at"])
ck(close(Gf[0], F(8, 3), 1e-4) and close(Gf[1], F(4, 3), 1e-4), "actual centroid-figure rounded coordinate")
spec = by_title["The cross product is normal to the spanned plane"]
uf = arrow_delta(element(spec, "arrow", "u")); vf = arrow_delta(element(spec, "arrow", "v")); nf = arrow_delta(element(spec, "arrow", "u × v"))
ck(cross(uf, vf) == nf == (0, 0, 6), "actual cross-product figure normal")
spec = by_title["The diagonal halves the edge parallelogram"]
Af = tuple(element(spec, "point", "A")["at"]); Bf = tuple(element(spec, "point", "B")["at"]); Cf = tuple(element(spec, "point", "C")["at"])
uf = arrow_delta(element(spec, "arrow", "u = B-A")); vf = arrow_delta(element(spec, "arrow", "v = C-A"))
ck(uf == sub(Bf, Af) and vf == sub(Cf, Af) and cross(uf, vf) == (6, 3, 2), "actual 3D triangle-figure edges")
spec = by_title["Volume = base area × perpendicular height"]
para = element(spec, "parallelepiped")
ck(triple(tuple(para["u"]), tuple(para["v"]), tuple(para["w"])) == 8, "actual parallelepiped-figure volume")
spec = by_title["Use three edges from one tetrahedron vertex"]
points = {e["label"]: tuple(e["at"]) for e in spec["elements"] if e.get("kind") == "point"}
ck(abs(triple(sub(points["A"], points["D"]), sub(points["B"], points["D"]), sub(points["C"], points["D"]))) == 5, "actual tetrahedron-figure volume numerator")
spec = by_title["Signed triple product -2 means volume 2"]
para = element(spec, "parallelepiped")
ck(triple(tuple(para["u"]), tuple(para["v"]), tuple(para["w"])) == -2, "actual signed-volume figure")
spec = by_title["Coplanar edges collapse the volume to zero"]
uf = arrow_delta(element(spec, "arrow", "u")); vf = arrow_delta(element(spec, "arrow", "v"))
wf = arrow_delta(element(spec, "arrow", "w: triple = 0")); wpf = arrow_delta(element(spec, "arrow", "w': triple = 1"))
ck(triple(uf, vf, wf) == 0 and triple(uf, vf, wpf) == 1, "actual dependence-figure triple products")
spec = by_title["The three cevians bound the central triangle PQR"]
coords = {e["label"]: tuple(e["at"]) for e in spec["elements"] if e.get("kind") == "point" and e.get("label") in {"A", "B", "C", "P", "Q", "R"}}
expected = {"A": (F(0), F(0)), "B": (F(5), F(0)), "C": (F(1), F(4)), "P": (F(7, 4), F(2)), "Q": (F(17, 6), F(4, 3)), "R": (F(21, 10), F(12, 5))}
ck(all(all(close(coords[name][i], expected[name][i], 1e-4) for i in range(2)) for name in expected), "actual Routh-figure rounded intersections")
ck(close(twice_area(coords["P"], coords["Q"], coords["R"])/twice_area(coords["A"], coords["B"], coords["C"]), routh, 1e-4), "actual Routh-figure area ratio")
spec = by_title["O, G and H lie on one Euler line"]
coords = {e["label"]: tuple(e["at"]) for e in spec["elements"] if e.get("kind") == "point"}
ck(close(coords["G"][0], F(1, 3), 1e-4) and close(coords["G"][1], F(2, 3), 1e-4), "actual Euler-figure centroid")
ck(all(norm2(coords[name]) == 25 for name in ("A(5,0)", "B(0,5)", "C(-4,-3)")), "actual Euler-figure circumcircle")
ck(dot(sub(coords["H(1,2)"], coords["A(5,0)"]), sub(coords["C(-4,-3)"], coords["B(0,5)"])) == 0, "actual Euler-figure altitude")

# Targeted assertions for the visual-method lesson.
for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    ck(_condition, f"visual lesson: {_name}")

print(f"Vectors: {checks}/{checks} checks PASS")
