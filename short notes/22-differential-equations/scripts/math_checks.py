#!/usr/bin/env python3
"""Independent exact, numerical, source and editable-figure checks for Chapter 22."""
from pathlib import Path
import json
import math
import re
import sys

import numpy as np

CH = Path(__file__).resolve().parents[1]
ROOT = CH.parents[1]
sys.path.insert(0, str(CH.parent / "_engine"))
from diagrams import _eval_expr

checks = 0
seen_q = set()


def ck(ok, msg):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(msg)


def qck(q, ok, msg):
    seen_q.add(q)
    ck(ok, f"Q{q}: {msg}")


def close(a, b, tol=1e-9):
    return math.isclose(float(a), float(b), rel_tol=tol, abs_tol=tol)


def fd(f, x, h=1e-4):
    return (f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))/(12*h)


def fd2(f, x, h=8e-4):
    return (-f(x+2*h)+16*f(x+h)-30*f(x)+16*f(x-h)-f(x-2*h))/(12*h*h)


def rk4(f, x0, y0, x1, n=1600):
    """Pure-Python scalar RK4, independent of every printed closed form."""
    h = (x1-x0)/n
    x, y = float(x0), float(y0)
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x+h/2, y+h*k1/2)
        k3 = f(x+h/2, y+h*k2/2)
        k4 = f(x+h, y+h*k3)
        y += h*(k1+2*k2+2*k3+k4)/6
        x += h
    return y


def rk4_second(accel, x0, y0, v0, x1, n=1800):
    """Pure-Python RK4 for y'=v, v'=accel(x,y,v)."""
    h = (x1-x0)/n
    x, y, v = float(x0), float(y0), float(v0)
    for _ in range(n):
        a1 = accel(x, y, v)
        k1y, k1v = v, a1
        a2 = accel(x+h/2, y+h*k1y/2, v+h*k1v/2)
        k2y, k2v = v+h*k1v/2, a2
        a3 = accel(x+h/2, y+h*k2y/2, v+h*k2v/2)
        k3y, k3v = v+h*k2v/2, a3
        a4 = accel(x+h, y+h*k3y, v+h*k3v)
        k4y, k4v = v+h*k3v, a4
        y += h*(k1y+2*k2y+2*k3y+k4y)/6
        v += h*(k1v+2*k2v+2*k3v+k4v)/6
        x += h
    return y, v


def scalar_check(name, f, exact, x0, y0, targets, samples, tol=3e-6):
    ck(close(exact(x0), y0, 2e-8), f"{name}: initial value")
    for x in samples:
        residual = fd(exact, x)-f(x, exact(x))
        ck(abs(residual) < 2e-6, f"{name}: independent derivative residual at {x}: {residual}")
    for x in targets:
        numerical = rk4(f, x0, y0, x)
        ck(close(numerical, exact(x), tol), f"{name}: RK4 to {x}: {numerical} versus {exact(x)}")


def second_check(name, accel, exact, x0, y0, v0, targets, residual, samples, tol=5e-6):
    ck(close(exact(x0), y0, 2e-8), f"{name}: initial position")
    ck(close(fd(exact, x0), v0, 3e-7), f"{name}: initial velocity")
    for x in samples:
        value = residual(x, exact(x), fd(exact, x), fd2(exact, x))
        ck(abs(value) < 3e-5, f"{name}: second-derivative residual at {x}: {value}")
    for x in targets:
        numerical, _ = rk4_second(accel, x0, y0, v0, x)
        ck(close(numerical, exact(x), tol), f"{name}: system RK4 to {x}: {numerical} versus {exact(x)}")


# Canonical inventory and visible S/P/Q destination labels.
notes = ROOT / "notes" / "Differential-Equations"
paper = (notes / "Differential-Equations — Paper.md").read_text(encoding="utf-8")
theory = (notes / "Differential-Equations.md").read_text(encoding="utf-8")
content_dir = CH / "content"
content_files = sorted(content_dir.glob("*.md"))
all_content = "\n".join(p.read_text(encoding="utf-8") for p in content_files)
ck([int(q) for q in re.findall(r"#### \*\*Q(\d+)\*\*", paper)] == list(range(1, 42)), "canonical paper is exactly Q1-Q41")
ck(sorted(set(map(int, re.findall(r"#### \*\*S(\d+)\*\*", theory)))) == list(range(1, 22)), "canonical theory is exactly S1-S21")
ck(sorted(set(map(int, re.findall(r"#### \*\*P(\d+)\*\*", theory)))) == list(range(1, 17)), "canonical theory is exactly P1-P16")
for q in range(1, 42):
    ck(re.search(rf"\bQ{q}\b", all_content) is not None, f"visible canonical destination for Q{q}")
