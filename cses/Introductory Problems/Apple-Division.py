# https://cses.fi/problemset/task/1623

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

n = int(input())

weight = [int(i) for i in input().split()]
ans=sys.maxsize
def solve(index=0,l=0,r=0):
    if index==n:
        return abs(l-r)
    lsum=solve(index+1,l+weight[index],r)
    rsum=solve(index+1,l,r+weight[index])
    return min(lsum,rsum)

print(solve())