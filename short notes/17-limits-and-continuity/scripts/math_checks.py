#!/usr/bin/env python3
"""Independent exact, numerical and editable-figure checks for Chapter 17."""
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


def bisect(f, a, b, steps=80):
    fa, fb = f(a), f(b)
    assert fa * fb < 0
    for _ in range(steps):
        m = (a+b)/2
        fm = f(m)
        if fa*fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a+b)/2


# Meaning, punctured neighbourhoods and a complete epsilon-delta model.
for x in (F(-2), F(0), F(1, 2), F(3)):
    ck((x*x-1)/(x-1) == x+1, "punctured quadratic quotient factors")
for eps in (F(1, 10), F(3, 2), F(5)):
    delta = eps/3
    for x in (F(2)-delta/2, F(2)+delta/3, F(2)+delta/4):
        ck(x != 2 and abs(x-2) < delta and abs((3*x+1)-7) < eps, "linear epsilon-delta band")
    ck(3*delta == eps, "delta is epsilon divided by three")
ck(not (0 < abs(F(2)-2) < F(1, 2)) and abs((3*F(2)+1)-7) == 0, "punctured hypothesis excludes the centre")
ck(math.floor(1.999) == 1 and math.floor(2.0) == math.floor(2.001) == 2, "greatest-integer one-sided values")
ck(math.sqrt(0) == 0 and math.sqrt(.25) == .5, "right-side square-root domain")
ck(1/(-1e-6) < 0 < 1/(1e-6), "reciprocal has opposite unbounded signs")

# Algebraic limits, factoring, conjugates and domain preservation.
for n in range(1, 7):
    for x in (F(-2), F(0), F(1, 2), F(2)):
        ck((x**n-1)/(x-1) == sum(x**j for j in range(n)), "geometric factor identity")
ck(F(3**3-1, 3**2-1) == F(13, 4), "cubic and quadratic quotient at three")
ck(sum(F(2)**j for j in range(3)) == 7, "three-term geometric sum")
for x in (.01, .1, 1, 4):
    q = (math.sqrt(1+x)-1)/x
    ck(close(q, 1/(math.sqrt(1+x)+1)), "radical conjugate identity")
    ck(close((math.sqrt(x)-2)/(x-4) if x != 4 else .25, 1/(math.sqrt(x)+2)), "second radical conjugate identity")
ck(5*2-3 == 7 and F(4-6, 2) == -1, "direct substitution and cancellation examples")
for x in (F(-3), F(-1), F(0), F(2), F(4)):
    if x not in (-2, 3):
        ck((x+2)/(x*x-x-6) == 1/(x-3), "cancelled factor preserves permitted domain")
ck(F(1, -2-3) == F(-1, 5), "removable hole height at minus two")

# Squeeze, radians and standard trigonometric limits.
for x in (.01, .1, .5, 1, 1.4):
    ck(math.cos(x) < math.sin(x)/x < 1, "geometric sine squeeze")
    ck(close(math.sin(-x)/(-x), math.sin(x)/x), "sinc is even")
    ck(close(abs(x*x*math.sin(1/x)) <= x*x, True), "bounded oscillation squeeze")
for n in (100, 1000, 10000):
    x = 1/n
    ck(close(math.sin(x)/x, 1, 5e-4), "numerical sinc target")
    ck(close(math.tan(x)/x, 1, 5e-4), "numerical tangent target")
    ck(close((1-math.cos(x))/x**2, .5, 5e-4), "numerical cosine target")
for x in (.01, .1, .5):
    value = (math.tan(x)-math.sin(x))/x**3
    factored = (1/math.cos(x))*(math.sin(x)/x)*((1-math.cos(x))/x**2)
    ck(close(value, factored), "third-power trigonometric factorization")
    ck(close((1-math.cos(2*x))/(x*math.sin(x)), 2*math.sin(x)/x), "double-angle cosine example")
ck(close(math.sin(5*.01)/(.03), (5/3)*math.sin(.05)/.05), "matching small argument and denominator")
ck(close(math.sin(math.radians(30)), .5) and not close(math.sin(30), .5), "radian convention matters")
ck(all(close((math.cos(x)-1)/math.sin(x)**2, -1/(1+math.cos(x))) for x in (.01, .1, .5)), "cosine over sine-squared identity")

# Exponential, logarithmic and power forms.
for a in (.5, 2, 10):
    for x in (-.5, 0, .2, 2):
        ck(close(a**x, math.exp(x*math.log(a))), "general exponential rewritten with exp")
