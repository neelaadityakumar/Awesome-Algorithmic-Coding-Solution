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
        sys.stdin = open("whereami.in", "r")
        sys.stdout = open("whereami.out", "w")


n = int(input())
farm = input()
dic = defaultdict(set)
ans = -1

for length in range(1, n + 1):
    for i in range(n - length + 1):
        dic[length].add(farm[i:i + length])
    if len(dic[length]) == (n - length + 1):
        ans = length
        break

print(ans)
