"""Targeted standard-library checks for the expanded visual-method lessons."""
from __future__ import annotations

from fractions import Fraction
import cmath
import math


def close(a, b, tol=1e-9):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def checks_for(slug: str):
    """Return (description, condition) pairs; chapter scripts own the counters."""
    n = int(slug[:2])
    out = []
    add = lambda desc, condition: out.append((desc, bool(condition)))

    if n == 1:
        f = lambda x: x * x - 2 * x - 1
        add("quadratic vertex and range", f(1) == -2 and f(0) == -1 and f(3) == 2)
        add("upper semicircle endpoints", all(close(math.sqrt(4-x*x), y) for x, y in [(-2, 0), (0, 2), (2, 0)]))
        add("restricted square inverse", all(close(math.sqrt(x*x), x) for x in [0, 0.2, 1, 4]))
        add("composition domain check", 1-math.sqrt(4) == -1 and 1-4 < 0)
        add("reflection swaps coordinates", (3, 5)[::-1] == (5, 3))
        add("horizontal line meets quadratic twice", close((1+math.sqrt(3))+(1-math.sqrt(3)), 2) and all(close(f(x), 1) for x in [1+math.sqrt(3), 1-math.sqrt(3)]))
        h = lambda x: math.sqrt(1-x*x)
        add("restricted self-inverse composition", all(close(h(h(x)), x) for x in [0, .2, .7, 1]) and h(0) == 1 and h(1) == 0)
    elif n == 2:
        add("exponential reflection", all(close(0.5**x, 2**(-x)) for x in [-3, -1, 0, 2]))
        add("logarithm inverse points", close(math.log(8, 2), 3) and close(math.log(1, 2), 0))
        add("ghost root filtering", 5 > 3 and not (-1 > 3) and (5-1)*(5-3) == 8 and (-1-1)*(-1-3) == 8)
        add("exponential substitution roots", all(close(4**x-5*2**x+4, 0) for x in [0, 2]))
        add("reciprocal base reverses order", 2**3 > 2**2 and 0.5**3 < 0.5**2)
        add("growth and decay model checks", 80*3**(10/5) == 720 and 64*.5**(12/3) == 4 and close(5*math.log(9, 3), 10))
    elif n == 3:
        add("unit circle identity", all(close(math.sin(t)**2+math.cos(t)**2, 1) for t in [0, .3, 2, 5]))
        add("cosine phase shift", all(close(math.cos(x-math.pi/2), math.sin(x)) for x in [-2, 0, .7, 4]))
        add("tangent period", all(close(math.tan(x+math.pi), math.tan(x)) for x in [-.4, 0, .7]))
        add("two sine base angles", close(math.sin(math.pi/6), .5) and close(math.sin(5*math.pi/6), .5))
        add("general solution endpoints", all(close(math.sin(2*k*math.pi+a), .5) for k in [-2, 0, 3] for a in [math.pi/6, 5*math.pi/6]))
    elif n == 4:
        add("arcsin principal correction", close(math.asin(math.sin(3*math.pi/4)), math.pi/4))
        add("arctan addition needs pi", close(math.atan(1)+math.atan(2), math.pi-math.atan(3)) and close(math.atan(-3)+math.pi, math.pi-math.atan(3)))
        add("arcsine endpoints", close(math.asin(-1), -math.pi/2) and close(math.asin(1), math.pi/2))
        add("arctan is odd", all(close(math.atan(-x), -math.atan(x)) for x in [0, .2, 1, 20]))
        add("sawtooth branch values", all(close(math.asin(math.sin(x)), y) for x, y in [(0, 0), (math.pi/2, math.pi/2), (math.pi, 0), (3*math.pi/2, -math.pi/2)]))
        add("branch-safe double angle", close(2*(3/5)*(4/5), 24/25) and 0 < math.asin(3/5) < math.pi/2)
    elif n == 5:
        z = 3+2j
        add("conjugate modulus identity", close(abs(z)**2, 13) and z*z.conjugate() == 13)
        add("complex product", (1+1j)*(1+2j) == -1+3j and close(abs((1+1j)*(1+2j)), math.sqrt(10)))
        roots = [cmath.exp(2j*math.pi*k/5) for k in range(5)]
        add("fifth roots sum to zero", close(abs(sum(roots)), 0) and all(close(abs(z**5-1), 0) for z in roots))
        add("unit-modulus reciprocal", all(close(z.conjugate(), 1/z) for z in roots))
        add("multiplication adds arguments", close(cmath.phase((1+1j)*(1+2j)), cmath.phase(1+1j)+cmath.phase(1+2j)))
    elif n == 6:
        add("vertex form", (1-1)**2-4 == -4 and (-1+1)*(-1-3) == 0 and (3+1)*(3-3) == 0)
        add("discriminant classification", all((b*b-4*a*c > 0) == expected for a, b, c, expected in [(1, 0, -1, True), (1, 0, 0, False), (1, 0, 1, False)]))
        def roots(m):
            d = 4*(m-2)*(m+1)
            if d < 0: return ()
            h = math.sqrt(d)
            return ((-h+2*m)/2, (h+2*m)/2)
        add("parameter lower boundary", roots(2) == (2.0, 2.0))
        add("parameter interior", min(roots(Fraction(5, 2))) > 1 and all(close(x*x-2*Fraction(5, 2)*x+Fraction(5, 2)+2, 0) for x in roots(Fraction(5, 2))))
        add("parameter upper exclusion", min(roots(3)) == 1)
    elif n == 7:
        add("finite geometric sum", sum(2**k for k in range(6)) == 63)
        a = [2, 3, 4, 5, 6]; sums = [sum(a[:k]) for k in range(1, 6)]
        add("AP partial sums", sums == [2, 5, 9, 14, 20] and sums[-1]-sums[-2] == 6)
        add("AM-GM equality point", min(x+1/x for x in [0.25, .5, 1, 2, 4]) == 2)
        add("telescoping boundary", all(close(sum(1/k-1/(k+1) for k in range(1, n+1)), 1-1/(n+1)) for n in [1, 2, 10, 50]))
        add("infinite geometric condition", abs(-.5) < 1 and close(1/(1-(-.5)), 2/3) and abs((-.5)**60/(1.5)) < 1e-12)
    elif n == 8:
        add("decision tree leaves", 2*3 == 6)
        add("lattice path count", math.comb(7, 3) == 35)
        nonnegative = sum(1 for a in range(10) for b in range(10) if 0 <= 9-a-b <= 9)
        add("stars and bars nonnegative count", nonnegative == math.comb(11, 2) == 55)
        add("positive solutions need shift", math.comb(8, 2) == 28)
        A, B, C = set(range(8)), set(range(5, 12)), set(range(1, 10, 2))
        ie = len(A)+len(B)+len(C)-len(A&B)-len(A&C)-len(B&C)+len(A&B&C)
        add("three-set inclusion exclusion", ie == len(A|B|C))
    elif n == 9:
        add("Pascal recurrence", all(math.comb(n+1, k) == math.comb(n, k-1)+math.comb(n, k) for n in range(1, 12) for k in range(1, n+1)))
        terms4 = [math.comb(4, k)*2**(4-k)*3**k for k in range(5)]
        add("tracked expansion terms", terms4 == [16, 96, 216, 216, 81] and sum(terms4) == 5**4)
        terms8 = [math.comb(8, k)*2**(8-k)*3**k for k in range(9)]
        add("greatest term and index", max(terms8) == terms8[5] == 108864 and sum(terms8) == 5**8)
        ratios = [Fraction(3*(8-k), 2*(k+1)) for k in range(8)]
        add("ratio turnover", all(ratios[k] > 1 for k in range(4)) and all(ratios[k] < 1 for k in range(5, 8)) and ratios[4] > 1)
        add("row sum", sum(math.comb(10, k) for k in range(11)) == 2**10)
    elif n == 10:
        det = lambda a, b, c, d: a*d-b*c
        add("transformation determinant", det(2, 1, 0, 1) == 2)
        add("reflection reverses orientation", det(0, 1, 1, 0) == -1)
        inv = [[Fraction(1, 2), Fraction(-1, 2)], [0, 1]]
        add("inverse product", all(inv[i][0]*[2, 1][j]+inv[i][1]*[0, 1][j] == (1 if i == j else 0) for i in range(2) for j in range(2)))
        add("linear-system intersection", 2+1 == 3 and 2-1 == 1 and det(1, 1, 1, -1) == -2)
        add("scalar determinant power", det(6, 3, 0, 3) == 3**2*det(2, 1, 0, 1))
    elif n == 11:
        add("without-replacement tree", close(Fraction(3, 5)*Fraction(2, 4)+Fraction(2, 5)*Fraction(1, 4), Fraction(2, 5)))
        probs = [Fraction(math.comb(4, k), 16) for k in range(5)]
        add("binomial total and mean", sum(probs) == 1 and sum(k*probs[k] for k in range(5)) == 2)
        add("binomial variance", sum((k-2)**2*probs[k] for k in range(5)) == 1)
        data = [2, 4, 4, 4, 5, 5, 7, 9]; mean = Fraction(sum(data), len(data))
        add("data mean and population variance", mean == 5 and sum((x-mean)**2 for x in data)/len(data) == 4)
        add("variance shift invariance", sum((x+7-(mean+7))**2 for x in data)/len(data) == 4)
    elif n == 12:
        add("perpendicular distance", close(abs(-4)/math.sqrt(2), 2*math.sqrt(2)) and 1*(-1) == -1)
        O, G, H = (Fraction(3), Fraction(1)), (Fraction(8, 3), Fraction(4, 3)), (Fraction(2), Fraction(2))
        dist2 = lambda p, q: (p[0]-q[0])**2+(p[1]-q[1])**2
        add("Euler ratio", dist2(G, H) == 4*dist2(O, G) and dist2(O, (0, 0)) == 10)
        add("Apollonius circle", (Fraction(5, 3)-3)**2 == (Fraction(4, 3))**2 and close(4, 2*2))
        add("second Apollonius axis point", (Fraction(1, 3)+1) == 2*(1-Fraction(1, 3)))
        add("pencil common point", all(1-1 == m*(1-1) for m in [-2, 0, 3]))
    elif n == 13:
        add("chord length", 2*math.sqrt(25-9) == 8 and 3**2+4**2 == 25)
        add("tangent radius perpendicular", 3*4+4*(-3) == 0 and 3*3+4*4 == 25)
        add("power secant tangent", 3*13 == 8**2-5**2 == 39)
        F1 = lambda x, y: x*x+y*y-9
        F2 = lambda x, y: (x-4)**2+y*y-16
        add("radical axis subtraction", F2(0, 0)-F1(0, 0) == 9 and all(close(F2(Fraction(9, 8), y)-F1(Fraction(9, 8), y), 0) for y in [-2, 0, 3]))
        add("radical axis intersections", all(close(F1(Fraction(9, 8), y), 0) and close(F2(Fraction(9, 8), y), 0) for y in [-math.sqrt(9-Fraction(81, 64)), math.sqrt(9-Fraction(81, 64))]))
        add("two-circle distance classification", abs(3-4) < 4 < 3+4)
    else:
        raise ValueError(f"no visual checks registered for {slug}")
    return out