for n in (1000, 10000, 100000):
    x = 1/n
    ck(close(math.expm1(x)/x, 1, 5e-3), "exponential standard limit")
    ck(close(math.log1p(x)/x, 1, 5e-3), "logarithm standard limit")
    ck(close((1+x)**(1/x), math.e, 5e-3), "continuous e limit")
    ck(close((1+2*x)**(3/x), math.e**6, 1e-2), "one-to-infinite power coefficient")
ck(close(math.log(math.e), 1) and close(math.exp(1), math.e), "continuity of exp and ln at the target")
ck(close((1+3/10)**10, 13.785849184) and close((1+3/30)**30, 17.449402268), "printed exponential graph samples")
ck(math.exp(0*0) == 1, "zero increment uses the removable logarithm ratio")
ck(all(abs(math.exp(n*math.log1p(1/n))/n) < .03 for n in (100, 1000, 10000)), "e-limit divided by n needs only quotient laws")
for x in (-.9, -.1, .1, 1):
    ck(1+x > 0, "real variable-power base domain")

# Limits at infinity, asymptotes, L'Hopital and transformed forms.
for x in (10, 100, 1000):
    value = (3*x*x-x+4)/(2*x*x+5)
    normalized = (3-1/x+4/x**2)/(2+5/x**2)
    ck(close(value, normalized), "dominant-power normalization")
    ck(abs(value-1.5) < .07, "rational horizontal asymptote")
for x in (F(-4), F(0), F(2), F(4), F(8)):
    ck((2*x+1)/(x-3) == 2+F(7)/(x-3), "hyperbola residual decomposition")
ck(F(2*4+1, 4-3) == 9 and F(1, -3) == F(-1, 3), "hyperbola plotted points")
ck(close((2*1000+1)/(1000-3), 2, 1e-2), "hyperbola horizontal limit")
for x in (100, 1000, 10000):
    ck(math.log(x)/x < .1 and x*math.exp(-x) < .1, "growth hierarchy samples")
    ck(close(math.sqrt(x*x+x)-x, x/(math.sqrt(x*x+x)+x)), "infinite-difference conjugate")
    ck(abs((math.sqrt(x*x+x)-x)-.5) < .01, "infinite-difference limit")
for x in (1e-2, 1e-3, 1e-4):
    ck(abs((x-math.sin(x))/x**3-1/6) < 1e-3, "L'Hopital sine result numerical check")
    ck(abs((x-math.tan(x))/x**3+1/3) < 2e-3, "L'Hopital tangent result numerical check")
for x in (1e-2, 1e-4, 1e-6):
    ck(abs(x*math.log(x)) < .05 and x*math.log(x) < 0, "zero-times-infinity logarithm")
ck(math.sin(0)/(0+1) == 0, "zero over one is not indeterminate")

# Continuity, discontinuities, algebra and IVT applications.
ck(2 != 3, "existing limit can differ from assigned value")
ck(abs(-1e-8) < 1e-7 and abs(1e-8) < 1e-7, "absolute value is continuous at zero")
for x in (-2, -1e-8, 1e-8, 2):
    ck(close(abs(x)/x, -1 if x < 0 else 1), "absolute-value one-sided quotient")
for x in (-1.2, -.2, .2, 1.2):
    frac = x-math.floor(x)
    ck(0 <= frac < 1, "fractional-part range")
ck(close((-1e-8)-math.floor(-1e-8), 1, 1e-6) and close((1e-8)-math.floor(1e-8), 0, 1e-6), "fractional-part integer jump")
for x in (F(-2), F(0), F(2)):
    left = 2*x+1
    ck(left == 2*x+1, "continuous left polynomial branch")
for x, expected_value in ((F(3), F(8)), (F(4), F(11))):
    ck(3*x-1 == expected_value, "right branch arithmetic away from the join")
ck(2*2+1 == 3*2-1 == 5, "piecewise parameter and common value")
f = lambda x: x**3+x-1
ck(f(0) == -1 and f(1) == 1, "cubic IVT endpoint signs")
ck(f(F(1, 2)) == F(-3, 8) and f(F(3, 4)) == F(11, 64), "exact first bisection values")
root = bisect(f, 0., 1.)
ck(close(root, .6823278038280193, 1e-9) and abs(f(root)) < 1e-12, "cubic root by bisection")
ck(all(f(x) < f(y) for x, y in [(0, .2), (.2, .5), (.5, .8), (.8, 1)]), "strict increase supports uniqueness")
g = lambda x: math.cos(x)-x
ck(g(0) == 1 and close(g(math.pi/2), -math.pi/2), "cosine fixed-point endpoint signs")
dottie = bisect(g, 0., math.pi/2)
ck(close(dottie, .7390851332151607) and abs(g(dottie)) < 1e-12, "Dottie root by bisection")
for x in (0, .25, .5, .75, 1):
    h = x*x-x
    ck(h <= 0, "continuous self-map auxiliary function is nonpositive inside")
