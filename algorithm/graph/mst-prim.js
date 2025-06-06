import { PriorityQueue } from "../heap.js";

function primMST(graph) {
  const V = graph.length;
  const parent = new Array(V).fill(-1);
  const key = new Array(V).fill(Infinity);
  const visited = new Array(V).fill(false);
  const pq = new PriorityQueue((a, b) => a[0] - b[0]); // Min-heap

  key[0] = 0;
  pq.add([0, 0]); // [key, vertex]
  while (!pq.isEmpty()) {
    const [_, u] = pq.poll(); // extract node u from [weight, u]
    if (visited[u]) continue;
    visited[u] = true;

    for (const { v, weight } of graph[u]) {
      if (!visited[v] && weight < key[v]) {
        parent[v] = u;
        key[v] = weight;
        pq.add([key[v], v]); // correct order
      }
    }
  }

  console.log("Edges of Minimum Spanning Tree:");
  for (let i = 1; i < V; i++) {
    console.log(`${parent[i]} - ${i}`);
  }
}

// Example graph represented as an adjacency list
const graph = [
  [
    { v: 1, weight: 3 },
    { v: 3, weight: 1 },
  ], // 0
  [
    { v: 0, weight: 3 },
    { v: 2, weight: 1 },
    { v: 3, weight: 3 },
    { v: 4, weight: 6 },
  ], // 1
  [
    { v: 1, weight: 1 },
    { v: 4, weight: 5 },
  ], // 2
  [
    { v: 0, weight: 1 },
    { v: 1, weight: 3 },
    { v: 4, weight: 5 },
    { v: 5, weight: 4 },
  ], // 3
  [
    { v: 1, weight: 6 },
    { v: 2, weight: 5 },
    { v: 3, weight: 5 },
    { v: 5, weight: 2 },
  ], // 4
  [
    { v: 3, weight: 4 },
    { v: 4, weight: 2 },
  ], // 5
];

primMST(graph);
