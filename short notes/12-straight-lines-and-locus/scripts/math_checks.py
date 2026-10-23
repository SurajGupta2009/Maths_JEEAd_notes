#!/usr/bin/env python3
"""Exact/rational checks for Chapter 12 coordinate geometry."""
from fractions import Fraction as F
from math import isclose, sqrt

checks = 0
def ck(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)

def dist2(P, Q):
    return (P[0]-Q[0])**2 + (P[1]-Q[1])**2

def line(L, P):
    a,b,c=L
    return a*P[0]+b*P[1]+c

# Distance, midpoint, internal/external division and translation.
A=(F(-2),F(1)); B=(F(4),F(9))
ck(dist2(A,B)==100, "3-4-5 scaled distance")
M=((A[0]+B[0])/2,(A[1]+B[1])/2)
ck(M==(F(1),F(5)), "midpoint")
A=(F(1),F(2)); B=(F(6),F(7)); m,n=F(2),F(3)
P=((n*A[0]+m*B[0])/(m+n),(n*A[1]+m*B[1])/(m+n))
ck(P==(F(3),F(4)) and dist2(A,P)*n*n==dist2(P,B)*m*m, "internal section orientation")
Pe=((m*B[0]-n*A[0])/(m-n),(m*B[1]-n*A[1])/(m-n))
ck(Pe==(F(-9),F(-8)) and dist2(A,Pe)*n*n==dist2(Pe,B)*m*m, "external section orientation")
# Translation by O'=(1,-2): old point equals new plus shift; equation preserved.
old=(F(1),F(3)); h,k=F(1),F(-2); new=(old[0]-h,old[1]-k)
ck((new[0]+h,new[1]+k)==old, "translation coordinates")
ck(2*old[0]-old[1]+1==0 and 2*new[0]-new[1]+5==0, "translated line")
# Signed area/determinant and collinearity.
def twice_area(A,B,C):
    return A[0]*(B[1]-C[1])+B[0]*(C[1]-A[1])+C[0]*(A[1]-B[1])
ck(twice_area((0,0),(3,0),(0,4))==12, "triangle determinant area")
ck(twice_area((1,1),(2,2),(3,3))==0, "collinearity determinant")
# Point-line distance and foot for several scaled lines.
for L,P in [((1,1,0),(1,2)), ((3,4,-5),(1,2)), ((2,-3,7),(-1,4))]:
    a,b,c=map(F,L); x,y=map(F,P); v=a*x+b*y+c; den=a*a+b*b
    H=(x-v*a/den,y-v*b/den)
    ck(line((a,b,c),H)==0, f"perpendicular foot on line {L}")
    ck((H[0]-x)*b-(H[1]-y)*a==0, f"foot displacement normal {L}")
    ck(dist2((x,y),H)==v*v/den, f"distance squared {L}")
# Scaling a line leaves the distance unchanged.
a,b,c=F(3),F(4),F(-5); x,y=F(1),F(2)
ck((abs(a*x+b*y+c)/sqrt(float(a*a+b*b)))==
   (abs(7*(a*x+b*y+c))/sqrt(float((7*a)**2+(7*b)**2))), "distance scale invariance")
# Parallel/perpendicular coefficient tests and normalized bisectors.
ck(3*4-4*3==0, "parallel determinant")
ck(1*0+0*1==0, "vertical-horizontal perpendicular")
L1=(F(3),F(4),F(-5)); L2=(F(4),F(-3),F(7))
for Q in [(F(-12),F(0)),(F(0),F(-2))]:
    d1=abs(line(L1,Q))/5; d2=abs(line(L2,Q))/5
    ck(d1==d2, "normalized angle-bisector point")
# Pencils and concurrency: all members contain the fixed intersection.
L1=(F(1),F(1),F(-2)); L2=(F(1),F(-1),F(0)); X=(F(1),F(1))
for lam,mu in [(1,0),(0,1),(2,-3),(-5,7)]:
    ck(lam*line(L1,X)+mu*line(L2,X)==0, "line pencil")
# Triangle centres of the 3-4-5 right triangle A=(0,0), B=(4,0), C=(0,3).
A=(F(0),F(0)); B=(F(4),F(0)); C=(F(0),F(3))
G=(F(4,3),F(1)); O=(F(2),F(3,2)); H=(F(0),F(0)); I=(F(1),F(1))
ck(G==((A[0]+B[0]+C[0])/3,(A[1]+B[1]+C[1])/3), "centroid average")
ck(dist2(O,A)==dist2(O,B)==dist2(O,C)==F(25,4), "circumcentre equidistance")
ck((H[0],H[1])==(A[0]+B[0]+C[0]-2*O[0],A[1]+B[1]+C[1]-2*O[1]), "orthocentre vector formula")
# Incentre equal distances from the three side lines (a=5,b=3,c=4).
ck(abs(I[1])==1 and abs(I[0])==1 and abs(3*I[0]+4*I[1]-12)/5==1, "incentre equal side distances")
# Euler line identity and ratio for a non-equilateral sample.
A=(F(0),F(0)); B=(F(4),F(0)); C=(F(1),F(3)); O=(F(2),F(1)); H=(F(1),F(1)); G=(F(5,3),F(1)); N=((O[0]+H[0])/2,(O[1]+H[1])/2)
ck((H[0],H[1])==(A[0]+B[0]+C[0]-2*O[0],A[1]+B[1]+C[1]-2*O[1]), "orthocentre identity sample")
ck((G[0]-O[0],G[1]-O[1])==((H[0]-O[0])/3,(H[1]-O[1])/3), "Euler 1:2 ratio")
ck(dist2(O,G)*36==dist2(G,N)*36*4 and dist2(G,N)*36==dist2(N,H)*36/9, "Euler segment ratio squared")
# Apollonius circle and equal-distance limiting line.
A=(F(0),F(0)); B=(F(4),F(0)); P=(F(16,3),F(8,3))
ck(dist2(P,A)==4*dist2(P,B), "Apollonius ratio 2")
center=(F(16,3),F(0)); radius2=F(64,9)
ck(dist2(P,center)==radius2, "Apollonius circle centre/radius")
Q=(F(2),F(3))
ck(dist2(Q,A)==dist2(Q,B) and Q[0]==2, "ratio one perpendicular bisector")
# Homogeneous pair example and perpendicular criterion.
ck((2*F(1)**2+3*F(1)*F(2)-2*F(2)**2)==0, "pair line y=2x")
ck((2*F(-4)**2+3*F(-4)*F(2)-2*F(2)**2)==0, "pair line x+2y=0")
ck(2+(-2)==0, "perpendicular pair coefficient test")
# Oly nine-point theorem's nine points for the documented triangle.
A=(F(0),F(0)); B=(F(4),F(0)); C=(F(1),F(3)); O=(F(2),F(1)); H=(F(1),F(1)); N=(F(3,2),F(1))
points=[(F(2),F(0)),(F(5,2),F(3,2)),(F(1,2),F(3,2)),
        (F(2),F(2)),(F(2,5),F(6,5)),(F(1),F(0)),
        (F(1,2),F(1,2)),(F(5,2),F(1,2)),(F(1),F(2))]
ck(all(dist2(Q,N)==F(5,4) for Q in points), "nine point circle sample")
print(f"Straight Lines & Locus: {checks}/{checks} checks PASS")
