import sys
import statistics

external = 1
useLocal = 0
if external == 1:
    if useLocal == 1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open(
            "/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("stacking.in", "r")
        sys.stdout = open("stacking.out", "w")

# m=

n, k = map(int, input().split())
timeline = [list(map(int, input().split())) for _ in range(k)]
count = [0]*(n+1)
curr = [0]*(n+1)
for start, end in timeline:
    count[start] += 1
    count[end+1] -= 1

for i in range(n):
    curr[i] += curr[i-1]+count[i]
# print(curr)
print(statistics.median(curr[1:]))