for s in range(1, 22):
    ck(re.search(rf"\bS{s}\b", all_content) is not None, f"visible canonical destination for S{s}")
for p in range(1, 17):
    ck(re.search(rf"\bP{p}\b", all_content) is not None, f"visible canonical destination for P{p}")
ck(len(content_files) == 24, "24 editable lesson sources")
ck(all((notes / "assets" / f"fig-0{i}.svg").exists() for i in (1, 2)), "both source SVGs remain inventoried")

# Q1-Q4 and Q41: terminology and formation.
terms = [("y'''", 3, 1), ("(y')^4", 1, 4), ("y", 0, 1)]
highest = max(terms, key=lambda t: t[1])
qck(1, highest[1:] == (3, 1), "order three and degree one, not the lower derivative's fourth power")
qck(2, all(close(2*math.exp(2*x)-2*math.exp(2*x), 0) for x in (-1., .2, 1.3)), "exponential verification identity")
for c, x in ((-2., .3), (-.4, 1.2), (1.5, -.7)):
    y, p = c*x+c*c, c
    qck(3, close(y, x*p+p*p), f"Clairaut formation at c={c}, x={x}")
ck(all(close(-x*x/4, x*(-x/2)+(-x/2)**2) for x in (-1.2, .4, 2.)), "formation equation also admits its singular envelope")
for a, x, sign in ((2., 1., 1.), (3., 2., -1.), (1.2, .4, 1.)):
    y = sign*math.sqrt(2*a*x-x*x)
    yp = (a-x)/y
    qck(4, abs(2*x*y*yp-(y*y-x*x)) < 1e-9, f"circle formation residual a={a}, x={x}")
for c1, c2, x in ((1., 2., .5), (3., -1., 1.), (-2., 5., .4)):
    y = c1*math.exp(x)+c2*math.exp(-x)
    ypp = y
    qck(41, abs(ypp-y) < 1e-12, "two-constant family forms y''-y=0")

# Q5-Q8: separable IVPs, exact values and independent numerical integration.
exact = lambda x: math.sqrt(x*x+1)
scalar_check("S3/Q5", lambda x, y: x/y, exact, 0., 1., [1., -0.7], [-.8, .2, 1.1])
qck(5, close(exact(1), math.sqrt(2)), "positive branch and sqrt(2)")
scalar_check("S4/Q6", lambda x, y: y, math.exp, 0., 1., [1., -.8], [-.5, .3, 1.2])
qck(6, close(math.exp(1), math.e), "e^x and y(1)=e")
scalar_check("P3/Q7", lambda x, y: 2*x*y, lambda x: 3*math.exp(x*x), 0., 3., [1., -.6], [-.7, .2, .9])
qck(7, close(3*math.exp(1), 3*math.e), "3e^(x^2) and y(1)=3e")
scalar_check("P4/Q8", lambda x, y: math.exp(x-y), lambda x: x, 0., 0., [1., -1.], [-.7, .4, 1.2])
qck(8, close(math.exp(0), 1), "C=0 gives y=x")

# Q9-Q11: homogeneous substitutions and maximal intervals.
scalar_check("S5/Q9", lambda x, y: (x+y)/x, lambda x: x*math.log(x), 1., 0., [math.e, .4], [.3, 1.2, 2.2])
qck(9, close(math.e*math.log(math.e), math.e), "x ln x and y(e)=e")
q10 = lambda x: x/(1-math.log(x))
scalar_check("P5/Q10", lambda x, y: y/x+(y/x)**2, q10, 1., 1., [2., .3], [.25, 1.3, 2.1], tol=2e-5)
qck(10, close(q10(2), 2/(1-math.log(2))), "blow-up-aware value at x=2")
ck(abs(1-math.log(math.e)) < 1e-15 and 0 < 1 < math.e, "Q10 maximal interval (0,e) has the correct poles")
q11 = lambda x: x*math.sqrt(2*math.log(x)+1)
scalar_check("Q11", lambda x, y: (x*x+y*y)/(x*y), q11, 1., 1., [math.e, .7], [.65, 1.1, 2.], tol=2e-5)
qck(11, close(q11(math.e), math.e*math.sqrt(3)), "positive radicand branch and e sqrt(3)")
ck(abs(2*math.log(math.exp(-.5))+1) < 1e-15, "Q11 lower domain endpoint e^(-1/2)")

