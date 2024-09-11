# https://usaco.org/index.php?page=viewproblem2&cpid=736

import sys
sys.setrecursionlimit(10**9)

external=1
useLocal=1
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
spots = [input() for _ in range(n)]
plains = [input() for _ in range(n)]

ans=0
for i in range(m-2):
    for j in range(i+1,m-1):
        for k in range(j+1,m):
            s=set()
            count=1
            for spot in spots:
                s.add(spot[i]+spot[j]+spot[k])
            for plain in plains:
                if plain[i]+plain[j]+plain[k] in s:
                    count=0
                    break
            ans+=count

print(ans)



