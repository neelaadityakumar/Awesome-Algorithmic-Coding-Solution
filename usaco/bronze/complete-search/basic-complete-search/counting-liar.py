# https://usaco.org/index.php?page=viewproblem2&cpid=1228


import sys
sys.setrecursionlimit(10**9)

external=0
useLocal=1
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("diamond.in", "r")
        sys.stdout = open("diamond.out", "w")
MOD = 10**9 + 7

import math

pos = []
for i in range(int(input())):
    lg, val = input().split()
    pos.append([lg, int(val)])

ans = math.inf
for _, val in pos:
    liars = 0
    for lg, v in pos:
        if lg == 'G':
            if v > val: liars += 1
        elif lg == 'L':
            if v < val: liars += 1
    ans = min(ans, liars)
print(ans)