# https://cses.fi/problemset/task/1623

import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("lineup.in", "r")
        sys.stdout = open("lineup.out", "w")
MOD = 10**9 + 7

COWS = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]

n = int(input())

c= [ input().split() for _ in range(n)]
pairs=[[c[i][0],c[i][-1]] for i in range(n)]
ans=[]
def validOrder(order):
    for x, y in pairs:
        found = False
        for i in range(1, 8):
            if order[i]==x and order[i-1]==y or order[i]==y and order[i-1]==x:
                found = True
        if not found:
            return False
    return True
def solve(order):
    global ans
    if len(order)==8:
        if validOrder(order):
            ans.append(order)
        return
    for i in range(8):
        if COWS[i] in order:
            continue
        solve(order+[COWS[i]])

solve([])
for i in ans[0]:
    print(i)
