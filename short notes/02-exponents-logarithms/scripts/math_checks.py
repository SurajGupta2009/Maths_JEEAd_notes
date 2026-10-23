#!/usr/bin/env python3
"""Independent numeric verification of Chapter 2 (Exponents & Logarithms) claims."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "_engine"))
from visual_math_checks import checks_for

import math

FAILS = []
N = [0]

def chk(cond, desc):
    N[0] += 1
    if not cond:
        FAILS.append(desc)
        print("FAIL", desc)

def close(a, b, tol=1e-9):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))

def cbrt(x):
    # real odd-root convention (Python float ** follows the complex principal branch)
    return math.copysign(abs(x) ** (1 / 3), x)

# --- index laws (a > 0) ---
for a in (0.5, 2.0, 3.7, 10.0):
    for r, s in ((2, 3), (0.5, 1.5), (-1.2, 2.3)):
        chk(close(a**r * a**s, a**(r + s)), f"a^r a^s {a} {r} {s}")
        chk(close(a**r / a**s, a**(r - s)), f"a^r/a^s {a}")
        chk(close((a**r)**s, a**(r * s)), f"(a^r)^s {a}")
        chk(close((a * 7.0)**r, a**r * 7.0**r), f"(ab)^r {a}")
        chk(close(a ** (-r), 1 / a**r), f"a^-r {a}")

# --- parity repairs ---
chk(close(math.sqrt((-3.4) ** 2), 3.4), "sqrt(x^2)=|x| negative")
chk(close(cbrt(-8.0), -2.0), "(-8)^(1/3) = -2")
chk(close(cbrt(-8.0) ** 2, 4.0), "(-8)^(2/3) = 4")
chk(close(((-2.0) ** 2) ** 0.5, 2.0), "( (-2)^2 )^(1/2) = 2 (not -2)")
for x in (16 * math.sqrt(2), -16 * math.sqrt(2)):
    chk(close(cbrt(x) ** 2, 8.0), f"x^(2/3)=8 at x=±16√2 ({x})")

# --- exponential function ---
chk(close(math.exp(0), 1.0), "e^0")
chk(close(math.exp(1.3) * math.exp(-1.3), 1.0), "e^x e^-x")
chk(2.718281828459045 == math.e, "e constant")
for x in (0, 2):
    chk(close(2 ** (2 * x) - 5 * 2**x + 4, 0.0), f"quad-exp root {x}")
for x in (0, 1):
    chk(close(4**x - 3 * 2**x + 2, 0.0), f"4^x root {x}")
for x in (0, math.log(2)):
    chk(close(math.exp(2 * x) - 3 * math.exp(x) + 2, 0.0), f"e-quad root {x}")
chk(math.log(3) * 200 > math.log(2) * 300, "3^200 > 2^300")
chk(math.log(math.e) * math.pi > math.log(math.pi) * math.e, "e^pi > pi^e")
chk(close(2**4, 4**2), "2^4 = 4^2")

# --- log definition & laws ---
for a in (2.0, 3.5, 0.4):
    for m, n in ((3.0, 7.0), (0.5, 2.5), (9.0, 0.25)):
        chk(close(math.log(m * n, a), math.log(m, a) + math.log(n, a)), f"log mn {a}")
        chk(close(math.log(m / n, a), math.log(m, a) - math.log(n, a)), f"log m/n {a}")
        chk(close(math.log(m**1.7, a), 1.7 * math.log(m, a)), f"log m^p {a}")
    chk(close(math.log(a**2.3, a), 2.3), f"log_a a^p {a}")
    chk(close(a ** (math.log(5.0, a)), 5.0), f"a^log_a x {a}")
    chk(close(math.log(7.0, a), math.log(7.0) / math.log(a)), "change of base")
chk(close(math.log(3.0, 2) * math.log(2.0, 3), 1.0), "reciprocity")
chk(close(math.log(3.0, 2) * math.log(5.0, 3), math.log(5.0, 2)), "chain rule")
chk(close(math.log10(2), 0.30102999566, 1e-9), "lg 2 ~ 0.30103")
chk(close(math.log10(3), 0.47712125472, 1e-9), "lg 3 ~ 0.47712")
chk(close(math.log(2), 0.69314718056, 1e-9), "ln 2 ~ 0.69315")
chk(math.log(5, 2) > 0 and math.log(5, 0.5) < 0 and math.log(0.3, 2) < 0, "sign rule samples")

# --- log equations ---
x = 1 + 2 * math.sqrt(3)
chk(close(math.log(x - 3, 2) + math.log(x + 1, 2), 3.0), "worked log eq root")
for x in (100.0, 0.01):
    chk(close(x ** (math.log10(x)), 1e4), f"x^lgx root {x}")
chk(close(math.log(19 - 3, 2), 4.0), "log2(x-3)=4 -> 19")
chk(close(math.log(8, 2), 3.0), "log_x 8 = 3 at x=2")
chk(close(math.log(6, 2) - math.log(3, 2) + math.log(16, 2), 5.0), "simplify log expression = 5")
chk(close(math.log(math.log(81, 3), 2), 2.0), "nested log = 2")
chk(close(math.log(8, 4), 1.5), "log_4 8 = 3/2")
for x in (2 ** math.sqrt(2), 2 ** (-math.sqrt(2))):
    chk(close(math.log(x, 2), math.log(4, x)), f"log_2 x = log_x 4 at {x}")

# --- inequalities samples ---
chk(math.log10(5 - 1) < 1 and math.log10(12 - 1) > 1 and abs(math.log10(11 - 1) - 1) < 1e-12,
    "lg(x-1)<1 sample (boundary = 11)")
chk(4**2 - 1 >= 3 * 4 and not (1**2 - 1 >= 3 * 1), "exp inequality samples")
a1 = (3 - math.sqrt(13)) / 2
a2 = (3 + math.sqrt(13)) / 2
chk(close(a1**2 - 3 * a1 - 1, 0.0) and close(a2**2 - 3 * a2 - 1, 0.0), "boundary roots of x^2-3x-1")

# --- digits ---
chk(len(str(2**100)) == 31 == math.floor(100 * math.log10(2)) + 1, "digits of 2^100 = 31")
chk(len(str(3**50)) == 24 == math.floor(50 * math.log10(3)) + 1, "digits of 3^50 = 24")
chk(str(3**50).startswith("7"), "3^50 starts with 7")
chk(close(10 ** (50 * math.log10(3) - 23), 7.17898, 1e-4), "3^50 ~ 7.18e23")

# --- x^y = y^x parametrisation ---
chk(close(2**4, 4**2), "(2,4) pair")
for n in (1, 2, 3, 5):
    t = 1 + 1 / n
    x = t ** (1 / (t - 1))
    y = t ** (t / (t - 1))
    chk(close(y * math.log(x), x * math.log(y)), f"x^y=y^x param n={n}")
chk(close((1 + 1) ** 1, 2.0) and close((1 + 1) ** 2, 4.0), "n=1 gives (2,4)")

# --- Legendre ---
def vp(n, p):
    return sum(n // p**k for k in range(1, 20) if p**k <= n)

def sp(n, p):
    s = 0
    while n:
        s += n % p
        n //= p
    return s

chk(vp(100, 2) == 97 == (100 - sp(100, 2)) // 1, "v2(100!) = 97")
chk(vp(100, 5) == 24 == (100 - sp(100, 5)) // 4, "v5(100!) = 24")
chk(vp(10, 3) == 4 == (10 - sp(10, 3)) // 2, "v3(10!) = 4")
for n in (10, 33, 100):
    for p in (2, 3, 5, 7):
        chk(vp(n, p) == (n - sp(n, p)) // (p - 1), f"Legendre n={n} p={p}")

# --- harmonic bounds ---
H = sum(1 / k for k in range(1, 101))
chk(math.log(101) <= H <= 1 + math.log(100), "H_100 in bounds")
chk(close(H, 5.187377517639621), "H_100 value")

# --- growth/doubling ---
k = 0.07
t2 = math.log(2) / k
chk(close(math.exp(k * t2), 2.0), "doubling time")
chk(math.log(100) * 200 > math.log(200) * 100, "100^n vs n^100 at n=200 (n^100 wins at n=50)")
chk(close(math.log(100) * 100, math.log(100) * 100), "100^100 = 100^100 crossover")

for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    chk(_condition, f"visual lesson: {_name}")

print(f"Chapter 2 math checks: {N[0] - len(FAILS)}/{N[0]} PASS", "FAILURES:", len(FAILS))
if FAILS:
    raise SystemExit(1)
