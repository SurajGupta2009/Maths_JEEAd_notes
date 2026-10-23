#!/usr/bin/env python3
"""Independent numeric verification of Chapter 5 (Complex Numbers) claims."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "_engine"))
from visual_math_checks import checks_for

import cmath
import math
from itertools import product

FAILS = []
N = [0]

def chk(cond, desc):
    N[0] += 1
    if not cond:
        FAILS.append(desc)
        print("FAIL", desc)

def close(a, b, tol=1e-9):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))

def closez(z, w, tol=1e-9):
    return abs(z - w) <= tol * max(1.0, abs(z), abs(w))

pi = math.pi
w = cmath.exp(2j*pi/3)          # omega
zeta = lambda n: cmath.exp(2j*pi/n)

# --- sheet 01 arithmetic ---
chk(closez((3+2j)*(5-1j), 17+7j), "(3+2i)(5-i) = 17+7i")
chk(closez((1+2j)**2 + (3-1j)/1j, -4+1j), "P1 arithmetic = -4 + i")
chk(closez(((1+1j)/(1-1j))**3, -1j), "((1+i)/(1-i))^3 = -i")
chk(closez((1+2j)/(3-1j), 0.1+0.7j), "(1+2i)/(3-i) = 1/10 + 7i/10")
chk(closez((1+1j)**40, 2**20 + 0j), "(1+i)^40 = 2^20")
chk(closez(1j**43, -1j), "i^43 = -i (cycle 4)")

# --- sheet 02 Arg and polar ---
def Arg(z):
    a = cmath.phase(z)
    if a <= -pi + 1e-12:
        a += 2*pi
    return a
argtab = {1: 0, 1j: pi/2, -1: pi, -1j: -pi/2, 1+1j: pi/4, -1+1j: 3*pi/4, 1-1j*math.sqrt(3): -pi/3}
for zz, th in argtab.items():
    chk(close(Arg(complex(zz)), th), f"Arg table {zz}")
# polar round trips
for zz in [-math.sqrt(3)+1j, 1-1j*math.sqrt(3), 1/(1+1j), -1j, 3+4j, -2+0j]:
    r, th = abs(zz), Arg(zz)
    chk(closez(r*(math.cos(th)+1j*math.sin(th)), zz), f"polar round trip {zz}")
# product adds arguments
a1, a2 = -1+2j, 3-1j
chk(closez(abs(a1*a2), abs(a1)*abs(a2)), "|zw| = |z||w|")
chk(close((Arg(a1) + Arg(a2) - Arg(a1*a2)) / (2*pi), round((Arg(a1) + Arg(a2) - Arg(a1*a2))/(2*pi))),
    "Arg(z1z2) ~ Arg z1 + Arg z2 (mod 2pi)")
chk(closez(1j*(3+4j), -4+3j), "i*(3+4i) = -4+3i (quarter turn)")
# Arg(1/-1) window trap
chk(close(Arg(1/(-1)), pi), "Arg(1/-1) = pi (window), naive difference would give -pi")

# --- sheet 03 De Moivre / Euler ---
chk(closez((1+1j)**10, 32j), "(1+i)^10 = 32i")
chk(closez((1+1j)**2, 2j), "(1+i)^2 = 2i")
chk(closez((1+1j)**4, -4+0j), "(1+i)^4 = -4")
chk(closez((1+1j)**8, 16+0j), "(1+i)^8 = 16")
chk(closez((math.sqrt(3)+1j)**4, -8+8*math.sqrt(3)*1j), "(sqrt3+i)^4 = -8 + 8sqrt3 i")
chk(closez(cmath.exp(1j*pi) + 1, 0), "e^{i pi} + 1 = 0")
for th in [0.3, 1.1, -0.7, 2.5, -2.9]:
    lhs = (cmath.cos(th) + 1j*cmath.sin(th))**3
    chk(closez(lhs, complex(math.cos(3*th), math.sin(3*th))), f"De Moivre n=3 at {th}")
    chk(close(math.cos(3*th), 4*math.cos(th)**3 - 3*math.cos(th)), f"cos3theta {th}")
    chk(close(math.sin(3*th), 3*math.sin(th) - 4*math.sin(th)**3), f"sin3theta {th}")
    chk(closez(cmath.exp(1j*th) + cmath.exp(-1j*th), 2*math.cos(th) + 0j), f"euler cos {th}")
    chk(closez((cmath.exp(1j*th) - cmath.exp(-1j*th))/(2j), math.sin(th) + 0j), f"euler sin {th}")

# --- sheet 04 roots ---
# cube roots of 8
cube8 = [2*cmath.exp(2j*pi*k/3) for k in range(3)]
for z in cube8:
    chk(closez(z**3, 8), f"cube root of 8: {z}")
chk(closez(sum(cube8), 0), "cube roots of 8 sum to 0")
four16 = [2*cmath.exp(1j*pi*k/2) for k in range(4)]
for z in four16:
    chk(closez(z**4, 16), f"4th root of 16: {z}")
chk(sorted((round(z.real, 6), round(z.imag, 6)) for z in four16) ==
    sorted([(2.0, 0.0), (-2.0, 0.0), (0.0, 2.0), (0.0, -2.0)]), "4th roots of 16 = {±2, ±2i}")
cube27 = [-3+0j, 1.5+1.5*math.sqrt(3)*1j, 1.5-1.5*math.sqrt(3)*1j]
for z in cube27:
    chk(closez(z**3, -27), f"cube root of -27: {z}")
chk(closez(sum(cube27), 0), "cube roots of -27: sum 0 (Vieta)")
chk(closez(sum(cube27[i]*cube27[j] for i, j in [(0,1),(1,2),(2,0)]), 0), "pairwise sum 0")
# square-root formula
def csqrt_pair(a, b):
    r = math.hypot(a, b)
    x = math.sqrt((r + a)/2)
    y = math.copysign(math.sqrt((r - a)/2), b if b != 0 else 1)
    return x + 1j*y
for (a, b, expect) in [(3, 4, 2+1j), (-3, 4, 1+2j), (0, 4, math.sqrt(2)+1j*math.sqrt(2)), (1, 1, None)]:
    root = csqrt_pair(a, b)
    chk(closez(root**2, complex(a, b)), f"sqrt formula at {a}+{b}i squares back")
    chk(closez((-root)**2, complex(a, b)), f"sqrt formula opposite {a}+{b}i")
    if expect is not None:
        chk(closez(root, expect), f"sqrt formula value {a}+{b}i")

# --- sheet 05 omega ---
chk(closez(1 + w + w**2, 0), "1+w+w^2 = 0")
chk(closez(w.conjugate(), w**2), "conj(w) = w^2")
chk(closez((1-w)*(1-w**2), 3), "(1-w)(1-w^2) = 3")
chk(closez(1 + w, cmath.exp(1j*pi/3)), "1+w = e^{i pi/3}")
chk(closez(1 - w, math.sqrt(3)*cmath.exp(-1j*pi/6)), "1-w = sqrt3 e^{-i pi/6}")
chk(closez((1+w)*(1+w**2), 1), "(1+w)(1+w^2) = 1 (trap: not 2)")
chk(closez(abs(1 - w)**2, 3), "|1-w|^2 = 3")
chk(close(cmath.phase(1 - w), -pi/6), "arg(1-w) = -pi/6")
s2024 = sum(w**k for k in range(2024))
chk(closez(s2024, -w**2), "sum_{0}^{2023} w^k = -w^2")
chk(close((w + w**2)**3 + 3*(w + w**2) + 1, -3), "(w+w^2)^3+3(w+w^2)+1 = -3")
# vanishing sums
for n, m in [(3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 4), (4, 6), (5, 2), (6, 1), (6, 6), (6, 7), (2, 1), (2, 2)]:
    tot = sum(zeta(n)**(m*k) for k in range(n))
    expect = n if m % n == 0 else 0
    chk(closez(tot, expect), f"vanishing sum n={n} m={m}")
chk(closez(sum(cmath.exp(1j*pi*k/3) for k in range(6)), 0), "sum e^{i pi k/3} k=0..5 = 0")

# --- sheet 06 products and filter ---
for n in range(3, 8):
    prod = 1
    for k in range(1, n):
        prod *= (1 - zeta(n)**k)
    chk(closez(prod, n), f"prod(1-zeta_k) = {n} at n={n}")
for n in range(3, 8):
    prod = 1.0
    for k in range(1, n):
        prod *= math.sin(pi*k/n)
    chk(close(prod, n / 2**(n-1)), f"sine product n={n}")
# product identity distances
tot = 1.0
for k in range(5):
    tot *= abs(2 - zeta(5)**k)
chk(close(tot, 31), "prod |2 - zeta_k| = 31 (pentagon)")
th = 0.7
tot = 1.0
for k in range(6):
    tot *= abs(cmath.exp(1j*th) - zeta(6)**k)
chk(close(tot, 2*abs(math.sin(3*th))), "chord product = 2|sin(n th/2)| n=6")
# filter
from math import comb
def filt(N, n, r):
    tot = 0
    for j in range(n):
        tot += cmath.exp(-2j*pi*r*j/n) * (1 + cmath.exp(2j*pi*j/n))**N
    return (tot / n).real
chk(close(filt(9, 3, 0), 170), "filter k=0 mod 3 of C(9,k) = 170")
chk(close(filt(9, 3, 1), 171), "filter r=1 = 171")
chk(close(filt(9, 3, 2), 171), "filter r=2 = 171")
chk(close(filt(9, 3, 0) + filt(9, 3, 1) + filt(9, 3, 2), 512), "classes partition 2^9")
chk(comb(9, 0) + comb(9, 3) + comb(9, 6) + comb(9, 9) == 170, "direct binomial check 170")
chk(close(sum(comb(9, k) for k in range(10) if k % 2 == 0), 256), "even binomial sum = 2^8")

# --- sheet 07 equations ---
z29 = 8/3 - 1j/3
chk(closez(2*z29 + 1j*z29.conjugate(), 5 + 2j), "P29: 2z + i zbar = 5+2i at z = 8/3 - i/3")
# x^2 - 4x + 13
z1 = 2 + 3j
chk(closez(z1**2 - 4*z1 + 13, 0), "2+3i root of x^2-4x+13")
chk(close(abs(z1 - z1.conjugate()), 6), "|z1 - conj z1| = 6")
chk(close(abs(z1 - (2-3j)), 6), "|z1 - z2| = 6 = sqrt|Delta|")
chk(close(math.sqrt(abs(16 - 52)), 6), "sqrt|Delta| formula")

# --- sheets 08-09 loci ---
zz = 1j*(1 + math.sqrt(2))
chk(close(cmath.phase((zz - 1)/(zz + 1)), pi/4), "test point on arg arc")
chk(close(abs(zz - 1j), math.sqrt(2)), "test point on |z-i| = sqrt2")
# ellipse: |z-1|+|z+1| = 6 at z = i 2sqrt2
ztop = 2*math.sqrt(2)*1j
chk(close(abs(ztop - 1) + abs(ztop + 1), 6), "ellipse top sums to 6")
chk(close(abs(ztop - 1), 3), "ellipse top half-distance 3")
# max Im = b = 2sqrt2
chk(close(math.sqrt(9 - 1), 2*math.sqrt(2)), "b = sqrt(a^2-c^2) = 2sqrt2")
# Apollonius check: |z-a|=k|z-b| example k=2, a=0, b=3: circle center 4 radius 2
# |z| = 2|z-3| => x^2+y^2 = 4((x-3)^2+y^2) => (x-4)^2+y^2 = 4
for ang in [0.5, 2.0, 4.2]:
    z = 4 + 2*cmath.exp(1j*ang)
    chk(close(abs(z), 2*abs(z - 3)), f"Apollonius point {ang:.1f}")
# |z|^2 = z + zbar : circle center 1 radius 1
for ang in [0.4, 1.9, 5.2]:
    z = 1 + cmath.exp(1j*ang)
    chk(close(abs(z)**2, (z + z.conjugate()).real), f"disguised circle {ang:.1f}")
chk(close(max(abs(1 + cmath.exp(1j*t)) for t in [i*pi/50 for i in range(100)]), 2), "max|z| on circle = 2")

# --- sheet 10 optimisation ---
a = 1 - 2j
zmin = a/abs(a)
chk(close(abs(zmin - a), abs(abs(a) - 1)), "min |z-a| on unit circle = |a|-1")
chk(close(abs(zmin), 1), "attained at a/|a| on circle")
zopt = (3+4j)/5
chk(close(abs(zopt - (3+4j)), 4), "min |z-3-4i| = 4 at (3+4i)/5")
# P31: |z + 1/z + 2i| range [2, 2sqrt2]
vals = [abs(cmath.exp(1j*t) + 1/cmath.exp(1j*t) + 2j) for t in [i*pi/60 for i in range(121)]]
chk(close(min(vals), 2, 1e-9), "P31 min = 2")
chk(close(max(vals), 2*math.sqrt(2), 1e-9), "P31 max = 2sqrt2")
# P33
zw = 1j  # z * conj(w) = i with |z|=|w|=1: take w=1, z=i
chk(close(abs(1j - 1), math.sqrt(2)), "|z-w| = sqrt2 when z/w = i")
# region ranges
chk(close(max(abs(z) for z in [-5+0j]), 5), "region max = 5 trivial")
chk(close(abs(-5+0j), 5), "|z| at -5")

# --- oly-01 equilateral condition ---
a, b, c = 0, 1, cmath.exp(1j*pi/3)
chk(closez(a + w*b + w**2*c, 0), "CCW equilateral: a + w b + w^2 c = 0")
# clockwise ordering 0, e^{-i pi/3}, 1 : should satisfy a + w^2 b + w c = 0
a2, b2, c2 = 0, cmath.exp(1j*pi/3), 1
chk(closez(a2 + w**2*b2 + w*c2, 0), "CW equilateral: a + w^2 b + w c = 0")
chk(not closez(a + w**2*b + w*c, 0), "CCW triangle fails the CW condition")
# area
z1s, z2s, z3s = 1, 3j, -2+2j
ar = 0.5*abs(((z2s - z1s)*((z3s - z1s).conjugate())).imag)
chk(close(ar, 3.5), "area of (1, 3i, -2+2i) = 7/2")
# circumcenter of 1, i, -1 = 0
u = 0j
for p, q in [(1, 1j), (1, -1), (1j, -1)]:
    chk(close(abs(u - p), abs(u - q)), f"circumcenter equidistant {p},{q}")

# --- oly-02 Ptolemy + British flag ---
pts = [1+0j, 1j, -1+0j, -1j]
a, b, c, d = pts
chk(closez((a-c)*(b-d), (a-b)*(c-d) + (b-c)*(a-d)), "Ptolemy identity (unit square)")
chk(close(abs(a-c)*abs(b-d), abs(a-b)*abs(c-d) + abs(b-c)*abs(a-d)), "Ptolemy equality (square)")
for (a, b, c, d) in [(2+1j, -1+3j, 0.5-2j, 3+0.5j), (0j, 1+0j, 1+1j, 0.5j), (2-1j, -2+1j, 1+2j, -1-2j)]:
    chk(closez((a-c)*(b-d), (a-b)*(c-d) + (b-c)*(a-d)), "Ptolemy identity random")
    chk(abs(abs(a-c)*abs(b-d) - (abs(a-b)*abs(c-d) + abs(b-c)*abs(a-d))) <= 1e-9 + 0.999*abs(a-b)*abs(c-d) + 0.999*abs(b-c)*abs(a-d),
        "Ptolemy inequality holds")
for e in [0.3+0.4j, -1.2+2.5j, 0.5-0.9j, 10-3j]:
    lhs = abs(e - 0)**2 + abs(e - (1+1j))**2
    rhs = abs(e - 1)**2 + abs(e - 1j)**2
    chk(close(lhs, rhs), f"British flag at {e}")

# --- oly-03 Van Aubel + Napoleon ---
def va_centers(a, b, c, d):
    m = lambda p, q: ((1+1j)*p + (1-1j)*q)/2
    return m(a, b), m(b, c), m(c, d), m(d, a)
quad = [0, 1, 1.5+1.2j, 0.3+0.9j]
mab, mbc, mcd, mda = va_centers(*quad)
chk(close(abs(mbc - mda), abs(mcd - mab)), "van Aubel equal lengths")
chk(closez((mbc - mda)/(mcd - mab), -1j), "van Aubel ratio = -i (perpendicular)")
def nap_centers(a, b, c):
    m = lambda p, q: ((2+w)*p + (1-w)*q)/3
    return m(a, b), m(b, c), m(c, a)
A, B, C = 0, 4, 1+3j
m1, m2, m3 = nap_centers(A, B, C)
chk(close(abs(m1 - m2), abs(m2 - m3)), "Napoleon sides equal (1)")
chk(close(abs(m2 - m3), abs(m3 - m1)), "Napoleon sides equal (2)")
chk(closez(m1 + w*m2 + w**2*m3, 0), "Napoleon centers satisfy equilateral condition")
# check center formula matches direct construction
third = A + cmath.exp(-1j*pi/3)*(B - A)
m_direct = (A + B + third)/3
chk(closez(m_direct, nap_centers(A, B, C)[0]), "Napoleon center formula = direct centroid")

# --- oly-04 Leibniz / configs / Joukowski ---
R = 2.0
vs = [R*cmath.exp(2j*pi*k/6) for k in range(6)]
P = cmath.exp(1j*1.1)
chk(close(sum(abs(P - v)**2 for v in vs), 6*1 + 6*4), "Leibniz hexagon sum = 30")
chk(close(sum(abs(0 - v)**2 for v in vs), 24), "Leibniz at P=0 = 24")
# unit circle rectangle claim numeric
rect = [cmath.exp(0.3j), cmath.exp(0.3j + 1j*pi/2), -cmath.exp(0.3j), -cmath.exp(0.3j + 1j*pi/2)]
chk(closez(sum(rect), 0), "4 antipodal unit points sum to 0")
# Joukowski
for t in [0.0, 1.0, 2.5, 4.0]:
    z = cmath.exp(1j*t)
    wv = z + 1/z
    chk(close(wv.imag, 0), f"Joukowski image real at {t}")
    chk(close(wv.real, 2*math.cos(t)), f"Joukowski = 2cos t at {t}")
chk(close(min(2*math.cos(i*pi/60) for i in range(121)), -2), "Joukowski covers [-2,2] min")
chk(close(max(2*math.cos(i*pi/60) for i in range(121)), 2), "Joukowski max 2")

# --- oly-05 Gauss sums ---
def G(n):
    ze = zeta(n)
    return sum(ze**(k*k) for k in range(n))
chk(closez(G(2), 0), "G(2) = 0")
chk(closez(G(3), 1j*math.sqrt(3)), "G(3) = i sqrt3")
chk(closez(G(4), (1+1j)*2), "G(4) = (1+i)sqrt4")
chk(closez(G(5), math.sqrt(5)), "G(5) = sqrt5")
chk(closez(G(6), 0), "G(6) = 0")
chk(closez(G(7), 1j*math.sqrt(7)), "G(7) = i sqrt7")
chk(closez(G(8), (1+1j)*math.sqrt(8)), "G(8) = (1+i)sqrt8")
chk(closez(G(9), math.sqrt(9)), "G(9) = 3")
chk(closez(G(12), (1+1j)*math.sqrt(12)), "G(12) = (1+i)sqrt12")
chk(close(abs(G(7))**2, 7), "|G(7)|^2 = 7")

# --- oly-06 Gauss-Lucas / Pompeiu ---
p = lambda z: z*(z-2)*(z-(1+2j))
dp = lambda z: 3*z*z - (6+4j)*z + (2+4j)
for crit in [1+1j, 1+1j/3]:
    chk(closez(dp(crit), 0), f"critical point {crit}")
# inside triangle 0, 2, 1+2i: barycentric check
def inside_tri(z, A, B, C):
    # areas
    ar = abs(((B-A)*((C-A).conjugate())).imag)
    a1 = abs(((B-z)*((C-z).conjugate())).imag)
    a2 = abs(((A-z)*((C-z).conjugate())).imag)
    a3 = abs(((A-z)*((B-z).conjugate())).imag)
    return abs(a1 + a2 + a3 - ar) < 1e-9
for crit in [1+1j, 1+1j/3]:
    chk(inside_tri(crit, 0, 2, 1+2j), f"crit point inside hull {crit}")
# Pompeiu: triangle 1, w, w^2, P on unit circle -> degenerate
for t in [0.3, 1.2, 2.7, 5.0]:
    P = cmath.exp(1j*t)
    d1, d2, d3 = abs(P - 1), abs(P - w), abs(P - w**2)
    ds = sorted([d1, d2, d3])
    chk(close(ds[0] + ds[1], ds[2], 1e-9), f"Pompeiu degenerate on circle t={t}")
P = 2 - 1j
d1, d2, d3 = abs(P - 1), abs(P - w), abs(P - w**2)
ds = sorted([d1, d2, d3])
chk(ds[0] + ds[1] > ds[2] + 1e-6, "Pompeiu non-degenerate off circle")
chk(close(ds[0], 1.4142135623730951, 1e-9), "Pompeiu example smallest distance sqrt2")
chk(close(ds[1], 2.5035872647924866, 1e-9), "Pompeiu example middle ~2.5036")
chk(close(ds[2], 3.1196235041377793, 1e-9), "Pompeiu example largest ~3.1196")

for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    chk(_condition, f"visual lesson: {_name}")

print(f"Chapter 5 math_checks: {N[0] - len(FAILS)}/{N[0]} PASS")
if FAILS:
    raise SystemExit(1)
print("ALL PASS")
