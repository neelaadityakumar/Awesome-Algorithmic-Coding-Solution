import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
external=0
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
n, s= map(int, input().split())
arr=[int(i) for i in input().split()]
dic=defaultdict(int)
dic[0]=1
ans=0
sums=0
for i in arr:
    sums+=i
    ans+=dic[sums-s]
    dic[sums]+=1
print(ans)