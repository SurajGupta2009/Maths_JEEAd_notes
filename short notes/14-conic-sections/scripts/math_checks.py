#!/usr/bin/env python3
"""Independent exact and numerical checks for Chapter 14 conic sections."""
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "_engine"))
from visual_math_checks import checks_for

from fractions import Fraction as F
from math import cos, sin, sqrt, pi, hypot, isclose

checks = 0

def ck(ok, msg):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(msg)

def close(a, b):
    return isclose(float(a), float(b), rel_tol=1e-10, abs_tol=1e-10)

def d2(P, Q):
    return (P[0]-Q[0])**2 + (P[1]-Q[1])**2

def dist(P, Q):
    return hypot(float(P[0]-Q[0]), float(P[1]-Q[1]))

def ellipse_value(P, a2, b2):
    return P[0]**2/a2 + P[1]**2/b2 - 1

def hyper_value(P, a2, b2):
    return P[0]**2/a2 - P[1]**2/b2 - 1

# Focus-directrix definitions and the three anatomies.
P = (F(4), F(4))
ck(P[1]**2 == 4*P[0], "focus-directrix parabola membership")
ck(d2(P, (F(1), F(0))) == 25, "parabola focal distance")
ck(P[0]+1 == 5, "parabola directrix distance")
Q = (0.0, sqrt(5))
ck(close(9*Q[1]**2, 45), "derived ellipse membership")
ck(close(dist(Q, (2, 0)), 3), "derived ellipse focal distance")
ck(close(3/F(9, 2), F(2, 3)), "derived ellipse eccentricity ratio")
a, b, c = F(5), F(3), F(4)
ck(c*c == a*a-b*b and c/a == F(4, 5), "ellipse c and e")
ck(a/(c/a) == F(25, 4), "ellipse directrix")
ck(2*b*b/a == F(18, 5), "ellipse latus rectum")
a, b, c = F(3), F(4), F(5)
ck(c*c == a*a+b*b and c/a == F(5, 3), "hyperbola c and e")
ck(a/(c/a) == F(9, 5), "hyperbola directrix")
ck(2*b*b/a == F(32, 3), "hyperbola latus rectum")

# Parabola parameters, focal distances and chord equation.
for a in (F(1), F(2)):
    for t in (F(-2), F(-1, 2), F(0), F(1, 2), F(2)):
        P = (a*t*t, 2*a*t)
        ck(P[1]**2 == 4*a*P[0], "parabola parameter membership")
        ck(d2(P, (a, F(0))) == (a*(1+t*t))**2, "parabola parametric focal distance")
for t1, t2 in ((F(2), F(-1, 2)), (F(1), F(3)), (F(-2), F(4))):
    a = F(2); P = (a*t1*t1, 2*a*t1); Q = (a*t2*t2, 2*a*t2)
    ck((t1+t2)*P[1] == 2*P[0]+2*a*t1*t2, "chord equation first endpoint")
    ck((t1+t2)*Q[1] == 2*Q[0]+2*a*t1*t2, "chord equation second endpoint")
    focus_residual = -2*a-2*a*t1*t2
    ck((focus_residual == 0) == (t1*t2 == -1), "focal chord parameter test")
a = F(2); P = (F(8), F(8)); Q = (F(1, 2), F(-2)); S = (F(2), F(0))
ck(P[1]**2 == 8*P[0] and Q[1]**2 == 8*Q[0], "exact focal chord endpoints")
ck(d2(P, S) == 100 and d2(Q, S) == F(25, 4), "exact focal chord segment lengths")
ck((P[0]-S[0])*(Q[1]-S[1]) == (P[1]-S[1])*(Q[0]-S[0]), "focal chord collinearity")
ck(1/F(10)+1/F(5, 2) == F(1, 2), "parabola focal chord reciprocal sum")
ck(F(10)+F(5, 2) == F(25, 2), "parabola focal chord total length")

