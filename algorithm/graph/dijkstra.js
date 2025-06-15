import { PriorityQueue } from "../heap.cjs";

function dijkstra(graph, start) {
  const distances = {};
  const heap = new PriorityQueue((a, b) => b[0] - a[0]); // compare by distance

  for (const node in graph) {
    distances[node] = Infinity;
  }
  distances[start] = 0;

  heap.add([0, start]);

  while (heap.size()) {
    const [dist, node] = heap.poll();
    if (dist > distances[node]) continue;

    for (const [neighbor, weight] of graph[node]) {
      const newDist = dist + weight;
      if (newDist < distances[neighbor]) {
        distances[neighbor] = newDist;
        heap.add([newDist, neighbor]);
      }
    }
  }

  return distances;
}

const graph = {
  A: [
    ["B", 2],
    ["C", 4],
    ["D", 1],
  ],
  B: [
    ["A", 2],
    ["E", 3],
  ],
  C: [
    ["A", 4],
    ["E", 1],
    ["F", 5],
  ],
  D: [
    ["A", 1],
    ["G", 2],
  ],
  E: [
    ["B", 3],
    ["C", 1],
    ["H", 4],
  ],
  F: [
    ["C", 5],
    ["H", 1],
    ["G", 1],
  ],
  G: [
    ["D", 2],
    ["F", 1],
    ["H", 1],
  ],
  H: [
    ["E", 4],
    ["F", 1],
    ["G", 1],
  ],
};

console.log(dijkstra(graph, "A"));
