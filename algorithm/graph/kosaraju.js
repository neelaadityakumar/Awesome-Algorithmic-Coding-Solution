class Graph {
  constructor(vertices) {
    this.V = vertices;
    this.graph = Array.from({ length: vertices }, () => []);
  }

  addEdge(u, v) {
    this.graph[u].push(v);
  }

  _dfs(v, visited, stack) {
    visited[v] = true;
    for (const neighbor of this.graph[v]) {
      if (!visited[neighbor]) {
        this._dfs(neighbor, visited, stack);
      }
    }
    stack.push(v);
  }

  _transpose() {
    const transposed = new Graph(this.V);
    for (let u = 0; u < this.V; u++) {
      for (const v of this.graph[u]) {
        transposed.addEdge(v, u);
      }
    }
    return transposed;
  }

  _fillOrder(visited, stack) {
    for (let i = 0; i < this.V; i++) {
      if (!visited[i]) {
        this._dfs(i, visited, stack);
      }
    }
  }

  _dfsUtil(v, visited, component) {
    visited[v] = true;
    component.push(v);
    for (const neighbor of this.graph[v]) {
      if (!visited[neighbor]) {
        this._dfsUtil(neighbor, visited, component);
      }
    }
  }

  kosarajuSCC() {
    const stack = [];
    const visited = Array(this.V).fill(false);

    this._fillOrder(visited, stack);

    const transposed = this._transpose();
    const visitedT = Array(this.V).fill(false);
    const sccList = [];

    while (stack.length > 0) {
      const node = stack.pop();
      if (!visitedT[node]) {
        const component = [];
        transposed._dfsUtil(node, visitedT, component);
        sccList.push(component);
      }
    }

    return sccList;
  }
}

// Example usage
const g = new Graph(5);
g.addEdge(1, 0);
g.addEdge(0, 2);
g.addEdge(2, 1);
g.addEdge(0, 3);
g.addEdge(3, 4);

const sccs = g.kosarajuSCC();
console.log("Strongly Connected Components:", sccs);
