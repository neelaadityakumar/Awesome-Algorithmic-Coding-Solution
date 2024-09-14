from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
external = 0
useLocal = 1
if external == 1:
    if useLocal == 1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open(
            "/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("cownomics.in", "r")
        sys.stdout = open("cownomics.out", "w")
MOD = 10**9 + 7

"""
https://codeforces.com/contest/701/problem/C
7
bcAAcbc should output 3
6
aaBCCe should output 5
"""
flat_num = int(input())
flats = input()
types = set(flats)

shortest_interval = float("inf")
closest_left = 0
curr_caught = {}
for right, f in enumerate(flats):
    if f not in curr_caught:
        curr_caught[f] = 0
    curr_caught[f] += 1

    # move the left pointer to the left only if we've caught another one like it
    while closest_left + 1 <= right and curr_caught.get(flats[closest_left], 0) > 1:
        curr_caught[flats[closest_left]] -= 1
        closest_left += 1

    """
	of course, it could be that the config wasn't valid in the first place,
	so we'll have to check for that
	"""
    if len(curr_caught) == len(types):
        shortest_interval = min(shortest_interval, right - closest_left + 1)

print(shortest_interval)