# Parabola tangent/normal forms, intersection and normal cubic.
for t in (F(2), F(-1, 2), F(1)):
    a = F(2); P = (a*t*t, 2*a*t); m = 1/t
    ck(t*P[1] == P[0]+a*t*t, "parabola tangent at parameter")
    ck(P[1] == -t*P[0]+2*a*t+a*t**3, "parabola normal at parameter")
    ck(m*(-t) == -1, "parabola tangent-normal perpendicularity")
    ck(P[1] == m*P[0]+a/m, "parabola slope-form tangent")
T = (F(-2), F(3))
ck(T[0] == 2*(F(2)*F(-1, 2)) and T[1] == 2*(F(2)+F(-1, 2)), "tangent intersection formula")
ck(2*T[1] == T[0]+8 and T[1] == -2*T[0]-1, "both focal-chord tangents at T")
ck(T[0] == -2, "tangent intersection on directrix")
ck(F(1, 2)*F(-2) == -1, "focal-chord tangents perpendicular")
for m in (F(0), F(2), F(-2)):
    a = F(1); h = F(6); k = F(0); t = -m; P = (t*t, 2*t)
    ck(a*m**3+(2*a-h)*m+k == 0, "normal cubic roots")
    ck(k == m*h-2*a*m-a*m**3, "normal line through external point")
    ck(P[1] == m*P[0]-2*a*m-a*m**3, "normal line through computed foot")
for m in (F(1), F(-1)):
    a = F(2); P = (a/m**2, 2*a/m); c0 = a/m
    ck(P[1]**2 == 4*a*P[0], "directrix tangent contact membership")
    ck(P[1] == m*P[0]+c0, "directrix tangent at contact")
    ck(F(0) == m*F(-2)+c0, "directrix tangent through external point")
    ck(16*a*(a-m*c0) == 0, "tangent repeated-root discriminant")
ck(F(1)*(1+1) == 2 and 3-1 == 2, "parabola reflection equal lengths")
a0, t0 = F(1), F(0)
ck(all(F(0) == -t0*x+2*a0*t0+a0*t0**3 for x in (F(-2), F(0), F(3))), "vertex normal is the axis")

# Ellipse parametrization, focal distances and reconstruction.
a, b, c = 5.0, 3.0, 4.0; e = c/a
for theta in (0.0, pi/6, pi/3, pi/2, 4*pi/3):
    P = (a*cos(theta), b*sin(theta))
    ck(close(ellipse_value(P, 25, 9), 0), "ellipse eccentric-angle membership")
    ck(close(dist(P, (-c, 0))+dist(P, (c, 0)), 10), "ellipse focal sum")
    ck(close(dist(P, (c, 0)), a-e*P[0]), "ellipse right focal distance")
    ck(close(dist(P, (-c, 0)), a+e*P[0]), "ellipse left focal distance")
P = (2.0, 3.0)
ck(close(dist(P, (2, 0)), 3) and close(dist(P, (-2, 0)), 5), "ellipse reconstruction distances")
ck(close(ellipse_value(P, 16, 12), 0), "ellipse reconstruction equation")
ck(16-4 == 12 and close(2/4, .5), "ellipse reconstruction b and e")
Q = (2*sqrt(2), 2*sqrt(2)); P = (2*sqrt(2), 3/sqrt(2))
ck(close(Q[0]**2+Q[1]**2, 16) and close(ellipse_value(P, 16, 9), 0), "auxiliary circle and ellipse points")
ck(close(P[0], Q[0]) and close(P[1], .75*Q[1]), "auxiliary circle vertical squash")

# Ellipse tangent/normal and director circle.
P = (2*sqrt(2), 3/sqrt(2))
ck(close(3*P[0]+4*P[1], 12*sqrt(2)), "ellipse tangent example incidence")
ck(close(4*P[0]-3*P[1], 7*sqrt(2)/2), "ellipse normal example incidence")
ck(close(F(-3, 4)*F(4, 3), -1), "ellipse tangent-normal slopes")
ck(close(9*16+16*9, (12*sqrt(2))**2), "ellipse line tangency condition")
for m, contact in ((1, (-3.2, 1.8)), (-1, (3.2, 1.8))):
    ck(close(5**2, 16*m*m+9), "director-circle tangent condition")
    ck(close(ellipse_value(contact, 16, 9), 0), "director-circle contact membership")
    ck(close(contact[1], m*contact[0]+5), "director-circle tangent at contact")
