# https://usaco.org/index.php?page=viewproblem2&cpid=712
import sys
sys.setrecursionlimit(10**9)

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("circlecross.in", "r")
        sys.stdout = open("circlecross.out", "w")
MOD = 10**9 + 7

s = input()
ans=0

for A in range(ord("A"), ord("Z") + 1):
    for B in range(ord("A"), ord("Z") + 1):
        if A == B:
            continue
        A_First = s.find(chr(A))
        A_Last = s.rfind(chr(A))

        B_First = s.find(chr(B))
        B_Last = s.rfind(chr(B))

        if A_First>=-1 and B_First>=-1 and A_First < B_First and B_First < A_Last and A_Last<B_Last :
            ans+=1

print(ans)