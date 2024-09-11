import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict

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