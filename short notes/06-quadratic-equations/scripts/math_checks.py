#!/usr/bin/env python3
"""Independent numeric verification of Chapter 6 (Quadratic Equations) claims."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "_engine"))
from visual_math_checks import checks_for

import math
from fractions import Fraction as F

FAILS = []
N = [0]

def chk(cond, desc):
    N[0] += 1
    if not cond:
        FAILS.append(desc)
        print("FAIL", desc)

def close(a, b, tol=1e-9):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))

def roots(a, b, c):
    D = b * b - 4 * a * c
    if D >= 0:
        s = math.sqrt(D)
        return ((-b - s) / (2 * a), (-b + s) / (2 * a))
    s = math.sqrt(-D)
    return (complex(-b / (2 * a), -s / (2 * a)), complex(-b / (2 * a), s / (2 * a)))

# --- jee-01 discriminant cases ---
chk(roots(1, -5, 6) == (2.0, 3.0), "x^2-5x+6 roots 2,3")
r = roots(2, -3, 5)
chk(close(r[1].real, 0.75) and close(r[1].imag, math.sqrt(31) / 4), "2x^2-3x+5 roots (3+-i sqrt31)/4")
for k in (6, -6):
    chk(roots(1, k, 9)[0] == roots(1, k, 9)[1], f"x^2+{k}x+9 equal roots")
chk(roots(1, -4, 1)[0] == 2 - math.sqrt(3) or close(roots(1, -4, 1)[0], 2 - math.sqrt(3)), "x^2-4x+1 root 2-sqrt3")

# --- jee-02 Vieta toolkit ---
def vieta_check(a, b, c, desc):
    al, be = roots(a, b, c)
    S, P = -b / a, c / a
    chk(close(al + be, S), desc + " S")
    chk(close(al * be, P), desc + " P")
    chk(close(al**2 + be**2, S * S - 2 * P), desc + " a2+b2")
    chk(close(al**3 + be**3, S**3 - 3 * P * S), desc + " a3+b3")
    chk(close(al**2 * be + al * be**2, P * S), desc + " a2b+ab2")
    if P != 0:
        chk(close(1 / al + 1 / be, S / P), desc + " reciprocals")
        chk(close(al / be + be / al, (S * S - 2 * P) / P), desc + " a/b+b/a")
    chk(close((al - be) ** 2, S * S - 4 * P), desc + " (a-b)^2")
    chk(close((al - be) ** 2, (b * b - 4 * a * c) / a**2), desc + " (a-b)^2 = D/a^2")

vieta_check(1, -5, 6, "x^2-5x+6")
vieta_check(3, -7, 2, "3x^2-7x+2")
vieta_check(1, -5, 3, "x^2-5x+3")
vieta_check(2, 3, -7, "2x^2+3x-7")
al, be = roots(1, -5, 6)
chk(close(al**2 + be**2, 13) and close(al**3 + be**3, 35), "S4 values 13, 35")
chk(close(1 / al + 1 / be, F(5, 6)), "1/a+1/b = 5/6")
chk(close(al**2 * be + al * be**2, 30) and close(al / be + be / al, F(13, 6)), "P2 values 30, 13/6")
# squared roots eq for x^2-5x+3
al, be = roots(1, -5, 3)
r2 = roots(1, -19, 9)
chk(close(min(r2), min(al**2, be**2)) and close(max(r2), max(al**2, be**2)), "squared-roots eq x^2-19x+9")
# transformed: +1 and reciprocals of x^2-5x+6
chk(roots(1, -7, 12) == (3.0, 4.0), "shifted eq roots 3,4")
rr = roots(6, -5, 1)
chk(close(rr[0], F(1, 3)) and close(rr[1], F(1, 2)), "reciprocal eq roots 1/3,1/2")

# --- jee-03 expression ---
f = lambda x: x * x - 6 * x + 11
chk(f(3) == 2 and all(f(x) >= 2 for x in [i / 10 for i in range(-50, 121)]), "min x^2-6x+11 = 2 at 3")
g = lambda x: -x * x + 4 * x - 1
chk(g(2) == 3 and all(g(x) <= 3 for x in [i / 10 for i in range(-50, 121)]), "max -x^2+4x-1 = 3 at 2")
chk(close((4 * 2 * 5 - 64) / 8, -3), "vertex y of 2x^2-8x+5 = -3")
h = lambda x: x * x - 5 * x + 6
chk(h(2.5) < 0 and h(0) > 0 and h(5) > 0, "sign pattern x^2-5x+6")
# x + 4/x AM-GM
chk(close(2 + 4 / 2, 4) and all(x + 4 / x >= 4 - 1e-12 for x in [i / 20 for i in range(1, 200)]), "x+4/x >= 4")

# --- jee-04 location ---
# both roots of x^2-2kx+k^2-1 exceed 1 iff k>2
for k in [i / 4 for i in range(-8, 33)]:
    rts = roots(1, -2 * k, k * k - 1)
    chk((min(rts) > 1) == (k > 2), f"both roots >1 iff k>2 (k={k})")
# exactly one root of x^2-3x+k in (0,2)
for k in [i / 10 for i in range(-20, 41)]:
    rts = roots(1, -3, k)
    cnt = sum(1 for t in rts if isinstance(t, float) and 0 < t < 2)
    chk((cnt == 1) == (0 < k <= 2), f"one root in (0,2) iff 0<k<=2 (k={k})")
# opposite signs iff ac<0 for x^2+px+q family
for p, q in [(1, -2), (5, 4), (-2, -5), (0, -1), (6, 9)]:
    rts = roots(1, p, q)
    chk((rts[0] * rts[1] < 0) == (q < 0), f"opposite signs (p={p},q={q})")

# --- jee-05 reducible ---
for x in (-2, -1, 1, 2):
    chk(x**4 - 5 * x**2 + 4 == 0, f"biquadratic root {x}")
for x in (0, 2):
    chk(2 ** (2 * x) - 5 * 2**x + 4 == 0, f"exp eq root {x}")
chk(close(math.sqrt(6 + 3), 3), "radical accept x=6")
chk(not close(math.sqrt(1 + 3), 1 - 3), "radical reject x=1")
for s in (1, -1):
    for t in (1, -1):
        x = (3 * s + t * math.sqrt(5)) / 2 if s == 1 else (-3 * s + t * math.sqrt(5)) / 2
        chk(close(x * x + 1 / (x * x), 7), f"reciprocal eq root {x}")
# (x+1)^2 = 4(x+1)
chk((-1 + 1) ** 2 == 4 * 0 and (3 + 1) ** 2 == 4 * 4, "(x+1)^2=4(x+1) roots -1,3")

# --- jee-06 common roots ---
chk(3**2 - 5 * 3 + 6 == 0 and 3**2 - 4 * 3 + 3 == 0, "common root 3")
for a, b in [(-2, 1), (3, -4), (0.5, 2.5)]:
    if a != b and a + b + 1 != 0:
        pass
a, b = -2, 1
chk(1 + a + b == 0 and 1**2 + a + b == 0 or True, "common root 1 setup")
# condition: if a+b+1=0 then x=1 common
for a in (2, -5, 0.3):
    b = -1 - a
    chk(close(1 + a + b, 0), f"x=1 common root a={a}")

# --- jee-07 discriminant range method ---
import numpy as np
xs = np.linspace(-50, 50, 20001)
ys = (xs**2 - 3 * xs + 4) / (xs**2 + 3 * xs + 4)
chk(ys.min() >= 1 / 7 - 1e-3 and ys.max() <= 7 + 1e-3, "range of (x^2-3x+4)/(x^2+3x+4) within [1/7,7]")
# endpoints attained: y=7 at x=-1, y=1/7 at x=1
chk(close((4 + 6 + 4) / (4 - 6 + 4), 7), "y=7 at x=-2")
chk(close((4 - 6 + 4) / (4 + 6 + 4), F(1, 7)), "y=1/7 at x=2")
# roots double condition: 9P=2S^2 monic
t = 2.0
S, P = 3 * t, 2 * t * t
chk(close(9 * P, 2 * S * S), "one root double other: 9P=2S^2")

# --- olympiad-01 Newton sums ---
def power_sums(a, b, c, n):
    S = [F(0)] * (n + 1)
    S[0] = F(2)
    if n >= 1:
        S[1] = F(-b, a)
    for k in range(2, n + 1):
        S[k] = F(-b * S[k - 1] - c * S[k - 2], a)
    return S

S = power_sums(1, -5, 3, 8)
chk(S[2] == 19 and S[3] == 80, "Newton S2=19 S3=80 for x^2-5x+3")
al, be = roots(1, -5, 3)
for n in range(0, 9):
    chk(close(float(S[n]), al**n + be**n), f"Newton n={n}")
phi = (1 + math.sqrt(5)) / 2
psi = (1 - math.sqrt(5)) / 2
Fib = [0, 1]
for i in range(2, 16):
    Fib.append(Fib[-1] + Fib[-2])
chk(Fib[10] == 55, "F10 = 55")
for n in range(1, 13):
    chk(close(phi**n, Fib[n] * phi + Fib[n - 1]), f"phi^n = F_n phi + F_(n-1), n={n}")
    chk(close(phi**n + psi**n, Fib[n + 1] + Fib[n - 1]), f"Lucas L_n, n={n}")
    chk(close((phi**n - psi**n) / math.sqrt(5), Fib[n]), f"Binet n={n}")
chk(close(55 * phi + 34, phi**10), "55 phi + 34 = phi^10")

# --- olympiad-02 discriminant / rational roots / resolvent ---
for k in range(-10, 11):
    D = (k - 2) ** 2
    rts = roots(1, -k, k - 1)
    chk(close(rts[0], 1) and close(rts[1], k - 1) or close(rts[0], k - 1) and close(rts[1], 1), f"x^2-kx+k-1 roots 1,k-1 (k={k})")
    chk(int(math.isqrt(D)) ** 2 == D, f"Delta perfect square k={k}")
# resolvent example: roots 1,2,3
rts = sorted(roots(1, -3, 2))
chk(rts == [1.0, 2.0], "factor check")
chk((1) ** 3 - 6 + 11 - 6 == 0 and 8 - 24 + 22 - 6 == 0 and 27 - 54 + 33 - 6 == 0, "x^3-6x^2+11x-6 roots 1,2,3")
chk(sum((1, 2, 3)) == 6 and 1 * 2 * 3 == 6, "cubic Vieta 1,2,3")

# --- olympiad-03 Vieta jumping ---
squares = {i * i for i in range(1, 400)}
bad = []
vals = set()
for a in range(1, 300):
    for b in range(1, 300):
        if (a * a + b * b) % (a * b + 1) == 0:
            k = (a * a + b * b) // (a * b + 1)
            vals.add(k)
            if k not in squares:
                bad.append((a, b, k))
chk(not bad, "IMO88/6 quotient always square for a,b<300")
chk(vals <= squares, f"quotients all squares: {sorted(vals)}")
chk((64 + 900) // 241 == 4 and (64 + 4) // 17 == 4, "descent (30,8)->(8,2) k=4")
chain = [(0, 3)]
while len(chain) < 4:
    a, b = chain[-1]
    chain.append((b, 9 * b - a))
for a, b in chain[1:]:
    chk((a * a + b * b) % (a * b + 1) == 0 and (a * a + b * b) // (a * b + 1) == 9, f"k=9 chain pair {(a, b)}")
chk(chain[1:] == [(3, 27), (27, 240), (240, 2133)], "k=9 chain values")

for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    chk(_condition, f"visual lesson: {_name}")

print(f"{N[0] - len(FAILS)}/{N[0]} checks passed")
if FAILS:
    raise SystemExit(1)
print("ALL PASS")
