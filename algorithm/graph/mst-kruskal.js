class UnionFind {
  constructor(size) {
    this.parent = new Array(size).fill(-1);
    this.rank = new Array(size).fill(0);
  }

  find(x) {
    if (this.parent[x] === -1) return x;
    return (this.parent[x] = this.find(this.parent[x]));
  }

  union(x, y) {
    let rootX = this.find(x);
    let rootY = this.find(y);
    if (rootX !== rootY) {
      if (this.rank[rootX] < this.rank[rootY]) {
        this.parent[rootX] = rootY;
      } else if (this.rank[rootX] > this.rank[rootY]) {
        this.parent[rootY] = rootX;
      } else {
        this.parent[rootY] = rootX;
        this.rank[rootX]++;
      }
      return true;
    }
    return false;
  }
}

function kruskal(graph, n) {
  // Sort edges by weight
  const edges = [];
  for (let u = 0; u < n; u++) {
    for (let [v, weight] of graph[u]) {
      edges.push([u, v, weight]);
    }
  }
  edges.sort((a, b) => a[2] - b[2]);

  const mst = [];
  const uf = new UnionFind(n);
  let edgesAdded = 0;

  for (const [u, v, weight] of edges) {
    if (edgesAdded === n - 1) break; // MST is complete
    if (uf.union(u, v)) {
      mst.push([u, v, weight]);
      edgesAdded++;
    }
  }

  return mst;
}

// Example usage:
const graph = [
  [
    [1, 5],
    [2, 2],
  ], // Edges from node 0: (1, 5), (2, 2)
  [
    [0, 5],
    [2, 3],
    [3, 3],
  ], // Edges from node 1: (0, 5), (2, 3), (3, 3)
  [
    [0, 2],
    [1, 3],
    [3, 1],
  ], // Edges from node 2: (0, 2), (1, 3), (3, 1)
  [
    [1, 3],
    [2, 1],
  ], // Edges from node 3: (1, 3), (2, 1)
];
const n = graph.length;
const minimumSpanningTree = kruskal(graph, n);
console.log(minimumSpanningTree);
