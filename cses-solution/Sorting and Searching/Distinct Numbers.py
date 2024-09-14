# https://cses.fi/problemset/task/1621
n = int(input())
arr = sorted([int(i) for i in input().split()])

ans = min(1, n)

for i in range(1, n):
    if arr[i] != arr[i-1]:
        ans += 1
