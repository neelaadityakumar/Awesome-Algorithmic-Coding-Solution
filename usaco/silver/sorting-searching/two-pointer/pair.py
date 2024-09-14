import sys

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("pairup.in", "r")
        sys.stdout = open("pairup.out", "w")
N = int(input())
cows = [[int(i) for i in input().split()] for _ in range(N)]
cows.sort(key=lambda g: g[1])
i, j = 0, N - 1
ans = 0
while i <= j:
    ans = max(cows[i][1] + cows[j][1], ans)
    cows_paired = min(cows[i][0], cows[j][0])
    cows[i][0] -= cows_paired
    cows[j][0] -= cows_paired
    if cows[i][0] <= 0:
        i+=1
    if cows[j][0] <= 0:
        j-=1

print(ans)
