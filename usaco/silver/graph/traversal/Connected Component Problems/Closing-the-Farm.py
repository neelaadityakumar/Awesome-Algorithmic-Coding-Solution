from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

# External input/output setup
external = 1
useLocal = 0
if external == 1:
    if useLocal == 1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open(
            "/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("closing.in", "r")
        sys.stdout = open("closing.out", "w")


n, m = map(int, input().split())
visited, closed, adj, order = [0 for _ in range(n)], [0 for _ in range(n)], [
    [] for _ in range(n)], []
nodes = 0

for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

for _ in range(n):
    order.append(int(input()) - 1)


def dfs(node):
    global nodes
    if visited[node] or closed[node]:
        return

    visited[node] = 1
    nodes += 1
    for i in adj[node]:
        dfs(i)


dfs(0)

if nodes == n:
    print("YES")
else:
    print("NO")

for i in range(n - 1):
    nodes = 0
    visited = [0 for _ in range(n)]
    closed[order[0]] = 1
    order.pop(0)

    dfs(order[0])

    if nodes == n - i - 1:
        print("YES")
    else:
        print("NO")
