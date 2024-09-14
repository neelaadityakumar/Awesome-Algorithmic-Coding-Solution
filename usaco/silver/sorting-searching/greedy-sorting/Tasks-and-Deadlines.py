import sys

external = 0
useLocal = 1
if external == 1:
    if useLocal == 1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open(
            "/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("pairup.in", "r")
        sys.stdout = open("pairup.out", "w")
n = int(input())
tasks = sorted([list(map(int, input().split()))
               for _ in range(n)], key=lambda x: x[0])

ans = 0
currentTime = 0
for duration, deadline in tasks:
    currentTime += duration
    ans += deadline-currentTime
print(ans)
