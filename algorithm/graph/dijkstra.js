import { MinHeap } from "../heap.js";

function dijkstra(graph, start) {
  const distances = {};
  const heap = new MinHeap();

  for (const node in graph) {
    distances[node] = Infinity;
  }
  distances[start] = 0;

  heap.push([0, start]);

  while (heap.size()) {
    const [dist, node] = heap.pop();
    if (dist > distances[node]) continue;

    for (const [neighbor, weight] of graph[node]) {
      const newDist = dist + weight;
      if (newDist < distances[neighbor]) {
        distances[neighbor] = newDist;
        heap.push([newDist, neighbor]);
      }
    }
  }

  return distances;
}

const graph = {
  A: [
    ["B", 2],
    ["C", 4],
  ],
  B: [
    ["A", 2],
    ["C", 1],
    ["D", 7],
  ],
  C: [
    ["A", 4],
    ["B", 1],
    ["D", 3],
  ],
  D: [
    ["B", 7],
    ["C", 3],
  ],
};

console.log(dijkstra(graph, "A"));
// { A: 0, B: 2, C: 3, D: 6 }
