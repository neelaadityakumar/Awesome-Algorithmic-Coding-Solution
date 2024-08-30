import sys
sys.setrecursionlimit(10**6)

# sys.stdin = open("../_test/test.in", "r")
# sys.stdout = open("../_test/test.out", "w")
input = sys.stdin.read

def setIO(name=""):
    if name:
        sys.stdin = open(f"{name}.in", "r")
        sys.stdout = open(f"{name}.out", "w")

def dfs(v, p, adj, dp):
    for to in adj[v]:
        if to != p:
            dfs(to, v, adj, dp)
            dp[v][0] += max(dp[to][0], dp[to][1])
    for to in adj[v]:
        if to != p:
            dp[v][1] = max(dp[v][1], dp[to][0] + 1 + dp[v][0] -
                             max(dp[to][0], dp[to][1]))

def main():
    data = input().split()
    idx = 0

    n = int(data[idx])
    idx += 1

    adj = [[] for _ in range(n)]
    dp = [[0, 0] for _ in range(n)]

    for _ in range(n - 1):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    dfs(0, -1, adj, dp)
    print(max(dp[0][0], dp[0][1]))

if __name__ == "__main__":
    setIO()
    main()
