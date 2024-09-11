# https://usaco.org/index.php?page=viewproblem2&cpid=1011
import sys
sys.setrecursionlimit(10**9)

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("triangles.in", "r")
        sys.stdout = open("triangles.out", "w")
MOD = 10**9 + 7

n = int(input())

points = [list(map(int,input().split())) for _ in range(n)]
ans=0

def vaild(point1,point2,point3):
    return point1[0] == point2[0] and point2[1] == point3[1]
def area(point1,point2,point3):
    height=((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5
    base=((point2[0]-point3[0])**2+(point2[1]-point3[1])**2)**0.5
    return height*base

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        for k in range(n):
            if i==k or j==k:
                continue
            if vaild(points[i],points[j],points[k]):
                ans=max(ans,area(points[i],points[j],points[k]))

print(int(ans))