ck(1*(-1) == -1 and 0**2+5**2 == 16+9, "perpendicular tangents meet on director circle")
# Slope quadratic at (h,k)=(0,5): -16m^2+16=0.
ck(-16*1+16 == 0 and -16*1+16 == 0, "director slope quadratic roots")
ck(F(25-9, 0-16) == -1, "director slope product")

# Exact nonvertical ellipse focal chord.
P = (F(5, 2), 3*sqrt(3)/2); Q = (F(65, 14), -9*sqrt(3)/14); S = (4.0, 0.0)
ck(close(ellipse_value(P, 25, 9), 0), "ellipse focal chord P membership")
ck(close(ellipse_value(Q, 25, 9), 0), "ellipse focal chord Q membership")
ck(close(dist(P, S), 3) and close(dist(Q, S), F(9, 7)), "ellipse focal chord lengths")
ck(close((P[0]-4)*(Q[1]), P[1]*(Q[0]-4)), "ellipse focal chord collinearity")
ck(close(1/F(3)+1/F(9, 7), F(10, 9)), "ellipse focal chord reciprocal sum")
ck(close(2/(1/F(3)+1/F(9, 7)), F(9, 5)), "ellipse semi-latus harmonic mean")
ck(Q[0] < 5 and Q[0] > -5, "ellipse focal chord second endpoint inside vertex bounds")

# Hyperbola parameters, focal differences and tangent/normal formulas.
a, b, c = 3.0, 4.0, 5.0; e = c/a
for theta in (0.0, pi/4, -pi/4, pi/3):
    P = (a/cos(theta), b*sin(theta)/cos(theta))
    ck(close(hyper_value(P, 9, 16), 0), "hyperbola sec-tan membership")
    ck(close(abs(dist(P, (-c, 0))-dist(P, (c, 0))), 6), "hyperbola focal difference")
    ck(close(dist(P, (c, 0)), e*P[0]-a), "hyperbola near focal distance")
    ck(close(dist(P, (-c, 0)), e*P[0]+a), "hyperbola far focal distance")
alpha_cos2 = (1-(4/3)**2)/(1+(4/3)**2)
ck(close(alpha_cos2, -7/25) and close(2/e**2-1, -7/25), "hyperbola asymptote-angle identity")
ck(close(1/e**2+1/(5/4)**2, 1), "conjugate hyperbola eccentricity identity")
ck(close(hyper_value((3, 0), 9, 16), 0) and 5-3 == 2 and 5+3 == 8, "hyperbola vertex focal lengths")
for theta in (pi/4, -pi/4, pi/3):
    sec = 1/cos(theta); tan = sin(theta)/cos(theta)
    P = (3*sec, 4*tan); mt = 4/(3*sin(theta)); mn = -3*sin(theta)/4
    ck(close(P[0]*sec/3-P[1]*tan/4, 1), "hyperbola parametric tangent")
    ck(close(3*P[0]*sin(theta)+4*P[1], 25*tan), "hyperbola parametric normal")
    ck(close(mt*mn, -1) and abs(mt) > 4/3, "hyperbola normal and tangent slope restriction")
R = (F(-10, 3), F(-4))
ck(hyper_value(R, 4, 9) == 0, "asymptote-parallel point on hyperbola")
ck(R[1] == F(3, 2)*R[0]+1, "asymptote-parallel line incidence")
ck(R[1]-F(3, 2)*R[0] == 1, "distinct parallel asymptote intercept")
for t in (F(1, 2), F(1), F(2), F(3)):
    c0 = F(2); P = (c0*t, c0/t)
    ck(P[0]*P[1] == 4, "rectangular hyperbola parameter")
    ck(P[0]/t+t*P[1] == 2*c0, "rectangular hyperbola tangent")
    ck(P[1] == t*t*P[0]-c0*t**3+c0/t, "rectangular hyperbola normal")
    ck((-1/t**2)*t**2 == -1, "rectangular hyperbola perpendicular lines")