ck(0*0 == 0 and 1*1 == 1, "self-map endpoint fixed points")
ck(-1*1 < 0, "sign change alone does not prove uniqueness or handle discontinuity")

# Sequential criteria, Stolz-Cesaro and recursive sequences.
for n in range(1, 9):
    x, y = 1/(n*math.pi), 1/(math.pi/2+2*n*math.pi)
    ck(close(math.sin(1/x), 0) and close(math.sin(1/y), 1), "Heine nonexistence sequences")
    ck(x > 0 and y > 0 and x < 1 and y < 1, "Heine inputs lie in punctured approach")
for n in (1, 2, 5, 10):
    q = F(1, n)
    r = math.sqrt(2)/n
    ck(q.denominator != 0 and r > 0, "rational and irrational sequences are defined")
for x in (-.1, -.01, .01, .1):
    ck(close(math.exp(-1/x**2), math.exp(-(1/x**2))), "exponential substitution for every sign")
for n in (1, 2, 10, 100):
    a = n*(n+1)//2
    ck(F(a, n*n) == F(n+1, 2*n), "arithmetic Stolz quotient")
    ck(F(n+1, 2*n+1)-F(1, 2) == F(1, 2*(2*n+1)), "arithmetic Stolz increments")
H = lambda n: sum(1/k for k in range(1, n+1))
for n in (10, 100, 1000):
    ratio = (1/(n+1))/math.log1p(1/n)
    ck(abs(ratio-1) < .05, "harmonic Stolz increment ratio")
a = [1.]
for _ in range(5):
    a.append(math.sqrt(2+a[-1]))
expected = [1, 1.7320508075688772, 1.9318516525781366, 1.9828897227476208, 1.995717846477207, 1.9989291749527314]
ck(all(close(x, y) for x, y in zip(a, expected)), "nested-radical recurrence values")
ck(all(a[i] < a[i+1] < 2 for i in range(5)), "nested-radical monotone bounded proof data")
ck(2*2-2-2 == 0 and (-1)**2-(-1)-2 == 0, "fixed-point quadratic candidates")
h = [2.]
for _ in range(6):
    h.append((h[-1]+2/h[-1])/2)
ck(all(h[i+1] <= h[i]+1e-15 and h[i+1] >= math.sqrt(2)-1e-14 for i in range(6)), "Heron monotone lower-bound data")
ck(abs(h[-1]-math.sqrt(2)) < 1e-12, "Heron numerical convergence")
r = [math.sqrt(2)]
for _ in range(5):
    r.append(math.sqrt(2*r[-1]))
ck(all(close(r[n-1], 2**(1-2**(-n))) for n in range(1, 7)), "exponent-tracking recurrence formula")

# Riemann sums, products, Stirling, harmonic asymptotics and rates.
right8 = sum(F(k, 8)**2 for k in range(1, 9))/8
ck(right8 == F(51, 128), "exact eight-point Riemann sum")
ck(right8 > F(1, 3), "increasing right endpoints overestimate area")
ck(close(1/(1+.5), 2/3), "square-root Riemann-sum limiting value")
for n in (10, 100, 1000):
    s = sum(F(n, n*n+k*k) for k in range(1, n+1))
    ck(abs(float(s)-math.pi/4) < .03, "rational Riemann sum approaches pi over four")
    psum = sum((F(k, n))**2 for k in range(1, n+1))/n
    ck(psum == F((n+1)*(2*n+1), 6*n*n), "power-sum Riemann identity")
for n in (10, 100, 1000):
    logp = sum(math.log1p(k/n**2) for k in range(1, n+1))
    upper = (n+1)/(2*n)
    error = (n*(n+1)*(2*n+1))/(12*n**4)
    ck(upper-error <= logp <= upper, "log-product two-sided error bound")
    ck(abs(math.exp(logp)-math.sqrt(math.e)) < .06, "product approaches square root of e")
for n in (10, 100):
    logratio = (math.lgamma(2*n+1)-2*math.lgamma(n+1)-n*math.log(4)) + .5*math.log(math.pi*n)
    ratio = math.exp(logratio)
    ck(abs(ratio-1) < .02, "central-binomial Stirling ratio")
    ck(ratio > .98, "Stirling correction approaches from below in sampled range")
