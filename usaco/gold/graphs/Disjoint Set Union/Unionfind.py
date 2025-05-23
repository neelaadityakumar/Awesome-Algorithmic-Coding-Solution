class DisjointSets:
    def __init__(self, size: int) -> None:
        self.parents = [i for i in range(size)]
        self.sizes = [1 for _ in range(size)]

    def find(self, x: int) -> int:
        """:return: the "representative" node in x's component"""
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def unite(self, x: int, y: int) -> bool:
        """:return: whether the merge changed connectivity"""
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False

        if self.sizes[x_root] < self.sizes[y_root]:
            x_root, y_root = y_root, x_root

        self.parents[y_root] = x_root
        self.sizes[x_root] += self.sizes[y_root]
        return True

    def connected(self, x: int, y: int) -> bool:
        """:return: whether x and y are in the same connected component"""
        return self.find(x) == self.find(y)


size, query_num = [int(i) for i in input().split()]

dsu = DisjointSets(size)
for _ in range(query_num):
    q_type, u, v = [int(i) for i in input().split()]
    if q_type == 0:
        dsu.unite(u, v)
    else:
        print(1 if dsu.connected(u, v) else 0)
