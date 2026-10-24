#!/usr/bin/env python3
"""Independent derivative, exact-identity and editable-figure checks for Chapter 20."""
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


def fd(f, x, h=1e-4):
    """Fourth-order central derivative, used as an independent oracle."""
    return (f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))/(12*h)


def deriv(Fn, fn, x, msg, tol=3e-6):
    ck(close(fd(Fn, x), fn(x), tol), f"{msg} at x={x}")


# Basic library, constants and initial conditions.
for x in (-2., -.4, .3, 1.7):
    deriv(lambda t: t**4/4, lambda t: t**3, x, "S1 power antiderivative")
    deriv(lambda t: t**6/6, lambda t: t**5, x, "Q1 power antiderivative")
    deriv(lambda t: t**3+t**2+t, lambda t: 3*t**2+2*t+1, x, "Q2 polynomial")
    deriv(lambda t: t**3+t**2, lambda t: 3*t**2+2*t, x, "P1 polynomial")
    deriv(lambda t: math.exp(2*t)/2, lambda t: math.exp(2*t), x, "Q3 exponential")
    deriv(lambda t: math.exp(3*t)/3, lambda t: math.exp(3*t), x, "P2 exponential")
    deriv(lambda t: -math.cos(2*t)/2, lambda t: math.sin(2*t), x, "S2 scaled sine")
    deriv(lambda t: t**3+t**2+t+5, lambda t: 3*t**2+2*t+1, x, "initial-value derivative")
ck(0**3+0**2+0+5 == 5, "initial condition selects C")
for x in (-2., -.5, .5, 2.):
    deriv(lambda t: -1/t, lambda t: 1/t**2, x, "negative power")
    deriv(lambda t: math.log(abs(t)), lambda t: 1/t, x, "absolute logarithm")
for x in (.2, .7, 1.2):
    deriv(lambda t: 2*t**1.5/3+2*t**.5, lambda t: t**.5+t**-.5, x, "algebraic preparation")
    deriv(lambda t: -math.cos(t), lambda t: math.sin(t), x, "sine library")
    deriv(lambda t: math.sin(t), lambda t: math.cos(t), x, "cosine library")
    deriv(lambda t: math.tan(t), lambda t: 1/math.cos(t)**2, x, "secant-square library")
    deriv(lambda t: -1/math.tan(t), lambda t: 1/math.sin(t)**2, x, "cosecant-square library")
    deriv(lambda t: 1/math.cos(t), lambda t: math.sin(t)/math.cos(t)**2, x, "secant-tangent library")
for c1, c2 in ((-2., 0.), (0., 2.), (-2., 2.)):
    ck(close((1**2+c1)-(1**2+c2), c1-c2), "vertical family difference")
    ck(close(fd(lambda t: t*t+c1, 1), fd(lambda t: t*t+c2, 1)), "constant does not change slope")

# Substitution and linear inner scales.
for x in (-1.5, -.2, .4, 1.3):
    deriv(lambda t: (t*t+1)**6/6, lambda t: 2*t*(t*t+1)**5, x, "S3 substitution")
    deriv(lambda t: (t*t+3)**5/5, lambda t: 2*t*(t*t+3)**4, x, "Q5 substitution")
    deriv(lambda t: math.exp(t*t)/2, lambda t: t*math.exp(t*t), x, "S4/Q6 substitution")
    deriv(lambda t: math.sin(3*t-1)/3, lambda t: math.cos(3*t-1), x, "linear inner sine")
    deriv(lambda t: (2*t+1)**5/10, lambda t: (2*t+1)**4, x, "linear inner power")
ck(not close(fd(lambda t: (t*t+1)**6/6, 1), (1+1)**5), "missing derivative factor is rejected")
ck(close(fd(lambda t: math.exp(t*t)/2, 0), 0), "zero derivative factor at origin")

# Logarithmic substitution and trigonometric logarithms.
for x in (-2., -1., 0., 2.):
    if x != -F(2, 3):
        deriv(lambda t: math.log(abs(3*t+2))/3, lambda t: 1/(3*t+2), x, "Q4 scaled log")
for x in (-2., -.3, .5, 2.):
    D = lambda t: t*t+2*t+2
    deriv(lambda t: math.log(D(t)), lambda t: (2*t+2)/D(t), x, "complete derivative numerator")
    deriv(lambda t: math.log(3*t*t+5), lambda t: 6*t/(3*t*t+5), x, "exact scaled quotient")
    deriv(lambda t: math.log(3*t*t+5)/6, lambda t: t/(3*t*t+5), x, "one-sixth scaled quotient")
