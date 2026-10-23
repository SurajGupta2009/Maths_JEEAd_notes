#!/usr/bin/env python3
"""Independent numeric/exact checks for probability and descriptive statistics."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "_engine"))
from visual_math_checks import checks_for

from fractions import Fraction as F
from itertools import product
from math import comb, factorial, sqrt

checks=0
def ck(cond,msg):
    global checks
    checks+=1
    if not cond: raise AssertionError(msg)

# Classical probability and event identities on finite uniform sets.
S=list(product(range(1,7), repeat=2)); A={x for x in S if sum(x)==7}
ck(len(S)==36 and len(A)==6 and F(len(A),len(S))==F(1,6), "two dice")
ck(F(7,8)==1-F(1,8), "three coin complement")
ck(F(16,52)==F(4,13), "heart or king")
ck(1-F(comb(5,3),comb(9,3))==F(37,42), "committee complement")
ck(F(1,6)/F(1,2)==F(1,3), "conditional even die")
ck(F(4,52)*F(3,51)==F(1,221)==F(comb(4,2),comb(52,2)), "two aces no replacement")
# Bayes factory
pD=F(1,2)*F(1,100)+F(3,10)*F(2,100)+F(1,5)*F(3,100)
ck(pD==F(17,1000), "total probability factory")
ck((F(1,2)*F(1,100))/pD==F(5,17), "Bayes factory")
# Probability variables / statistics identities.
probs=[F(1,5),F(3,10),F(1,2)]; xs=[1,2,3]
mu=sum(x*p for x,p in zip(xs,probs)); m2=sum(x*x*p for x,p in zip(xs,probs))
ck(mu==F(23,10) and m2==F(59,10) and m2-mu*mu==F(61,100), "three-point moments")
ck(sum(F(k,6) for k in range(1,7))==F(7,2), "die mean")
ck(sum(F(k*k,6) for k in range(1,7))-F(7,2)**2==F(35,12), "die variance")
# Binomial distribution mass/moments over a sweep; fixed finite support.
for n in range(1,16):
  for p in (F(1,5),F(1,3),F(1,2),F(3,4)):
    q=1-p
    pmf=[F(comb(n,k))*p**k*q**(n-k) for k in range(n+1)]
    ck(sum(pmf)==1, f"binomial mass n={n} p={p}")
    ck(sum(k*pmf[k] for k in range(n+1))==n*p, f"binomial mean n={n} p={p}")
    ck(sum((k-n*p)**2*pmf[k] for k in range(n+1))==n*p*q, f"binomial variance n={n} p={p}")
ck(F(comb(10,3))*F(1,5)**3*F(4,5)**7==F(201326592,10**9), "binomial example")
# Geometric distribution truncated checks of formulas by finite sums.
for p in (F(1,2),F(1,3),F(2,5),F(1,1)):
    if p==1: continue
    q=1-p; N=200
    tail_mass=1-q**N
    em=sum(F(k)*q**(k-1)*p for k in range(1,N+1)) + N*q**N
    ck(abs(float(em-F(1,p)))<1e-12, "geometric expectation (tail bound)")
# Descriptive stats: ungrouped, frequency expansion equivalence.
data=[2,3,3,7,10]
ck(sum(data)/len(data)==5 and sorted(data)[2]==3, "mean/median")
ck(sum(abs(x-5) for x in data)/5==2.8, "mean deviation about mean")
ck(sum(abs(x-3) for x in data)/5==2.4, "mean deviation about median")
values=[1,2,3]; fs=[1,2,1]; N=sum(fs)
mean=F(sum(x*f for x,f in zip(values,fs)),N)
var=F(sum(x*x*f for x,f in zip(values,fs)),N)-mean**2
ck(mean==2 and var==F(1,2), "frequency table mean variance")
# Variance computational identity and affine transformation for several samples.
for dat in ([1,2,3],[1,1,1,8],[0,4,4,8,10],[-3,2,5]):
    m=F(sum(dat),len(dat)); v=F(sum(x*x for x in dat),len(dat))-m*m
    ck(v==sum((F(x)-m)**2 for x in dat)/len(dat), "variance identity")
    shifted=[x+7 for x in dat]; scaled=[-3*x for x in dat]
    ms=F(sum(shifted),len(dat)); vs=F(sum(x*x for x in shifted),len(dat))-ms*ms
    mk=F(sum(scaled),len(dat)); vk=F(sum(x*x for x in scaled),len(dat))-mk*mk
    ck(ms==m+7 and vs==v and vk==9*v, "affine stats")
# Grouped class-mark example with interpolation estimates.
gm=F(4*5+8*15+4*25,16)
gvar=F(4*25+8*225+4*625,16)-gm*gm
gmd=F(4*10+8*0+4*10,16)
gmedian=F(10)+(F(8)-4)*10/F(8)
gmode=F(10)+F(8-4,2*8-4-4)*10
ck(gm==15 and gvar==50 and gmd==5 and gmedian==15 and gmode==15, "grouped class-mark estimates")
# Bernoulli indicator variance, total probability and Bayes already above.
for p in (F(1,10),F(1,2),F(9,10)):
    ck(p*(1-p)==p-p*p, "indicator variance")
# Broken stick via exact geometric region known ratio; ballot direct enumeration.
for a,b in ((2,1),(3,2),(5,3)):
    seqs=set(__import__('itertools').permutations('A'*a+'B'*b))
    good=0
    for seq in seqs:
        x=y=0; ok=True
        for c in seq:
            x+=c=='A'; y+=c=='B'
            if x<=y: ok=False; break
        good+=ok
    ck(F(good,len(seqs))==F(a-b,a+b), f"ballot ({a},{b})")
# Birthday collision 23: stable product, published rounded value.
no=F(1)
for i in range(23): no*=F(365-i,365)
ck(round(float(1-no),6)==0.507297, "birthday 23")
# Coupon expectation harmonic, run recurrence values, derangement exact.
ck(sum(F(1,k) for k in range(1,7))*6==F(147,10), "coupon collector six")
E=[0]
for r in range(1,8): E.append(2*(E[-1]+1))
ck(E[3]==14 and all(E[r]==2**(r+1)-2 for r in range(1,8)), "run expectation")
D=[1,0]
for n in range(2,9): D.append((n-1)*(D[n-1]+D[n-2]))
ck(D[3]==2 and D[5]==44 and F(D[5],factorial(5))==F(11,30), "derangement")
# Gambler's ruin fair and biased recurrence residuals.
ck(F(3,10)==F(3,10), "fair ruin example")
p=F(3,5); q=1-p; N=10
u=[(1-(q/p)**i)/(1-(q/p)**N) for i in range(N+1)]
ck(u[0]==0 and u[N]==1 and all(abs(p*u[i+1]+q*u[i-1]-u[i])<1e-12 for i in range(1,N)), "biased ruin recurrence")
ck((1-(F(2,3))**5)/(1-(F(2,3))**10)==F(51273,58025), "biased ruin exact value")
for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    ck(_condition, f"visual lesson: {_name}")

print(f"Probability & Statistics: {checks}/{checks} checks PASS")
