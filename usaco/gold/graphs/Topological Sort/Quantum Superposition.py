from collections import deque
MAX_N = 1000
MAX_Q = 2000


n = [0, 0]
m = [0, 0]
g = [[[] for _ in range(MAX_N + 1)] for _ in range(2)]
back = [[[] for _ in range(MAX_N + 1)] for _ in range(2)]
dp = [[[False for _ in range(MAX_Q + 1)]
       for _ in range(MAX_N + 1)] for _ in range(2)]


def gen(x):
    """Generates the topological sort, filling in the DP array in the process."""
    in_degree = [0] * (MAX_N + 1)
    for _ in range(m[x]):
        a, b = map(int, input().split())
        g[x][a].append(b)
        back[x][b].append(a)
        in_degree[b] += 1

    # Run topological sort.
    q = deque()
    for i in range(n[x] + 1):
        if in_degree[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        for nxt in g[x][node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)

        # `node` can be visited in `i + 1` steps if `before` can in `i` steps.
        if not back[x][node]:
            dp[x][node][0] = True
        for before in back[x][node]:
            for i in range(MAX_Q + 1):
                if dp[x][before][i]:
                    dp[x][node][i + 1] = True


n[0], n[1], m[0], m[1] = map(int, input().split())

gen(0)
gen(1)

# Preprocess for all queries: ans[x] is true if the sum of steps
# in both universes can be equal to x.
ans = [False for _ in range(MAX_Q + 1)]
for i in range(MAX_N + 1):
    if dp[0][n[0]][i]:
        for j in range(MAX_N + 1):
            if dp[1][n[1]][j]:
                ans[i + j] = True

for _ in range(int(input())):
    a = int(input())
    print("Yes" if ans[a] else "No")