for x in (-.7, .4, 1., 2.5):
    deriv(lambda t: math.log(abs(1/math.cos(t))), lambda t: math.tan(t), x, "P3/Q8 tangent")
for x in (-2.5, -.7, .4, 2.):
    deriv(lambda t: math.log(abs(math.sin(t))), lambda t: 1/math.tan(t), x, "cotangent log")
for x in (-.7, .4, 1., 2.8):
    deriv(lambda t: math.log(abs(1/math.cos(t)+math.tan(t))), lambda t: 1/math.cos(t), x, "secant log")
for x in (-2.5, -.7, .4, 2.):
    deriv(lambda t: math.log(abs(1/math.sin(t)-1/math.tan(t))), lambda t: 1/math.sin(t), x, "cosecant log")

# Trigonometric preparation and equivalent answers.
for x in (-2., -.3, .4, 1.4, 2.2):
    deriv(lambda t: math.sin(t)**4/4, lambda t: math.sin(t)**3*math.cos(t), x, "Q9 sine power")
    deriv(lambda t: -math.cos(t)+math.cos(t)**3/3, lambda t: math.sin(t)**3, x, "odd sine power")
    deriv(lambda t: t/2-math.sin(2*t)/4, lambda t: math.sin(t)**2, x, "even sine power")
    deriv(lambda t: t/2+math.sin(2*t)/4, lambda t: math.cos(t)**2, x, "even cosine power")
    A = lambda t: .5*math.sin(t)**2
    B = lambda t: -.5*math.cos(t)**2
    C = lambda t: -.25*math.cos(2*t)
    target = lambda t: math.sin(t)*math.cos(t)
    deriv(A, target, x, "equivalent answer A")
    deriv(B, target, x, "equivalent answer B")
    deriv(C, target, x, "equivalent answer C")
    ck(close(A(x)-B(x), .5), "A-B is exactly one-half")
    ck(close(A(x)-C(x), .25), "A-C is exactly one-quarter")
    ck(close(math.sin(x)**2, (1-math.cos(2*x))/2), "sine half-angle identity")
    ck(close(math.cos(x)**2, (1+math.cos(2*x))/2), "cosine half-angle identity")

# Inverse-trigonometric standard forms and completion of squares.
for x in (-2., -.4, .3, 1.5):
    deriv(lambda t: math.atan(t+1), lambda t: 1/(t*t+2*t+2), x, "S5 completed square")
    deriv(lambda t: math.atan(t/2)/2, lambda t: 1/(t*t+4), x, "Q13 arctangent")
    deriv(lambda t: math.atan(t), lambda t: 1/(1+t*t), x, "arctangent library")
    deriv(lambda t: math.atan(2*t/3)/6, lambda t: 1/(4*t*t+9), x, "scaled arctangent")
for x in (-1.5, -.3, .4, 1.5):
    deriv(lambda t: math.asin(t/2), lambda t: 1/math.sqrt(4-t*t), x, "Q12 arcsine antiderivative")

# Difference-of-squares and radical forms on each valid branch.
for a in (.5, 1., 2.):
    for x in (-2*a-1, -1.2*a, 1.2*a, 2*a+1):
        if abs(x) > a:
            deriv(lambda t, a=a: math.log(abs((t-a)/(t+a)))/(2*a), lambda t, a=a: 1/(t*t-a*a), x, "Q21 difference of squares")
            deriv(lambda t, a=a: math.log(abs(t+math.sqrt(t*t-a*a))), lambda t, a=a: 1/math.sqrt(t*t-a*a), x, "radical difference branch")
    for x in (-.7*a, 0., .6*a):
        deriv(lambda t, a=a: math.log(abs((a+t)/(a-t)))/(2*a), lambda t, a=a: 1/(a*a-t*t), x, "reversed difference of squares")
        deriv(lambda t, a=a: t*math.sqrt(a*a-t*t)/2+a*a*math.asin(t/a)/2, lambda t, a=a: math.sqrt(a*a-t*t), x, "semicircle antiderivative")
    for x in (-2., -.2, .7, 3.):
        deriv(lambda t, a=a: math.log(t+math.sqrt(t*t+a*a)), lambda t, a=a: 1/math.sqrt(t*t+a*a), x, "radical sum logarithm")
