#!/usr/bin/env python3
"""Independent exact, numerical and editable-figure checks for Chapter 19."""
from pathlib import Path
from fractions import Fraction as F
import json
import math
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "_engine"))
from diagrams import _eval_expr
from visual_math_checks import checks_for

checks = 0


def ck(ok, msg):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(msg)


def close(a, b, tol=1e-9):
    return math.isclose(float(a), float(b), rel_tol=tol, abs_tol=tol)


def fd(f, x, h=1e-5):
    return (f(x+h)-f(x-h))/(2*h)


def bisect(f, a, b):
    fa, fb = f(a), f(b)
    if fa*fb > 0:
        raise ValueError("bisection interval has no sign change")
    for _ in range(100):
        m = (a+b)/2
        fm = f(m)
        if fa*fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a+b)/2


# Rates of change: exact geometric relations and independent finite differences.
ck(close(2*math.pi*5*2, 20*math.pi), "circle area rate")
ck(3*10**2*3 == 900, "cube volume rate")
ck(close(100/(4*math.pi*10**2), 1/(4*math.pi)), "balloon radius rate")
ck(F(-5, 12)*F(1, 2) == F(-5, 24), "ladder signed rate")
ck(5**2+12**2 == 13**2, "ladder 5-12-13 constraint")
for r in (.5, 2., 5.):
    ck(close(fd(lambda x: math.pi*x*x, r), 2*math.pi*r, 2e-6), "circle area derivative oracle")
for s in (.5, 3., 10.):
    ck(close(fd(lambda x: x**3, s), 3*s*s, 2e-6), "cube volume derivative oracle")
for r in (1., 4., 10.):
    ck(close(fd(lambda x: 4*math.pi*x**3/3, r), 4*math.pi*r*r, 2e-6), "balloon volume derivative oracle")

# Tangents, normals, angles and lengths.
f = lambda x: x**3-3*x
ck(f(2) == 2 and 3*2**2-3 == 9, "cubic tangent point and slope")
for x in (-1., 0., 2., 3.):
    ck(close(f(2)+9*(x-2), 9*x-16), "cubic tangent equation")
    ck(close(2-(x-2)/9, (20-x)/9), "cubic normal equation")
ck(9*F(-1, 9) == -1 and 2+9*2 == 20, "cubic normal perpendicular and on point")
ck(1+2*1 == 3 and 2*F(-1, 2) == -1, "parabola normal at one")
chord_slope = F(9-1, 3-1)
ck(chord_slope == 4 and 2*2 == chord_slope and 2**2 == 4, "parallel chord and tangent")
ck(close(math.degrees(math.atan(abs(F(2-3, 1+2*3)))), 8.1301023542), "angle between curves")
for y in (-2, 2):
    x = 1
    ck(y*y == 4*x and x*x+y*y == 5, "actual parabola-circle intersections")
    ck(F(2, y)*F(-x, y) == F(-1, 2), "nonorthogonal tangent slopes")
for x0 in (F(-2), F(1, 2), F(1)):
    y0, m = x0**3, 3*x0**2
    T, N = x0-y0/m, x0+m*y0
    ck(abs(y0/m) == abs(x0-T), "subtangent from intercept")
    ck(abs(m*y0) == abs(N-x0), "subnormal from intercept")
    tangent_length = (x0-T)**2+y0**2
    normal_length = (x0-N)**2+y0**2
    ck(tangent_length == y0**2*(1+m**2)/m**2, "tangent segment length identity")
    ck(normal_length == y0**2*(1+m**2), "normal segment length identity")
ck(F(1, 3) == abs(F(1)/3) and 3 == abs(3*1), "source subtangent and subnormal")
ck(close(math.sqrt(10)/3, math.sqrt(1+9)/3), "source tangent segment")
ck(close(math.sqrt(10), math.sqrt(1+9)), "source normal segment")

# Differentials: direct numerical values, signs and second-order error estimates.
actual = math.sqrt(25.4)
ck(close(actual, 5.039841267341661, 1e-12), "correct square-root numerical value")
ck(not close(actual, 5.03968, 1e-12), "source square-root typo is rejected")
ck(close(5+0.4/10, 5.04), "square-root differential estimate")
ck(close(5.04-actual, 0.0001587326583392, 1e-8), "square-root linearisation error")
ck(close(-0.4**2/(8*25**1.5), -0.00016), "square-root second-order error estimate")
ck(5.04 > actual, "concavity puts tangent above square root")
ck(close((1.01)**10, 1.1046221254112045, 1e-12), "power true value")
ck(close(1+10*.01, 1.1) and 1.1 < 1.01**10, "power differential estimate")
ck(close(math.log(1.02), 0.01980262729617973, 1e-12), "logarithm true value")
ck(close(.02, 0+1*.02) and .02 > math.log(1.02), "logarithm differential estimate")

