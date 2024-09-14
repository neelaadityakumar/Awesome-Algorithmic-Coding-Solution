# https://usaco.org/index.php?page=viewproblem2&cpid=736

import sys
sys.setrecursionlimit(10**9)

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("cownomics.in", "r")
        sys.stdout = open("cownomics.out", "w")
MOD = 10**9 + 7

# Read the values of n and m
n, m = map(int, input().split())

# Read m lines of genomic data
spot = [input() for _ in range(n)]
plain = [input() for _ in range(n)]

ans=0
for i in range(m):
    s=set()
    for j in range(n):
        s.add(spot[j][i])
    p=set()
    for j in range(n):
        p.add(plain[j][i])
    if not s.intersection(p):
        ans+=1



print(ans)
