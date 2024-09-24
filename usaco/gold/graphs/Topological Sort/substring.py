from collections import deque
# import sys
# sys.setrecursionlimit(10**9)
# external = 1
# useLocal = 1
# if external == 1:
#     if useLocal == 1:
#         sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
#         sys.stdout = open(
#             "/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
#     else:
#         sys.stdin = open("ccski.in", "r")
#         sys.stdout = open("ccski.out", "w")

n, m = map(int, input().split())
a = input()

adj = [[] for _ in range(n)]
in_degree = [0] * n
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    in_degree[y] += 1
    adj[x].append(y)

queue = deque()
# dp[i][j] is the frequency of letter j when we are at node i.
dp = [[0] * 26 for _ in range(n)]

for i in range(n):
    if in_degree[i] == 0:
        queue.append(i)
        dp[i][ord(a[i]) - ord("a")] += 1

# Run topological sort.
size = 0
ans = 0
while len(queue) > 0:
    cur = queue.popleft()
    for nxt in adj[cur]:
        for j in range(26):
            # Update the frequency with the next occurrence.
            if j == ord(a[nxt]) - ord("a"):
                dp[nxt][j] = max(dp[cur][j] + 1, dp[nxt][j])
            else:
                dp[nxt][j] = max(dp[cur][j], dp[nxt][j])
            ans = max(ans, dp[nxt][j])
        # Add the next node to the queue.
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            queue.append(nxt)
    size += 1

# No answer.
if size < n:
    print(-1)
else:
    print(ans)
