import sys

# sys.stdin = open("../../_test/test.in", "r")
# sys.stdout = open("../../_test/test.out", "w")
sys.setrecursionlimit(10**6)

class LCA:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.timer = 0
        self.tin = [-1] * n
        self.euler_tour = [-1] * (2 * n)
        self.segtree = [-1] * (4 * 2 * n)  # Increased size to prevent IndexError

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node=0, parent=-1):
        """Performs DFS to populate tin and euler_tour arrays."""
        self.tin[node] = self.timer
        self.euler_tour[self.timer] = node
        self.timer += 1

        for neighbor in self.graph[node]:
            if neighbor != parent:
                self.dfs(neighbor, node)
                self.euler_tour[self.timer] = node
                self.timer += 1

    def mn_tin(self, x, y):
        """Returns the node with minimum tin value between x and y."""
        if x == -1:
            return y
        if y == -1:
            return x
        return x if self.tin[x] < self.tin[y] else y

    def build(self, node=1, l=0, r=None):
        """Builds the segment tree using the euler_tour array."""
        if r is None:
            r = self.timer - 1

        if l == r:
            self.segtree[node] = self.euler_tour[l]
        else:
            mid = (l + r) // 2
            self.build(node * 2, l, mid)
            self.build(node * 2 + 1, mid + 1, r)
            self.segtree[node] = self.mn_tin(self.segtree[node * 2], self.segtree[node * 2 + 1])

    def query(self, a, b, node=1, l=0, r=None):
        """Queries the segment tree to find the LCA within the range [a, b]."""
        if r is None:
            r = self.timer - 1

        if l > b or r < a:
            return -1
        if l >= a and r <= b:
            return self.segtree[node]

        mid = (l + r) // 2
        left_query = self.query(a, b, node * 2, l, mid)
        right_query = self.query(a, b, node * 2 + 1, mid + 1, r)
        return self.mn_tin(left_query, right_query)

    def lca(self, a, b):
        """Finds the LCA of nodes a and b."""
        if self.tin[a] > self.tin[b]:
            a, b = b, a
        return self.query(self.tin[a], self.tin[b])


# Example usage
if __name__ == "__main__":
    n, q = map(int, input().split())
    lca_finder = LCA(n)

    # Add edges
    edges = list(map(int, input().split()))

    for i in range(n - 1):
        u = edges[i]
        lca_finder.add_edge(u - 1, i + 1)

    # Perform DFS and build the segment tree
    lca_finder.dfs()
    lca_finder.build()

    # Process queries for LCA
    for _ in range(q):
        a, b = map(int, input().split())
        print(lca_finder.lca(a - 1, b - 1) + 1)

