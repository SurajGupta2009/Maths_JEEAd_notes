#!/usr/bin/env python3
"""Independent numeric verification of Chapter 4 (Inverse Trigonometric Functions) claims."""
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

def cot(x):
    return math.cos(x) / math.sin(x)

def acot(x):
    # JEE convention: principal cot^{-1} in (0, pi)
    return math.pi / 2 - math.atan(x)

def asec(x):
    # principal sec^{-1} in [0, pi] \ {pi/2}
    return math.acos(1.0 / x)

def acsc(x):
    return math.asin(1.0 / x)

pi = math.pi

# --- standard values ---
std_asin = {0: 0, 0.5: pi/6, 1/math.sqrt(2): pi/4, math.sqrt(3)/2: pi/3, 1: pi/2, -0.5: -pi/6, -1: -pi/2}
for x, v in std_asin.items():
    chk(close(math.asin(x), v), f"asin std {x}")
std_acos = {0: pi/2, 0.5: pi/3, 1/math.sqrt(2): pi/4, math.sqrt(3)/2: pi/6, 1: 0, -0.5: 2*pi/3, -1: pi}
for x, v in std_acos.items():
    chk(close(math.acos(x), v), f"acos std {x}")
std_atan = {0: 0, 1/math.sqrt(3): pi/6, 1: pi/4, math.sqrt(3): pi/3, -1: -pi/4}
for x, v in std_atan.items():
    chk(close(math.atan(x), v), f"atan std {x}")

# --- complementary pairs ---
for x in (-1, -0.7, -0.3, 0, 0.2, 0.6, 1):
    chk(close(math.asin(x) + math.acos(x), pi/2), f"asin+acos=pi/2 at {x}")
for x in (-3.7, -1, -0.4, 0, 0.9, 2.5, 50):
    chk(close(math.atan(x) + acot(x), pi/2), f"atan+acot=pi/2 at {x}")
for x in (-3.7, -1.2, -1, 1, 1.5, 40):
    chk(close(asec(x) + acsc(x), pi/2), f"asec+acsc=pi/2 at {x}")

# --- inverse-of-trig reduction reads ---
def asin_sin(x):
    # reduce to [-pi/2, 3pi/2)
    t = x - 2*pi*round(x/(2*pi))
    while t < -pi/2 - 1e-12:
        t += 2*pi
    while t >= 3*pi/2 - 1e-12:
        t -= 2*pi
    return t if t <= pi/2 else pi - t

def acos_cos(x):
    t = x - 2*pi*math.floor(x/(2*pi))
    if t < 0:
        t += 2*pi
    return t if t <= pi else 2*pi - t

def atan_tan(x):
    t = x - pi*round(x/pi)
    while t <= -pi/2 - 1e-12:
        t += pi
    while t > pi/2 - 1e-12:   # keep in (-pi/2, pi/2]
        t -= pi
    return t

for x in [0, 0.3, -0.3, pi/2, pi/2 + 0.4, 7*pi/6, 5*pi/4, 9*pi/5, 3.0, pi, 4.0, -2.5, -7*pi/6, 2*pi + 0.3, 11*pi/4]:
    chk(close(asin_sin(x), math.asin(math.sin(x))), f"asin(sinx) reduce {x:.3f}")
    chk(close(acos_cos(x), math.acos(math.cos(x))), f"acos(cosx) reduce {x:.3f}")
for x in [0, 0.4, -0.4, pi/4, 3*pi/4, 5.0, -5.0, 2.0, -2.2, 10.0, -10.5]:
    chk(close(atan_tan(x), math.atan(math.tan(x))), f"atan(tanx) reduce {x:.3f}")
chk(close(math.asin(math.sin(3)), pi - 3), "asin(sin 3) = pi - 3")
chk(close(math.acos(math.cos(7*pi/4)), pi/4), "acos(cos 7pi/4) = pi/4")
chk(close(math.atan(math.tan(3*pi/4)), -pi/4), "atan(tan 3pi/4) = -pi/4")

# --- trig of inverses (triangle method) ---
for x in [-3.2, -1, -0.5, 0, 0.7, 1, 4.5]:
    chk(close(math.sin(math.atan(x)), x/math.sqrt(1 + x*x)), f"sin(atan x) {x}")
    chk(close(math.cos(math.atan(x)), 1/math.sqrt(1 + x*x)), f"cos(atan x) {x}")
for x in [-1, -0.8, -0.2, 0, 0.4, 0.9, 1]:
    chk(close(math.cos(math.asin(x)), math.sqrt(1 - x*x)), f"cos(asin x) {x}")
    chk(close(math.sin(math.acos(x)), math.sqrt(1 - x*x)), f"sin(acos x) {x}")
    if abs(x) < 1:
        chk(close(math.tan(math.asin(x)), x/math.sqrt(1 - x*x)), f"tan(asin x) {x}")
