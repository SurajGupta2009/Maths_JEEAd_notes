#!/usr/bin/env python3
"""Independent exact, numerical and editable-figure checks for Chapter 18."""
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


def check_fd(f, x, expected, msg, tol=2e-6):
    ck(close(fd(f, x), expected, tol), msg)


def cauchy_derivative(f, x, n, radius=.35, samples=256):
    """Independent analytic differentiation by a trapezoidal Cauchy integral."""
    theta = 2*math.pi*np.arange(samples)/samples
    z = x+radius*np.exp(1j*theta)
    value = math.factorial(n)/radius**n*np.mean(f(z)*np.exp(-1j*n*theta))
    if abs(value.imag) > 2e-7:
        raise AssertionError(f"nonreal Cauchy derivative at order {n}: {value}")
    return float(value.real)


# First principles, exact difference quotients and basic tangents.
for x in (F(-2), F(0), F(1, 2), F(3)):
    for h in (F(-1, 2), F(1, 10), F(2)):
        ck(((x+h)**2-x**2)/h == 2*x+h, "exact quadratic difference quotient")
for x in (F(-2), F(1, 2), F(3)):
    for h in (F(-1, 10), F(1, 10), F(1, 3)):
        q = (1/(x+h)-1/x)/h
        ck(q == -1/(x*(x+h)), "exact reciprocal difference quotient")
for h in (F(-1, 2), F(1, 10), F(3)):
    ck(((2+h)**3-8)/h == 12+6*h+h**2, "exact cubic quotient at two")
check_fd(lambda x: x*x, 2, 4, "quadratic derivative numerical")
check_fd(lambda x: 1/x, 2, -1/4, "reciprocal derivative numerical")
check_fd(math.log, math.e, 1/math.e, "logarithm definition-recognition example")
for h in (F(-1, 2), F(1, 10), F(1, 100)):
    ck((1+h)**3-1 == 3*h+3*h**2+h**3, "differentiable increment tends to zero")
ck(1**2 == 1 and 2*1-1 == 1 and 3*1-2 == 1, "parabola, tangent and secant share P")
ck(2**2 == 4 and 3*2-2 == 4, "secant shares Q with parabola")
ck(2*1-1 == 1 and 2*0-1 == -1 and 2*2-1 == 3, "basic tangent equation samples")

# One-sided derivatives, corners, smooth joins and infinite quotients.
for h in (-.2, -.01, .01, .2):
    ck(close(abs(h)/h, -1 if h < 0 else 1), "absolute-value one-sided quotient")
    ck(close(h*abs(h)/h, abs(h)), "smooth flat-join quotient")
for h in (-1e-5, -1e-7, 1e-7, 1e-5):
    left = ((1+h)**2-1)/h
    right = (2*(1+h)-1-1)/h
    ck(close(left, 2, 1e-4) and close(right, 2), "piecewise join one-sided derivatives")
ck(2+(-1) == 1 and 2*1-1 == 1, "piecewise parameters satisfy value and slope")
ck(not (2+0 == 1), "slope-only parameter choice fails continuity")
for h in (-.1, -.01, .01, .1):
    cbrt = math.copysign(abs(h)**(1/3), h)
    ck(close(cbrt/h, abs(h)**(-2/3)), "cube-root infinite difference quotient")
ck(abs(1e-6)**(-2/3) > 1000, "cube-root quotient is unbounded")

# Derivative algebra and domain-preserving simplification.
for x in (.4, 1., 2.):
    expected = 2*x*math.sin(x)+x*x*math.cos(x)
    check_fd(lambda t: t*t*math.sin(t), x, expected, "product rule x^2 sin(x)")
check_fd(lambda x: x*math.exp(x), 0, 1, "product rule xe^x at zero")
for x in (F(-2), F(-1), F(0), F(2)):
    derivative = (1-x**2)/(1+x**2)**2
    direct = ((1)*(1+x**2)-x*(2*x))/(1+x**2)**2
    ck(derivative == direct, "quotient rule x/(1+x^2)")
for x in (F(0), F(2), F(3)):
    ck((x**2+2*x)/(x+1)**2 == (2*x*(x+1)-x**2)/(x+1)**2, "quotient rule x^2/(x+1)")
for x in (F(-2), F(0), F(2), F(4)):
    ck(x**2/(x+1) == x-1+1/(x+1), "domain-preserving polynomial division")
ck(F(5)-F(3, 2) == F(7, 2), "mixed power derivative at one")

