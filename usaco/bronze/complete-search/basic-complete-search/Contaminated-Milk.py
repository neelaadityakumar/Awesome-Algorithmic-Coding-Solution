# https://usaco.org/index.php?page=viewproblem2&cpid=569
import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("badmilk.in", "r")
        sys.stdout = open("badmilk.out", "w")
MOD = 10**9 + 7

# Read the values of n and m
n, m,d,s = map(int, input().split())
drinks=[ list(map(int, input().split())) for _ in range(d)]
sick=[ list(map(int, input().split())) for _ in range(s)]
sickSet=set([x[0] for x in sick])
ans=0
dic=defaultdict(set)
for sp,st in sick:
    for dp,dtype,dtime in drinks:
        if sp==dp and dtime<st:
            dic[dtype].add(dp)
for drink in dic:
    for sp in sickSet:
        if sp not in dic[drink]:
            break
    else:
        res=set()
        for dp,dm,dt in drinks:
            if drink==dm:
                res.add(dp)
        ans=max(ans,len(res))

print(ans)