for a, x in ((F(1), F(3)), (F(2), F(5)), (F(3), F(7))):
    lhs = F(1, x*x-a*a)
    rhs = (F(1, x-a)-F(1, x+a))/(2*a)
    ck(lhs == rhs, "exact partial-fraction identity for difference of squares")

# Integration by parts, including cyclic and algebraic products.
for x in (-1.5, -.2, .4, 1.3):
    deriv(lambda t: math.exp(t)*(t-1), lambda t: t*math.exp(t), x, "S6/Q14 by parts")
    deriv(lambda t: math.exp(t)*(t*t-2*t+2), lambda t: t*t*math.exp(t), x, "P6/Q16 repeated parts")
    deriv(lambda t: math.exp(t)*(t**3-3*t*t+6*t-6), lambda t: t**3*math.exp(t), x, "cubic exponential reduction")
    deriv(lambda t: -t*math.cos(t)+math.sin(t), lambda t: t*math.sin(t), x, "Q17 antiderivative")
    deriv(lambda t: math.exp(t)*(math.sin(t)-math.cos(t))/2, lambda t: math.exp(t)*math.sin(t), x, "P7/Q18 cyclic parts")
    deriv(lambda t: (t*t+1)*math.atan(t)/2-t/2, lambda t: t*math.atan(t), x, "algebraic arctangent product")
for x in (.2, .7, 1.5, 3.):
    deriv(lambda t: t*math.log(t)-t, lambda t: math.log(t), x, "S7/Q15 logarithm")
for x in (-1.2, -.2, .4, 1.1):
    deriv(lambda t: t*math.atan(t)-math.log(1+t*t)/2, lambda t: math.atan(t), x, "inverse by parts")
ck(not close(fd(lambda t: math.exp(t)*(math.sin(t)-math.cos(t)), .7), math.exp(.7)*math.sin(.7)), "missing cyclic one-half is rejected")

# Partial fractions: exact decompositions, all branches and the P8 correction.
for x in (F(-3), F(-3, 2), F(0), F(1), F(4)):
    xx = float(x)
    deriv(lambda t: math.log(abs((t+1)/(t+2))), lambda t: 1/((t+1)*(t+2)), xx, "S8/Q19 log ratio")
    ck(F(1, (x+1)*(x+2)) == F(1, x+1)-F(1, x+2), "exact distinct-linear decomposition")
for x in (-3., -1.5, 0., 2.):
    deriv(lambda t: 2*math.log(abs(t+1))-1/(t+1), lambda t: (2*t+3)/(t+1)**2, x, "repeated linear factor")
    deriv(lambda t: t*t/2-t+2*math.log(abs(t+1)), lambda t: (t*t+1)/(t+1), x, "polynomial division first")
for x in (-2., -.3, .5, 2.):
    D = lambda t: t*t+2*t+2
    correct = lambda t: math.log(D(t))/2
    target = lambda t: (t+1)/D(t)
    deriv(correct, target, x, "corrected P8")
    wrong = lambda t: correct(t)+math.atan(t+1)/2
    ck(close(fd(wrong, x), target(x)+1/(2*D(x)), 3e-6), "P8 extra derivative measured independently")
    ck(not close(fd(wrong, x), target(x), 3e-6), "incorrect P8 answer is rejected")
    ck(close((x+1)-.5*(2*x+2), 0), "P8 remainder is exactly zero")
    D5 = lambda t: t*t+2*t+5
    deriv(lambda t: 1.5*math.log(D5(t))+math.atan((t+1)/2), lambda t: (3*t+5)/D5(t), x, "log plus arctangent quadratic")
    ck(close(3*x+5, 1.5*(2*x+2)+2), "quadratic numerator split")
for A, B, p in ((F(1), F(1), F(2)), (F(3), F(5), F(2)), (F(-2), F(7), F(-4))):
    alpha, beta = A/2, B-A*p/2
    for x in (F(-1), F(0), F(2)):
        ck(A*x+B == alpha*(2*x+p)+beta, "exact alpha-beta numerator decomposition")

# Half-angle substitution and branch-aware equivalent forms.
for x in (-2.5, -1., 0., .7, 2.5):
    Fn = lambda t: 2/math.sqrt(3)*math.atan(math.tan(t/2)/math.sqrt(3))
    deriv(Fn, lambda t: 1/(2+math.cos(t)), x, "S13/Q35 half-angle antiderivative")
