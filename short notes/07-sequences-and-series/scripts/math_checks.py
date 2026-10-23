#!/usr/bin/env python3
"""Independent numeric verification of Chapter 7 (Sequences & Series) claims."""
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
    return abs(float(a) - float(b)) <= tol * max(1.0, abs(float(a)), abs(float(b)))

# --- jee-01 AP ---
a, d = 2, 3
chk(a + 19 * d == 59, "AP a20 = 59")
chk(sum(a + (i) * d for i in range(20)) == 610, "AP S20 = 610")
chk(F(20, 2) * (2 * 2 + 19 * 3) == 610, "AP S20 formula")
chk(sum(range(2, 42, 2)) == 420, "first 20 even sum 420")
chk(F(14 - 2, 4) == 3, "insert means d=3")
# Sn quadratic recovery
Sn = lambda n: sum(8 + (i) * 6 for i in range(n))
chk(all(Sn(n) == 3 * n * n + 5 * n for n in range(1, 15)), "Sn=3n^2+5n <-> AP 8,14,...")
# AP data a5=17, a9=29
d2 = F(29 - 17, 9 - 5)
a1 = 17 - 4 * d2
chk(d2 == 3 and a1 == 5, "AP a5/a9 give d=3 a1=5")
chk(F(20, 2) * (2 * a1 + 19 * d2) == 670, "AP S20 = 670")
# identify 2,3,5,9,17
seq = [2 ** (n - 1) + 1 for n in range(1, 8)]
chk(seq[:5] == [2, 3, 5, 9, 17], "a_n = 2^(n-1)+1 pattern")

# --- jee-02 GP ---
chk(3 * 2**9 == 1536, "GP a10 = 1536")
chk(3 * (2**10 - 1) == 3069, "GP S10 = 3069")
chk(sum(3 * 2**i for i in range(10)) == 3069, "GP S10 direct")
chk(close(sum(F(1, 2**i) for i in range(40)), 2), "infinite GP -> 2")
chk(close(F(1) / (1 - F(1, 2)), 2), "S_inf formula")
chk(close((2 * 8 * 32) ** (1 / 3), 8), "GM of 2,8,32 = 8")
chk(close(81 ** 0.25, 3), "insert GM r=3")
# GP facts: a_m a_n with m+n const
gp = [5 * 3**i for i in range(8)]
chk(gp[0] * gp[5] == gp[2] * gp[3], "GP equidistant product")