# Chain rule and standard derivatives.
check_fd(math.sin, .7, math.cos(.7), "sine standard derivative")
check_fd(math.cos, .7, -math.sin(.7), "cosine standard derivative")
check_fd(math.exp, .7, math.exp(.7), "exponential standard derivative")
check_fd(math.log, .7, 1/.7, "logarithm standard derivative")
check_fd(lambda x: math.sin(3*x*x), .4, 6*.4*math.cos(3*.4**2), "chain rule sine of quadratic")
check_fd(lambda x: math.exp(x*x), .4, 2*.4*math.exp(.4**2), "chain rule exponential of quadratic")
check_fd(lambda x: math.cos(x**3), .4, -3*.4**2*math.sin(.4**3), "chain rule cosine of cubic")
for x in (.4, 1.2):
    check_fd(lambda t: math.log(math.sin(t)), x, 1/math.tan(x), "chain rule logarithm of sine")
check_fd(lambda x: math.sin(3*x), 0, 3, "inner scale triples initial slope")
for h in (1e-3, 1e-5, 1e-7):
    ck(close(math.sin(3*h)/(3*h), 1, 1e-5), "matched small-angle chain limit")

# Inverse functions, inverse trigonometry and principal branches.
check_fd(math.asin, 0, 1, "arcsine derivative at zero")
for x in (-.5, .5):
    check_fd(math.asin, x, 1/math.sqrt(1-x*x), "arcsine derivative")
    check_fd(math.acos, x, -1/math.sqrt(1-x*x), "arccosine derivative")
check_fd(math.atan, 1, .5, "arctangent derivative at one")
for x in (-.25, 0, .3):
    check_fd(lambda t: math.asin(2*t), x, 2/math.sqrt(1-4*x*x), "scaled arcsine derivative")
for k in range(-2, 3):
    x = 2*k*math.pi+.7
    original = math.atan(math.sin(x)/(1+math.cos(x)))
    ck(close(original, .35), "principal-branch reduction by k pi")
    ck(close(math.atan(math.tan(x/2)), x/2-k*math.pi), "arctan-tan branch formula")
    check_fd(lambda t: math.atan(math.sin(t)/(1+math.cos(t))), x, .5, "branch-wise derivative one half")
ck(1+math.cos(math.pi) == 0, "odd pi is excluded from original denominator")

# Implicit differentiation, verified independently from the relation.
ck(3**2+4**2 == 25 and close(-3/4 * 4/3, -1), "circle point and perpendicular radius")
check_fd(lambda x: math.sqrt(25-x*x), 3, -3/4, "circle upper-branch derivative")
for x in (0, 3, 5):
    ck(close(4-3*(x-3)/4, 25/4-3*x/4), "circle tangent equation")
ck(1**3+1*1 == 2 and close(-1/(3*1**2+1), -.25), "implicit cubic point and slope")


def cubic_branch(x):
    lo, hi = .2, 1.8
    for _ in range(100):
        mid = (lo+hi)/2
        if mid**3+x*mid-2 > 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


ck(close(cubic_branch(1), 1), "independent implicit cubic solve at the base point")
ck(close(fd(cubic_branch, 1, 1e-4), -.25, 2e-6), "implicit cubic slope from solved branch")

# Logarithmic differentiation and real powers.
xx = lambda x: math.exp(x*math.log(x))
check_fd(xx, 1, 1, "x^x derivative at one")
check_fd(xx, 1.5, 1.5**1.5*(1+math.log(1.5)), "x^x derivative away from one")
u_power = lambda x: (x*x+1)**x
x = .7
expected = u_power(x)*(math.log(x*x+1)+2*x*x/(x*x+1))
check_fd(u_power, x, expected, "general u(x)^v(x) logarithmic derivative")
product = lambda x: x*x*math.sin(x)/math.sqrt(1+x)
for x in (1., 2.):
    expected = product(x)*(2/x+1/math.tan(x)-1/(2*(1+x)))
    check_fd(product, x, expected, "product-quotient logarithmic derivative")
for r in (.5, 2.3):
    check_fd(lambda x: x**r, 1.4, r*1.4**(r-1), "real-power derivative")

# Parametric first and second derivatives, including an ellipse cross-check.
xpar, ypar = lambda t: t*t, lambda t: t**3
slope = lambda t: 3*t/2
for t in (-2., -1., 1., 2.):
    dt = 1e-5
    numerical = (ypar(t+dt)-ypar(t-dt))/(xpar(t+dt)-xpar(t-dt))
    ck(close(numerical, slope(t), 1e-7), "parametric first derivative")
    second = (slope(t+dt)-slope(t-dt))/(xpar(t+dt)-xpar(t-dt))
    ck(close(second, 3/(4*t)), "parametric second derivative")
