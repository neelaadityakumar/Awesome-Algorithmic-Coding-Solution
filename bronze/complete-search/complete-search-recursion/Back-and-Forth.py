import sys
from itertools import product

sys.setrecursionlimit(10**9)

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("backforth.in", "r")
        sys.stdout = open("backforth.out", "w")
MOD = 10**9 + 7

first = [int(i) for i in input().split()]
second = [int(i) for i in input().split()]
ans=set()
def solve(day,carry,first,second):
    global ans
    if day==4:
        ans.add(carry)
        return
    n=len(first if day%2==1 else second)
    n = len(first if day % 2 == 0 else second)  # Corrected day check
    for i in range(n):
        if day % 2 == 0:  # Corrected day check for the first to second transfer
            solve(day + 1, carry - first[i], first[:i] + first[i+1:], second + [first[i]])
        else:  # Corrected day check for the second to first transfer
            solve(day + 1, carry + second[i], first + [second[i]], second[:i] + second[i+1:])



solve(0,1000,first,second)
print(len(ans))