# Monotonicity, inequalities and exact root counting.
for x in (-3., -1.2, 1.2, 3.):
    ck(3*(x-1)*(x+1) > 0, "cubic increasing branches")
for x in (-.8, 0., .8):
    ck(3*(x-1)*(x+1) < 0, "cubic decreasing branch")
for x in (-3., 0., 3.):
    ck(6*(x-1)*(x-2) > 0, "second cubic increasing branches")
for x in (1.1, 1.5, 1.9):
    ck(6*(x-1)*(x-2) < 0, "second cubic decreasing branch")
for a, b in ((-2., -1.), (-.1, .2), (0., 3.)):
    ck(a**3 < b**3, "x^3 strict increase despite stationary point")
for x in (.05, .2, .8, 1., 1.5, 3., 20.):
    ck(math.log(x) <= x-1+1e-13, "logarithm below x-1")
    ck(x-math.log(x) >= 1-1e-13, "x-ln x global lower bound")
ck(math.log(1) == 0 and 1-math.log(1) == 1, "logarithm inequalities equality")
root_cubic = lambda x: x**3-3*x+1
for a, b in ((-2, -1), (-1, 1), (1, 2)):
    r = bisect(root_cubic, a, b)
    ck(a < r < b and close(root_cubic(r), 0, 1e-10), "independent bisection root")
roots = np.roots([1., 0., -3., 1.])
ck(len(roots) == 3 and all(abs(r.imag) < 1e-9 for r in roots), "numpy cubic root oracle")
real_roots = sorted(float(r.real) for r in roots)
ck(all(a < r < b for r, (a, b) in zip(real_roots, ((-2, -1), (-1, 1), (1, 2)))), "three roots occupy three monotone branches")
ck(all(close(root_cubic(r), 0, 1e-9) for r in real_roots), "numpy roots satisfy source cubic")
ck(root_cubic(-2) == -1 and root_cubic(-1) == 3 and root_cubic(1) == -1 and root_cubic(2) == 3, "root-count sign anchors")
for m, c, expected in ((1, -1, 0), (1, -.25, 1), (1, 0, 2)):
    disc = m*m+4*c
    count = 2 if disc > 0 else (1 if disc == 0 else 0)
    ck(count == expected, "line-parabola intersection discriminant")

# Local and absolute extrema.
g = lambda x: x**3-6*x*x+9*x+2
ck(g(1) == 6 and g(3) == 2, "source local maximum and companion minimum")
ck(3*(1-1)*(1-3) == 0 and 3*(3-1)*(3-3) == 0, "local-extremum critical points")
ck(3*(0-1)*(0-3) > 0 and 3*(2-1)*(2-3) < 0 and 3*(4-1)*(4-3) > 0, "local-extremum derivative sign changes")
ck(f(-1) == 2 and f(1) == -2, "cubic local extrema values")
for x in (-2., -1., 1., 2.):
    expected = {-2: -2, -1: 2, 1: -2, 2: 2}[int(x)]
    ck(f(x) == expected, "closed-interval candidate values")
ck(max(map(f, (-2, -1, 1, 2))) == 2 and min(map(f, (-2, -1, 1, 2))) == -2, "closed-interval absolute extrema")
quartic = lambda x: x**4-4*x*x
for x in (-math.sqrt(2), math.sqrt(2)):
    ck(close(quartic(x), -4) and close(12*x*x-8, 16), "quartic minima and second derivative")
ck(quartic(0) == 0 and 12*0-8 == -8, "quartic local maximum")
for x in (-2., -1., -.5, .5, 1., 2.):
    ck(close(4*x**3-8*x, 4*x*(x*x-2)), "quartic derivative factorisation")
for x in (F(-2), F(1, 2), F(4)):
    h = x+1/x
    expected = {F(-2): F(-5, 2), F(1, 2): F(5, 2), F(4): F(17, 4)}[x]
    ck(h == expected, "reciprocal-sum candidate value")
for x in (.05, .2, .5, 1., 2., 4., 20.):
    ck(x+1/x >= 2-1e-13, "reciprocal-sum global minimum")