for t in (.3, math.pi/4, 1.2):
    x, y = 2*math.cos(t), math.sin(t)
    parametric = -(1/2)/math.tan(t)
    implicit = -x/(4*y)
    ck(close(x*x/4+y*y, 1) and close(parametric, implicit), "ellipse parametric-implicit slope")
ck(abs(slope(1e-8)) < 2e-8 and xpar(0) == 0, "zero parameter rate needs limiting analysis")
ck(8 == 3*4-4, "semicubical tangent at t=2")

# Higher derivatives, normals and independent Cauchy-integral formulas.
for n in range(9):
    x = .7
    expected = (math.sin(x), math.cos(x), -math.sin(x), -math.cos(x))[n % 4]
    ck(close(expected, math.sin(x+n*math.pi/2)), "four-step sine derivative cycle")
h = 1e-4
second_sine = (math.sin(math.pi/2+h)-2*math.sin(math.pi/2)+math.sin(math.pi/2-h))/h**2
ck(close(second_sine, -1, 1e-6), "second derivative of sine at pi/2")
for n in range(6):
    actual = cauchy_derivative(lambda z: np.exp(2*z), .3, n)
    ck(close(actual, 2**n*math.exp(.6), 2e-7), "nth derivative of exponential")
ck(3*(-1/3) == -1 and close(1-(1-1)/3, 1), "normal slope and point for y=x^3")
ck(close(0-(0-1)/3, 1/3) and close(2-(2-1)/3, 5/3), "normal line samples")

# Leibniz termination and advanced closed forms.
for n in range(7):
    actual = cauchy_derivative(lambda z: z*z*np.exp(z), .3, n)
    expected = math.exp(.3)*(.3**2+2*n*.3+n*(n-1))
    ck(close(actual, expected, 3e-7), "Leibniz closed form for x^2e^x")
for n in range(1, 7):
    actual = cauchy_derivative(lambda z: z*z*np.cos(z), .3, n)
    expected = (.3**2*math.cos(.3+n*math.pi/2)
                +2*n*.3*math.cos(.3+(n-1)*math.pi/2)
                +n*(n-1)*math.cos(.3+(n-2)*math.pi/2))
    ck(close(actual, expected, 4e-7), "Leibniz closed form for x^2 cos(x)")
for n in range(6):
    actual = cauchy_derivative(lambda z: np.exp(2*z)*np.sin(z), .2, n)
    expected = sum(math.comb(n, k)*2**(n-k)*math.exp(.4)*math.sin(.2+k*math.pi/2) for k in range(n+1))
    ck(close(actual, expected, 4e-7), "general Leibniz sum with exponential and sine")
for n in range(6):
    r = 2.5
    actual = cauchy_derivative(lambda z: (2*z+1)**r, .4, n)
    falling = math.prod(r-j for j in range(n))
    expected = 2**n*falling*(2*.4+1)**(r-n)
    ck(close(actual, expected, 4e-7), "real-power falling-factorial formula")
for n in range(6):
    x, a, b, m = F(1, 2), 2, 1, 3
    expected = F(math.factorial(m), math.factorial(m-n))*a**n*(a*x+b)**(m-n) if n <= m else F(0)
    actual = cauchy_derivative(lambda z: (2*z+1)**3, .5, n)
    ck(close(actual, expected, 4e-7), "integer-power derivatives terminate")
for n in range(6):
    actual = cauchy_derivative(lambda z: 1/(2*z+1), .4, n)
    expected = (-1)**n*math.factorial(n)*2**n/(2*.4+1)**(n+1)
    ck(close(actual, expected, 4e-7), "reciprocal nth-derivative formula")
for n in range(6):
    actual = cauchy_derivative(lambda z: 1/(1-z), .2, n)
    expected = math.factorial(n)/(1-.2)**(n+1)
    ck(close(actual, expected, 4e-7), "source reciprocal 1/(1-x) nth derivative")
for x in (-2., 2.):
    for n in range(1, 5):
        actual = cauchy_derivative(lambda z: np.log(z*z-1), x, n)
        expected = (-1)**(n-1)*math.factorial(n-1)*((x-1)**(-n)+(x+1)**(-n))
        ck(close(actual, expected, 5e-7), "log(x^2-1) nth derivative on both real components")
for n in range(7):
    actual = cauchy_derivative(lambda z: np.exp(z)*np.cos(z), .7, n)
    expected = 2**(n/2)*math.exp(.7)*math.cos(.7+n*math.pi/4)
    ck(close(actual, expected, 4e-7), "exponential-cosine amplitude and phase")
