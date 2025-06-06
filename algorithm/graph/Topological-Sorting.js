function courseSchedule(n, m, edges) {
  const graph = Array.from({ length: n }, () => []);
  const inDegree = Array(n).fill(0);

  // Build the graph
  for (const [a, b] of edges) {
    graph[a - 1].push(b - 1);
  }

  // Calculate in-degrees
  for (const nodes of graph) {
    for (const node of nodes) {
      inDegree[node]++;
    }
  }

  // Initialize queue with nodes having in-degree 0
  const queue = [];
  for (let i = 0; i < n; i++) {
    if (inDegree[i] === 0) queue.push(i);
  }

  const topSort = [];

  while (queue.length > 0) {
    const curr = queue.shift();
    topSort.push(curr);

    for (const next of graph[curr]) {
      inDegree[next]--;
      if (inDegree[next] === 0) queue.push(next);
    }
  }

  if (topSort.length === n) {
    console.log(topSort.map((x) => x + 1).join(" "));
  } else {
    console.log("IMPOSSIBLE");
  }
}
const n = 4,
  m = 3;
const edges = [
  [1, 2],
  [2, 3],
  [3, 4],
];

courseSchedule(n, m, edges); // Output: 1 2 3 4
