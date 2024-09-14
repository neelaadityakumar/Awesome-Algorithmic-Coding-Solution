# https://usaco.org/index.php?page=viewproblem2&cpid=784
import sys
sys.setrecursionlimit(10**9)

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("lifeguards.in", "r")
        sys.stdout = open("lifeguards.out", "w")
MOD = 10**9 + 7

n = int(input())

time = [list(map(int,input().split())) for _ in range(n)]
ans=0
for i in range(n):
    s=set()
    for j in range(n):
        if i==j:
            continue
        for k in range(time[j][0],time[j][1]):
            s.add(k)
    ans=max(ans,len(s))

print(ans)