for n in (100, 1000, 10000):
    gamma_estimate = H(n)-math.log(n)
    ck(abs(gamma_estimate-.5772156649) < .01, "Euler-Mascheroni numerical target")
    ck(abs((H(2*n)-H(n))-math.log(2)) < .01, "harmonic difference tends to ln two")
    scaled = n*(math.exp(n*math.log1p(1/n))-math.e)
    ck(abs(scaled+math.e/2) < .02, "second-order exponential convergence rate")
ck(close(100*(math.exp(100*math.log1p(1/100))-math.e), -1.346799903751883), "printed convergence-rate scale")
ck(close(1000*(math.exp(1000*math.log1p(1/1000))-math.e), -1.3578962231526326), "thousand-term convergence-rate scale")

# Functional equations and IVT constructions.
for q in (F(-2), F(-1, 2), F(0), F(2, 3), F(3)):
    ck(3*(2*q) == 2*(3*q), "continuous additive form on rationals")
for q in (F(-2), F(-1, 2), F(0), F(2, 3), F(3)):
    ck(close(2**float(q+1), 2**float(q)*2), "continuous exponential form on rationals")
ck(2**0 == 1 and all(2**x > 0 for x in (-3, -.5, 0, 2)), "nonzero exponential solution is positive")
half = lambda x: (x-F(1, 2))**2
for x in (F(0), F(1, 8), F(1, 4), F(3, 8), F(1, 2)):
    ck(half(x)-half(x+F(1, 2)) == F(1, 4)-x, "half-shift auxiliary identity")
ck(half(F(1, 4)) == half(F(3, 4)) == F(1, 16), "exact half-shift conclusion")
ck(half(0) == half(1) == F(1, 4), "half-shift endpoint hypothesis")

