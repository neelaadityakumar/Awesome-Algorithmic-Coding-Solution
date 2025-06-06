class DisjointSets {
  constructor(size) {
    this.parents = Array.from({ length: size }, (_, i) => i);
    this.sizes = Array(size).fill(1);
  }

  find(x) {
    if (this.parents[x] !== x) {
      this.parents[x] = this.find(this.parents[x]); // Path compression
    }
    return this.parents[x];
  }

  unite(x, y) {
    let xRoot = this.find(x);
    let yRoot = this.find(y);
    if (xRoot === yRoot) return false;

    if (this.sizes[xRoot] < this.sizes[yRoot]) {
      [xRoot, yRoot] = [yRoot, xRoot];
    }

    this.parents[yRoot] = xRoot;
    this.sizes[xRoot] += this.sizes[yRoot];
    return true;
  }

  connected(x, y) {
    return this.find(x) === this.find(y);
  }
}

// Example usage:
function runQueries(size, queries) {
  const dsu = new DisjointSets(size);
  for (const [qType, u, v] of queries) {
    if (qType === 0) {
      dsu.unite(u, v);
    } else {
      console.log(dsu.connected(u, v) ? 1 : 0);
    }
  }
}
const size = 5;
const queries = [
  [0, 1, 2],
  [0, 3, 4],
  [1, 1, 2],
  [1, 2, 3],
  [0, 2, 4],
  [1, 1, 4],
];

runQueries(size, queries);
// Output:
// 1
// 0
// 1
