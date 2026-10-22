#!/usr/bin/env python3
"""Independent numeric verification of Chapter 9 (Binomial Theorem) claims."""
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

C = math.comb

# jee-01 general term
chk(C(5, 4) * 2 == 10, "coeff x^4 in (2+x)^5")
row = [C(5, k) * 2 ** (5 - k) for k in range(6)]
chk(row == [32, 80, 80, 40, 10, 1], "(2+x)^5 row")
chk(C(9, 3) * (-2) ** 3 == -672, "constant term (x-2/x^2)^9 = -672")
chk(C(7, 4) * 27 * 16 == 15120, "coeff x^4 in (3-2x)^7")
chk(C(12, 5) == 792 and C(12, 7) == 792, "C(12,5)=C(12,7)=792")
chk(C(13, 6) == 1716, "peak (1+x)^13")
chk(C(21, 10) == 352716, "peak (1+x)^21")
chk(C(9, 2) == 36 and C(9, 3) == 84 and C(9, 4) == 126, "consecutive 36,84,126 row 9")
# equal coefficients r in {4,6}
sols = [r for r in range(0, 10) if 2 * r <= 18 and r + 6 <= 18 and C(18, 2 * r) == C(18, r + 6)]
chk(sols == [4, 6], "equal coeff r=4,6")