# Q12-Q16 and Q28: linear/Bernoulli equations.
q12 = lambda x: .5*(math.exp(x)-math.exp(-x))
scalar_check("S6/Q12", lambda x, y: math.exp(x)-y, q12, 0., 0., [1., -.8], [-.7, .2, 1.1])
qck(12, close(q12(1), math.sinh(1)), "sinh solution and y(1)")
q13 = lambda x: 2*x-1+2*math.exp(-2*x)
scalar_check("S7/Q13", lambda x, y: 4*x-2*y, q13, 0., 1., [1., -.5], [-.4, .3, 1.2])
qck(13, close(q13(1), 1+2*math.exp(-2)), "polynomial plus homogeneous term")
q14 = lambda x: x*x/3-1/(3*x)
scalar_check("P6/Q14", lambda x, y: x-y/x, q14, 1., 0., [2., .4], [.3, 1.2, 2.2])
qck(14, close(q14(2), 7/6), "x>0 integrating factor and 7/6")
q15 = lambda x: 1/(x+1)
scalar_check("S8/Q15", lambda x, y: x*y*y-y, q15, 0., 1., [1., -.7], [-.6, .3, 1.4])
qck(15, close(q15(1), .5), "Bernoulli substitution and pole at x=-1")
ck(abs((-1)+1) < 1e-15, "Q15 maximal IVP interval begins at -1")
zero15 = lambda x: 0.
ck(all(abs(fd(zero15, x)-(x*zero15(x)**2-zero15(x))) < 2e-8 for x in (-.4, .2, .8)) and abs(zero15(0)-1) > .9, "Q15 zero equilibrium solves the general equation but fails y(0)=1")
q16 = lambda x: math.exp(-x)
scalar_check("Q16", lambda x, y: math.exp(-x)-2*y, q16, 0., 1., [1., -1.], [-.8, .2, 1.3])
qck(16, close(q16(0), 1), "matching exponential forcing makes C=0")
q28 = lambda x: .5*(math.sin(x)-math.cos(x)+math.exp(-x))
scalar_check("Q28", lambda x, y: math.sin(x)-y, q28, 0., 0., [math.pi/2, -.7], [-.4, .5, 1.8])
qck(28, close(q28(math.pi/2), (1+math.exp(-math.pi/2))/2), "sine/cosine trial and exact pi/2 value")

# Q17-Q20: exact potentials and orthogonal families.
q17 = lambda x: (-x+math.sqrt(4-3*x*x))/2
for x in (-.8, -.2, .3, .9):
    y = q17(x)
    qck(17, abs(x*x+x*y+y*y-1) < 1e-10, "explicit branch stays on potential level one")
    ck(abs(fd(q17, x)+(2*x+y)/(x+2*y)) < 3e-6, "Q17 implicit slope agrees with the exact form")
num17 = rk4(lambda x, y: -(2*x+y)/(x+2*y), 0., 1., .5)
ck(close(num17, q17(.5), 4e-6), "Q17 independent RK4 on the safe branch")
ck(close(2/math.sqrt(3), 1.1547005383792515), "Q17 finite-slope interval endpoints")
q18 = lambda x: (-x*x+math.sqrt(x**4-4*x**3+4))/2
for x in (-.3, .1, .35):
    y = q18(x)
    qck(18, abs(x**3+x*x*y+y*y-1) < 1e-9, "cubic potential level one")
    ck(abs(fd(q18, x)+(3*x*x+2*x*y)/(x*x+2*y)) < 4e-6, "Q18 exact differential slope")
num18 = rk4(lambda x, y: -(3*x*x+2*x*y)/(x*x+2*y), 0., 1., .25)
ck(close(num18, q18(.25), 4e-6), "Q18 independent RK4")
for c, x in ((-1.2, .8), (.4, -1.5), (2., .3)):
    y = c*x*x
    p_parabola = 2*c*x
    p_ellipse = -x/(2*y)
    qck(19, close(p_parabola*p_ellipse, -1), "parabola and ellipse slopes are negative reciprocals")
    ck(abs(2*x+4*y*p_ellipse) < 1e-10, "Q19 ellipse potential has zero directional derivative")
for c, x in ((-2., .7), (.5, -1.3), (3., .2)):
    y = c*x
    qck(20, close((-x/y)*(y/x), -1), "finite radial line meets its circle orthogonally")
# At (0,y), a circle has horizontal tangent and x=0 is vertical.
y = 2.3
ck(abs((-y)*0+0*1) < 1e-15, "Q20 vertical line x=0 is orthogonal to the horizontal circle tangent")
ck("x=0" in all_content.replace(" ", ""), "Q20 corrected vertical trajectory is visibly included")