# --- jee-03 sums and AM-GM ---
sk = lambda n: sum(range(1, n + 1))
sk2 = lambda n: sum(k * k for k in range(1, n + 1))
sk3 = lambda n: sum(k**3 for k in range(1, n + 1))
sk4 = lambda n: sum(k**4 for k in range(1, n + 1))
for n in range(1, 31):
    chk(sk(n) == n * (n + 1) // 2, f"sum k n={n}")
    chk(sk2(n) == n * (n + 1) * (2 * n + 1) // 6, f"sum k^2 n={n}")
    chk(sk3(n) == (n * (n + 1) // 2) ** 2, f"sum k^3 n={n}")
    chk(close(sk4(n), n * (n + 1) * (2 * n + 1) * (3 * n * n + 3 * n - 1) / 30), f"sum k^4 n={n}")
chk(sk2(10) == 385 and sk3(10) == 3025, "n=10 sums 385, 3025")
val = sum(3 * k * k - 2 * k for k in range(1, 11))
chk(val == 1045, "mixed sum n=10 = 1045")
chk(sum(2 * k - 1 for k in range(1, 16)) == 15**2, "first n odds sum n^2")
# AM-GM numeric sweep + equality
import random
random.seed(7)
for _ in range(200):
    x, y = random.random() * 10 + 0.01, random.random() * 10 + 0.01
    chk((x + y) / 2 >= math.sqrt(x * y) - 1e-12, "AM>=GM sweep")
    # A>=G>=H and G^2=AH
    A, G, H = (x + y) / 2, math.sqrt(x * y), 2 * x * y / (x + y)
    chk(A >= G >= H or close(A, G) or close(G, H), "A>=G>=H")
    chk(close(G * G, A * H), "G^2 = AH")
chk(close(3 + F(4, 3), F(13, 3)), "x+4/x at x=3 is 13/3")

# --- jee-04 AGP & telescoping ---
chk(close(sum(F(k, 2**k) for k in range(1, 60)), 2), "sum k/2^k = 2")
finite = sum(F(k + 1, 2**k) for k in range(80))
chk(close(finite, 4), "sum (k+1)2^-k = 4")
x = F(1, 2)
s5 = sum((k + 1) * x**k for k in range(5))
chk(s5 == F(57, 16), "finite AGP 5 terms = 57/16")
n = 5
formula = (1 - (n + 1) * x**n + n * x ** (n + 1)) / (1 - x) ** 2
chk(formula == F(57, 16), "finite AGP formula n=5")
# k^2 x^k infinite
chk(close(sum(k * k * 0.5**k for k in range(1, 200)), 0.5 * 1.5 / 0.125), "sum k^2 x^k formula x=1/2 = 6")
# telescoping
for n in range(1, 21):
    chk(sum(F(1, k * (k + 1)) for k in range(1, n + 1)) == F(n, n + 1), f"telescope m=1 n={n}")
    chk(sum(F(1, k * (k + 2)) for k in range(1, n + 1)) == F(1, 2) * (F(3, 2) - F(1, n + 1) - F(1, n + 2)), f"telescope m=2 n={n}")
    chk(sum(F(1, k * (k + 1) * (k + 2)) for k in range(1, n + 1)) == F(n * (n + 3), 4 * (n + 1) * (n + 2)), f"triple telescope n={n}")
chk(sum(F(1, k * (k + 2)) for k in range(1, 6)) == F(25, 42), "telescope m=2 n=5 = 25/42")
chk(sum(k * math.factorial(k) for k in range(1, 8)) == math.factorial(8) - 1, "sum k*k! = (n+1)!-1")
chk(sum(F(k, math.factorial(k + 1)) for k in range(1, 8)) == 1 - F(1, math.factorial(8)), "sum k/(k+1)!")

# --- olympiad-01 HP ---
chk(F(2 * 2 * 4, 2 + 4) == F(8, 3), "HM(2,4) = 8/3")
chk(close(2 * 30 * 60 / (30 + 60), 40), "average speed HM = 40")

# --- olympiad-02 recurrences / Binet ---
a_seq = [1]
for i in range(10):
    a_seq.append(2 * a_seq[-1] + 1)
chk(all(a_seq[i] == 2 ** (i + 1) - 1 for i in range(11)), "a_n=2^n-1 recurrence")
phi = (1 + math.sqrt(5)) / 2
psi = (1 - math.sqrt(5)) / 2
Fib = [0, 1]
for i in range(2, 16):
    Fib.append(Fib[-1] + Fib[-2])
for n in range(0, 14):
    chk(close((phi**n - psi**n) / math.sqrt(5), Fib[n]), f"Binet n={n}")
# characteristic: repeated root example a_n = 2a_{n-1} - a_{n-2} -> AP-like (A+Bn)1^n
seq = [1, 3]
for i in range(8):
    seq.append(2 * seq[-1] - seq[-2])
chk(seq == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], "repeated root r=1 gives (A+Bn)")

# --- olympiad-03 products, Stolz, asymptotics ---
for n in range(2, 15):
    p = F(1)
    for k in range(2, n + 1):
        p *= 1 - F(1, k * k)
    chk(p == F(n + 1, 2 * n), f"product (1-1/k^2) n={n}")
chk(close(F(5, 8), 3 / 4 * 8 / 9 * 15 / 16), "product n=4 = 5/8")
# Wallis finite closed form
for n in range(1, 8):
    p = 1.0
    for k in range(1, n + 1):
        p *= 4 * k * k / (4 * k * k - 1)
    closed = 2 ** (4 * n) * math.factorial(n) ** 4 / ((2 * n + 1) * math.factorial(2 * n) ** 2)
    chk(close(p, closed), f"Wallis finite form n={n}")
p = 1.0
for k in range(1, 3000):
    p *= 4 * k * k / (4 * k * k - 1)
chk(abs(p - math.pi / 2) < 0.001, "Wallis -> pi/2")
# Stolz H_n/ln n
H = 0.0
vals = {}
for n in range(1, 200001):
    H += 1.0 / n
    if n in (100, 1000, 10000, 100000):
        vals[n] = H / math.log(n)
chk(close(vals[100], 1.1264, 2e-3), "H_n/ln n at 1e2")
chk(close(vals[100000], 1.0501, 2e-3), "H_n/ln n at 1e5")
chk(vals[100] > vals[1000] > vals[10000] > vals[100000] > 1, "H_n/ln n decreasing to 1")
# arctan telescope
for n in (1, 3, 5, 10):
    s = sum(math.atan(1 / (k * k + k + 1)) for k in range(1, n + 1))
    chk(close(s, math.pi / 4 - math.atan(1 / (n + 1))), f"arctan telescope n={n}")
# asymptotics a_{n+1} = a_n + 1/a_n
a = 1.0
seq = {1: a}
for n in range(1, 2000):
    a = a + 1 / a
    seq[n + 1] = a
chk(close(seq[10], 4.5699, 2e-3), "a_10 = 4.5699")
chk(abs(seq[2000] / math.sqrt(4000) - 1) < 0.02, "a_n ~ sqrt(2n) at n=2000")
# remainder diverges like (1/2) ln n: a_n^2 - 2n grows unbounded but sublinear
chk(seq[2000] ** 2 - 4000 > seq[100] ** 2 - 200, "a_n^2 - 2n grows (log divergence)")

for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    chk(_condition, f"visual lesson: {_name}")

print(f"{N[0] - len(FAILS)}/{N[0]} checks passed")
if FAILS:
    raise SystemExit(1)
print("ALL PASS")
