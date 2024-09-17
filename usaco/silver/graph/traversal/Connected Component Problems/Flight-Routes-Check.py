from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**9)

# External input/output setup
external = 0
useLocal = 1
if external == 1:
    if useLocal == 1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open(
            "/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("closing.in", "r")
        sys.stdout = open("closing.out", "w")


def dfs(a, adj1, visited):
    if visited[a]:
        return
    visited[a] = True
    for b in adj1[a]:
        dfs(b, adj1, visited)


def main():
    n, m = map(int, input().split())
    adj1 = [[] for _ in range(n)]
    adj2 = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj1[a].append(b)
        adj2[b].append(a)

    visited = [False] * n

    # Check if you can get from node 0 to all other nodes
    # a->b
    dfs(0, adj1, visited)

    for i in range(n):
        if not visited[i]:
            print("NO")
            print(1, i + 1)
            return

    visited = [False] * n

    # Check if you can get from all other nodes to node 0
    # b->a
    dfs(0, adj2, visited)

    for i in range(n):
        if not visited[i]:
            print("NO")
            print(i + 1, 1)
            return

    print("YES")


if __name__ == "__main__":
    main()