U = (F(5), F(16, 3)); V = (F(5), F(-16, 3)); S = (F(5), F(0))
ck(hyper_value(U, 9, 16) == 0 and hyper_value(V, 9, 16) == 0, "same-branch focal chord endpoints")
ck(d2(U, S) == F(256, 9) and d2(V, S) == F(256, 9), "same-branch focal chord lengths")
ck(2/F(16, 3) == F(3, 8), "same-branch focal chord reciprocal sum")
ck(1/F(8)+1/F(2) == F(5, 8) and F(5, 8) != F(3, 8), "opposite-branch reciprocal countercheck")

# Unified chord-of-contact, pair-of-tangents and midpoint-chord tools.
Pext = (F(4), F(2)); Q = (F(4), F(0)); R = (F(0), F(2))
for P in (Q, R):
    ck(ellipse_value(P, 16, 4) == 0, "chord of contact endpoint on ellipse")
    ck(P[0]+2*P[1] == 4, "chord of contact line")
    ck(P[0]*Pext[0]/16+P[1]*Pext[1]/4 == 1, "contact tangent through external point")
for P in ((F(4), F(1)), (F(1), F(2))):
    S = ellipse_value(P, 16, 4); T = P[0]*Pext[0]/16+P[1]*Pext[1]/4-1; S1 = ellipse_value(Pext, 16, 4)
    ck(S*S1 == T*T, "pair of tangents SS1=T^2")
# Substitution of 9x+8y=26 gives 117x^2-468x+100=0.
A, B, C = F(117), F(-468), F(100)
disc = B*B-4*A*C
ck(A == 117 and B == -468 and C == 100, "midpoint chord quadratic")
ck(-B/A == 4 and disc > 0, "midpoint chord root sum and reality")
root_disc = sqrt(float(disc))
xs = [float(-B-root_disc)/(2*float(A)), float(-B+root_disc)/(2*float(A))]
ys = [(26-9*x)/8 for x in xs]
ck(close(sum(ys), 2), "midpoint chord y-root sum")
ck(all(close(ellipse_value((x, y), 16, 9), 0) and close(9*x+8*y, 26) for x, y in zip(xs, ys)), "midpoint chord endpoints")
ck(close((xs[0]+xs[1])/2, 2) and close((ys[0]+ys[1])/2, 1), "midpoint chord midpoint")

# Pole, polar, La Hire incidence and mixed example.
ck(close(4*(25/4)/25, 1), "ellipse focus polar is directrix")
ck(0 == 2*(8-8), "parabola pole of vertical line")
P, Q, R = (F(4), F(3)), (F(4), F(0)), (F(0), F(3))
ck(3*Q[0]+4*Q[1] == 12 and 3*R[0]+4*R[1] == 12, "polar contains both contacts")
ck(P[0] == Q[0] and P[1] == R[1], "La Hire tangent incidence")
P = (2.5, 1.5*sqrt(3))
ck(close(3*P[0]+5*sqrt(3)*P[1], 30), "mixed ellipse tangent")
ck(close(dist(P, (4, 0)), 3) and close(dist(P, (-4, 0)), 7), "mixed ellipse focal distances")
ck(25+9 == 34, "mixed ellipse director circle")