# worked: sin(cos^{-1} 3/5 + sin^{-1} 5/13) = 63/65
chk(close(math.sin(math.acos(3/5) + math.asin(5/13)), 63/65), "sin(acos 3/5 + asin 5/13) = 63/65")

# --- tan addition table with corrections ---
def atan2_sum(x, y):
    """True principal-sum: atan x + atan y (in (-pi, pi))."""
    return math.atan(x) + math.atan(y)

def atan_add(x, y):
    """Formula with corrections, as on the sheet."""
    base = math.atan((x + y) / (1 - x*y)) if x*y != 1 else None
    if x*y < 1:
        return base
    if x*y > 1 and x > 0:
        return pi + base
    if x*y > 1 and x < 0:
        return -pi + base
    return float("nan")

pts = [(2, 3), (0.5, 1/3), (1/7, 1/8), (-2, -3), (-0.5, -0.4), (5, 0.25), (0.2, -3), (-4, 0.1),
       (10, 0.5), (-10, -0.5), (2, 0.6), (0.9, 0.8), (1.5, 2.0), (-1.5, -2.0), (3, -1), (-3, 1)]
for x, y in pts:
    if x*y == 1:
        continue
    chk(close(atan_add(x, y), atan2_sum(x, y), 1e-9), f"atan add table ({x},{y})")
chk(close(math.atan(2) + math.atan(3), 3*pi/4), "atan2+atan3 = 3pi/4")
chk(close(math.atan(0.5) + math.atan(1/3), pi/4), "atan(1/2)+atan(1/3) = pi/4")
chk(close(math.atan(1/7) + math.atan(1/8), math.atan(3/11)), "atan(1/7)+atan(1/8) = atan(3/11)")

# --- 2 atan x three faces ---
for x in [-5, -2, -1.3, -0.9, -0.5, 0, 0.5, 0.9, 1.3, 2, 5]:
    two = 2*math.atan(x)
    if abs(x) <= 1:
        chk(close(two, math.asin(2*x/(1 + x*x))), f"2atan=asin face {x}")
    elif x > 1:
        chk(close(two, pi - math.asin(2*x/(1 + x*x))), f"2atan=pi-asin face {x}")
    else:
        chk(close(two, -pi - math.asin(2*x/(1 + x*x))), f"2atan=-pi-asin face {x}")
    if x >= 0:
        chk(close(two, math.acos((1 - x*x)/(1 + x*x))), f"2atan=acos face {x}")
    else:
        chk(close(two, -math.acos((1 - x*x)/(1 + x*x))), f"2atan=-acos face {x}")
    if abs(x) < 1:
        chk(close(two, math.atan(2*x/(1 - x*x))), f"2atan=atan face {x}")
chk(close(2*math.atan(2), pi - math.asin(4/5)), "2atan2 = pi - asin(4/5)")
chk(not close(2*math.atan(2), math.asin(4/5)), "2atan2 != asin(4/5) (trap preserved)")

# --- sin asin addition with cases ---
def asin_add(x, y):
    sig = x*math.sqrt(1 - y*y) + y*math.sqrt(1 - x*x)
    base = math.asin(sig)
    if x*y <= 0 or x*x + y*y <= 1:
        return base
    if x > 0 and y > 0:
        return pi - base
    return -pi - base

apts = [(3/5, 8/17), (4/5, 12/13), (3/5, 3/5), (4/5, 4/5), (-4/5, -4/5), (-3/5, 8/17),
        (0.9, 0.3), (-0.9, -0.3), (0.2, 0.2), (-1, 1), (1, -1), (0.6, -0.6), (1, 0), (-1, -1)]
for x, y in apts:
    chk(close(asin_add(x, y), math.asin(x) + math.asin(y)), f"asin add ({x},{y})")
chk(close(math.asin(3/5) + math.asin(8/17), math.asin(77/85)), "asin(3/5)+asin(8/17) = asin(77/85)")
chk(close(math.asin(4/5) + math.asin(12/13), pi - math.asin(56/65)), "asin(4/5)+asin(12/13) = pi - asin(56/65)")
chk(close(math.asin(4/5) + math.asin(12/13), 2.1033004250967474), "asin(4/5)+asin(12/13) numeric 2.10330")
chk(close(math.asin(56/65), pi - 2.1033004250967474), "asin(56/65) = 1.03829")

# --- telescoping series ---
def teles1(n):
    return sum(math.atan(1/(1 + k + k*k)) for k in range(1, n+1))
def teles2(n):
    return sum(math.atan(2/(k*k)) for k in range(1, n+1))
def teles3(n):
    return sum(math.atan(2*k/(k**4 + k*k + 2)) for k in range(1, n+1))