ck(close((2/math.sqrt(3)*math.atan(math.tan((math.pi/2)/2)/math.sqrt(3))), math.pi/(3*math.sqrt(3))), "half-angle anchor at pi/2")
for x in (-2., -.5, .3, 2.):
    deriv(lambda t: -2/(1+math.tan(t/2)), lambda t: 1/(1+math.sin(t)), x, "half-angle sine denominator")
for x in (-1., -.3, .4, 1.):
    deriv(lambda t: math.tan(t)-1/math.cos(t), lambda t: 1/(1+math.sin(t)), x, "equivalent sine-denominator antiderivative")
    difference = -2/(1+math.tan(x/2))-(math.tan(x)-1/math.cos(x))
    ck(close(difference, -1), "equivalent half-angle forms differ by constant")

# Euler substitution: rationalisation, initial condition and differential identity.
for a in (.5, 1., 2.):
    for x in (-2., -.3, .4, 2.):
        s = math.sqrt(x*x+a*a)
        t = x+s
        ck(t > 0, "Euler t is positive")
        ck(close((t*t-a*a)/(2*t), x), "Euler x(t)")
        ck(close((t*t+a*a)/(2*t), s), "Euler s(t)")
        x_of_t = lambda u, a=a: (u*u-a*a)/(2*u)
        s_of_t = lambda u, a=a: (u*u+a*a)/(2*u)
        ck(close(fd(x_of_t, t)/s_of_t(t), 1/t, 3e-6), "Euler dx/s=dt/t")
    for x in (-1., .2, 1.5):
        deriv(lambda u, a=a: math.log(u+math.sqrt(u*u+a*a)), lambda u, a=a: 1/math.sqrt(u*u+a*a), x, "Euler antiderivative")
F_init = lambda x: math.log((x+math.sqrt(x*x+4))/2)
ck(close(F_init(0), 0), "Euler initial condition")
for x in (-1., .3, 2.):
    deriv(F_init, lambda t: 1/math.sqrt(t*t+4), x, "Euler initial-value derivative")

# Reduction formulae checked recursively and against closed forms.
def I_exp(n, x):
    if n == 0:
        return math.exp(x)
    return x**n*math.exp(x)-n*I_exp(n-1, x)


def J_log(n, x):
    if n == 0:
        return x
    return x*math.log(x)**n-n*J_log(n-1, x)


def S_sin(n, x):
    if n == 0:
        return x
    if n == 1:
        return -math.cos(x)
    return -math.sin(x)**(n-1)*math.cos(x)/n+(n-1)/n*S_sin(n-2, x)


for n in range(1, 7):
    for x in (-.7, .2, 1.1):
        deriv(lambda t, n=n: I_exp(n, t), lambda t, n=n: t**n*math.exp(t), x, f"exponential reduction n={n}")
for n in range(1, 6):
    for x in (.25, .8, 1.7):
        deriv(lambda t, n=n: J_log(n, t), lambda t, n=n: math.log(t)**n, x, f"logarithmic reduction n={n}")
for n in range(2, 8):
    for x in (-.6, .3, 1.2):
        deriv(lambda t, n=n: S_sin(n, t), lambda t, n=n: math.sin(t)**n, x, f"sine reduction n={n}")
S6_closed = lambda x: (-math.sin(x)**5*math.cos(x)/6-5*math.sin(x)**3*math.cos(x)/24-5*math.sin(x)*math.cos(x)/16+5*x/16)
for x in (-1., -.2, .5, 1.4):
    ck(close(S6_closed(x), S_sin(6, x)), "S6 closed form equals recursive form")
    deriv(S6_closed, lambda t: math.sin(t)**6, x, "S6 displayed closed form")

# Parameter differentiation: first and second logarithmic derivatives.
for a in (-.5, 0., 1., 2.):
    for x in (.25, .8, 1.7):
        Fn = lambda t, a=a: t**(a+1)*((a+1)*math.log(t)-1)/(a+1)**2
        deriv(Fn, lambda t, a=a: t**a*math.log(t), x, f"parameter first derivative a={a}")
        Gn = lambda t, a=a: t**(a+1)*(math.log(t)**2/(a+1)-2*math.log(t)/(a+1)**2+2/(a+1)**3)
        deriv(Gn, lambda t, a=a: t**a*math.log(t)**2, x, f"parameter second derivative a={a}")
