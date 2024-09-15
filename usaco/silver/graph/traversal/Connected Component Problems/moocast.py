
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
        sys.stdin = open("moocast.in", "r")
        sys.stdout = open("moocast.out", "w")


class Point:
    def __init__(self, x, y, power):
        self.x = x
        self.y = y
        self.power = power

    def squared_distance(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def can_reach(self, other):
        return self.squared_distance(other) <= self.power ** 2


def dfs(node, adj, visited):
    count = 1
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            count += dfs(neighbor, adj, visited)
    return count


n = int(input())
points = []

for _ in range(n):
    x, y, power = map(int, input().split())
    points.append(Point(x, y, power))

adj = defaultdict(list)

for i in range(n):
    for j in range(n):
        if i != j:
            if points[i].can_reach(points[j]):
                adj[i].append(j)

max_reachable = 0

for i in range(n):
    visited = [False] * n
    max_reachable = max(max_reachable, dfs(i, adj, visited))

print(max_reachable)
