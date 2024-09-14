# https://cses.fi/problemset/task/1623

import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

external=0
useLocal=1
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("lineup.in", "r")
        sys.stdout = open("lineup.out", "w")
MOD = 10**9 + 7

n = int(input()) * 2
people = sorted(int(i) for i in input().split())
assert len(people) == n

min_instability = float("inf")
for i in range(n):
	for j in range(i + 1, n):
		new_people = [people[p] for p in range(n) if p != i and p != j]
		total_instability = 0
		for p in range(0, n - 2, 2):
			total_instability += new_people[p + 1] - new_people[p]
		min_instability = min(min_instability, total_instability)

print(min_instability)