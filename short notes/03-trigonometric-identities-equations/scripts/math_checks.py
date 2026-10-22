#!/usr/bin/env python3
"""Independent numeric verification of Chapter 3 (Trig Identities & Equations) claims."""
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

R = math.radians

# --- Pythagorean + reciprocal ---
for deg in (0, 17, 45, 80, 123, 190, 250, 331):
    s, c = math.sin(R(deg)), math.cos(R(deg))
    chk(close(s * s + c * c, 1.0), f"sin^2+cos^2 {deg}")
    chk(close(math.tan(R(deg)), s / c) if c else True, f"tan=sin/cos {deg}")
    chk(close(1 + math.tan(R(deg)) ** 2, 1 / (c * c)) if abs(c) > 1e-12 else True, f"1+tan^2=sec^2 {deg}")
chk(close(math.sqrt(math.sin(R(-123)) ** 2), abs(math.sin(R(-123)))), "sqrt(sin^2)=|sin|")

# --- allied angles ---
for deg in (20, 65, 140):
    chk(close(math.sin(R(180 - deg)), math.sin(R(deg))), f"sin(180-A) {deg}")
    chk(close(math.cos(R(180 - deg)), -math.cos(R(deg))), f"cos(180-A) {deg}")
    chk(close(math.sin(R(90 - deg)), math.cos(R(deg))), f"sin(90-A) {deg}")
    chk(close(math.sin(R(270 + deg)), -math.cos(R(deg))), f"sin(270+A) {deg}")
    chk(close(math.tan(R(180 + deg)), math.tan(R(deg))), f"tan period 180 {deg}")
chk(close(math.sin(R(135)), math.sqrt(2) / 2), "sin135")
chk(close(math.cos(R(225)), -math.sqrt(2) / 2), "cos225")
chk(close(math.tan(R(210)), math.sqrt(3) / 3), "tan 7pi/6")

# --- compound angles ---
chk(close(math.sin(R(75)), (math.sqrt(6) + math.sqrt(2)) / 4), "sin75")
chk(close(math.tan(R(105)), -(2 + math.sqrt(3))), "tan105")
A, B = math.asin(3 / 5), math.acos(5 / 13)
chk(close(math.sin(A + B), 63 / 65), "sin(A+B)=63/65")
for a, b in ((20, 35), (70, -15), (123, 47)):
    chk(close(math.sin(R(a + b)), math.sin(R(a)) * math.cos(R(b)) + math.cos(R(a)) * math.sin(R(b))), f"sin(A+B) {a},{b}")
    chk(close(math.cos(R(a - b)), math.cos(R(a)) * math.cos(R(b)) + math.sin(R(a)) * math.sin(R(b))), f"cos(A-B) {a},{b}")
    chk(close(math.cos(R(a + b)), math.cos(R(a)) * math.cos(R(b)) - math.sin(R(a)) * math.sin(R(b))), f"cos(A+B) {a},{b}")
ta, tb = math.tan(R(23)), math.tan(R(41))
chk(close(math.tan(R(64)), (ta + tb) / (1 - ta * tb)), "tan(A+B)")
for a, b in ((75, 15), (50, 20)):
    chk(close(2 * math.sin(R(a)) * math.sin(R(b)), math.cos(R(a - b)) - math.cos(R(a + b))), f"product identity {a},{b}")
chk(close(math.cos(R(75)) - math.cos(R(15)), -math.sqrt(2) / 2), "cos75-cos15")
chk(close(math.sin(R(75)) + math.sin(R(15)), math.sqrt(6) / 2), "sin75+sin15")
a, b = 3.0, -4.0
mx = max(abs(a * math.sin(R(x)) + b * math.cos(R(x))) for x in range(0, 360, 2))
chk(mx <= math.sqrt(a * a + b * b) + 1e-9 and close(mx, math.sqrt(a * a + b * b), 1e-2), "amplitude bound 3sin-4cos")

# --- multiple angles ---
A = math.acos(3 / 5)
chk(close(math.cos(2 * A), -7 / 25), "cos2A = -7/25")
chk(close(math.sin(2 * A), 24 / 25), "sin2A = 24/25")
chk(close(math.tan(A / 2), 0.5), "tan(A/2)=1/2 for cosA=3/5 acute")
for deg in (10, 44, 77, 123):
    s, c = math.sin(R(deg)), math.cos(R(deg))
    chk(close(math.sin(R(2 * deg)), 2 * s * c), f"sin2A {deg}")
    chk(close(math.cos(R(2 * deg)), c * c - s * s), f"cos2A {deg}")
    chk(close(math.cos(R(2 * deg)), 2 * c * c - 1), f"cos2A form2 {deg}")
    chk(close(math.sin(R(3 * deg)), 3 * s - 4 * s**3), f"sin3A {deg}")
    chk(close(math.cos(R(3 * deg)), 4 * c**3 - 3 * c), f"cos3A {deg}")
    chk(close(math.sin(R(deg)) ** 2, (1 - math.cos(R(2 * deg))) / 2), f"power red sin {deg}")
    chk(close(math.tan(R(deg / 2)), (1 - c) / s), f"tan half identity {deg}")
    chk(close(math.tan(R(deg / 2)), s / (1 + c)), f"tan half identity-2 {deg}")