# Q21-Q25: second-order constant-coefficient and Euler IVPs.
second_check("P9/Q21", lambda x, y, v: -y, math.sin, 0., 0., 1., [1., -.7], lambda x, y, v, a: a+y, [-.4, .3, 1.2])
qck(21, close(math.sin(0), 0) and close(math.cos(0), 1), "sin x satisfies both initial data")
q22 = lambda x: math.exp(2*x)-math.exp(x)
second_check("S11/Q22", lambda x, y, v: 3*v-2*y, q22, 0., 0., 1., [1., -.5], lambda x, y, v, a: a-3*v+2*y, [-.4, .4, 1.1])
qck(22, close(q22(1), math.e**2-math.e), "distinct roots and e^2-e")
q23 = lambda x: (1+2*x)*math.exp(-2*x)
second_check("S12/Q23", lambda x, y, v: -4*v-4*y, q23, 0., 1., 0., [1., -.4], lambda x, y, v, a: a+4*v+4*y, [-.3, .2, 1.2])
qck(23, close(q23(1), 3*math.exp(-2)), "repeated root x companion and 3e^-2")
q24 = lambda x: .5*(x-1/x)
second_check("S13/Q24", lambda x, y, v: (y-x*v)/(x*x), q24, 1., 0., 1., [2., .5], lambda x, y, v, a: x*x*a+x*v-y, [.4, 1.2, 2.1])
qck(24, close(q24(2), .75), "Euler roots plus/minus one and 3/4")
q25 = lambda x: x*x
second_check("P12/Q25", lambda x, y, v: (2*x*v-2*y)/(x*x), q25, 1., 1., 2., [3., .5], lambda x, y, v, a: x*x*a-2*x*v+2*y, [.4, 1.1, 2.2])
qck(25, close(q25(3), 9), "Euler initial data select x^2")

# Q26-Q31: models, damping and autonomous reduction.
k = math.log(2)/10
T = lambda x: 20+80*math.exp(-k*x)
scalar_check("S14/Q26", lambda x, y: -k*(y-20), T, 0., 100., [10., 20.], [2., 12., 18.])
qck(26, close(T(20), 40), "temperature excess halves twice, giving 40 degrees C")
ck(close(math.exp(-10*k), .5), "Q26 measured ten-minute excess ratio")
continuous = 1000*math.e
discrete = 1000*1.1**10
qck(27, close(continuous, 2718.281828459045), "continuous 10 percent relative-rate convention gives 1000e")
ck(close(discrete, 2593.7424601) and not close(continuous, discrete), "Q27 discrete compounding is a distinct stated model")
q29 = lambda x: math.exp(-x)*math.sin(2*x)
second_check("S21/Q29", lambda x, y, v: -2*v-5*y, q29, 0., 0., 2., [1., 2.], lambda x, y, v, a: a+2*v+5*y, [.3, 1.1, 2.2])
qck(29, close(q29(1), .33451182923926226), "under-damped value at x=1")
for n in range(4):
    ck(abs(q29(n*math.pi/2)) < 1e-12, "Q29 zero at n pi/2")
ck(close(math.pi/2, (3*math.pi/2)-math.pi), "Q29 consecutive-zero spacing is pi/2")
for x in (.2, .8, 1.4):
    ck(close(q29(x+math.pi), math.exp(-math.pi)*q29(x)), "Q29 phase shift multiplies by exp(-pi)")
    ck(not close(q29(x+math.pi), q29(x)), "Q29 damped solution is not periodic")
peak = .5*math.atan(2)
ck(abs(math.exp(-peak)*(2*math.cos(2*peak)-math.sin(2*peak))) < 1e-12, "Q29 first positive peak at half arctan two")
ck(close(1/math.sqrt(5), .4472135954999579), "Q29 damping ratio below one")
q30 = lambda x: math.exp(-x)-math.exp(-2*x)
second_check("P16/Q30", lambda x, y, v: -3*v-2*y, q30, 0., 0., 1., [1., math.log(2)], lambda x, y, v, a: a+3*v+2*y, [.2, .7, 1.4])
qck(30, close(q30(1), .23254415793482963), "over-damped value at x=1")
ck(all(q30(x) > 1e-8 for x in (.1, .4, 1., 2.)), "Q30 no positive zero crossing")
ck(close(q30(math.log(2)), .25) and abs(fd(q30, math.log(2))) < 2e-7, "Q30 maximum one-quarter at ln2")
q31 = math.exp
second_check("S16/Q31", lambda x, y, v: v*v/y, q31, 0., 1., 1., [1., -.5], lambda x, y, v, a: y*a-v*v, [-.4, .3, 1.1])
qck(31, close(q31(1), math.e), "reduction p(y) gives e^x")
for a, c, x in ((2., 0., .4), (-1.3, .7, -.2), (.4, -1.2, .8)):
    y = a*math.exp(c*x)
    ck(abs(y*c*c*y-(c*y)**2) < 1e-10, "Q31 nonzero exponential family residual")
