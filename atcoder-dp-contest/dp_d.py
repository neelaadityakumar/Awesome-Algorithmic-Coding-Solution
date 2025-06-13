N, W = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # arr[i] = [weight, value]

dp = [[0] * (W + 1) for _ in range(N)]  # Only N rows

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
