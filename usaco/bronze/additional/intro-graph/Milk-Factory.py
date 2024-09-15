from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
external = 1
useLocal = 0
if external == 1:
    if useLocal == 1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open(
            "/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("factory.in", "r")
        sys.stdout = open("factory.out", "w")

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n-1)]

adj = defaultdict(list)
for u, v in edges:
    adj[v].append(u)


def dfs(v, visited):
    visited[v] = 1
    for u in adj[v]:
        if not visited[u]:
            dfs(u, visited)


ans = -1
for i in range(1, n+1):
    visited = [0]*(n+1)
    dfs(i, visited)
    allVisited = all(v == 1 for v in visited[1:])
    if allVisited:
        ans = i
        break
print(ans)