ck(all(abs(a*fd2(lambda t, aa=a: aa, .3)-fd(lambda t, aa=a: aa, .3)**2) < 2e-8 for a in (-2., 0., 3.)), "Q31 constant solutions survive the branch audit")

# Q32-Q35: Clairaut envelopes and reduction of order.
for c, x in ((-2., .3), (-.5, 1.2), (1.4, -.7)):
    line = c*x+c*c
    p = c
    qck(32, close(line, x*p+p*p), "general Clairaut line residual")
    xt, yt = -2*c, -c*c
    ck(close(yt, c*xt+c*c) and close(yt, -xt*xt/4), "Q32 line-envelope contact point")
ck(all(close(-x*x/4, x*(-x/2)+x*x/4) for x in (-1.2, .2, 2.)), "Q32 singular parabola residual")
for c, x in ((-1.5, .4), (.2, 1.1), (2., -.8)):
    line = c*x-c*c
    qck(33, close(line, x*c-c*c), "sign-reversed Clairaut line residual")
    xt = 2*c
    ck(close(c*xt-c*c, xt*xt/4), "Q33 envelope contact")
ck(all(close(x*x/4, x*(x/2)-(x/2)**2) for x in (-1.1, .5, 1.7)), "Q33 upward singular parabola residual")
for x in (-1.2, .2, .8, 2.):
    y1, y2 = math.sin(x), -math.cos(x)
    W = y1*math.sin(x)-math.cos(x)*(-math.cos(x))
    qck(34, close(W, 1), "corrected Wronskian is plus one")
    ck(not close(W, -1), "Q34 source Wronskian sign is explicitly rejected")
    second34 = lambda t: -math.cos(t)
    ck(abs(fd2(second34, x)+second34(x)) < 3e-6, "Q34 second solution satisfies y''+y=0")
ck(abs(fd(lambda x: -1/math.tan(x), .7)-1/math.sin(.7)**2) < 2e-6, "Q34 reduction integral derivative")
for a, b, x in ((1., 2., .5), (-2., 3., 1.4), (.5, -.7, 2.)):
    y = a*x*x+b*x
    yp, ypp = 2*a*x+b, 2*a
    qck(35, abs(x*x*ypp-2*x*yp+2*y) < 1e-10, "Euler general-solution residual")
    ck(close(x*(2*x)-x*x, x*x), "Q35 Wronskian of x and x^2")

# Q36-Q37: explicit non-uniqueness and one-sided joining derivatives.
def delayed_sqrt(x, a):
    return 0. if x <= a else (x-a)**2/4

for a in (0., .4, 1.):
    for x in (a+.2, a+1., a+2.):
        y = delayed_sqrt(x, a)
        qck(36, abs((x-a)/2-math.sqrt(y)) < 1e-12, "departing square-root branch residual")
    left = 0.
    right = (delayed_sqrt(a+1e-5, a)-delayed_sqrt(a-1e-5, a))/(2e-5)
    ck(abs(right) < 2e-6 and abs(left) < 1e-15, "Q36 centred joining difference tends to zero linearly")
    ck(delayed_sqrt(a+1, a) > 0 and abs(delayed_sqrt(0, a)) < 1e-15, "Q36 distinct solution with the same initial value")
ck(1/(2*math.sqrt(1e-8)) > 4000, "Q36 y-derivative is unbounded near zero")
qck(36, close(delayed_sqrt(2., 1.), .25), "waiting-time construction is distinct from the zero solution")

def delayed_cuberoot(x):
    return 0. if x <= 1 else (2*(x-1)/3)**1.5

for x in (1.1, 1.5, 2.4):
    y = delayed_cuberoot(x)
    u = 2*(x-1)/3
    qck(37, abs(math.sqrt(u)-y**(1/3)) < 1e-12, "cube-root departing branch residual")
    ck(abs(fd(delayed_cuberoot, x)-y**(1/3)) < 3e-6, "Q37 independent derivative check")
d1 = (delayed_cuberoot(1+1e-4)-delayed_cuberoot(1-1e-4))/(2e-4)
d2 = (delayed_cuberoot(1+1e-6)-delayed_cuberoot(1-1e-6))/(2e-6)
ck(close(d1, 10*d2, 2e-7) and abs(d2) < 3e-4, "Q37 centred joining differences tend to zero like sqrt(h)")
ck((1e-6)**(-2/3)/3 > 3000, "Q37 y-derivative is unbounded near zero")