chk(close(((math.sin(R(30)) + math.cos(R(30))) ** 2), 1 + math.sin(R(60))), "(sin+cos)^2 = 1+sin2A")

# --- transformations ---
for A, B in ((20, 35), (80, 25)):
    chk(close(2 * math.sin(R(A)) * math.cos(R(B)), math.sin(R(A + B)) + math.sin(R(A - B))), f"2sinAcosB {A},{B}")
    chk(close(2 * math.cos(R(A)) * math.cos(R(B)), math.cos(R(A + B)) + math.cos(R(A - B))), f"2cosAcosB {A},{B}")
C, D = 75.0, 15.0
chk(close(math.sin(R(C)) + math.sin(R(D)), 2 * math.sin(R((C + D) / 2)) * math.cos(R((C - D) / 2))), "sum-to-product sin")
chk(close(math.cos(R(C)) - math.cos(R(D)), -2 * math.sin(R((C + D) / 2)) * math.sin(R((C - D) / 2))), "sum-to-product cos diff")
for deg in (30, 47):
    lhs = math.sin(R(deg)) + math.sin(R(3 * deg)) + math.sin(R(5 * deg))
    chk(close(lhs, math.sin(R(3 * deg)) * (2 * math.cos(R(2 * deg)) + 1)), f"factor sin3x(2cos2x+1) {deg}")

# --- general solutions ---
for n in range(-3, 4):
    x = n * math.pi + ((-1) ** n) * math.pi / 6
    chk(close(math.sin(x), 0.5), f"sin general n={n}")
    chk(close(math.cos(2 * n * math.pi + math.pi / 3), 0.5), f"cos general n={n}")
    chk(close(math.cos(2 * n * math.pi - math.pi / 3), 0.5), f"cos general -alpha n={n}")
    chk(close(math.tan(n * math.pi + math.pi / 4), 1.0), f"tan general n={n}")

# --- equations methods ---
prev = math.sin(0) - math.cos(0)
count = 0
for i in range(1, 14401):
    x = R(i / 40)
    f = math.sin(2 * x) - math.cos(x)
    if prev == 0 or f * prev < 0:
        count += 1
    prev = f
chk(count == 4, "sin2x=cosx has exactly 4 roots in [0, 2pi)")
for x in (math.pi / 6, math.pi / 2, 5 * math.pi / 6, 3 * math.pi / 2):
    chk(close(math.sin(2 * x), math.cos(x)), f"sin2x=cosx root {x:.4f}")
chk(close(math.sqrt(3) * math.sin(0) + math.cos(0), 1.0), "root x=0 of sqrt3 sinx + cosx = 1")
chk(close(math.sqrt(3) * math.sin(2 * math.pi / 3) + math.cos(2 * math.pi / 3), 1.0), "root x=2pi/3")
for x in (7 * math.pi / 6, 11 * math.pi / 6):
    chk(close(2 * math.cos(x) ** 2 + 3 * math.sin(x), 0.0), f"2cos^2+3sin=0 root {x:.4f}")
for x in (0, math.pi / 2, math.pi, 3 * math.pi / 2):
    ok = abs(math.sin(x) + math.cos(x) - 1) < 1e-12
    chk(ok == (x in (0, math.pi / 2)), f"filter check at {x:.3f}")

# --- conditional identities ---
for A, B in ((50, 60), (30, 90), (20, 140)):
    C = 180 - A - B
    sa, sb, sc = math.tan(R(A)), math.tan(R(B)), math.tan(R(C))
    if all(abs(t) < 1e6 for t in (sa, sb, sc)) and abs(math.cos(R(A)) * math.cos(R(B)) * math.cos(R(C))) > 1e-9:
        chk(close(sa + sb + sc, sa * sb * sc), f"tan identity {A},{B},{C}")
    chk(close(math.sin(R(2 * A)) + math.sin(R(2 * B)) + math.sin(R(2 * C)),
              4 * math.sin(R(A)) * math.sin(R(B)) * math.sin(R(C))), f"sin2 identity {A},{B}")
    chk(close(math.cos(R(A)) ** 2 + math.cos(R(B)) ** 2 + math.cos(R(C)) ** 2
              + 2 * math.cos(R(A)) * math.cos(R(B)) * math.cos(R(C)), 1.0), f"cos^2 identity {A},{B}")
    chk(close(math.sin(R(A)) + math.sin(R(B)) + math.sin(R(C)),
              4 * math.cos(R(A / 2)) * math.cos(R(B / 2)) * math.cos(R(C / 2))), f"sin sum identity {A},{B}")
    h = (math.tan(R(A / 2)) * math.tan(R(B / 2)) + math.tan(R(B / 2)) * math.tan(R(C / 2))
         + math.tan(R(C / 2)) * math.tan(R(A / 2)))
    chk(close(h, 1.0), f"half-angle product identity {A},{B}")
