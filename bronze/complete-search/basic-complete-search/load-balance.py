# https://usaco.org/index.php?page=viewproblem2&cpid=617


import sys
from itertools import product

sys.setrecursionlimit(10**9)

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("balancing.in", "r")
        sys.stdout = open("balancing.out", "w")
MOD = 10**9 + 7

n, b = map(int, input().split())
points = [list(map(int,input().split())) for _ in range(n)]

fencesX=[p[0]+1 for p in points]
fencesY=[p[1]+1 for p in points]

ans=sys.maxsize

for fenceX,fenceY in product(fencesX,fencesY):
    count,topLeft,topRight,bottomLeft,bottomRight=0,0,0,0,0
    for i in range(n):
        if points[i][0]<fenceX and points[i][1]>fenceY:
            topLeft+=1
        elif points[i][0]>fenceX and points[i][1]>fenceY:
            topRight+=1
        elif points[i][0]<fenceX and points[i][1]<fenceY:
            bottomLeft+=1
        elif points[i][0]>fenceX and points[i][1]<fenceY:
            bottomRight+=1


    count=max(count,topLeft,topRight,bottomLeft,bottomRight)

    ans=min(ans,count)

print(ans)