ck(F(1, 2)+2 == F(5, 2) and 4+F(1, 4) == F(17, 4), "reciprocal-sum closed interval")

# Convexity, inflection and curve-sketching anchors, including Q26 correction.
for x in (-2., -.5, .5, 2.):
    ck((6*x > 0) == (x > 0), "cubic second-derivative sign")
    ck((f(x)-(-3*x) > 0) == (x > 0), "cubic crosses inflection tangent")
ck(f(0) == 0 and -3*0 == 0, "cubic inflection point")
ck(6*2-6 > 0 and 6*0-6 < 0, "source convex interval for x^3-3x^2")
for x2 in (F(2, 3),):
    y = x2*x2-4*x2
    ck(12*x2-8 == 0, "correct quartic inflection abscissa")
    ck(y == F(-20, 9), "correct quartic inflection ordinate")
wrong_x2 = F(1, 3)
ck(12*wrong_x2-8 == -4 and wrong_x2*wrong_x2-4*wrong_x2 == F(-11, 9), "printed Q26 point is not an inflection point")
for x in (-1., -.5, 0., .5, 1.):
    ck(12*x*x >= 0, "x^4 has no inflection at zero")
for x, y in ((0, 0), (-2, 0), (2, 0)):
    ck(quartic(x) == y, "quartic intercept")
ck(quartic(-1.1) == quartic(1.1), "quartic even symmetry")
for x in (-2., -1.5, -.5, .5, 1.5, 2.):
    ck(close(12*x*x-8, 12*(x*x-F(2, 3))), "quartic concavity factorisation")

# Feasible optimisation, including completed-square and grid oracles.
fence = lambda x: 40*x-2*x*x
for x in (F(0), F(5), F(10), F(15), F(20)):
    ck(fence(x) == 200-2*(x-10)**2, "fence completed square")
ck(fence(10) == 200 and 40-2*10 == 20, "fence optimum dimensions")
grid = np.linspace(0, 20, 4001)
ck(close(grid[np.argmax(fence(grid))], 10, 2e-6), "fence numerical grid optimum")
box = lambda x: x*(12-2*x)**2
for x in (F(0), F(1), F(2), F(3), F(6)):
    direct = (12-2*x)*(12-6*x)
    factored = 12*(6-x)*(2-x)
    ck(direct == factored, "box derivative factorisation")
ck(box(2) == 128 and box(0) == box(6) == 0, "box optimum and endpoints")
ck(24*2-96 == -48, "box second derivative at optimum")
for x in (F(1), F(5), F(10), F(15), F(19)):
    y = 20-x
    ck(x*y == 100-(x-10)**2, "sum-twenty product square")
ck(10*10 == 100, "sum-twenty maximum product")
for p in (F(10), F(20), F(50)):
    ell = p/4
    ck(ell*(p/2-ell) == p*p/16, "fixed-perimeter square optimum")
    ck((ell+1)*(p/2-ell-1) < p*p/16, "fixed-perimeter nonsquare comparison")
for a, b in ((5, 3), (2, 7)):
    t = math.pi/4
    x, y = a*math.cos(t), b*math.sin(t)
    ck(close(x*x/a**2+y*y/b**2, 1), "ellipse rectangle contact")
    ck(close(4*x*y, 2*a*b), "ellipse rectangle maximum")
    for t in (.1, .5, 1.1):
        ck(2*a*b*math.sin(2*t) <= 2*a*b+1e-12, "ellipse area upper bound")
window_c = 2+math.pi/2
rstar = 10/(4+math.pi)
rmax = 10/(2+math.pi)
Amax = 50/(4+math.pi)
window = lambda r: 10*r-window_c*r*r
height = lambda r: 5-r*(1+math.pi/2)
ck(close(rstar, 1.4002478837788934) and close(rmax, 1.9449226482417137), "window numerical radii")
ck(close(Amax, 7.0012394188944675) and close(window(rstar), Amax), "window numerical area")
ck(0 < rstar < rmax and close(height(rstar), rstar), "window optimum feasible with h=r")
for r in np.linspace(0, rmax, 25):
    ck(close(window(r), Amax-window_c*(r-rstar)**2, 2e-9), "window completed-square identity")
    ck(window(r) <= Amax+1e-10, "window global upper bound")
ck(close(window(0), 0) and close(window(rmax), math.pi*rmax*rmax/2), "window degenerate endpoints")
ck(not close(10*1-2*1**2, window(1)), "source window area cancellation is rejected")