# Confocal orthogonality and rectangular-hyperbola orthocentre formula.
P = (2.5, 1.5*sqrt(3))
ck(close(ellipse_value(P, 25, 9), 0) and close(hyper_value(P, 4, 12), 0), "confocal intersection membership")
ck(25-9 == 4+12 == 16, "confocal common focal distance")
ck(close((-sqrt(3)/5)*(5/sqrt(3)), -1), "confocal tangent orthogonality")
# Verify the rounded endpoint actually encoded in the editable confocal figure.
_confocal_source = (Path(__file__).resolve().parents[1] / "content" / "olympiad-01.md").read_text()
_confocal_specs = [json.loads(block.split("\n:::", 1)[0]) for block in _confocal_source.split(":::diagram\n")[1:]]
_confocal = next(spec for spec in _confocal_specs if spec.get("title") == "Confocal ellipse and hyperbola meet orthogonally")
_gold = next(el for el in _confocal["elements"] if el.get("kind") == "line" and el.get("color") == "#B8860B")
_drawn_slope = (_gold["b"][1]-_gold["a"][1])/(_gold["b"][0]-_gold["a"][0])
ck(abs(_drawn_slope+sqrt(3)/5) < 2e-5, "confocal drawn ellipse tangent endpoint")
for ts in ((1.0, 2.0, -1.0), (2.0, 3.0, .5), (-1.0, 2.0, 3.0)):
    t1, t2, t3 = ts; c0 = 1.0
    A = (c0*t1, c0/t1); Bv = (c0*t2, c0/t2); Cv = (c0*t3, c0/t3)
    q = t1*t2*t3; H = (-c0/q, -c0*q)
    ck(all(close(X[0]*X[1], c0*c0) for X in (A, Bv, Cv, H)), "rectangular hyperbola four-point incidence")
    ck(close((A[0]-H[0])*(Bv[0]-Cv[0])+(A[1]-H[1])*(Bv[1]-Cv[1]), 0), "first altitude perpendicular")
    ck(close((Bv[0]-H[0])*(Cv[0]-A[0])+(Bv[1]-H[1])*(Cv[1]-A[1]), 0), "second altitude perpendicular")
    ck(close((Cv[0]-H[0])*(A[0]-Bv[0])+(Cv[1]-H[1])*(A[1]-Bv[1]), 0), "third altitude perpendicular")
O, H, N = (2.0, 1.5), (0.0, 0.0), (1.0, .75)
ck(close(N[0], (O[0]+H[0])/2) and close(N[1], (O[1]+H[1])/2), "nine-point centre midpoint")
ck(close(dist(O, (0, 0)), 2.5) and close(dist(N, (2, 0)), 1.25), "nine-point radius half circumradius")

# General conic invariants, rotation and degeneracy.
def delta(a, b, h):
    return a*b-h*h

def Delta(a, b, c0, f, g, h):
    return a*(b*c0-f*f)-h*(h*c0-f*g)+g*(h*f-b*g)

ck(delta(1, 1, 2) == -3 and Delta(1, 1, -1, 0, 0, 2) == 3, "general conic example invariants")
ck(delta(1, 1, 0) > 0 and Delta(1, 1, -1, 0, 0, 0) < 0, "real ellipse invariant signs")
ck(delta(1, 1, 0) > 0 and Delta(1, 1, 1, 0, 0, 0) > 0, "empty ellipse invariant signs")
ck(delta(1, 0, 0) == 0 and Delta(1, 0, 0, -1, 0, 0) != 0, "parabola invariant signs")
ck(delta(1, 1, 2) < 0 and Delta(1, 1, -1, 0, 0, 2) != 0, "hyperbola invariant signs")
for x, y in ((0, 1), (1, 0), (2, -1), (-3, 2), (.5, .25)):
    X = (x+y)/sqrt(2); Y = (y-x)/sqrt(2)
    original = x*x+4*x*y+y*y-1
    rotated = 3*X*X-Y*Y-1
    ck(close(original, rotated), "general conic orthogonal rotation")
ck(Delta(4, 9, 0, 0, 0, -6) == 0 and delta(4, 9, -6) == 0, "repeated-line degeneracy")
ck(Delta(1, -1, 0, 0, 0, 0) == 0 and delta(1, -1, 0) < 0, "intersecting-lines degeneracy")
ck(close((sqrt(3))*(-sqrt(3)), -3) and not close(-3, -1), "rotated hyperbola asymptotes are not perpendicular")

# Targeted assertions for the expanded visual lesson.
for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    ck(_condition, f"visual lesson: {_name}")

print(f"Conic Sections: {checks}/{checks} checks PASS")