for x in (-.8, -.3, 0, .4, .9):
    y = math.sqrt(1-x*x)
    yp, ypp = -x/y, -1/y**3
    ck(close((1-x*x)*ypp-x*yp, -y), "radical differential identity")
    ck(close(-(1-x*x)/y**3+x*x/y, -1/y+x*x/y), "corrected radical intermediate line")
    ck(close((x*x-1)/y, -y), "radical identity final simplification")

# Functional equations with zero and domain cases handled first.
for c in (-1., 0., .5, 2.):
    f = lambda x: math.exp(c*x)
    for x, y in ((-.7, .2), (.3, 1.1)):
        ck(close(f(x+y), f(x)*f(y)), "exponential functional equation family")
        ck(close(c*f(x), fd(f, x)), "exponential rate equation")
    ck(all(close(math.exp(-c*x)*f(x), 1) for x in (-.5, 0, 1.2)), "normalized exponential factor is constant")
ck(all(0*math.exp(.3*x) == 0 for x in (-2, 0, 3)), "zero exponential value would force zero solution")
for a in (-2., .5, 3.):
    f = lambda x: a*math.log(x)
    for x, y in ((.5, .75), (2., 1.5)):
        ck(close(f(x*y), f(x)+f(y)), "logarithmic functional equation family")
        ck(close(x*(a/x), a), "logarithmic rate equation x f'(x)=a")
    ck(f(1) == 0, "logarithmic functional equation normalization")

for a in (-2., 3.):
    f = lambda x: a*x
    for x, y in ((-.7, .2), (.3, 1.1)):
        ck(close(f(x+y), f(x)+f(y)), "additive functional equation family")
    ck(close(fd(f, .4), a), "additive equation has constant derivative")
    ck(f(0) == 0, "additive functional equation normalization")

# Everywhere-existing but discontinuous derivative; Darboux-compatible oscillation.
f_osc = lambda x: x*x*math.sin(1/x) if x else 0.
fp_osc = lambda x: 2*x*math.sin(1/x)-math.cos(1/x)
for h in (-.1, -.01, .01, .1):
    ck(abs(f_osc(h)/h) <= abs(h), "oscillatory derivative squeeze at zero")
for n in range(1, 6):
    xn, yn = 1/(2*n*math.pi), 1/((2*n+1)*math.pi)
    ck(close(fp_osc(xn), -1), "derivative minus-one sequence")
    ck(close(fp_osc(yn), 1), "derivative plus-one sequence")
for x in (.03, .07, .16, .3):
    ck(close(fp_osc(-x), fp_osc(x)), "oscillatory derivative is even")
ck(f_osc(0) == 0 and abs(fd(f_osc, 0, 1e-5)) <= 1e-5, "zero derivative value at the oscillation centre")

# Rolle, MVT and derivative inequalities as a forward bridge.
ck((-1)**3-(-1) == 1**3-1 == 0, "Rolle equal endpoints")
for c in (-1/math.sqrt(3), 1/math.sqrt(3)):
    ck(close(3*c*c-1, 0) and -1 < c < 1, "Rolle stationary points")
ck((3**2-1**2)/(3-1) == 4 and 2*2 == 4 and 1 < 2 < 3, "MVT quadratic secant and point")
for a, b in ((0, .4), (-2, 1), (2, 2.5), (-3, -.5), (.7, -.7)):
    ck(abs(math.sin(a)-math.sin(b)) <= abs(a-b)+1e-14, "MVT sine Lipschitz inequality")
for x in (0, .2, 1., 3., 10.):
    ck(math.sin(x) <= x+1e-14, "sine upper bound for nonnegative x")
for x in (-3., -1., -.2, 0., .4, 2.):
    ck(math.exp(x) >= 1+x-1e-14, "exponential tangent inequality")
    ck(x == 0 or math.exp(x) > 1+x, "exponential inequality is strict away from zero")
for x in (.1, .3, .8, 1., 1.5, 3.):
    ck(math.log(x) <= x-1+1e-14, "logarithm tangent inequality")
    if x != 1:
        c = (x-1)/math.log(x)
        ck((1 < c < x) if x > 1 else (x < c < 1), "MVT logarithm point lies in the interval")
ck(math.log(1) == 0, "logarithm inequality equality case")