# Supporting lines, Jensen, cosine, Young, Cauchy and AM-GM.
for x in (F(-3), F(0), F(1, 2), F(3), F(8)):
    ck(x*x-(6*x-9) == (x-3)**2 and x*x >= 6*x-9, "supporting line exact square")
for a, b, c in ((1., 2., 3.), (.2, .2, .2), (2., 5., 1.)):
    left = (math.exp(a)+math.exp(b)+math.exp(c))/3
    right = math.exp((a+b+c)/3)
    ck(left >= right-1e-13, "exponential Jensen")
exp_mean = (math.e+math.e**2+math.e**3)/3
ck(close(exp_mean, 10.064291616859121, 1e-12) and not close(exp_mean, 10.71, 1e-9), "correct Q34 numerical check")
ck(close((math.e+math.e+math.e)/3, math.e), "exponential Jensen equality")
for x in (-10., -2., -.3, 0., .4, 2., 10.):
    ck(math.cos(x) >= 1-x*x/2-1e-13, "cosine quadratic lower bound")
    gp = x-math.sin(x)
    ck((gp > 0) == (x > 0), "cosine-bound derivative sign")
for p, a, b in ((3., 2., 4.), (4., 2., 3.), (2., 5., 7.)):
    q = p/(p-1)
    ck(close(1/p+1/q, 1), "conjugate exponents")
    ck(a*b <= a**p/p+b**q/q+1e-12, "Young inequality")
ck(close(2*4, 2**3/3+4**1.5/1.5), "Young equality example")
for a, b in ((.1, 2.), (4., 9.), (3., 3.)):
    ck(math.sqrt(a*b) <= (a+b)/2+1e-13, "two-variable AM-GM")
for x, y, z in ((1., 2., 6.), (.2, 3., 4.), (2., 2., 2.)):
    ck((x*y*z)**(1/3) <= (x+y+z)/3+1e-13, "three-variable AM-GM")
for a, b in ((-3., 2.), (0., 5.), (4., 4.)):
    ck(close(a*a+b*b-2*a*b, (a-b)**2) and a*a+b*b >= 2*a*b, "signed square bound")
a, b = 1., -1.
source_expr = (a*a+b*b)/2-math.sqrt(a*a*b*b)
ck(not close(source_expr, (a-b)**2/2), "invalid sqrt(a^2b^2) identity is rejected")
for aa, xx in (([1., 2., 3.], [2., 1., 4.]), ([-1., 2.], [3., 5.])):
    lhs = sum(a*a/x for a, x in zip(aa, xx))
    rhs = sum(aa)**2/sum(xx)
    ck(lhs >= rhs-1e-12, "Cauchy Engel inequality")

# Envelopes, directrix, director circle and Lagrange multipliers.
for a in (.7, 1., 2.5):
    for m in (-2., -.5, .5, 1., 3.):
        x, y = a/m**2, 2*a/m
        ck(close(y*y, 4*a*x), "envelope contact lies on parabola")
        ck(close(y, m*x+a/m), "envelope contact lies on member line")
        yperp1, yperp2 = m*(-a)+a/m, -(-a)/m-a*m
        ck(close(yperp1, yperp2), "perpendicular tangents meet on directrix")
for P in ((5., 3.), (-5., 3.), (0., math.sqrt(34))):
    ck(close(P[0]**2+P[1]**2, 34), "ellipse director-circle point")
ck(5**2/25+0**2/9 == 1 and 0**2/25+3**2/9 == 1, "vertical-horizontal ellipse contact points")
ck(close(math.hypot(5, 3), math.sqrt(34)), "ellipse director distance")
for R in (.5, 1., 3.):
    for t in (0., .7, 1.4):
        n1 = np.array([math.cos(t), math.sin(t)])
        n2 = np.array([math.cos(t+math.pi/2), math.sin(t+math.pi/2)])
        P = R*(n1+n2)
        ck(close(np.dot(n1, P), R) and close(np.dot(n2, P), R), "circle perpendicular tangents")
        ck(close(np.dot(P, P), 2*R*R), "circle director distance")
for x, y, z in ((1., 1., 1.), (2., 0., 1.), (-1., 2., 2.), (4., -2., 1.)):
    if close(x+y+z, 3):
        ck(close(x*x+y*y+z*z-3, (x-1)**2+(y-1)**2+(z-1)**2), "Lagrange global square identity")
        ck(x*x+y*y+z*z >= 3-1e-13, "Lagrange plane minimum")

