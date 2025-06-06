function bellmanFord(graph, V, E, src) {
  const dis = Array(V).fill(Infinity);
  dis[src] = 0;

  for (let i = 0; i < V - 1; i++) {
    for (let j = 0; j < E; j++) {
      const [u, v, weight] = graph[j];
      if (dis[u] !== Infinity && dis[u] + weight < dis[v]) {
        dis[v] = dis[u] + weight;
      }
    }
  }

  let hasNegativeCycle = false;
  for (let i = 0; i < E; i++) {
    const [u, v, weight] = graph[i];
    if (dis[u] !== Infinity && dis[u] + weight < dis[v]) {
      hasNegativeCycle = true;
      break;
    }
  }

  if (hasNegativeCycle) {
    console.log("Graph contains negative weight cycle");
  } else {
    console.log("Vertex Distance from Source");
    for (let i = 0; i < V; i++) {
      console.log(i + "   " + dis[i]);
    }
  }
}

// Driver code
const V = 5; // Number of vertices in graph
const E = 8; // Number of edges in graph

// Graph represented as an array of edges with format [u, v, weight]
const graph = [
  [0, 1, -1],
  [0, 2, 4],
  [1, 2, 3],
  [1, 3, 2],
  [1, 4, 2],
  [3, 2, 5],
  [3, 1, 1],
  [4, 3, -3],
];

console.log(bellmanFord(graph, V, E, 0));
