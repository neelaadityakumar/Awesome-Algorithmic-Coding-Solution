from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("../_test/test.in", "r")
sys.stdout = open("../_test/test.out", "w")
MOD = 10**9 + 7

def dfs(u, p):
    dp[u][0] = 1
    dp[u][1] = 1
    for v in adj[u]:
        if v != p:
            dfs(v, u)
            dp[u][1] *= dp[v][0]
            dp[u][1] %= MOD
            dp[u][0] *= (dp[v][0] + dp[v][1]) % MOD
            dp[u][0] %= MOD



if __name__ == "__main__":
    n = int(input())

    # Process queries for LCA
    adj = [[] for _ in range(n)]
    dp = [[0] * 2 for _ in range(n)]
    # 0 is white
    # 1 is black

    for i in range(n - 1):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        adj[x].append(y)
        adj[y].append(x)

    dfs(0, -1)
    ans = (dp[0][0] + dp[0][1]) % MOD
    print(ans)
