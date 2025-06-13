
import sys
sys.setrecursionlimit(10000)
N, W = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # arr[i] = [weight, value]

dp = [[-1] * (W + 1) for _ in range(N)]  # Only N rows

# Initialize first row separately
weight, value = arr[0]
for w in range(W + 1):
    if w >= weight:
        dp[0][w] = value

# Fill dp for the rest
for i in range(1, N):
    weight, value = arr[i]
    for w in range(W + 1):
        dp[i][w] = dp[i - 1][w]  # Not taking the item
        if w >= weight:
            dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)  # Take it

print(dp[N - 1][W])


def knapsack(i, w):
    if i == 0:
        weight, value = arr[0]
        return value if w >= weight else 0
    if dp[i][w] != -1:
        return dp[i][w]

    # Not taking current item
    not_take = knapsack(i - 1, w)
    take = 0
    weight, value = arr[i]
    if w >= weight:
        take = knapsack(i - 1, w - weight) + value

    dp[i][w] = max(take, not_take)
    return dp[i][w]

print(knapsack(N - 1, W))