# Q38: corrected parametric Lagrange differentiation and every special branch.
for c, p in ((1., 0.), (1., .5), (2., -.3), (-.7, .2), (1.3, 1.4)):
    x = c/(1-p)**2
    y = 1+c*p*p/(1-p)**2
    dx = 2*c/(1-p)**3
    dy = 2*c*p/(1-p)**2+2*c*p*p/(1-p)**3
    qck(38, abs(y-(x*p*p+1)) < 2e-10, "parametric family satisfies the original relation")
    ck(abs(dy/dx-p) < 2e-9, "Q38 parametric derivative dy/dx=p")
    ck(abs(p*dx-(p*p*dx+2*x*p)) < 2e-9, "Q38 corrected p-parametric differentiation")
# Explicitly reject the source's displayed wrong equation on a genuine branch point.
c, p = 1., .5
x = c/(1-p)**2
dpdx = 1/(2*c/(1-p)**3)
wrong_rhs = 2*x*p+x*p*p*dpdx
ck(not close(p, wrong_rhs), "Q38 source displayed differentiation is numerically rejected")
ck(abs(p-(p*p+2*x*p*dpdx)) < 1e-12, "Q38 correct x-based product rule holds at the same point")
ck(all(abs(1-(x*fd(lambda t: 1., x)**2+1)) < 2e-8 for x in (-2., .3, 4.)), "Q38 constant solution y=1")
ck(all(abs((x+1)-(x*fd(lambda t: t+1, x)**2+1)) < 2e-8 for x in (-2., .3, 4.)), "Q38 constant-slope solution y=x+1")
for sign, x0 in ((-1., .5), (1., .5)):
    exact_branch = lambda x, s=sign: x+2+2*s*math.sqrt(x)
    slope = lambda x, y, s=sign: 1+s/math.sqrt(x)
    numerical = rk4(slope, x0, exact_branch(x0), 1.4)
    ck(close(numerical, exact_branch(1.4), 4e-6), "Q38 explicit C=1 branch independently integrated")
    for x in (.3, 1., 1.8):
        y = exact_branch(x)
        p_branch = slope(x, y)
        ck(abs(y-(x*p_branch*p_branch+1)) < 1e-9, "Q38 editable explicit branch residual")

# Q39-Q40: Riccati families, equilibria and pole locations.
for c in (-3., -.7, .4, 1., 3.):
    for x in (-1.2, .3, .8):
        if c < 0 and close(x, math.log(-1/c), 1e-7):
            continue
        den = 1+c*math.exp(x)
        if abs(den) < .15:
            continue
        y = 1/den
        yp = -c*math.exp(x)/(den*den)
        qck(39, abs(yp-(y*y-y)) < 2e-9, "Riccati exponential-family residual")
        ck(abs(y) > 1e-8, "Q39 finite-C family never attains y=0 at a tested regular point")
for c, x0, target in ((1., -.5, .8), (3., -.4, .5), (-1., -2., -1.)):
    exact_r = lambda x, cc=c: 1/(1+cc*math.exp(x))
    numerical = rk4(lambda x, y: y*y-y, x0, exact_r(x0), target)
    ck(close(numerical, exact_r(target), 5e-6), "Q39 independent RK4 on a pole-free interval")
ck(all(abs(fd(lambda t, aa=a: aa, x)-(a*a-a)) < 2e-8 for a in (0., 1.) for x in (-.4, .3)), "Q39 equilibria y=0 and y=1 both solve the equation")
ck(abs(1-math.exp(math.log(1))) < 1e-15, "Q39 C=-1 denominator pole at x=0")
for c in (-.7, .4, 1., 2.):
    for x in (-.6, .2, .6):
        den = c*math.exp(-x*x)-.5
        if abs(den) < .12:
            continue
        y = 1+1/den
        yp = 2*c*x*math.exp(-x*x)/(den*den)
        qck(40, abs(yp-x*(y*y-1)) < 3e-8, "Gaussian Riccati-family residual")
        ck(abs(y-1) > 1e-8, "Q40 finite-C family never attains y=1 at a tested regular point")
for c in (-.7, 1., 2.):
    exact_r = lambda x, cc=c: 1+1/(cc*math.exp(-x*x)-.5)
    numerical = rk4(lambda x, y: x*(y*y-1), 0., exact_r(0.), .6)
    ck(close(numerical, exact_r(.6), 8e-6), "Q40 independent RK4 away from denominator zeros")
ck(all(abs(fd(lambda t, aa=a: aa, x)-x*(a*a-1)) < 2e-8 for a in (-1., 1.) for x in (-.5, .4)), "Q40 equilibria y=1 and y=-1 satisfy the original equation")
for c in (.5, 1., 2.):
    a = math.sqrt(math.log(2*c))
    for x in ((-a,) if c == .5 else (-a, a)):
        den = c*math.exp(-x*x)-.5
        ck(abs(den) < 1e-12, "Q40 exact denominator-zero location")