# Symmetric optimisation and open-boundary distinctions.
for x, y in ((1., 9.), (4., 6.), (5., 5.)):
    s = x*y
    ck(close(1/x+1/y, 10/s) and close(x*x+y*y, 100-2*s), "symmetric sum-ten reductions")
    ck(1/x+1/y >= F(2, 5)-1e-13 and x*x+y*y >= 50-1e-13, "sum-ten minima")
for x, y, z in ((.2, .3, .5), (1/3, 1/3, 1/3), (.5, .25, .25)):
    ck(x*y*z <= F(1, 27)+1e-13, "positive plane product maximum")
ck(close(F(1, 3)**3, F(1, 27)), "product equality point")
for x in (.001, .1, 1., 3., 5.9):
    y = 6-x
    value = x**3+y**3
    ck(close(value, 216-18*x*y) and close(value, 18*(x-3)**2+54), "symmetric cubic identities")
    ck(54-1e-12 <= value < 216+1e-12, "symmetric cubic bounds")
ck(close(.1**3+5.9**3, 205.38) and not close(.1**3+5.9**3, 205.8), "correct Q45 numerical check")
ck(3**3+3**3 == 54, "symmetric cubic attained minimum")
for eps in (.1, .01, .001):
    value = eps**3+(6-eps)**3
    ck(value < 216 and 216-value < 108*eps, "supremum approached but not attained")
for x, y, z in ((.2, .3, .5), (.5, .25, .25), (1/3, 1/3, 1/3)):
    lhs = (x-F(1, 3))**2+(y-F(1, 3))**2+(z-F(1, 3))**2
    ck(close(lhs, x*x+y*y+z*z-F(1, 3)), "plane sum-of-squares identity")
    ck(x*x+y*y+z*z >= F(1, 3)-1e-13, "plane sum-of-squares minimum")

