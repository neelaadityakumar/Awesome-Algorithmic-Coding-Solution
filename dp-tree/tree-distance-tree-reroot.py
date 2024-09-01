# https://cses.fi/problemset/task/1132/

from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

# sys.stdin = open("../_test/test.in", "r")
# sys.stdout = open("../_test/test.out", "w")


sys.setrecursionlimit(10**9)

# Graph as adjacency list
graph = defaultdict(list)
fir = [0] * 200001
sec = [0] * 200001
ans = [0] * 200001

def dfs1(node=1, parent=0):
    for i in graph[node]:
        if i != parent:
            dfs1(i, node)
            if fir[i] + 1 > fir[node]:
                sec[node] = fir[node]
                fir[node] = fir[i] + 1
            elif fir[i] + 1 > sec[node]:
                sec[node] = fir[i] + 1

def dfs2(node=1, parent=0, to_p=0):
    ans[node] = max(to_p, fir[node])
    for i in graph[node]:
        if i != parent:
            if fir[i] + 1 == fir[node]:
                dfs2(i, node, max(to_p, sec[node]) + 1)
            else:
                dfs2(i, node, ans[node] + 1)

def main():
    n = int(input())
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # Running the first DFS to calculate fir and sec values
    dfs1()

    # Running the second DFS to calculate ans values
    dfs2()

    # Print the answer for each node
    print(' '.join(map(str, ans[1:n + 1])))

if __name__ == "__main__":
    main()