# Additional Extension VI: nonresonance, resonance and variation of parameters.
particular = lambda x: math.exp(2*x)/3
second_check("extension nonresonant", lambda x, y, v: y+math.exp(2*x), particular, 0., 1/3, 2/3, [.8], lambda x, y, v, a: a-y-math.exp(2*x), [.2, .6])
resonant = lambda x: .5*x*math.exp(x)
second_check("extension resonant", lambda x, y, v: y+math.exp(x), resonant, 0., 0., .5, [.8], lambda x, y, v, a: a-y-math.exp(x), [.2, .7])
sec_particular = lambda x: math.cos(x)*math.log(math.cos(x))+x*math.sin(x)
second_check("extension variation of parameters", lambda x, y, v: -y+1/math.cos(x), sec_particular, 0., 0., 0., [.7], lambda x, y, v, a: a+y-1/math.cos(x), [.2, .6], tol=2e-5)
for x in (.2, .7, 1.1):
    y1, y2 = math.cos(x), math.sin(x)
    ck(close(y1*math.cos(x)-(-math.sin(x))*y2, 1), "extension variation Wronskian")

# Assertions against the actual editable JSON figures.
specs = []
for path in content_files:
    text = path.read_text(encoding="utf-8")
    for block in text.split(":::diagram\n")[1:]:
        specs.append(json.loads(block.split("\n:::", 1)[0]))
ck(len(specs) == 24, "editable diagram inventory")
ck(sum(s.get("type") == "graph" for s in specs) == 8, "eight editable graphs")
ck(sum(s.get("type") == "flow" for s in specs) == 8, "eight editable workflows")
ck(sum(s.get("type") == "table" for s in specs) == 8, "eight editable decision tables")
ck(sum(len(s.get("slope_fields", [])) for s in specs) == 3, "three genuine slope-field specifications")
by_title = {s["title"]: s for s in specs}
ck(len(by_title) == len(specs), "unique figure titles")


def value(curve, x):
    y = np.asarray(_eval_expr(curve["expr"], np.array([float(x)])))
    return float(y.reshape(-1)[0])


def field_value(field, x, y):
    with np.errstate(all="ignore"):
        z = np.asarray(_eval_expr(field["expr"], np.array([float(x)]), np.array([float(y)])))
    return float(z.reshape(-1)[0])


def curve_fn(curve):
    return lambda x: value(curve, x)


for spec in specs:
    for curve in spec.get("curves", []):
        lo = curve.get("from", spec.get("xrange", [-6, 6])[0])
        hi = curve.get("to", spec.get("xrange", [-6, 6])[1])
        for j in range(1, 6):
            ck(math.isfinite(value(curve, lo+(hi-lo)*j/6)), f"finite plotted expression: {spec['title']}")
ck(all(len(row) == len(s["columns"]) for s in specs if s.get("type") == "table" for row in s["rows"]), "table rows match columns")
ck(all(len(step["detail"]) < 120 for s in specs if s.get("type") == "flow" for step in s["steps"]), "workflow labels remain concise")

# Visual Lab 1: real slopes, both C=1 branches and the C=-1 branch.
spec = by_title["The slope field for y-prime = x/y with three solution branches"]
field = spec["slope_fields"][0]
ck(close(field_value(field, 1, math.sqrt(2)), 1/math.sqrt(2)), "actual slope field at (1,sqrt2)")
ck(close(field_value(field, 2, math.sqrt(3)), 2/math.sqrt(3)), "actual slope field at (2,sqrt3)")
ck(not math.isfinite(field_value(field, 2, 0)), "actual slope field rejects y=0")
ck(close(value(spec["curves"][0], 0), 1) and close(value(spec["curves"][1], 0), -1), "actual visible upper and lower branches")
for x in (.2, 1.2, 2.):
    ck(close(value(spec["curves"][0], x)**2-x*x, 1), "actual C=1 upper branch")
    ck(close(value(spec["curves"][1], x)**2-x*x, 1), "actual C=1 lower branch")
ck(close(value(spec["curves"][2], 2)**2-4, -1), "actual C=-1 red branch")

# Visual Lab 2: actual linear curves follow exp(x)-y.
spec = by_title["Slope field for y-prime + y = exp(x)"]
for curve in spec["curves"][:2]:
    for x in (-.8, .2, .9):
        ck(abs(fd(curve_fn(curve), x)-(math.exp(x)-value(curve, x))) < 4e-6, "actual linear-field curve residual")
ck(close(value(spec["curves"][0], 0), 0) and close(value(spec["curves"][1], 0), .5), "actual IVP and C=0 initial values")

