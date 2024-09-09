
# https://cses.fi/problemset/task/1621

import sys
sys.setrecursionlimit(10**9)

external=0
useLocal=1
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("lifeguards.in", "r")
        sys.stdout = open("lifeguards.out", "w")
MOD = 10**9 + 7


n=int(input())
arr=sorted([int(i) for i in input().split()])

ans=min(1,n)

for i in range(1,n):
    if arr[i]!=arr[i-1]:
        ans+=1

print(ans)