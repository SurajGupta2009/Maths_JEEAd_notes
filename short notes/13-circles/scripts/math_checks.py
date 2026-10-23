#!/usr/bin/env python3
"""Exact and numerical checks for Chapter 13 circle geometry."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "_engine"))
from visual_math_checks import checks_for

from fractions import Fraction as F
from math import cos, sin, pi, sqrt, isclose

checks=0
def ck(ok,msg):
    global checks
    checks+=1
    if not ok: raise AssertionError(msg)

def d2(P,Q): return (P[0]-Q[0])**2+(P[1]-Q[1])**2

def val_circle(P, D,E,F0):
    x,y=P
    return x*x+y*y+D*x+E*y+F0

# Standard/general form and real-radius classification.
D,E,F0=F(-2),F(-4),F(-4)
C=(-D/2,-E/2); r2=D*D/4+E*E/4-F0
ck(C==(F(1),F(2)) and r2==9, "complete square centre/radius")
ck(val_circle((F(1),F(5)),D,E,F0)==0, "circle boundary point")
ck(F(1)+F(1)-F(5)<0, "empty-circle discriminant sign")
ck(F(1)+F(1)-F(2)==0, "point-circle discriminant sign")
# Circle through three noncollinear points / diameter equation.
A=(F(1),F(2)); B=(F(5),F(8)); P=(F(1),F(8))
ck((P[0]-A[0])*(P[0]-B[0])+(P[1]-A[1])*(P[1]-B[1])==0, "diameter equation")
mid=((A[0]+B[0])/2,(A[1]+B[1])/2)
ck(d2(P,mid)==d2(A,B)/4, "Thales circle radius")
# Circumcircle through (0,0),(1,0),(0,1): x²+y²-x-y=0.
ck(all(x*x+y*y-x-y==0 for x,y in [(0,0),(1,0),(0,1)]), "three-point circle")
# Trigonometric parametrization and rational parameter.
for t in (0,pi/7,pi/2,pi,5*pi/3):
    x=2+3*cos(t); y=-1+3*sin(t)
    ck(isclose((x-2)**2+(y+1)**2,9,rel_tol=1e-12,abs_tol=1e-12), "angular parameter on circle")
for u in (-5,-1,0,F(2,3),3):
    uf=float(u); x=F(2)+F(3)*(1-uf*uf)/(1+uf*uf); y=F(-1)+F(3)*2*uf/(1+uf*uf)
    ck(isclose(float((x-2)**2+(y+1)**2),9,rel_tol=1e-12,abs_tol=1e-12), "rational parameter on circle")
# Secant example, distance/chord formula and tangent classification.
r=F(5); d2_line=F(25,2)
chord2=4*(r*r-d2_line)
ck(chord2==50, "secant chord length squared")
ck(F(25,2)<r*r and F(25)==r*r and F(30)>r*r, "line-circle position thresholds")
# Point-line distance and chord endpoints are symmetric around projection.
# x+y=5 cuts x²+y²=25 at projection (5/2,5/2), half-chord (5/2,-5/2)/? endpoints (0,5),(5,0).
ck((F(0)**2+F(5)**2)==25 and F(0)+F(5)==5, "first chord endpoint")
ck((F(5)**2+F(0)**2)==25 and F(5)+F(0)==5, "second chord endpoint")
# Tangent equation at a circle point, normal perpendicularity.
T=(F(3),F(4)); X=(F(7),F(1))
ck(d2(T,(0,0))==25 and T[0]*X[0]+T[1]*X[1]==25, "tangent through point")
ck((T[0],T[1])==(3,4) and (T[0]*(X[0]-T[0])+T[1]*(X[1]-T[1]))==0, "tangent normal condition")
# Power/tangent length and chord of contact.
P=(F(5),F(5)); ck(d2(P,(0,0))-9==41, "power equals tangent length squared")
contacts=[(F(9,5),F(12,5)),(F(9,5),F(-12,5))]
ck(all(d2(Q,(0,0))==9 and 5*Q[0]==9 for Q in contacts), "polar contact points")
Pext=(F(5),F(0))
ck(d2(contacts[0],Pext)==16 and d2(contacts[1],Pext)==16, "equal tangent lengths")
# Radical axis example: equal power at points on the line.
def s1(P): x,y=P; return x*x+y*y-9
def s2(P): x,y=P; return x*x+y*y-4*x+6*y-3
for Q in [(F(0),F(-1)),(F(3),F(1)),(F(6),F(3))]:
    ck(2*Q[0]-3*Q[1]-3==0 and s1(Q)==s2(Q), "radical-axis equal power")
# Radical-centre set from the reviewed paper, all three powers agree.
R=(F(1,4),F(3,4))
pow=[R[0]**2+R[1]**2-1,
     R[0]**2+R[1]**2-4*R[0],
     (R[0]-1)**2+(R[1]-1)**2-1]
ck(pow[0]==pow[1]==pow[2], "radical centre equal powers")
# Two equal radius-2 circles, intersection and radical axis.
for ysign in (-1,1):
    Q=(F(3,2), ysign*sqrt(7)/2)
    ck(isclose(float(Q[0]**2+Q[1]**2),4) and isclose(float((Q[0]-3)**2+Q[1]**2),4) and Q[0]==F(3,2), "two circle intersections")
# Circle-position cases, including containment and concentric degeneracy.
ck(5>2+2 and 3<3+2 and 3>abs(3-2), "disjoint / intersecting center criteria")
ck(2==1+1 and 1==abs(2-1), "external/internal tangency equalities")
ck(1<abs(5-1), "strict containment condition")
# Coaxal family x²+y²+lambda(x-y)-2=0 shares (1,1),(-1,-1).
for lam in (-7,-1,0,F(2,3),5):
    for Q in [(F(1),F(1)),(F(-1),F(-1))]:
        ck(Q[0]**2+Q[1]**2+lam*(Q[0]-Q[1])-2==0, "coaxal base points")
# Unit inversion is involutive, and x=a maps to a circle through the origin.
for P in [(F(3),F(4)),(F(1),F(2)),(F(-2),F(5))]:
    norm=d2(P,(0,0)); P1=(P[0]/norm,P[1]/norm); norm1=d2(P1,(0,0))
    P2=(P1[0]/norm1,P1[1]/norm1)
    ck(P2==P, "inversion involution")
# x=2 under unit inversion: X=2(X²+Y²), circle centre (1/4,0), radius 1/4.
for X,Y in [(F(1,2),F(0)),(F(1,4),F(1,4)),(F(0),F(0))]:
    ck(X==2*(X*X+Y*Y), "inverted line/circle equation")
# Simson line exact example: right triangle and opposite circumcircle point.
A=(F(0),F(0)); B=(F(4),F(0)); C=(F(0),F(3)); P=(F(4),F(3))
feet=[(F(64,25),F(27,25)),(F(0),F(3)),(F(4),F(0))]
ck(d2(P,(F(2),F(3,2)))==F(25,4), "Simson point on circumcircle")
ck(all(3*X+4*Y==12 for X,Y in feet), "Simson feet collinear")
Poff=(F(4),F(4)); off_foot=(F(52,25),F(36,25))
ck(off_foot[0]+off_foot[1]!=4, "off-circle feet not collinear")
# Ptolemy for a 3-by-4 rectangle: diagonals 5, sides 3,4,3,4.
ck(F(5)*F(5)==F(3)*F(3)+F(4)*F(4), "Ptolemy rectangle / Pythagoras")
# Source-paper data are impossible: a triangle with sides 3,4,7 is degenerate.
ck(F(3)+F(4)==F(7), "source diagonal equals adjacent side sum")
for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    ck(_condition, f"visual lesson: {_name}")

print(f"Circles: {checks}/{checks} checks PASS")