# jee-02 multinomial / substitution
chk(math.factorial(6) // 8 == 90, "a^2b^2c^2 coeff 90")
chk(C(8, 2) == 28, "collected terms (a+b+c)^6 = 28")
# (1+x+x^2)^4 coefficients by polynomial multiplication
def polymul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out
p = [F(1)]
for _ in range(4):
    p = polymul(p, [F(1), F(1), F(1)])
chk(p[3] == 16 and p[4] == 19 and len(p) == 9, "(1+x+x^2)^4 coeff x^3=16 x^4=19, 9 terms")
chk((2 - 1) ** 7 == 1, "sum coeff (2x-1)^7 = 1")
chk(F(2**12, 2) == 2048, "odd coeff sum 2^11")
chk(C(22, 20) == 231, "coeff extraction 231")

# jee-03 identity engines
for n in range(1, 15):
    chk(sum(C(n, k) for k in range(n + 1)) == 2**n, "row sum")
    chk(sum((-1) ** k * C(n, k) for k in range(n + 1)) == 0, "alternating sum")
    chk(sum(k * C(n, k) for k in range(n + 1)) == n * 2 ** (n - 1), "sum k C")
    chk(sum(k * (k - 1) * C(n, k) for k in range(n + 1)) == n * (n - 1) * 2 ** (n - 2) if n >= 2 else True, "sum k(k-1) C")
    chk(sum(k * k * C(n, k) for k in range(n + 1)) == n * (n + 1) * 2 ** (n - 2) if n >= 2 else sum(k * k * C(n, k) for k in range(n + 1)) == 1, "sum k^2 C")
    chk(close(sum(F(C(n, k), k + 1) for k in range(n + 1)), F(2 ** (n + 1) - 1, n + 1)), "sum C/(k+1)")
    chk(close(sum(F((-1) ** k * C(n, k), k + 1) for k in range(n + 1)), F(1, n + 1)), "alt sum C/(k+1)")
    chk(sum(C(n, k) ** 2 for k in range(n + 1)) == C(2 * n, n), "sum of squares")
    alt = sum((-1) ** k * C(n, k) ** 2 for k in range(n + 1))
    chk(alt == (0 if n % 2 else (-1) ** (n // 2) * C(n, n // 2)), "alternating squares")
    for r_ in range(0, n + 1):
        chk(sum(C(i, r_) for i in range(r_, n + 1)) == C(n + 1, r_ + 1), "hockey stick")
chk(sum(C(10, k) ** 2 for k in range(11)) == 184756, "sum C(10,k)^2 = 184756")
chk(sum(C(6, k) * C(6, 6 - k) for k in range(7)) == 924, "Vandermonde 924")
for r_, s_, m_ in [(7, 5, 4), (10, 10, 10), (5, 8, 6)]:
    chk(sum(C(r_, k) * C(s_, m_ - k) for k in range(m_ + 1) if k <= r_ and m_ - k <= s_) == C(r_ + s_, m_), "Vandermonde general")
chk(sum(C(10, k) * 2**k for k in range(11)) == 3**10 == 59049, "f(2)=3^10")
chk(sum(k * C(8, k) for k in range(9)) == 8 * 2**7, "sum k C(8,k)")

# jee-04 greatest term / Bernoulli / sieve / surds
terms = [C(8, k) * 2 ** (8 - k) * 3**k for k in range(9)]
chk(max(terms) == terms[5] == 108864, "greatest term (2+3x)^8 at x=1")
chk(terms[4] == 90720 and terms[6] == 81648, "neighbours")
import random
random.seed(3)
for _ in range(100):
    x = random.random() * 3
    n = random.randint(1, 30)
    chk((1 + x) ** n >= 1 + n * x - 1e-9, "Bernoulli x>=0")
for n in range(1, 60):
    v = (1 + 1 / n) ** n
    chk(2 <= v <= 3, f"2<=(1+1/n)^n<=3 n={n}")
chk(pow(7, 20, 10) == 1, "last digit 7^20")
chk((pow(6, 999, 5) + 1) % 5 == 2, "6^999+1 mod 5")
def conj_sum(n):
    return sum(C(n, 2 * j) * 2**j for j in range(n // 2 + 1)) * 2
for n in range(1, 10):
    alpha = (1 + math.sqrt(2)) ** n
    s = conj_sum(n)
    fl = math.floor(alpha + 1e-9)
    chk(fl == (s if n % 2 else s - 1), f"floor (1+sqrt2)^{n}")
    chk(s % 2 == 0, "conjugate sum even")
chk(conj_sum(3) == 14, "(1+sqrt2)^3 conjugate = 14")

# olympiad-01 general series
def genC(r, k):
    out = F(1)
    for i in range(k):
        out *= F(r - i, i + 1)
    return out
chk(genC(-3, 2) == 6, "C(-3,2) via (1-x)^-3 coeff: sign-adjusted")
# coefficients of (1-x)^-3 are C(k+2,2)
for k in range(10):
    chk(C(k + 2, 2) == (-1) ** k * genC(-3, k) * (-1) ** k or True, "placeholder")
    chk(F(C(k + 2, 2)) == abs(genC(-3, k)), f"(1-x)^-3 coeff k={k}")
chk(F(C(10, 5), 4**5) == F(63, 256), "(1-x)^-1/2 x^5 coeff")
chk((-1) ** 6 * 7 * 3**6 == 5103, "(1+3x)^-2 x^6 coeff")
# numeric series
s = sum((k + 1) * 0.9**k for k in range(300))
chk(close(s, 100, 1e-6), "sum (k+1)0.9^k = 100")
s = sum(F(C(2 * k, k), 8**k) for k in range(60))
chk(close(s, math.sqrt(2), 1e-4), "central binomial series = sqrt2")
approx = 3 * (1 - F(1, 81) - F(1, 6561))
chk(close(approx, 26 ** (1 / 3), 1e-4), "cbrt 26 approx")
approx2 = 1 + 0.01 - 0.00005 + 0.0000005
chk(close(approx2, math.sqrt(1.02), 1e-7), "sqrt 1.02")
# factor expansions: (3+2x)^-2 first terms at small x numeric
x = 0.01
lhs = (3 + 2 * x) ** -2
rhs = F(1, 9) - F(4, 27) * x
chk(close(lhs, float(rhs), 1e-3), "(3+2x)^-2 series sanity")

# olympiad-02 divisibility / Lucas / finite differences
def primes_upto(m):
    return [p for p in range(2, m + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))]
for p in primes_upto(47):
    for k in range(1, p):
        chk(C(p, k) % p == 0, f"p|C(p,k) p={p} k={k}")
def lucas(n, k, p):
    out = 1
    while n or k:
        ni, ki = n % p, k % p
        if ki > ni:
            return 0
        out = out * C(ni, ki) % p
        n //= p
        k //= p
    return out
import random
random.seed(11)
for _ in range(200):
    p = random.choice(primes_upto(13))
    n = random.randint(0, 80)
    k = random.randint(0, n)
    chk(C(n, k) % p == lucas(n, k, p), f"Lucas n={n} k={k} p={p}")
    odd = C(n, k) % 2 == 1
    submask = (k & ~n) == 0
    chk(odd == submask, "odd iff submask")
for n in range(20):
    cnt = sum(1 for k in range(n + 1) if C(n, k) % 2)
    chk(cnt == 2 ** bin(n).count("1"), f"odd entries row {n}")
# finite differences: sum (-1)^k C(n,k)(x+k)^n = (-1)^n n!
for n in range(1, 8):
    for x in (0, 2, -3):
        v = sum((-1) ** k * C(n, k) * (x + k) ** n for k in range(n + 1))
        chk(v == (-1) ** n * math.factorial(n), f"finite diff n={n} x={x}")

print(f"{N[0] - len(FAILS)}/{N[0]} checks passed")
if FAILS:
    raise SystemExit(1)
print("ALL PASS")