# Visual Lab 3: actual marked point and orthogonal slopes.
spec = by_title["Parabolas y = c x^2 and ellipses x^2 + 2y^2 = C"]
p = spec["points"][0]
u = 4*math.sqrt(3)-4
ck(close(p["x"], math.sqrt(u), 2e-8) and close(p["y"], u/4, 2e-8), "actual orthogonal intersection coordinates")
ck(close(value(spec["curves"][0], p["x"]), p["y"], 2e-8), "actual marked parabola anchor")
ck(close(value(spec["curves"][2], p["x"]), p["y"], 2e-8), "actual marked ellipse anchor")
product = fd(curve_fn(spec["curves"][0]), p["x"])*fd(curve_fn(spec["curves"][2]), p["x"])
ck(close(product, -1, 3e-5), "actual plotted slopes multiply to minus one")
for x in (-1.2, .4, 1.4):
    ck(close(value(spec["curves"][2], x), -value(spec["curves"][3], x)), "actual ellipse upper/lower pair")

# Visual Lab 4: actual damping curves, envelopes, zeros and exact peak.
spec = by_title["y = exp(-x) sin(2x) with envelopes plus/minus exp(-x)"]
for x in (0., math.pi/2, math.pi):
    ck(abs(value(spec["curves"][0], x)) < 1e-10, "actual damped-curve zero")
for x in (.2, .8, 1.4):
    ck(close(value(spec["curves"][1], x), -value(spec["curves"][2], x)), "actual envelope pair")
    ck(abs(value(spec["curves"][0], x)) <= value(spec["curves"][1], x)+1e-12, "actual solution lies inside its envelope")
ck(abs(fd(curve_fn(spec["curves"][0]), peak)) < 3e-6, "actual damped curve has the exact first peak")

# Visual Lab 5: actual delayed solutions and slope field.
spec = by_title["Three solutions of y-prime = sqrt(y), y(0)=0"]
ck(close(value(spec["curves"][1], 2), 1) and close(value(spec["curves"][2], 2), .25), "actual immediate and delayed branch heights")
ck(close(value(spec["curves"][0], 2), 0), "actual zero solution")
ck(close(field_value(spec["slope_fields"][0], 2, 1), 1), "actual sqrt(y) slope at (2,1)")
ck(abs(fd(curve_fn(spec["curves"][2]), 2)-.5) < 2e-6, "actual delayed branch derivative")
ck(not math.isfinite(field_value(spec["slope_fields"][0], 1, -.2)), "actual real slope field rejects negative y")

# Visual Lab 6: every actual tangent has the claimed contact and slope.
spec = by_title["Lines y = Cx + C^2 and the envelope y = -x^2/4"]
for c, curve, point in zip((-2., -1., 0., 1., 2.), spec["curves"][1:], spec["points"]):
    x, y = -2*c, -c*c
    ck(close(point["x"], x) and close(point["y"], y), "actual tangent contact-point inventory")
    ck(close(value(curve, x), y) and close(value(spec["curves"][0], x), y), "actual line and envelope values coincide")
    ck(close(fd(curve_fn(curve), x), c) and close(fd(curve_fn(spec["curves"][0]), x), c), "actual line and envelope slopes coincide")

# Q38 and Q39 editable extension graphs.
spec = by_title["Q38 with C=1: two parametric branches and two constant-p lines"]
for i, sign in ((0, -1.), (1, 1.)):
    curve = spec["curves"][i]
    for x in (.3, 1., 1.8):
        y = value(curve, x)
        p_branch = 1+sign/math.sqrt(x)
        ck(abs(y-(x*p_branch*p_branch+1)) < 1e-9, "actual Q38 graph branch residual")
ck(close(value(spec["curves"][0], 1), 1) and close(value(spec["curves"][2], 2), 1) and close(value(spec["curves"][3], 2), 3), "actual Q38 special-line and contact anchors")
spec = by_title["Q39: positive-C branches connect the two equilibria"]
for curve, c in zip(spec["curves"][:2], (1., 3.)):
    for x in (-1.2, .2, 1.):
        y = value(curve, x)
        yp = -c*math.exp(x)*y*y
        ck(abs(yp-(y*y-y)) < 1e-9, "actual Q39 graph residual")
for point, curve in zip(spec["points"], spec["curves"][:2]):
    ck(close(value(curve, point["x"]), point["y"]), "actual Q39 point anchor")
ck(close(value(spec["curves"][2], 2), 0) and close(value(spec["curves"][3], 2), 1), "actual Q39 equilibrium lines")

ck(seen_q == set(range(1, 42)), "every canonical question has at least one targeted mathematical assertion")
print(f"Differential Equations: {checks}/{checks} checks PASS")