for x in (.3, .9, 2.):
    deriv(lambda t: t**3*(math.log(t)/3-F(1, 9)), lambda t: t*t*math.log(t), x, "a=2 cross-method check")
    ck(close(J_log(2, x), x*(math.log(x)**2-2*math.log(x)+2)), "parameter and reduction J2 agree")

# Non-elementary functions: independent erf derivative and a Si power series oracle.
for x in (-1.5, -.2, .4, 1.7):
    deriv(lambda t: math.sqrt(math.pi)*math.erf(t)/2, lambda t: math.exp(-t*t), x, "erf antiderivative")
ck(math.erf(0) == 0, "erf normalisation")


def si_series(x):
    total = 0.0
    for k in range(80):
        m = 2*k+1
        term = (-1)**k*x**m/(m*math.factorial(m))
        total += term
        if abs(term) < 1e-16:
            break
    return total


for x in (0., .5, 1.5):
    target = lambda t: 1.0 if t == 0 else math.sin(t)/t
    deriv(si_series, target, x, "Si series derivative", tol=2e-6)
ck(si_series(0) == 0, "Si normalisation")

# Complexification and undetermined coefficients for general a,b.
for a, b in ((1., 1.), (-2., 3.), (.5, -2.), (2., .7)):
    den = a*a+b*b
    for x in (-.6, .2, 1.1):
        Fs = lambda t, a=a, b=b: math.exp(a*t)*(a*math.sin(b*t)-b*math.cos(b*t))/den
        Fc = lambda t, a=a, b=b: math.exp(a*t)*(a*math.cos(b*t)+b*math.sin(b*t))/den
        deriv(Fs, lambda t, a=a, b=b: math.exp(a*t)*math.sin(b*t), x, "general complexified sine")
        deriv(Fc, lambda t, a=a, b=b: math.exp(a*t)*math.cos(b*t), x, "general complexified cosine")
    sol_s = np.linalg.solve(np.array([[a, -b], [b, a]]), np.array([1., 0.]))
    sol_c = np.linalg.solve(np.array([[a, -b], [b, a]]), np.array([0., 1.]))
    ck(np.allclose(sol_s, [a/den, -b/den]) and np.allclose(sol_c, [b/den, a/den]), "independent coefficient solve")
for x in (-.5, .2, 1.):
    deriv(lambda t: math.exp(-2*t)*(-2*math.cos(3*t)+3*math.sin(3*t))/13, lambda t: math.exp(-2*t)*math.cos(3*t), x, "damped cosine example")