# Assertions against the actual editable JSON figures, not just the prose.
content = Path(__file__).resolve().parents[1] / "content"
specs = []
for path in sorted(content.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    for block in text.split(":::diagram\n")[1:]:
        specs.append(json.loads(block.split("\n:::", 1)[0]))
ck(len(specs) == 22, "editable diagram inventory")
ck(sum(s.get("type") == "graph" for s in specs) == 15, "editable graph inventory")
ck(sum(s.get("type") == "flow" for s in specs) == 4, "editable workflow inventory")
ck(sum(s.get("type") == "table" for s in specs) == 3, "editable table inventory")
by_title = {s["title"]: s for s in specs}
ck(len(by_title) == len(specs), "unique figure titles")


def value(curve, x):
    y = np.asarray(_eval_expr(curve["expr"], np.array([float(x)])))
    return float(y.reshape(-1)[0])


for spec in specs:
    for curve in spec.get("curves", []):
        lo = curve.get("from", spec.get("xrange", [-6, 6])[0])
        hi = curve.get("to", spec.get("xrange", [-6, 6])[1])
        ck(math.isfinite(value(curve, (lo+hi)/2)), f"finite plotted expression: {spec['title']}")

spec = by_title["The cubic tangent and normal are perpendicular at (2,2)"]
ck(all(close(value(c, 2), 2) for c in spec["curves"]), "actual cubic, tangent and normal meet")
ck(close(fd(lambda x: value(spec["curves"][1], x), 2)*fd(lambda x: value(spec["curves"][2], x), 2), -1), "actual tangent-normal slopes")
spec = by_title["The derivative sign partitions the cubic into three monotone pieces"]
ck(all(close(value(spec["curves"][0], p["x"]), p["y"]) for p in spec["points"]), "actual monotonicity turning points")
ck([v["x"] for v in spec["vlines"]] == [-1, 1], "actual monotonicity partition")
spec = by_title["A quartic can have two local minima and one local maximum"]
ck(all(close(value(spec["curves"][0], p["x"]), p["y"]) for p in spec["points"]), "actual quartic extrema anchors")
spec = by_title["At a cubic inflection point the curve crosses its tangent"]
ck(all(close(value(c, 0), 0) for c in spec["curves"]), "actual inflection tangent contact")
ck(value(spec["curves"][0], -1) < value(spec["curves"][1], -1) and value(spec["curves"][0], 1) > value(spec["curves"][1], 1), "actual inflection crossing")
spec = by_title["The feasible fencing area is a downward parabola"]
ck(all(close(value(spec["curves"][0], p["x"]), p["y"]) for p in spec["points"]), "actual fencing candidate anchors")
ck(len(spec["xticks"]) == 5 and len(spec["yticks"]) == 5, "fencing graph readable tick scales")
spec = by_title["The physical 5-12-13 ladder state gives a Pythagorean constraint"]
ladder = spec["rays"][0]
ck(close(math.hypot(ladder["x"][1]-ladder["x"][0], ladder["y"][1]-ladder["y"][0]), 13), "actual ladder drawing length")
ck(not spec.get("curves"), "physical ladder is not mixed with abstract state circle")
spec = by_title["Two curves and their tangents at the common point (1,1)"]
ck(all(close(value(c, 1), 1) for c in spec["curves"]), "actual angle curves and tangents meet")
ck(close(fd(lambda x: value(spec["curves"][2], x), 1), 2) and close(fd(lambda x: value(spec["curves"][3], x), 1), 3), "actual angle tangent slopes")
spec = by_title["A zoom near sqrt(25.4) separates the curve from its tangent"]
ck(close(value(spec["curves"][0], 25.4), actual) and close(value(spec["curves"][1], 25.4), 5.04), "actual zoom curve and estimate")
ck(all(close(value(spec["curves"][i], 25.4), spec["points"][i]["y"], 1e-8) for i in (0, 1)), "actual zoom point anchors")
spec = by_title["Each monotone branch of the cubic crosses the x-axis once"]
ck(len(spec["points"]) == 3 and all(close(value(spec["curves"][0], p["x"]), 0) for p in spec["points"]), "actual three root markers")
spec = by_title["On [0,2], the cubic's maximum occurs at the right endpoint"]
ck(all(close(value(spec["curves"][0], p["x"]), p["y"]) for p in spec["points"]), "actual closed-interval markers")
ck(spec["bands"][0]["a"] == 0 and spec["bands"][0]["b"] == 2, "actual feasible band")
spec = by_title["The window area vertex lies before the zero-height endpoint"]
ck(close(value(spec["curves"][0], rstar), Amax) and close(value(spec["curves"][0], rmax), math.pi*rmax*rmax/2, 1e-8), "actual window curve anchors")
ck(all(close(value(spec["curves"][0], p["x"]), p["y"], 1e-8) for p in spec["points"]), "actual window marked points")
ck(spec["points"][1]["x"] < spec["points"][2]["x"], "actual window vertex precedes zero-height endpoint")
spec = by_title["A convex parabola lies above its supporting line"]
ck(all(value(spec["curves"][0], x) >= value(spec["curves"][1], x)-1e-12 for x in (0, 1, 2, 3, 4)), "actual supporting-line ordering")
ck(len(spec["yticks"]) == 4, "supporting-line readable tick scale")
spec = by_title["A family of lines envelops the parabola y^2=4x"]
for i, m in enumerate((.5, 1., 2.), start=2):
    p = spec["points"][i-2]
    ck(close(value(spec["curves"][i], p["x"]), p["y"]) and close(p["y"]**2, 4*p["x"]), "actual envelope contact marker")
ck(spec["vlines"][0]["x"] == -1, "actual parabola directrix")
spec = by_title["Perpendicular tangents to the ellipse meet on its director circle"]
p = spec["points"][0]
ck(close(value(spec["curves"][2], p["x"]), p["y"]) and close(p["x"]**2+p["y"]**2, 34), "actual director-circle marker")
ck(close(value(spec["curves"][0], 5), 0) and close(value(spec["curves"][0], 0), 3), "actual ellipse tangent contact points")
spec = by_title["The symmetric cubic has an interior minimum but no attained maximum"]
ck(close(value(spec["curves"][0], 3), 54), "actual symmetric-cubic minimum")
ck(all(p.get("face", "").lower() == "#ffffff" for p in (spec["points"][0], spec["points"][2])), "actual open endpoint markers")
ck(len(spec["yticks"]) == 5, "symmetric-cubic readable tick scale")
ck(all(len(row) == len(s["columns"]) for s in specs if s.get("type") == "table" for row in s["rows"]), "table rows match columns")
ck(all(len(step["detail"]) < 120 for s in specs if s.get("type") == "flow" for step in s["steps"]), "workflow labels remain concise")

# Targeted independent assertions for the six-page visual lab.
for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    ck(_condition, f"visual lab: {_name}")

print(f"Applications of Derivatives: {checks}/{checks} checks PASS")
