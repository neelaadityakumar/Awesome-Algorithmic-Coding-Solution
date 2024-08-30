import sys
import math

sys.setrecursionlimit(200000)

class LCA:
    def __init__(self, n, edges):
        self.n = n
        self.timer = 0
        self.graph = [[] for _ in range(n)]
        self.tin = [-1] * n
        self.euler_tour = []
        self.depth = []
        self.segtree = [0] * (4 * 2 * n)

        # Build the graph
        for u, v in edges:
            self.graph[v].append(u)

        # DFS to fill tin, euler_tour, and depth
        self.dfs(0, -1, 0)

        # Build the segment tree
        self.build(1, 0, len(self.euler_tour) - 1)

    def dfs(self, node, parent, d):
        self.tin[node] = self.timer
        self.euler_tour.append(node)
        self.depth.append(d)
        self.timer += 1
        for neighbor in self.graph[node]:
            if neighbor != parent:
                self.dfs(neighbor, node, d + 1)
                self.euler_tour.append(node)
                self.depth.append(d)

    def mn_depth(self, x, y):
        if x == -1:
            return y
        if y == -1:
            return x
        return x if self.depth[x] < self.depth[y] else y

    def build(self, node, l, r):
        if l == r:
            self.segtree[node] = self.euler_tour[l]
        else:
            mid = (l + r) // 2
            self.build(node * 2, l, mid)
            self.build(node * 2 + 1, mid + 1, r)
            self.segtree[node] = self.mn_depth(self.segtree[node * 2], self.segtree[node * 2 + 1])

    def query(self, a, b, node, l, r):
        if l > b or r < a:
            return -1
        if l >= a and r <= b:
            return self.segtree[node]
        mid = (l + r) // 2
        return self.mn_depth(
            self.query(a, b, node * 2, l, mid),
            self.query(a, b, node * 2 + 1, mid + 1, r)
        )

    def lca(self, a, b):
        if self.tin[a] > self.tin[b]:
            a, b = b, a
        return self.query(self.tin[a], self.tin[b], 1, 0, len(self.euler_tour) - 1)

# Example usage
# Example usage
n = 5  # Number of nodes

edges = [
    (1, 0),
    (2, 0),
    (3, 2),
    (3, 4)
]  # List of edges
lca_solver = LCA(n, edges)

queries = [
    (3, 2),
    (3, 4),
    (0, 2) ,(1, 0),
    (2, 0),
    (3, 2),
    (4, 3)
]  # Example queries

for a, b in queries:
    print(lca_solver.lca(a , b ))  # Convert to 0-based index