# Assertions against the actual editable JSON figures.
content = Path(__file__).resolve().parents[1] / "content"
specs = []
for path in sorted(content.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    for block in text.split(":::diagram\n")[1:]:
        specs.append(json.loads(block.split("\n:::", 1)[0]))
ck(len(specs) == 25, "editable diagram inventory")
ck(sum(s.get("type") == "graph" for s in specs) == 10, "editable graph inventory")
ck(sum(s.get("type") == "flow" for s in specs) == 6, "editable workflow inventory")
ck(sum(s.get("type") == "table" for s in specs) == 9, "editable table inventory")
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
        ck(math.isfinite(value(curve, (lo+hi)/2)), f"finite plotted expression: {spec['title']}")
ck(all(len(row) == len(s["columns"]) for s in specs if s.get("type") == "table" for row in s["rows"]), "table rows match columns")
ck(all(len(step["detail"]) < 120 for s in specs if s.get("type") == "flow" for step in s["steps"]), "workflow labels remain concise")

spec = by_title["Arctangent has derivative 1/(1+x^2)"]
for x in (-1., 0., 1.):
    deriv(curve_fn(spec["curves"][1]), curve_fn(spec["curves"][0]), x, "actual arctangent figure derivative")
ck(all(close(value(spec["curves"][1], p["x"]), p["y"]) for p in spec["points"]), "actual arctangent point anchors")
spec = by_title["The semicircle is the derivative of its antiderivative"]
for x in (-1., 0., 1.):
    deriv(curve_fn(spec["curves"][1]), curve_fn(spec["curves"][0]), x, "actual semicircle figure derivative")
ck(all(close(value(spec["curves"][1], p["x"]), p["y"]) for p in spec["points"]), "actual semicircle point anchors")
spec = by_title["Three antiderivatives of 2x have parallel tangents at x=1"]
for i, curve in enumerate(spec["curves"]):
    deriv(curve_fn(curve), lambda t: 2*t, 1, "actual vertical-family derivative")
    ck(close(value(curve, 1), spec["points"][i]["y"]), "actual vertical-family point")
    ray = spec["rays"][i]
    slope = (ray["y"][1]-ray["y"][0])/(ray["x"][1]-ray["x"][0])
    ck(close(slope, 2), "actual parallel tangent slope")
spec = by_title["ln|x| differentiates to 1/x on both sides of zero"]
deriv(curve_fn(spec["curves"][2]), curve_fn(spec["curves"][0]), -2, "actual negative log branch")
deriv(curve_fn(spec["curves"][3]), curve_fn(spec["curves"][1]), 2, "actual positive log branch")
for i, p in enumerate(spec["points"]):
    curve = spec["curves"][i+2]
    ck(close(value(curve, p["x"]), p["y"]), "actual log point anchor")
    ray = spec["rays"][i]
    ck(close((ray["y"][1]-ray["y"][0])/(ray["x"][1]-ray["x"][0]), 1/p["x"]), "actual log tangent slope")
spec = by_title["The antiderivative x ln x - x has tangent slope ln x"]
for x in (1., math.e):
    deriv(curve_fn(spec["curves"][1]), curve_fn(spec["curves"][0]), x, "actual by-parts figure derivative")
ck(all(close(value(spec["curves"][1], p["x"]), p["y"], 1e-8) for p in spec["points"]), "actual by-parts point anchors")
ck(close((spec["rays"][0]["y"][1]-spec["rays"][0]["y"][0]), 0), "actual horizontal tangent")
spec = by_title["A positive partial-fraction integrand makes its antiderivative increase"]
for x in (0., 1.):
    deriv(curve_fn(spec["curves"][1]), curve_fn(spec["curves"][0]), x, "actual partial-fraction figure derivative")
ck(all(close(value(spec["curves"][1], p["x"]), p["y"], 1e-8) for p in spec["points"]), "actual partial-fraction point anchors")
for i, p in enumerate(spec["points"]):
    ray = spec["rays"][i]
    ck(close((ray["y"][1]-ray["y"][0])/(ray["x"][1]-ray["x"][0]), value(spec["curves"][0], p["x"]), 1e-8), "actual partial-fraction tangent slope")
spec = by_title["Three correct antiderivatives of sin x cos x have the same shape"]
for curve in spec["curves"]:
    deriv(curve_fn(curve), lambda t: math.sin(t)*math.cos(t), .7, "actual equivalent-answer derivative")
for i in (1, 2):
    for x in (-1., .2, 1.4):
        expected = .5 if i == 1 else .25
        ck(close(value(spec["curves"][0], x)-value(spec["curves"][i], x), expected), "actual equivalent-answer vertical gap")
spec = by_title["The half-angle formula differentiates to 1/(2+cos x) on (-pi,pi)"]
for x in (0., math.pi/2):
    deriv(curve_fn(spec["curves"][1]), curve_fn(spec["curves"][0]), x, "actual half-angle figure derivative")
ck(all(close(value(spec["curves"][1], p["x"]), p["y"], 1e-8) for p in spec["points"]), "actual half-angle point anchors")
spec = by_title["Euler's logarithm has derivative 1/sqrt(x^2+1)"]
for x in (-1., 0., 1.):
    deriv(curve_fn(spec["curves"][1]), curve_fn(spec["curves"][0]), x, "actual Euler figure derivative")
ck(all(close(value(spec["curves"][1], p["x"]), p["y"], 1e-8) for p in spec["points"]), "actual Euler point anchors")
spec = by_title["The cyclic antiderivative has slope e^x sin x"]
for x in (0., math.pi/2):
    deriv(curve_fn(spec["curves"][1]), curve_fn(spec["curves"][0]), x, "actual cyclic figure derivative")
ck(all(close(value(spec["curves"][1], p["x"]), p["y"], 1e-8) for p in spec["points"]), "actual cyclic point anchors")

# Targeted independent assertions for the six-page visual lab.
for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    ck(_condition, f"visual lab: {_name}")

print(f"Indefinite Integration: {checks}/{checks} checks PASS")
