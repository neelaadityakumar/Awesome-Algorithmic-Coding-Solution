
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
        sys.stdin = open("wormsort.in", "r")
        sys.stdout = open("wormsort.out", "w")


def dfs(graph, visited, node, k, group):
    visited[node] = group
    for neighbor, weight in graph[node]:
        if visited[neighbor] != -1:
            continue
        if weight < k:
            continue
        dfs(graph, visited, neighbor, k, group)


def bisearch(graph, cows, k):
    n = len(cows)
    visited = [-1] * n
    for i in range(n):
        if visited[i] != -1:
            continue
        dfs(graph, visited, i, k, i)

    for i in range(n):
        if visited[cows[i] - 1] != visited[i]:
            return False
    return True


def main():
    n, m = map(int, input().split())
    cows = list(map(int, input().split()))

    graph = [[] for _ in range(n)]
    max_weight = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        max_weight = max(max_weight, c)
        graph[a].append((b, c))
        graph[b].append((a, c))

    # Check if cows are already in the correct position
    already_sorted = sum(1 for i in range(n) if cows[i] - 1 == i)
    if already_sorted == n:
        print('-1')
        return

    # Binary search to find the maximum wormhole width
    start, end = 1, max_weight
    ans = start
    while start <= end:
        mid = (start + end) // 2
        if bisearch(graph, cows, mid):
            start = mid + 1  # Increase the lower bound
            ans = mid
        else:
            end = mid - 1    # Decrease the upper bound

    print(str(ans))


if __name__ == "__main__":
    main()
