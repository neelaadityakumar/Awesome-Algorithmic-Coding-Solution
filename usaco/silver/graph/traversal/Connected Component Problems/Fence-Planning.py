
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
        sys.stdin = open("fenceplan.in", "r")
        sys.stdout = open("fenceplan.out", "w")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


n, m = map(int, input().split())

points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)


def dfs(node, group) -> None:
    group.append(node)
    for n in adj[node]:
        if not visited[n]:
            visited[n] = True
            dfs(n, group)


visited = [False for _ in range(n)]
rep_cities = []
for i in range(n):
    if visited[i]:
        continue
    group = []
    visited[i] = True

    dfs(i, group)
    rep_cities.append(group)
perimeter = sys.maxsize
for i in range(len(rep_cities)):
    minX, maxX, minY, maxY = 10**9, 0, 10**9, 0
    for j in range(len(rep_cities[i])):
        x, y = points[rep_cities[i][j]].x, points[rep_cities[i][j]].y
        minX = min(minX, x)
        maxX = max(maxX, x)
        minY = min(minY, y)
        maxY = max(maxY, y)

    perimeter = min(perimeter, (maxX - minX) + (maxY - minY))

print(perimeter*2)