for n in range(1, 12):
    chk(close(teles1(n), math.atan(n+1) - pi/4), f"series1 n={n}")
    chk(close(teles2(n), math.atan(n+1) + math.atan(n) - pi/4), f"series2 n={n}")
    chk(close(teles3(n), math.atan(n*n + n + 1) - pi/4), f"series3 n={n}")
chk(close(teles1(20000), pi/4, 1e-3), "series1 -> pi/4")
chk(close(teles2(20000), 3*pi/4, 1e-3), "series2 -> 3pi/4")

# --- structural identities ---
def cbrt_like_sum(x, y, z):
    return math.atan(x) + math.atan(y) + math.atan(z)
for (x, y, z) in [(math.sqrt(3),)*3, (1, 2, 3), (0.5, 3, 7), (4, 0.5, 4.5), (2, 2, 4/3)]:
    chk(close(x + y + z, x*y*z), f"xyz condition {x:.2f},{y:.2f},{z:.2f}")
    chk(close(cbrt_like_sum(x, y, z), pi), f"atan x+y+z = pi {x:.2f},{y:.2f},{z:.2f}")
for (x, y, z) in [(0.5, 0.5, 0.75), (1/3, 1/2, 1.0), (0.2, 0.3, 1.88)]:
    chk(close(x*y + y*z + z*x, 1), f"xy+yz+zx=1 {x},{y},{z}")
    chk(close(cbrt_like_sum(x, y, z), pi/2), f"sum = pi/2 {x},{y},{z}")
chk(close(math.atan(0.5) + math.atan(0.2) + math.atan(1/8), pi/4), "chain 1/2,1/5,1/8 = pi/4")

# --- extrema claims ---
xs = [i*pi/400 for i in range(-800, 801)]
vals = [math.atan(math.sin(x)) + math.atan(math.cos(x)) for x in xs]
chk(close(max(vals), math.atan(2*math.sqrt(2)), 1e-3), "max of atan(sinx)+atan(cosx) = atan(2sqrt2)")
chk(close(min(vals), -math.atan(2*math.sqrt(2)), 1e-3), "min symmetric")
chk(close(math.atan(math.sin(pi/4)) + math.atan(math.cos(pi/4)), math.atan(2*math.sqrt(2)), 1e-9),
    "max attained at pi/4")

# --- f(x) = asin(sinx) + acos(cosx) piecewise (sheet oly-01) ---
def f_piece(t):
    t = t % (2*pi)
    if t <= pi/2 + 1e-12:
        return 2*t
    if t <= pi + 1e-12:
        return pi
    if t <= 3*pi/2 + 1e-12:
        return 3*pi - 2*t
    return 0.0
for t in [0, 0.4, pi/2, 2.0, pi, 3.5, 3*pi/2, 5.5, 2*pi - 0.1, -0.7, -2.5, -4.5, 7.0, 10.0]:
    chk(close(f_piece(t), math.asin(math.sin(t)) + math.acos(math.cos(t))), f"piecewise f at {t:.2f}")
chk(close(f_piece(2.0), pi), "f plateau pi")

# --- equations ---
# tan^{-1}2x + tan^{-1}3x = pi/4 only at x = 1/6
def eq1(x):
    return math.atan(2*x) + math.atan(3*x)
chk(close(eq1(1/6), pi/4), "eq1 holds at 1/6")
chk(not close(eq1(-1), pi/4), "eq1 rejects ghost -1")
chk(close(math.asin(1/math.sqrt(2)), math.acos(1/math.sqrt(2))), "asin=acos at 1/sqrt2")
xstar = math.sqrt((math.sqrt(5) - 1)/2)
chk(close(math.atan(xstar), math.acos(xstar)), "atan=acos at sqrt((sqrt5-1)/2)")
chk(close(math.sin(math.acos(xstar)), xstar*xstar), "xstar cross-check sin(theta) = x^2 with cos=tan=x")
for x in (0.0, 1.0):
    chk(close(math.asin(x) + math.asin(1 - x), pi/2), f"asin x + asin(1-x) = pi/2 at {x}")
for x in (0.3, 0.7):
    chk(not close(math.asin(x) + math.asin(1 - x), pi/2), f"eq3 rejects x={x}")

# --- monotone inequality claim ---
chk(math.atan(0.5 - 1) < math.atan(0.5), "atan(x-1) < atan x")
# --- sin^{-1} x + cos^{-1} y = pi/2 only when x=y ---
chk(close(math.asin(0.3) + math.acos(0.3), pi/2), "complement same arg")
chk(not close(math.asin(0.3) + math.acos(0.4), pi/2), "complement differs on different args")

print(f"Chapter 4 math_checks: {N[0] - len(FAILS)}/{N[0]} PASS")
if FAILS:
    raise SystemExit(1)
print("ALL PASS")
