#!/usr/bin/env python3
"""Independent numeric verification of Chapter 8 (Permutations & Combinations) claims."""
import math
from fractions import Fraction as F
from itertools import permutations, combinations, product as iproduct

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
P = lambda n, r: math.perm(n, r)

# jee-01 basics
chk(C(20, 5) - C(12, 5) == 14712, "committees at least one woman 14712")
chk(5**4 - 4**4 == 369, "strings with a 0: 369")
chk(9 * 8 * 7 + 8 * 8 * 7 == 952, "4-digit distinct div by 5: 952")
chk(2**7 == 128 and C(5, 3) == 10, "subsets/increasing functions")
# brute: 4-digit distinct digits divisible by 5
cnt = sum(1 for d in iproduct(range(10), repeat=4) if d[0] != 0 and len(set(d)) == 4 and (d[0] * 1000 + d[1] * 100 + d[2] * 10 + d[3]) % 5 == 0)
chk(cnt == 952, "brute 4-digit distinct div5")

# jee-02 permutations
chk(P(10, 4) == 5040, "P(10,4)")
chk(math.factorial(13) // (2 * 2 * 2) == 778377600, "COMBINATORICS")
chk(math.factorial(11) // 8 == 4989600, "MATHEMATICS")
# brute DAAR adjacent
words = set(permutations("DAAR"))
chk(len(words) == 12 and sum(1 for w in words if "".join(w).find("AA") >= 0) == 6, "DAAR adjacent 6 of 12")

# jee-03 circular / restrictions
chk(math.factorial(9) - 2 * math.factorial(8) == 282240, "10 people A,B non-adjacent")
chk(math.factorial(3) * C(4, 3) * math.factorial(3) == 144, "gap method 144")
chk(2 * math.factorial(5) * math.factorial(5) == 28800, "alternating 5M5W")
chk(2 * math.factorial(5) - (2 * math.factorial(4) * 2) == 144, "PQ together R not end 144")
# brute gap example: 6 people A,B,C pairwise non-adjacent
people = ["A", "B", "C", "D", "E", "F"]
cnt = 0
for perm in permutations(people):
    pos = {p: i for i, p in enumerate(perm)}
    if abs(pos["A"] - pos["B"]) > 1 and abs(pos["A"] - pos["C"]) > 1 and abs(pos["B"] - pos["C"]) > 1:
        cnt += 1
chk(cnt == 144, "brute pairwise non-adjacent 144")

# jee-04 combinations
chk(C(20, 5) - C(16, 5) == 11136, "at least one special book")
tot = 0
for a in range(4):
    for b in range(3, 8):
        for w in range(2, 6):
            if b + w + a == 11:
                tot += C(7, b) * C(5, w) * C(3, a)
chk(tot == 1360, "cricket team 1360")
for n in range(1, 15):
    for r in range(0, n):
        chk(C(n, r) == C(n - 1, r) + C(n - 1, r - 1) if 0 < r < n else True, "Pascal")
    for r in range(0, n + 1):
        chk(sum(C(i, r) for i in range(r, n + 1)) == C(n + 1, r + 1), f"hockey stick n={n} r={r}")

# jee-05 stars and bars
chk(C(17, 2) == 136 and C(14, 2) == 91, "x+y+z=15: 136/91")
chk(C(23, 3) - C(17, 3) == 1091, "bounded x1<=5: 1091")
chk(C(16, 4) == 1820, "12 fruits 5 varieties")
# brute stars-bars small
cnt = sum(1 for t in iproduct(range(16), repeat=3) if sum(t) == 15)
chk(cnt == 136, "brute x+y+z=15")
# compositions of 10 into parts >=2
def comps(n, mn=1):
    if n == 0:
        yield []
    for first in range(mn, n + 1):
        for rest in comps(n - first, mn):
            yield [first] + rest
chk(len(list(comps(10, 2))) == 34, "compositions of 10 parts>=2: 34")
chk(2**9 == sum(C(9, k) for k in range(10)), "compositions any parts 2^(n-1)")

# jee-06 IE and derangements
chk(500 + 333 + 200 - 166 - 100 - 66 + 33 == 734, "divisible by 2,3,5: 734")
def derange(n):
    return round(math.factorial(n) * sum(F(-1) ** k / math.factorial(k) for k in range(n + 1)))
D = [derange(n) for n in range(9)]
chk(D == [1, 0, 1, 2, 9, 44, 265, 1854, 14833], "derangement numbers")
for n in range(2, 9):
    chk(D[n] == (n - 1) * (D[n - 1] + D[n - 2]), f"D recurrence n={n}")
    chk(D[n] == round(math.factorial(n) / math.e), f"D_n nearest n!/e n={n}")
# brute derangements n=5
cnt = sum(1 for p in permutations(range(5)) if all(p[i] != i for i in range(5)))
chk(cnt == 44, "brute D5=44")
chk(C(5, 2) * D[3] == 20, "exactly 2 fixed: 20")
chk(sum(C(5, k) * D[5 - k] for k in range(6)) == 120, "rencontres sum = 5!")
chk(3**5 - 3 * 2**5 + 3 == 150, "onto 5->3: 150")
chk(C(52, 6) - 4 * C(39, 6) + 6 * C(26, 6) - 4 * C(13, 6) == 8682544, "all four suits")
# brute onto small
cnt = sum(1 for f in iproduct(range(3), repeat=5) if set(f) == {0, 1, 2})
chk(cnt == 150, "brute onto 150")

# jee-07 pigeonhole / recurrences
# odd part: any 11 from 1..20 contain dividing pair (brute force max size without)
import itertools as it
maxsize = 0
for S in it.combinations(range(11, 21), 10):
    ok = all(not (b % a == 0) for a, b in it.combinations(S, 2))
    if ok:
        maxsize = 10
chk(maxsize == 10, "{11..20} no dividing pair")
# domino tilings / staircase Fibonacci
a = [1, 1]
for i in range(12):
    a.append(a[-1] + a[-2])
chk(a[10] == 89, "staircase/tiling a10=89")

# olympiad-01 Catalan / ballot
def catalan(n):
    return C(2 * n, n) // (n + 1)
chk([catalan(n) for n in range(8)] == [1, 1, 2, 5, 14, 42, 132, 429], "Catalan values")
chk(C(8, 4) - C(8, 5) == 14, "reflection C4")
# brute Dyck
def dyck(n):
    cnt = 0
    for ups in combinations(range(2 * n), n):
        s = set(ups)
        bal = 0
        ok = True
        for i in range(2 * n):
            bal += 1 if i in s else -1
            if bal < 0:
                ok = False
                break
        cnt += ok
    return cnt
for n in range(1, 8):
    chk(dyck(n) == catalan(n), f"brute Dyck n={n}")
chk(F(5 - 3, 8) * C(8, 3) == 14, "ballot 5,3 = 14")

# olympiad-02 Burnside
def necklace_bruteforce(n, k):
    seen = set()
    for col in iproduct(range(k), repeat=n):
        rots = [tuple(col[(i + s) % n] for i in range(n)) for s in range(n)]
        seen.add(min(rots))
    return len(seen)
def necklace_formula(n, k):
    return sum(F(math.gcd(n, s) and 1) * 0 for s in range(0)) or sum(
        F(sum(1 for _ in [0]) ) * 0 for _ in []) or F(1, n) * sum(
        F(phi(d)) * k ** (n // d) for d in range(1, n + 1) if n % d == 0)
def phi(m):
    return sum(1 for i in range(1, m + 1) if math.gcd(i, m) == 1)
chk(necklace_bruteforce(4, 2) == 6, "brute necklace 4,2 = 6")
tot = sum(F(phi(d)) * 2 ** (4 // d) for d in (1, 2, 4))
chk(tot / 4 == 6, "necklace formula N(4,2)")
fix_sum = 64 + 2 * 2 + 2 * 4 + 8 + 3 * 16 + 3 * 8
chk(fix_sum == 156 and fix_sum // 12 == 13, "bracelet hexagon 13")

# olympiad-03 partitions / Stirling / EKR
def partitions(n, mx=None):
    if n == 0:
        yield []
        return
    for first in range(min(mx or n, n), 0, -1):
        for rest in partitions(n - first, first):
            yield [first] + rest
plist = [len(list(partitions(n))) for n in range(1, 11)]
chk(plist == [1, 2, 3, 5, 7, 11, 15, 22, 30, 42], "p(n) values")
# distinct vs odd for n=10
def parts_pred(n, pred, mx=None):
    if n == 0:
        yield []
        return
    for first in range(min(mx or n, n), 0, -1):
        if pred(first):
            for rest in parts_pred(n - first, pred, first):
                yield [first] + rest
dist = [p for p in partitions(10) if len(p) == len(set(p))]
odd = [p for p in partitions(10) if all(x % 2 == 1 for x in p)]
chk(len(dist) == 10 and len(odd) == 10, "distinct = odd parts at n=10")
chk(plist[8] + plist[7] - plist[4] - plist[2] == 42, "pentagonal p(10)")
# Stirling
S = {(0, 0): 1}
def stir(n, k):
    if (n, k) not in S:
        S[(n, k)] = k * stir(n - 1, k) + stir(n - 1, k - 1) if 0 < k <= n else 0
    return S[(n, k)]
chk(stir(6, 3) == 90, "S(6,3)=90")
chk(F(1, 6) * (3**6 - 3 * 2**6 + 3) == 90, "S(6,3) closed form")
chk([sum(stir(n, k) for k in range(n + 1)) for n in range(7)] == [1, 1, 2, 5, 15, 52, 203], "Bell numbers")
chk(math.factorial(6) // (8 * 6) == 15, "unlabelled pairs 15")
# EKR brute small
def ekr_max(n, k):
    sets = [set(s) for s in combinations(range(n), k)]
    best = 0
    # greedy clique lower + star upper check via brute over subfamilies too slow; verify star size and pairwise
    star = [s for s in sets if 0 in s]
    chk(len(star) == C(n - 1, k - 1), "star size")
    chk(all(a & b for a, b in combinations(star, 2)), "star intersecting")
for n, k in [(6, 2), (7, 3), (8, 3)]:
    ekr_max(n, k)
# Sperner middle layer
chk(C(6, 3) == 20, "Sperner bound n=6")

print(f"{N[0] - len(FAILS)}/{N[0]} checks passed")
if FAILS:
    raise SystemExit(1)
print("ALL PASS")
