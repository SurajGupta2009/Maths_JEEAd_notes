#!/usr/bin/env python3
"""Independent exact, quadrature and editable-figure checks for Chapter 21."""
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


def simpson(f, a, b, n=2048):
    """Composite Simpson quadrature; independent of all stated antiderivatives."""
    if n % 2:
        n += 1
    h = (b-a)/n
    total = f(a)+f(b)
    total += 4*math.fsum(f(a+(2*k-1)*h) for k in range(1, n//2+1))
    total += 2*math.fsum(f(a+2*k*h) for k in range(1, n//2))
    return total*h/3


def quad_ck(f, a, b, expected, msg, n=2048, tol=3e-7):
    value = simpson(f, a, b, n)
    ck(close(value, expected, tol), f"{msg}: quadrature={value}, expected={expected}")
    return value


def fd(f, x, h=1e-4):
    return (f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))/(12*h)


# Riemann sums: finite sums, asymptotic limit and signed accumulation.
for n in (1, 2, 4, 10, 50, 200):
    direct = (2/n)*sum((2*i/n)**2 for i in range(1, n+1))
    closed = 4*(n+1)*(2*n+1)/(3*n*n)
    ck(close(direct, closed), f"Riemann finite-sum identity n={n}")
n = 100000
Rn = 4*(n+1)*(2*n+1)/(3*n*n)
ck(close((Rn-F(8, 3))*n, 4+4/(3*n), 2e-8), "Riemann error has the predicted first-order expansion")
quad_ck(lambda x: x*x, 0, 2, F(8, 3), "source x-squared area")
quad_ck(lambda x: x, 0, 1, .5, "unit-interval Riemann recognition")

# FTC, variable limits and the basic deferred source values.
quad_ck(lambda x: x*x, 0, 1, F(1, 3), "S9 FTC value")
quad_ck(lambda x: x**3, 0, 1, F(1, 4), "Q23 FTC value")
for x in (.2, .7, 1.4):
    ck(close(fd(lambda t: t**3/3, x), x*x), "S10 accumulation derivative")
    ck(close(fd(lambda t: t**4/4, x), x**3), "Q22 accumulation derivative")
for x in (.3, .7, 1.0):
    def G(t):
        return simpson(lambda u: math.exp(u*u), 0, t, 512)
    accumulated = lambda t: G(math.sin(t))-G(t*t)
    expected = math.exp(math.sin(x)**2)*math.cos(x)-2*x*math.exp(x**4)
    ck(close(fd(accumulated, x, 2e-4), expected, 2e-5), "variable-limit chain rule")

# Q7, Q10-Q12: definite substitutions with transformed limits.
quad_ck(lambda x: 2*x*math.exp(x*x), 0, 1, math.e-1, "P4/Q7 exponential substitution")
quad_ck(lambda x: 1/(1+x*x), 0, 1, math.pi/4, "Q10 arctangent limits")
quad_ck(lambda x: 1/(x*x+2*x+2), 0, 1, math.atan(2)-math.pi/4, "P5/Q11 completed-square limits")
quad_ck(lambda x: 1/math.sqrt(4-x*x), 0, 1, math.pi/6, "Q12 arcsine limits")
ck(close(math.atan(2)-math.pi/4, .3217505543966422), "Q11 independently stated decimal")

# Q17, Q20 and Q35: parts, partial fractions and half-angle.
quad_ck(lambda x: x*math.sin(x), 0, math.pi, math.pi, "Q17 definite by parts")
for x in (F(0), F(1, 3), F(1), F(3)):
    ck(F(1, (x+1)*(x+2)) == F(1, x+1)-F(1, x+2), "Q20 exact partial fractions")
quad_ck(lambda x: 1/((x+1)*(x+2)), 0, 1, math.log(F(4, 3)), "Q20 logarithmic limits")
quad_ck(lambda x: 1/(2+math.cos(x)), 0, math.pi/2, math.pi/(3*math.sqrt(3)), "S13/Q35 half-angle value")
for x in (0., .3, 1.0, math.pi/2):
    t = math.tan(x/2)
    ck(close(2/(3+t*t), 1/(2+math.cos(x))*2/(1+t*t)), "half-angle transformed integrand")

# Interval properties, King reflection and the Q36 source correction.
quad_ck(lambda x: x**3, -1, 1, 0, "S11/Q25 odd cubic")
quad_ck(lambda x: math.sin(x)**5, -math.pi/2, math.pi/2, 0, "P11 odd sine power")
quad_ck(lambda x: x*x, -1, 1, F(2, 3), "even-function doubling")
for a in (-2., .2, 1.3):
    left = simpson(lambda x: abs(math.sin(x)), a, a+math.pi, 1024)
    ck(close(left, 2, 3e-6), "periodic absolute-sine area")
quad_ck(lambda x: math.sin(x)**2, 0, math.pi/2, math.pi/4, "P10/Q24 King sine square")
quad_ck(lambda x: math.cos(x)**2, 0, math.pi/2, math.pi/4, "King reflected cosine square")

def tan_king(x):
    if close(x, math.pi/2, 1e-12):
        return 0.
    return 1/(1+math.tan(x))
quad_ck(tan_king, 0, math.pi/2, math.pi/4, "S12/Q26 King reciprocal tangent")
for x in (.1, .4, 1.0, 1.4):
    reflected = math.pi/2-x
    ck(close(tan_king(x)+tan_king(reflected), 1), "King reciprocal pair sums to one")
    ratio = math.sin(x)**2/(math.sin(x)**2+math.cos(x)**2)
    ck(close(ratio, math.sin(x)**2), "Q36 simplified integrand is sine squared")
ck(not close(math.sin(.3)**2, .5), "Q36 incorrect one-half prose is rejected")
quad_ck(lambda x: math.sin(x)**2/(math.sin(x)**2+math.cos(x)**2), 0, math.pi/2, math.pi/4, "Q36 corrected evaluation")

# Infinite p-integrals, exponential tails and comparison.
quad_ck(lambda x: math.exp(-x), 0, 40, 1, "P12/Q27 exponential improper value", n=4096)
for p in (1.5, 2., 3.):
    exact = 1/(p-1)
    finite = lambda R: (R**(1-p)-1)/(1-p)
    ck(close(finite(1e12), exact, 2e-6), f"infinite p-test value p={p}")
    numerical_with_tail = simpson(lambda x: x**(-p), 1, 50, 4096)+50**(1-p)/(p-1)
    ck(close(numerical_with_tail, exact, 3e-7), f"p-integral independent quadrature p={p}")
for p in (.5, 1.):
    finite = lambda R: math.log(R) if p == 1 else (R**(1-p)-1)/(1-p)
    ck(finite(1e8) > (10 if p == 1 else 1000), f"infinite p-test divergence p={p}")
arctan_with_tail = simpson(lambda x: 1/(1+x*x), 1, 50, 4096)+(math.pi/2-math.atan(50))
ck(close(arctan_with_tail, math.pi/4, 3e-7), "arctangent infinite tail")

# Finite singularities and all source logarithmic limits.
for p in (-1., 0., .5, .8):
    exact = 1/(1-p)
    finite = lambda e: (1-e**(1-p))/(1-p)
    ck(close(finite(1e-60), exact, 2e-6), f"finite p-test value p={p}")
for p in (1., 2.):
    finite = lambda e: -math.log(e) if p == 1 else (1-e**(1-p))/(1-p)
    ck(finite(1e-10) > (20 if p == 1 else 1000), f"finite p-test divergence p={p}")
U = 45.
quad_ck(lambda u: u*math.exp(-u), 0, U, 1, "P13 logarithmic endpoint integral", n=4096)
quad_ck(lambda u: u*math.exp(-2*u), 0, U, .25, "Q28 x log x transformed integral", n=4096)
quad_ck(lambda u: u*u*math.exp(-u), 0, U, 2, "P14/Q29 squared logarithm", n=4096)
for k in (1, 2):
    ck(abs(1e-12*math.log(1e-12)**k) < 1e-9, f"endpoint x log^k vanishes k={k}")
ck(abs(1e-6**2*math.log(1e-6)) < 1e-7, "endpoint x^2 log vanishes")

# P15/Q31: absolute convergence and inversion on both transformed tails.
Jpos = simpson(lambda u: u*math.exp(-u)/(1+math.exp(-2*u)), 0, U, 4096)
Jleft = simpson(lambda u: -u*math.exp(-u)/(1+math.exp(-2*u)), 0, U, 4096)
Jright = simpson(lambda u: u*math.exp(-u)/(1+math.exp(-2*u)), 0, U, 4096)
ck(Jpos > 0 and Jpos < 1, "inversion component is finite")
ck(close(Jleft+Jright, 0), "P15/Q31 inversion gives zero")
ck(2*Jpos < 2, "inversion integral converges absolutely")

# Signed and geometric areas in all slicing modes.
quad_ck(lambda x: x**3, -1, 1, 0, "cubic signed area")
quad_ck(lambda x: abs(x**3), -1, 1, .5, "cubic total area")
quad_ck(lambda x: x-x*x, 0, 1, F(1, 6), "line-parabola vertical area")
quad_ck(lambda x: math.sin(x), 0, math.pi, 2, "P9 sine arch")
quad_ck(lambda y: y+2-y*y, -1, 2, 4.5, "horizontal-strip area")
first = simpson(lambda x: math.cos(x)-math.sin(x), 0, math.pi/4, 1024)
second = simpson(lambda x: math.sin(x)-math.cos(x), math.pi/4, math.pi/2, 1024)
ck(close(first, math.sqrt(2)-1) and close(second, math.sqrt(2)-1), "split sine-cosine pieces")
ck(close(first+second, 2*math.sqrt(2)-2), "split sine-cosine total")
ellipse_value = simpson(lambda x: 2*math.sqrt(max(0., 1-x*x/4)), -2, 2, 8192)
ck(close(ellipse_value, 2*math.pi, 3e-6), "ellipse vertical-slice area")

# Wallis recurrences, closed forms and the actual product.
def wallis(n):
    if n == 0:
        return math.pi/2
    if n == 1:
        return 1.
    return (n-1)/n*wallis(n-2)


def dfact(n):
    return 1 if n <= 0 else n*dfact(n-2)


for n in range(2, 31):
    ck(close(wallis(n), (n-1)/n*wallis(n-2)), f"Wallis recurrence n={n}")
for m in range(1, 13):
    even = F(dfact(2*m-1), dfact(2*m))*math.pi/2
    odd = F(dfact(2*m), dfact(2*m+1))
    ck(close(wallis(2*m), even), "Wallis even closed form")
    ck(close(wallis(2*m+1), odd), "Wallis odd closed form")
    ck(wallis(2*m+1) < wallis(2*m) < wallis(2*m-1), "Wallis squeeze ordering")
ck(close(wallis(5), F(8, 15)), "additional Wallis odd value")
ck(close(wallis(6), 5*math.pi/32), "S15/Q30 Wallis even value")
quad_ck(lambda x: math.sin(x)**6, 0, math.pi/2, 5*math.pi/32, "Q30 independent quadrature")
product = 1.
for k in range(1, 1001):
    product *= (2*k)/(2*k-1)*(2*k)/(2*k+1)
    if k in (1, 2, 5, 20):
        ck(0 < product < math.pi/2, "Wallis partial-product bound")
ck(close(product, math.pi/2, 8e-4), "Wallis product approaches pi/2")
ck(close(wallis(40)/wallis(41), 1, .03), "Wallis adjacent ratio tends to one")

# Beta/Gamma definitions, the canonical source values and corrected substitutions.
for p, q in ((.5, .5), (3., 2.), (.7, 1.3), (1.5, 2.5)):
    trig = lambda x: 2*math.sin(x)**(2*p-1)*math.cos(x)**(2*q-1)
    exact = math.exp(math.lgamma(p)+math.lgamma(q)-math.lgamma(p+q))
    quad_ck(trig, 0, math.pi/2, exact, f"Beta Gamma identity p={p}, q={q}", n=32768, tol=8e-7)
ck(close(math.exp(math.lgamma(3)+math.lgamma(2)-math.lgamma(5)), F(1, 12)), "additional Beta factorial value")
ck(close(math.gamma(.5)**2, math.pi), "S18/Q39 Beta one-half value")
q40_exact = math.sqrt(math.pi)/(2*math.sqrt(2))*math.gamma(3/4)/math.gamma(5/4)
quad_ck(lambda x: math.sqrt(math.sin(x)*math.cos(x)), 0, math.pi/2, q40_exact, "Q40 Beta square-root product", n=32768, tol=8e-7)
ck(close(q40_exact, .8472130847939789), "Q40 independently stated decimal")
q43_beta = math.sqrt(math.pi)/2*math.gamma(7/2)/math.gamma(4)
ck(close(q43_beta, 5*math.pi/32), "S19/Q43 Beta-Gamma Wallis value")
for z in (.5, 1., 1.5, 2., 3.):
    transformed = lambda u: 2*u**(2*z-1)*math.exp(-u*u)
    quad_ck(transformed, 0, 7, math.gamma(z), f"Gamma integral z={z}", n=4096, tol=1e-6)
for z in (.1, .25, .5, .7, .9):
    ck(close(math.gamma(z)*math.gamma(1-z), math.pi/math.sin(math.pi*z), 2e-8), "Q42 Gamma reflection identity")
for z in (.2, .25, .5, .8, 1.4):
    left = math.gamma(z)*math.gamma(z+.5)
    right = 2**(1-2*z)*math.sqrt(math.pi)*math.gamma(2*z)
    ck(close(left, right, 2e-8), "Q44 Legendre duplication identity")
ck(close(math.gamma(.5), math.sqrt(math.pi)), "duplication at one-half reduces correctly")
ck(not close(math.pi, 2*math.sqrt(math.pi)), "source duplication contradiction is rejected")
ck(close(math.gamma(.25)*math.gamma(.75), math.sqrt(2)*math.pi), "P18/Q41 duplication at one-quarter")

# S16/Q32, P16/Q33, Q46 and an additional cosine transform.
gaussian = quad_ck(lambda x: math.exp(-x*x), 0, 12, math.sqrt(math.pi)/2, "S16/Q32 Gaussian", n=4096, tol=1e-8)
ck(close(2*gaussian, math.sqrt(math.pi)), "full-line Gaussian")
q33 = 2*simpson(lambda x: math.exp(-2*x*x), 0, 12, 4096)
ck(close(q33, math.sqrt(math.pi/2), 1e-8), "P16/Q33 scaled Gaussian")
for a, b in ((.5, 0.), (1., 2.), (2., -1.), (3., .7)):
    expected = math.sqrt(math.pi/a)*math.exp(b*b/(4*a))
    quad_ck(lambda x: math.exp(-a*x*x+b*x), -15, 15, expected, f"Q46 general Gaussian a={a}, b={b}", n=8192, tol=2e-7)
for a in (0., .5, 1., 1.7):
    exact = math.sqrt(math.pi)/2*math.exp(-a*a)
    quad_ck(lambda x: math.exp(-x*x)*math.cos(2*a*x), 0, 12, exact, f"additional cosine transform a={a}", n=4096, tol=2e-7)
    ck(close(fd(lambda b: math.sqrt(math.pi)/2*math.exp(-b*b), a), -2*a*exact), "cosine-transform differential equation")

# Canonical exponential Frullani values and additional damped oscillatory examples.
for a, b in ((1., 2.), (3., 5.)):
    def ef(x):
        if x == 0:
            return b-a
        return (math.exp(-a*x)-math.exp(-b*x))/x
    label = "S17/Q34" if a == 1 else "P17/Q38"
    quad_ck(ef, 0, 60, math.log(b/a), f"{label} exponential Frullani", n=8192, tol=3e-7)
for a, b in ((1., 2.), (.5, 2.), (2., .7)):
    for delta in (.2, 1.):
        def cf(x):
            if x == 0:
                return 0.
            return math.exp(-delta*x)*(math.cos(a*x)-math.cos(b*x))/x
        def sf(x):
            if x == 0:
                return a-b
            return math.exp(-delta*x)*(math.sin(a*x)-math.sin(b*x))/x
        cexact = .5*math.log((delta*delta+b*b)/(delta*delta+a*a))
        sexact = -(math.atan(b/delta)-math.atan(a/delta))
        quad_ck(cf, 0, 60, cexact, f"additional damped cosine Frullani a={a}, b={b}, d={delta}", n=12000, tol=3e-6)
        quad_ck(sf, 0, 60, sexact, f"corrected damped sine Frullani a={a}, b={b}, d={delta}", n=12000, tol=3e-6)
    ck(close(.5*math.log(b*b/(a*a)), math.log(b/a)), "additional cosine Abel limit")
    tiny_delta = 1e-8
    sine_limit = -(math.atan(b/tiny_delta)-math.atan(a/tiny_delta))
    ck(close(sine_limit, 0, 1e-7), "corrected sine-difference Abel limit is zero")
ck(close(.5*math.log((1e-12+4)/(1e-12+1)), math.log(2)), "additional cosine a1 b2 value")

# Feynman power derivatives, Q45 and the damped family used by Q37.
for a in (-.5, 0., 1., 3.):
    ck(close(fd(lambda b: 1/(b+1), a), -1/(a+1)**2), "S14/Q28 Feynman first derivative")
    ck(close(fd(lambda b: -1/(b+1)**2, a), 2/(a+1)**3), "P14/Q29 Feynman second derivative")
for a in (-.5, 0., 1., 3., 5.):
    def log_parameter(u):
        if u == 0:
            return a
        return (math.exp(-u)-math.exp(-(a+1)*u))/u
    quad_ck(log_parameter, 0, 50, math.log1p(a), f"Q45 Feynman log family a={a}", n=4096, tol=1e-6)
for x in (.2, .7, 2.):
    for a in (-.5, 3.):
        represented = simpson(lambda t: math.exp(t*math.log(x)), 0, a, 1024)
        exact = (x**a-1)/math.log(x)
        ck(close(represented, exact, 2e-7), "Q45 lower limit zero representation")
        if a == 3:
            wrong_lower = (x**a-x)/math.log(x)
            ck(not close(wrong_lower, exact), "Q45 printed lower limit one is rejected")
ck(close(math.log1p(3), math.log(4)), "Q45 final value ln4")
for t in (.5, 1., 2.):
    def damped(x):
        return 1. if x == 0 else math.exp(-t*x)*math.sin(x)/x
    exact = math.pi/2-math.atan(t)
    quad_ck(damped, 0, 60, exact, f"Q37 damped sine family t={t}", n=12000, tol=3e-6)
    quad_ck(lambda x: math.exp(-t*x)*math.sin(x), 0, 60, 1/(1+t*t), f"Q37 damped derivative t={t}", n=12000, tol=3e-6)
ck(close(math.pi/2-math.atan(1), math.pi/4), "additional damped t1 anchor")

# Q37 Dirichlet: accelerated independent arch sum and a harmonic absolute-area bound.
def dirichlet_integrand(x):
    return 1. if x == 0 else math.sin(x)/x

arches = [simpson(dirichlet_integrand, n*math.pi, (n+1)*math.pi, 80) for n in range(513)]
I512 = math.fsum(arches[:512])
I513 = I512+arches[512]
accelerated = (I512+I513)/2
ck(close(accelerated, math.pi/2, 2e-5), f"Q37 Dirichlet accelerated value {accelerated}")
ck(all((-1)**n*arches[n] > 0 for n in range(30)), "Dirichlet arches alternate")
absolute_lower = math.fsum(1/(3*(n+1)) for n in range(1, 201))
ck(absolute_lower > 1.5, "Dirichlet absolute area dominates a divergent harmonic sum")

# Additional special values: independent transformed quadratures.
rational_tail = lambda t: 0. if t == math.pi/2 else 1/((math.tan(t)**2+1)*(math.tan(t)**2+4))/(math.cos(t)**2)
quad_ck(rational_tail, 0, math.pi/2, math.pi/12, "additional rational infinite tail", n=4096)
quartic_tail = lambda t: 0. if t == math.pi/2 else 1/(1+math.tan(t)**4)/(math.cos(t)**2)
quad_ck(quartic_tail, 0, math.pi/2, math.pi/(2*math.sqrt(2)), "additional quartic infinite tail", n=4096)
for x in (F(0), F(1), F(3)):
    ck(F(1, (x*x+1)*(x*x+4)) == F(1, 3)/(x*x+1)-F(1, 3)/(x*x+4), "additional exact partial fractions")
log_sine = lambda t: 0. if t == 0 else 2*t*math.log(math.sin(t*t))
quad_ck(log_sine, 0, math.sqrt(math.pi/2), -math.pi/2*math.log(2), "additional logarithmic sine", n=8192, tol=2e-6)
for x in (.1, .4, .8, 1.2):
    reflected = math.pi/2-x
    ck(close(math.log(math.tan(x)), -math.log(math.tan(reflected))), "additional log-tangent reflection")

# Assertions against the actual editable JSON figures.
content = Path(__file__).resolve().parents[1] / "content"
specs = []
for path in sorted(content.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    for block in text.split(":::diagram\n")[1:]:
        specs.append(json.loads(block.split("\n:::", 1)[0]))
ck(len(specs) == 24, "editable diagram inventory")
ck(sum(s.get("type") == "graph" for s in specs) == 11, "editable graph inventory")
ck(sum(s.get("type") == "flow" for s in specs) == 6, "editable workflow inventory")
ck(sum(s.get("type") == "table" for s in specs) == 7, "editable table inventory")
by_title = {s["title"]: s for s in specs}
ck(len(by_title) == len(specs), "unique figure titles")


def value(curve, x):
    y = np.asarray(_eval_expr(curve["expr"], np.array([float(x)])))
    return float(y.reshape(-1)[0])


def curve_fn(curve):
    return lambda x: value(curve, x)


for spec in specs:
    for curve in spec.get("curves", []):
        lo = curve.get("from", spec.get("xrange", [-6, 6])[0])
        hi = curve.get("to", spec.get("xrange", [-6, 6])[1])
        for j in range(1, 6):
            ck(math.isfinite(value(curve, lo+(hi-lo)*j/6)), f"finite plotted expression: {spec['title']}")
    for fill in spec.get("fills", []):
        for key in ("y1", "y2"):
            if isinstance(fill[key], str):
                pseudo = {"expr": fill[key]}
                ck(math.isfinite(value(pseudo, (fill["from"]+fill["to"])/2)), f"finite fill expression: {spec['title']}")
ck(all(len(row) == len(s["columns"]) for s in specs if s.get("type") == "table" for row in s["rows"]), "table rows match columns")
ck(all(len(step["detail"]) < 120 for s in specs if s.get("type") == "flow" for step in s["steps"]), "workflow labels remain concise")

spec = by_title["Four right-endpoint rectangles for y=x^2 on [0,2]"]
ck(len(spec["rectangles"]) == 4, "actual rectangle inventory")
ck(all(close(r["height"], (r["x"]+r["width"])**2) for r in spec["rectangles"]), "actual right-endpoint heights")
ck(close(sum(r["width"]*r["height"] for r in spec["rectangles"]), 3.75), "actual rectangle sum")
spec = by_title["Height f(x)=2x and accumulation A(x)=x^2"]
for x in (.4, 1., 1.6):
    ck(close(fd(curve_fn(spec["curves"][1]), x), value(spec["curves"][0], x), 2e-6), "actual FTC figure derivative")
ck(all(close(value(spec["curves"][1], p["x"]), p["y"]) for p in spec["points"]), "actual FTC accumulation points")
spec = by_title["Mirror-related integrands on [0,pi/2]"]
for x in (.1, .4, .8, 1.3):
    ck(close(value(spec["curves"][0], x)+value(spec["curves"][1], x), 1), "actual King curves sum to one")
spec = by_title["The exponential area on [0,infinity) equals one"]
ck(close(value(spec["curves"][0], 2), math.exp(-2)), "actual exponential split height")
ck(close(quad := simpson(curve_fn(spec["curves"][0]), 0, 2, 1024), 1-math.exp(-2)), "actual exponential gold area")
ck(0 < quad < 1, "actual exponential finite-part bound")
spec = by_title["The cubic on [-1,1] has signed integral zero"]
ck(all(close(value(spec["curves"][0], p["x"]), p["y"]) for p in spec["points"]), "actual cubic point anchors")
ck(close(simpson(curve_fn(spec["curves"][0]), -1, 1, 1024), 0), "actual cubic signed integral")
spec = by_title["The area between y=x and y=x^2 is one-sixth"]
ck(close(value(spec["curves"][0], .4)-value(spec["curves"][1], .4), .24), "actual vertical-slice height")
ck(all(close(value(spec["curves"][0], p["x"]), p["y"]) for p in spec["points"]), "actual line-parabola intersections")
spec = by_title["Vertical slices of an ellipse give area pi ab"]
for x in (-1.5, -.5, .5, 1.5):
    ck(close(value(spec["curves"][0], x), -value(spec["curves"][1], x)), "actual ellipse upper and lower branches")
spec = by_title["Two positive regions between sine and cosine"]
p = spec["points"][0]
ck(close(value(spec["curves"][0], p["x"]), p["y"]) and close(value(spec["curves"][1], p["x"]), p["y"]), "actual sine-cosine intersection")
spec = by_title["A cosine Frullani integrand with a1 and b2"]
ck(abs(value(spec["curves"][0], 1e-5)) < 1e-4, "actual Frullani removable origin limit")
ck(close(value(spec["curves"][0], 1), math.cos(1)-math.cos(2)), "actual Frullani curve anchor")
spec = by_title["Alternating Dirichlet arches have a finite signed sum"]
ck(spec["points"][0]["y"] == 1 and len(spec["fills"]) == 4, "actual Dirichlet continuous extension and fills")
ck(value(spec["curves"][0], math.pi) < 1e-12, "actual Dirichlet zero")
spec = by_title["Two positive rational tails with exact areas"]
ck(close(value(spec["curves"][0], 1), .5), "actual quartic-tail curve anchor")
ck(close(value(spec["curves"][1], 0), .25), "actual rational-tail curve anchor")

# Targeted independent assertions for the six-page visual lab.
for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    ck(_condition, f"visual lab: {_name}")

print(f"Definite Integration & Areas: {checks}/{checks} checks PASS")
