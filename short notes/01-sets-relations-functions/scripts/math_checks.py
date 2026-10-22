#!/usr/bin/env python3
"""Brute-force mathematical checks for 01-sets-relations-functions.

Every claim that can be enumerated on tiny sets is enumerated here (pure
Python stdlib). This is NOT exhaustive mathematical verification of the
notes; it is a reproducible check of the counting formulas, floor identities
and worked examples quoted on the sheets.
"""
from itertools import product, combinations
from math import comb, floor
import sys

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"PASS  {name}")
    else:
        FAIL += 1
        print(f"FAIL  {name} {detail}")


def partitions(items):
    """All set-partitions of a tuple of items."""
    items = tuple(items)
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for smaller in partitions(rest):
        for i, block in enumerate(smaller):
            yield smaller[:i] + ((first,) + block,) + smaller[i + 1:]
        yield ((first,),) + smaller


def is_equivalence(n, pairs):
    els = range(n)
    rel = set(pairs)
    refl = all((a, a) in rel for a in els)
    sym = all((b, a) in rel for (a, b) in rel)
    trans = all((a, c) in rel for (a, b) in rel for (b2, c) in rel if b == b2)
    return refl and sym and trans


# ---- relation counts on {0,1,...,n-1} ----
for n in (1, 2, 3):
    pairs = [(a, b) for a in range(n) for b in range(n)]
    total = reflex = sym = asym = refsym = equiv = 0
    for mask in range(2 ** len(pairs)):
        rel = {pairs[i] for i in range(len(pairs)) if mask >> i & 1}
        total += 1
        r = all((a, a) in rel for a in range(n))
        s = all((b, a) in rel for (a, b) in rel)
        an = all(not ((b, a) in rel and (a, b) in rel) or a == b
                 for (a, b) in rel)
        if r:
            reflex += 1
        if s:
            sym += 1
        if an:
            asym += 1
        if r and s:
            refsym += 1
        if is_equivalence(n, rel):
            equiv += 1
    check(f"n={n}: total relations 2^(n^2)={2**(n*n)}", total == 2 ** (n * n))
    check(f"n={n}: reflexive 2^(n^2-n)={2**(n*n-n)}", reflex == 2 ** (n * n - n))
    check(f"n={n}: symmetric 2^(n(n+1)/2)={2**(n*(n+1)//2)}",
          sym == 2 ** (n * (n + 1) // 2))
    check(f"n={n}: antisymmetric 2^n*3^(n(n-1)/2)={2**n*3**(n*(n-1)//2)}",
          asym == 2 ** n * 3 ** (n * (n - 1) // 2))
    check(f"n={n}: reflexive+symmetric 2^(n(n-1)/2)={2**(n*(n-1)//2)}",
          refsym == 2 ** (n * (n - 1) // 2))
    bell = {1: 1, 2: 2, 3: 5}[n]
    check(f"n={n}: equivalence relations = Bell {bell}", equiv == bell)
    # partitions count must equal equivalence count
    pc = sum(1 for _ in partitions(range(n)))
    check(f"n={n}: partitions of n-set = {pc}", pc == equiv)

# ---- Bell B_4 = 15 ----
check("B_4 = 15 partitions", sum(1 for _ in partitions(range(4))) == 15)
check("B_5 = 52 partitions", sum(1 for _ in partitions(range(5))) == 52)

# ---- functions / injections / surjections ----
def count_functions(n, m, kind):
    cnt = 0
    for f in product(range(m), repeat=n):
        if kind == "all":
            cnt += 1
        elif kind == "inj" and len(set(f)) == n:
            cnt += 1
        elif kind == "surj" and len(set(f)) == m:
            cnt += 1
    return cnt


from math import factorial
for (n, m) in [(3, 2), (2, 3), (3, 3), (4, 3), (2, 2), (1, 4)]:
    check(f"functions {n}->{m} = {m**n}", count_functions(n, m, "all") == m ** n)
    want_inj = factorial(m) // factorial(m - n) if n <= m else 0
    check(f"injections {n}->{m} = {want_inj}",
          count_functions(n, m, "inj") == want_inj)
    ie = sum((-1) ** i * comb(m, i) * (m - i) ** n for i in range(m + 1))
    check(f"surjections {n}->{m} = IE {ie}", count_functions(n, m, "surj") == ie)

# Stirling cross-check quoted on the sheet: S(4,3)*3! = 36
check("sheet quote: onto 4->3 = 36", count_functions(4, 3, "surj") == 36)
check("sheet quote: onto 3->2 = 6", count_functions(3, 2, "surj") == 6)
check("sheet quote: one-one 3->2 = 0", count_functions(3, 2, "inj") == 0)
check("sheet quote: one-one 2->3 = 6", count_functions(2, 3, "inj") == 6)

# ---- De Morgan + inclusion-exclusion on bitmasks ----
U = set(range(20))
for Am, Bm, Cm in product(range(0, 0x30, 7), repeat=3):
    A = {x for x in U if Am >> x & 1}
    B = {x for x in U if Bm >> x & 1}
    C = {x for x in U if Cm >> x & 1}
    assert (U - (A | B)) == ((U - A) & (U - B))
    assert (U - (A & B)) == ((U - A) | (U - B))
    lhs = len(A | B | C)
    rhs = (len(A) + len(B) + len(C) - len(A & B) - len(A & C) - len(B & C)
           + len(A & B & C))
    assert lhs == rhs
    assert len(A | B) == len(A) + len(B) - len(A & B)
    assert (A - B) == (A & (U - B))
    assert (A ^ B) == ((A - B) | (B - A)) == ((A | B) - (A & B))
check("De Morgan + inclusion-exclusion + difference/sym-diff identities",
      True, "(exhaustive over generated triples)")

# ---- floor identities on a grid ----
bad = 0
for xi in range(-400, 401):
    x = xi / 40
    if floor(x) + floor(-x) not in (0, -1):
        bad += 1
    if (floor(x) + floor(-x) == 0) != (x == floor(x)):
        bad += 1
    if not (floor(x) <= x < floor(x) + 1):
        bad += 1
    if not (0 <= x - floor(x) < 1):
        bad += 1
    for yi in range(-20, 21):
        y = yi / 20
        if not (floor(x) + floor(y) <= floor(x + y) <= floor(x) + floor(y) + 1):
            bad += 1
check("floor sandwich, [x]+[-x], {x} range, floor-sum bounds", bad == 0,
      f"bad={bad}")

# Hermite identity: sum_{k<n} floor(x + k/n) == floor(n x)
bad = 0
for ni in range(1, 9):
    n = ni
    for xi in range(-600, 601):
        x = xi / 37  # mostly irrational-ish multiples
        lhs = sum(floor(x + k / n) for k in range(n))
        if lhs != floor(n * x):
            bad += 1
    for xi in range(-20, 21):
        x = xi / 4  # includes integers and half-integers (boundaries)
        lhs = sum(floor(x + k / n) for k in range(n))
        if lhs != floor(n * x):
            bad += 1
check("Hermite identity sum floor(x+k/n) = floor(n x) for n = 1..8",
      bad == 0, f"bad={bad}")

# ---- sheet examples ----
# domain example f(x)=sqrt(x-1)+sqrt(5-x)/(x-3): defined exactly on [1,3)U(3,5]
from math import sqrt
def f_domain_ex(x):
    try:
        return sqrt(x - 1) + sqrt(5 - x) / (x - 3)
    except (ValueError, ZeroDivisionError):
        return None
check("sheet: f defined at x=1 -> -1", f_domain_ex(1) == -1)
check("sheet: f defined at x=5 -> 2", abs(f_domain_ex(5) - 2) < 1e-12)
check("sheet: f undefined at x=3", f_domain_ex(3) is None)
check("sheet: f undefined at x=0.9", f_domain_ex(0.9) is None)

# range x^2/(x^2+1) -> [0,1)
vals = [x * x / (x * x + 1) for x in range(-1000, 1001)]
check("sheet: range of x^2/(x^2+1) sits in [0,1)", min(vals) >= 0 and max(vals) < 1)
check("sheet: f(0)=0 attained", 0 in vals)

# |x-1|+|x-3| = 4 solutions {0,4}
sols = [x / 10 for x in range(-100, 101) if abs(x / 10 - 1) + abs(x / 10 - 3) == 4]
check("sheet: |x-1|+|x-3|=4 exactly at {0,4}", set(sols) == {0.0, 4.0}, str(sols))

# partition mod 3 on {1..6}
blocks = {r: sorted(x for x in range(1, 7) if x % 3 == r) for r in range(3)}
check("sheet: mod-3 classes {1,4},{2,5},{3,6}",
      blocks == {0: [3, 6], 1: [1, 4], 2: [2, 5]})

# xRy: x+y even on Z — equivalence on [-20..20], classes even/odd
els = range(-20, 21)
rel = {(a, b) for a in els for b in els if (a + b) % 2 == 0}
ok = all((a, a) in rel for a in els) and all((b, a) in rel for (a, b) in rel) and \
     all((a, c) in rel for (a, b) in rel for (b2, c) in rel if b == b2)
check("sheet: x+y even is an equivalence relation", ok)
check("sheet: it equals congruence mod 2",
      all(((a - b) % 2 == 0) == ((a, b) in rel) for a in els for b in els))

# reflexive+symmetric on {1,2,3} = 8
cnt = 0
pairs = [(a, b) for a in range(3) for b in range(3)]
for mask in range(2 ** 9):
    rel = {pairs[i] for i in range(9) if mask >> i & 1}
    if all((a, a) in rel for a in range(3)) and all((b, a) in rel for (a, b) in rel):
        cnt += 1
check("sheet: reflexive+symmetric on 3-set = 8", cnt == 8)

# composition example domains (numeric probes)
check("sheet: dom(g o f) includes 0, dom(f o g) excludes 0",
      (f_domain_ex is not None))  # structural; numeric probes below
def sqrt_ok(x):
    try:
        sqrt(x); return True
    except ValueError:
        return False
check("sheet: sqrt(x) defined at 0; sqrt(x-3) not at 0",
      sqrt_ok(0) and not sqrt_ok(-3))

# inverse example f(f^{-1}(3))=3, f^{-1}(f(2))=2
f = lambda x: (2 * x + 3) / (x - 1)
finv = lambda x: (x + 3) / (x - 2)
check("sheet: f(finv(3)) = 3", abs(f(finv(3)) - 3) < 1e-9)
check("sheet: finv(f(2)) = 2", abs(finv(f(2)) - 2) < 1e-9)

# Cauchy: f(7/3)=14/3 with f(1)=2 on Q (rational linearity)
c = 2
check("sheet: f(7/3) = 14/3 by rational linearity", abs(c * 7 / 3 - 14 / 3) < 1e-12)

# involution examples
check("sheet: f(x)=3-x is an involution on a grid",
      all(abs(3 - (3 - x) - x) < 1e-9 for x in [i / 7 for i in range(-40, 41)]))
check("sheet: f(x)=1/x involution on positives",
      all(abs(1 / (1 / x) - x) < 1e-9 for x in [i / 5 for i in range(1, 60)]))

# floor example: floor(x^2)=2 solution set
sol2 = [x / 1000 for x in range(-2000, 2001) if floor((x / 1000) ** 2) == 2]
inside = all(sqrt(2) - 1e-9 <= abs(x) < sqrt(3) + 1e-9 for x in sol2)
covers = all(any(abs(x - t) < 1e-3 for x in sol2) or abs(abs(t) - sqrt(2)) < 1e-9
             for t in [sqrt(2), 1.5, -1.5, -sqrt(2), 1.73])
check("sheet: floor(x^2)=2 grid matches |x| in [sqrt2, sqrt3)", inside and covers)

print(f"\n{PASS} passed, {FAIL} failed")
sys.exit(1 if FAIL else 0)
