function floydWarshall(graph) {
  const dist = [];
  const numVertices = graph.length;

  // Initialize distance matrix with initial values
  for (let i = 0; i < numVertices; i++) {
    dist[i] = [];
    for (let j = 0; j < numVertices; j++) {
      if (i === j) {
        dist[i][j] = 0;
      } else if (graph[i][j] === 0) {
        dist[i][j] = Infinity;
      } else {
        dist[i][j] = graph[i][j];
      }
    }
  }

  // Compute shortest paths
  for (let k = 0; k < numVertices; k++) {
    for (let i = 0; i < numVertices; i++) {
      for (let j = 0; j < numVertices; j++) {
        if (
          dist[i][k] !== Infinity &&
          dist[k][j] !== Infinity &&
          dist[i][j] > dist[i][k] + dist[k][j]
        ) {
          dist[i][j] = dist[i][k] + dist[k][j];
        }
      }
    }
  }

  return dist;
}
const graph1 = [
  [0, 5, 0, 10],
  [0, 0, 3, 0],
  [0, 0, 0, 1],
  [0, 0, 0, 0],
];

// Expected Output:
// Vertex Distance from Source
// 0   0
// 1   5
// 2   8
// 3   9
const graph2 = [
  [0, 3, 0, 0],
  [0, 0, 1, 0],
  [0, 0, 0, 2],
  [4, 0, 0, 0],
];

// Expected Output:
// Vertex Distance from Source
// 0   0
// 1   3
// 2   4
// 3   6

console.log(floydWarshall(graph1));
console.log(floydWarshall(graph2));