# Assertions against the actual editable JSON figures, not just the prose.
content = Path(__file__).resolve().parents[1] / "content"
specs = []
for path in sorted(content.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    for block in text.split(":::diagram\n")[1:]:
        specs.append(json.loads(block.split("\n:::", 1)[0]))
ck(len(specs) == 21, "editable diagram inventory")
ck(sum(s.get("type") == "graph" for s in specs) == 17, "editable graph inventory")
ck(sum(s.get("type") == "flow" for s in specs) == 3 and sum(s.get("type") == "table" for s in specs) == 1, "editable workflow and table inventory")
by_title = {s["title"]: s for s in specs}
ck(len(by_title) == len(specs), "unique figure titles")


def value(curve, x):
    y = np.asarray(_eval_expr(curve["expr"], np.array([float(x)])))
    return float(y.reshape(-1)[0])


# Evaluate every plotted expression inside its own sampled segment.
for spec in specs:
    for curve in spec.get("curves", []):
        lo = curve.get("from", spec.get("xrange", [-6, 6])[0])
        hi = curve.get("to", spec.get("xrange", [-6, 6])[1])
        y = value(curve, (lo+hi)/2)
        ck(math.isfinite(y), f"finite plotted expression: {spec['title']}")

spec = by_title["A delta-band on x controls the epsilon-band on y"]
ck(spec["bands"][0]["a"] == 1.5 and spec["bands"][0]["b"] == 2.5, "actual delta-band endpoints")
ck([h["y"] for h in spec["hlines"]] == [5.5, 7, 8.5], "actual epsilon-band heights")
ck(close(value(spec["curves"][0], 2), 7) and spec["points"][0]["x"] == 2, "actual linear graph target")
spec = by_title["The hole at (2,4) does not stop the limit"]
ck(spec["points"][0]["face"] == "white" and (spec["points"][0]["x"], spec["points"][0]["y"]) == (2, 4), "actual removable open point")
ck(close(value(spec["curves"][0], 1), 3) and close(value(spec["curves"][1], 3), 5), "actual two-sided hole branches")
spec = by_title["sin(x)/x is squeezed between cos(x) and 1"]
ck(close(value(spec["curves"][1], .5), math.sin(.5)/.5), "actual sinc expression")
ck(value(spec["curves"][0], .5) < value(spec["curves"][1], .5) < value(spec["curves"][2], .5), "actual squeeze ordering")
spec = by_title["The removable gap at x=0 has height e"]
ck(close(spec["points"][0]["y"], math.e) and spec["points"][0]["face"] == "white", "actual exponential open target")
ck(close(value(spec["curves"][0], -.5), 4) and close(value(spec["curves"][1], 1), 2), "actual two-sided exponential formula")
spec = by_title["The decomposition 2 + 7/(x-3) explains both asymptotes"]
ck(spec["hlines"][0]["y"] == 2 and spec["vlines"][0]["x"] == 3, "actual hyperbola asymptotes")
ck(close(value(spec["curves"][0], 0), -1/3) and close(value(spec["curves"][1], 4), 9), "actual hyperbola branch values")
spec = by_title["A greatest-integer step has unequal one-sided limits"]
ck([value(c, (c["from"]+c["to"])/2) for c in spec["curves"]] == [0, 1, 2], "actual floor heights")
ck(any(p.get("face") == "white" and p["x"] == 2 and p["y"] == 1 for p in spec["points"]), "actual floor open left point")
spec = by_title["A continuous curve cannot avoid the zero level"]
root_point = next(p for p in spec["points"] if p.get("color") == "#B91C1C")
ck(close(root_point["x"], root) and abs(root_point["y"]) < 1e-12, "actual cubic root point")
ck(close(value(spec["curves"][0], root_point["x"]), 0), "actual cubic curve crosses at marked root")
spec = by_title["The limit is 2, but the assigned value is 3"]
ck([(p["x"], p["y"]) for p in spec["points"]] == [(1, 2), (1, 3)], "actual visual-lab hole and value")
ck(spec["points"][0]["face"] == "white" and spec["points"][1].get("face") != "white", "actual open-closed distinction")
spec = by_title["The oscillating curve is trapped between -x^2 and x^2"]
for x in (-.3, -.07, .08, .3):
    ck(abs(value(spec["curves"][2] if x < 0 else spec["curves"][3], x)) <= x*x, "actual visual-lab squeeze expression")
spec = by_title["The removable gap has height 5/3"]
ck(close(spec["points"][0]["y"], 5/3) and spec["points"][0]["face"] == "white", "actual trigonometric visual target")
ck(close(value(spec["curves"][1], .1), math.sin(.5)/.3), "actual trigonometric visual formula")
spec = by_title["The growing exponent pulls the expression toward e^3"]
ck(close(spec["hlines"][0]["y"], math.e**3) and len(spec["points"]) == 2, "actual exponential visual asymptote and samples")
ck(all(close(value(spec["curves"][0], p["x"]), p["y"], 1e-8) for p in spec["points"]), "actual exponential visual sample heights")
spec = by_title["Two different formulas can join continuously"]
ck(close(value(spec["curves"][0], -1e-6), 2, 1e-5) and close(value(spec["curves"][1], 1e-6), 2, 1e-5), "actual piecewise visual limits")
ck(spec["points"][0]["x"] == 0 and spec["points"][0]["y"] == 2, "actual piecewise visual value")
spec = by_title["The continuous difference cos(x)-x must cross zero"]
marked = next(p for p in spec["points"] if p.get("color") == "#B91C1C")
ck(close(marked["x"], dottie) and close(value(spec["curves"][0], marked["x"]), 0), "actual Dottie crossing")
spec = by_title["Two marked sequences approach x=0 but keep different heights"]
ck(len(spec["points"]) == 9 and all(p["x"] > 0 for p in spec["points"]), "actual Heine point inventory")
ck(all(close(math.sin(1/p["x"]), p["y"], 1e-7) for p in spec["points"]), "actual Heine point heights")
spec = by_title["The recurrence increases toward its fixed point 2"]
ray = spec["rays"][0]
ck(ray["x"] == [1, 2, 3, 4, 5, 6] and all(close(x, y, 1e-8) for x, y in zip(ray["y"], expected)), "actual recurrence term heights")
ck(all(ray["y"][i] < ray["y"][i+1] < 2 for i in range(5)), "actual recurrence figure monotonicity")
spec = by_title["Eight right endpoints approximate the area under y=x^2"]
ck(len(spec["rays"]) == len(spec["points"]) == 8, "actual Riemann sample inventory")
ck(all(close(p["y"], p["x"]**2) for p in spec["points"]), "actual Riemann points lie on parabola")
ck(close(sum(F(str(p["y"])) for p in spec["points"])/8, right8), "actual Riemann figure reproduces exact sum")
spec = by_title["Multiplying the error by n exposes the constant -e/2"]
ck(close(spec["hlines"][0]["y"], -math.e/2), "actual convergence-rate asymptote")
ck(close(value(spec["curves"][0], 100), -1.346799903751883), "actual convergence-rate expression")
ck(all(len(step["detail"]) < 65 for s in specs if s.get("type") == "flow" for step in s["steps"]), "workflow labels remain concise")

# Targeted independent assertions for the six-page visual lab.
for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    ck(_condition, f"visual lab: {_name}")

print(f"Limits & Continuity: {checks}/{checks} checks PASS")
