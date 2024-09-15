
import sys
sys.setrecursionlimit(10**9)
external = 1
useLocal = 1
if external == 1:
    if useLocal == 1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open(
            "/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("factory.in", "r")
        sys.stdout = open("factory.out", "w")


n, m = map(int, input().split())

adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)


def dfs(node: int) -> None:
    for n in adj[node]:
        if not visited[n]:
            visited[n] = True
            dfs(n)


visited = [False for _ in range(n)]
rep_cities = []
for i in range(n):
    if visited[i]:
        continue

    visited[i] = True
    rep_cities.append(i)
    dfs(i)

print(len(rep_cities) - 1)
for i in range(len(rep_cities) - 1):
    print(rep_cities[i] + 1, rep_cities[i + 1] + 1)