chk(close(math.tan(R(20)) * math.tan(R(40)) * math.tan(R(80)), math.sqrt(3)), "tan20 tan40 tan80 = sqrt3")
ts = [math.tan(R(20)), math.tan(R(80)), math.tan(R(140))]
chk(close(ts[0] * ts[1] * ts[2], -math.sqrt(3)), "cubic root product = -sqrt3")
chk(close(ts[0] + ts[1] + ts[2], 3 * math.sqrt(3)), "cubic root sum = 3sqrt3")

# --- Weierstrass ---
for x in (0, math.pi / 2):
    t = math.tan(x / 2)
    chk(close(math.sin(x), 2 * t / (1 + t * t)) and close(math.cos(x), (1 - t * t) / (1 + t * t)),
        f"Weierstrass at {x:.3f}")
for deg in (30, 100, 250):
    t = math.tan(R(deg / 2))
    chk(close(math.sin(R(deg)), 2 * t / (1 + t * t)), f"weierstrass sin {deg}")

# --- roots of unity products ---
def sinprod(n):
    p = 1.0
    for k in range(1, n):
        p *= math.sin(math.pi * k / n)
    return p

chk(close(sinprod(7), 7 / 64), "prod sin k pi/7 = 7/64")
chk(close(sinprod(5), 5 / 16), "prod sin k pi/5 = 5/16")
chk(close(sinprod(6), 6 / 32), "prod sin k pi/6")
chk(close(math.cos(math.pi / 7) * math.cos(2 * math.pi / 7) * math.cos(3 * math.pi / 7), 1 / 8), "cos product 1/8")
chk(close(math.sin(R(36)) * math.sin(R(72)), math.sqrt(5) / 4), "sin36 sin72 = sqrt5/4")

# --- series + square sums ---
theta = math.pi / 6
lhs = sum(math.sin(k * theta) for k in range(1, 4))
chk(close(lhs, math.sin(3 * theta / 2) * math.sin(4 * theta / 2) / math.sin(theta / 2)), "sum sin ktheta n=3")
lhs2 = sum(math.cos(k * theta) for k in range(1, 4))
chk(close(lhs2, math.sin(3 * theta / 2) * math.cos(4 * theta / 2) / math.sin(theta / 2)), "sum cos ktheta n=3")
for n in (3, 4, 5, 6, 7):
    s = sum((math.cos(math.pi * k / n) / math.sin(math.pi * k / n)) ** 2 for k in range(1, n))
    chk(close(s, (n - 1) * (n - 2) / 3), f"cot^2 sum n={n}")
    s2 = sum(1 / math.sin(math.pi * k / n) ** 2 for k in range(1, n))
    chk(close(s2, (n * n - 1) / 3), f"csc^2 sum n={n}")

# --- special values ---
chk(close(math.sin(R(18)), (math.sqrt(5) - 1) / 4), "sin18")
chk(close(math.cos(R(36)), (math.sqrt(5) + 1) / 4), "cos36")
chk(close(math.sin(R(36)), math.cos(R(54))), "sin36 = cos54")

# --- triangle toolkit (worked example A=60, b=5, c=8) ---
a = math.sqrt(25 + 64 - 2 * 5 * 8 * 0.5)
chk(close(a, 7.0), "cosine rule a=7")
D = 0.5 * 5 * 8 * math.sin(R(60))
chk(close(D, 10 * math.sqrt(3)), "area = 10sqrt3")
s = (7 + 5 + 8) / 2
chk(close(D, math.sqrt(s * (s - 7) * (s - 5) * (s - 8))), "Heron agrees")
Rcirc = 7 / (2 * math.sin(R(60)))
chk(close(Rcirc, 7 / math.sqrt(3)), "circumradius")
r = D / s
chk(close(r, math.sqrt(3)), "inradius r = sqrt3")
chk(close(math.tan(R(30)), r / (s - 7)), "tan(A/2) = r/(s-a)")

print(f"Chapter 3 math checks: {N[0] - len(FAILS)}/{N[0]} PASS", "FAILURES:", len(FAILS))
if FAILS:
    raise SystemExit(1)
