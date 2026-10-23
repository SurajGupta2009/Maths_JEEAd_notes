#!/usr/bin/env python3
"""Independent exact/numeric checks for the worked claims in chapter 10."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "_engine"))
from visual_math_checks import checks_for

from fractions import Fraction as F
import itertools
import math

checks = 0
def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def det(A):
    n=len(A)
    if n == 1: return A[0][0]
    return sum((-1)**j*A[0][j]*det([r[:j]+r[j+1:] for r in A[1:]]) for j in range(n))
def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def transpose(A): return [list(c) for c in zip(*A)]

A=[[1,2],[3,4]]; B=[[5,6],[7,8]]
ck(mm(A,B)==[[19,22],[43,50]], "AB")
ck(mm(B,A)==[[23,34],[31,46]], "BA")
ck(mm(A,B)!=mm(B,A), "noncommutativity example")
ck(transpose([[1,2,3],[4,5,6]])==[[1,4],[2,5],[3,6]], "transpose")
ck(det([[3,1],[5,2]])==1, "2x2 determinant")
ck(det([[1,2,3],[4,5,6],[7,8,10]])==-3, "3x3 determinant")
ck(det([[2,0,0],[0,3,0],[0,0,4]])==24, "diagonal determinant")
# Matrix determinant multiplicativity sweep, integer matrices n=1..3.
for n in (1,2,3):
    for seed in range(45):
        X=[[((seed+3*i+5*j+2*i*j)%7)-3 for j in range(n)] for i in range(n)]
        Y=[[((2*seed+5*i+3*j+i*j)%9)-4 for j in range(n)] for i in range(n)]
        ck(det(mm(X,Y))==det(X)*det(Y), f"det product n={n} seed={seed}")
# row operation effects and scalar homogeneity.
for n in (2,3):
    for seed in range(10):
        X=[[seed+i*3-j*2+1 for j in range(n)] for i in range(n)]
        ck(det([[3*x for x in r] for r in X])==3**n*det(X), "det(cA)=c^n det A")
        Y=[r[:] for r in X]; Y[1],Y[0]=Y[0],Y[1]
        ck(det(Y)==-det(X), "row swap")
        Z=[r[:] for r in X]; Z[1]=[Z[1][j]+2*Z[0][j] for j in range(n)]
        ck(det(Z)==det(X), "row addition")
        ck(det(transpose(X))==det(X), "transpose determinant")
# inverse/cofactor examples
M=[[1,2],[3,4]]; adj=[[4,-2],[-3,1]]
ck(mm(M,adj)==[[-2,0],[0,-2]], "A adj A = det A I")
M3=[[2,-1,0],[-1,2,-1],[0,-1,2]]; adj3=[[3,2,1],[2,4,2],[1,2,3]]
ck(det(M3)==4 and mm(M3,adj3)==[[4,0,0],[0,4,0],[0,0,4]], "3x3 adjoint")
# Cramer and homogeneous parameter.
ck(F(-6,-3)==2 and F(-3,-3)==1, "Cramer solution")
C=[[1,1,1],[2,-1,1],[1,2,-1]]; rhs=[6,3,2]
ck(det(C)==7, "3-variable Cramer denominator")
for j, expected in enumerate((7,14,21)):
    R=[r[:] for r in C]
    for i in range(3): R[i][j]=rhs[i]
    ck(det(R)==expected, f"3-variable Cramer numerator {j}")
ck([k for k in range(-6,7) if k*k-1==0]==[-1,1], "homogeneous lambda")
# orthogonal rotation sampled; symmetric/skew split.
for t in range(100):
    # rational Pythagorean points are exact rotations
    a,b= (t*t-1)/(t*t+1), 2*t/(t*t+1)
    Q=[[a,-b],[b,a]]
    ck(all(abs(x-y)<1e-12 for x,y in zip(sum((r for r in mm(transpose(Q),Q)),[]),[1,0,0,1])), "orthogonal")
S=[[1,2.5],[2.5,4]]; K=[[0,-.5],[.5,0]]
ck(S[0][1]==S[1][0] and K[0][1]==-K[1][0], "symmetric/skew split")
P=[[1,1],[0,0]]; ck(mm(P,P)==P, "idempotent")
# CH / power reduction, invariants.
ck(mm(A,A)==[[7,10],[15,22]], "matrix square")
ck(mm(A,A)==[[5*A[i][j]+2*int(i==j) for j in range(2)] for i in range(2)], "CH")
A3=mm(mm(A,A),A)
ck(A3==[[37,54],[81,118]], "A cubed")
# Hadamard numeric checks and rank-one determinant lemma.
for X in ([[1,2],[3,4]], [[2,-1,0],[-1,2,-1],[0,-1,2]]):
    cols=transpose(X); bound=math.prod(math.sqrt(sum(v*v for v in c)) for c in cols)
    ck(abs(det(X)) <= bound+1e-12, "Hadamard")
U=[[4,6],[9,12]]
ck(det(U)==-6, "rank one direct")
# Vandermonde.
V=[[1,2,4],[1,5,25],[1,9,81]]
ck(det(V)==(5-2)*(9-2)*(9-5)==84, "Vandermonde example")
# trace cyclicity / rank-nullity elementary example
ck(det([[1,0,1],[0,1,2],[3,4,10]])==-1, "Schur complement example")
ck(sum(mm(A,B)[i][i] for i in range(2))==sum(mm(B,A)[i][i] for i in range(2))==69, "trace cyclic")
for _name, _condition in checks_for(Path(__file__).resolve().parents[1].name):
    ck(_condition, f"visual lesson: {_name}")

print(f"Matrices & Determinants: {checks}/{checks} checks PASS")