# Assertions against the actual editable JSON figures, not just the prose.
content = Path(__file__).resolve().parents[1] / "content"
specs = []
for path in sorted(content.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    for block in text.split(":::diagram\n")[1:]:
        specs.append(json.loads(block.split("\n:::", 1)[0]))
ck(len(specs) == 20, "editable diagram inventory")
ck(sum(s.get("type") == "graph" for s in specs) == 12, "editable graph inventory")
ck(sum(s.get("type") == "flow" for s in specs) == 5, "editable workflow inventory")
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

spec = by_title["The secant slope approaches the tangent slope"]
ck(all(close(value(c, 1), 1) for c in spec["curves"]), "actual parabola, secant and tangent meet at P")
ck(close(value(spec["curves"][0], 2), value(spec["curves"][1], 2)), "actual secant meets parabola at Q")
spec = by_title["A corner and a smooth flat join are different"]
ck(value(spec["curves"][0], -1) == value(spec["curves"][0], 1) == 1, "actual corner has unequal sides")
ck(close(value(spec["curves"][1], -1), -1) and close(value(spec["curves"][1], 1), 1), "actual smooth odd join")
spec = by_title["arctan(tan(x/2)) repeats the principal branch"]
for k, c in zip((-1, 0, 1), spec["curves"]):
    x = 2*k*math.pi+.7
    ck(close(value(c, x), .35), "actual inverse-trigonometric branch heights")
ck(len(spec["points"]) == 4 and all(p.get("face") == "white" for p in spec["points"]), "actual inverse-branch open endpoints")
spec = by_title["The implicit tangent is perpendicular to the radius"]
ck(all(close(value(c, 3), 4) for c in (spec["curves"][0], spec["curves"][2])), "actual circle and tangent share (3,4)")
ck(spec["rays"][0]["x"] == [0, 3] and spec["rays"][0]["y"] == [0, 4], "actual circle radius")
spec = by_title["Two reciprocal secants approach the tangent of slope -1"]
ck(all(close(value(c, 1), 1) for c in spec["curves"]), "actual reciprocal secants and tangent share P")
ck(all(close(value(spec["curves"][0], p["x"]), p["y"]) for p in spec["points"]), "actual reciprocal marked points")
spec = by_title["The line 2x-1 joins x^2 without a corner"]
ck(all(close(value(c, 1), 1) for c in spec["curves"]), "actual smooth-join curves share value")
ck(close((value(spec["curves"][0], 1)-value(spec["curves"][0], 1-1e-5))/1e-5, 2, 1e-4) and close(value(spec["curves"][1], 2)-value(spec["curves"][1], 1), 2), "actual smooth-join slopes")
spec = by_title["The inner factor 3 triples the initial slope"]
ck(all(close(value(c, 0), 0) for c in spec["curves"]), "actual sine curves and tangents share origin")
ck(close((value(spec["curves"][1], 1e-5)-value(spec["curves"][1], -1e-5))/(2e-5), 3, 1e-6), "actual scaled-sine initial slope")
spec = by_title["Two differentiation methods produce the same ellipse tangent"]
p = spec["points"][0]
ck(close(p["x"]**2/4+p["y"]**2, 1) and close(value(spec["curves"][2], p["x"]), p["y"]), "actual ellipse point and tangent")
ck(close(value(spec["curves"][0], p["x"]), p["y"]), "actual ellipse upper branch")
spec = by_title["The tangent to x^x at (1,1) is y=x"]
ck(all(close(value(c, 1), 1) for c in spec["curves"]), "actual variable-power curve and tangent")
ck(close(fd(lambda x: value(spec["curves"][0], x), 1), 1, 1e-5), "actual variable-power plotted slope")
spec = by_title["The semicubical parabola has slope 3 at t=2"]
ck(close(value(spec["curves"][0], 4), 8) and close(value(spec["curves"][1], 4), -8), "actual semicubical branches")
ck(close(value(spec["curves"][2], 4), 8) and close(value(spec["curves"][2], 2), 2), "actual semicubical tangent")
spec = by_title["This everywhere-existing derivative oscillates near zero"]
ck(spec["points"][0]["x"] == spec["points"][0]["y"] == 0, "actual oscillation centre value")
for n in (1, 2):
    ck(close(value(spec["curves"][1], 1/(2*n*math.pi)), -1), "actual plotted derivative sequence")
spec = by_title["The logarithm lies below its tangent upper bound x-1"]
for x in (.2, .5, 1., 2.):
    ck(value(spec["curves"][0], x) <= value(spec["curves"][1], x)+1e-12, "actual logarithm inequality curves")
ck(all(len(step["detail"]) < 90 for s in specs if s.get("type") == "flow" for step in s["steps"]), "workflow labels remain concise")
ck(all(len(row) == len(s["columns"]) for s in specs if s.get("type") == "table" for row in s["rows"]), "table rows match their columns")

# Targeted independent assertions for the six-page visual lab.
for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    ck(_condition, f"visual lab: {_name}")

print(f"Differentiability & Methods: {checks}/{checks} checks PASS")
