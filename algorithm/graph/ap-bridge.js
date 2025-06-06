// Class to represent a graph object
class Graph {
  constructor(vertices) {
    this.V = vertices; // Number of vertices
    this.adjList = Array.from({ length: vertices }, () => []); // Adjacency list representation of the graph
    this.id = 0; // Counter for assigning ids during DFS
  }

  // Function to add an edge to the graph
  addEdge(u, v) {
    this.adjList[u].push(v);
    this.adjList[v].push(u);
  }

  // Function to perform DFS and find bridges and articulation points
  dfs(u, parent, disc, low, visited, isArticulation, bridges) {
    // Initialize discovery time and low value for the current node
    disc[u] = low[u] = this.id++;
    visited[u] = true;
    let children = 0; // Count of children in DFS tree

    // Iterate through all adjacent vertices of u
    for (const v of this.adjList[u]) {
      // If v is not visited yet, then make it a child of u in DFS tree and continue DFS for it
      if (!visited[v]) {
        children++;
        this.dfs(v, u, disc, low, visited, isArticulation, bridges);

        // Check if the subtree rooted with v has a connection to one
        //of the ancestors of u
        low[u] = Math.min(low[u], low[v]);

        // Check for bridge
        //if low[v] > disc[u], it indicates that there is no back edge
        //from v to any ancestor of u, making the edge (u, v) a bridge.
        if (low[v] > disc[u]) {
          //Now, there is a back edge from vertex v or one of its descendants
          ////to one of its ancestors if and only if vertex  v has a child   $to
          //for which low[v] < disc[u]. If low[v] = disc[u],
          // the back edge comes directly to v..hence it can be ap but not bridge,
          // otherwise
          // it comes to one of the ancestors of  v.

          bridges.push([u, v]);
        }

        // Check if u is an articulation point
        if (
          (parent === -1 && children > 1) ||
          (parent !== -1 && low[v] >= disc[u])
        ) {
          isArticulation[u] = true;
        }
      }
      // Update low value of u for parent function calls
      else if (v !== parent) {
        low[u] = Math.min(low[u], disc[v]);
      }
    }
  }

  // Function to find bridges and articulation points
  findBridgesAndArticulationPoints() {
    const disc = new Array(this.V).fill(0); // Discovery time of vertices
    const low = new Array(this.V).fill(0); // Earliest visited vertex reachable from subtree rooted with i
    const visited = new Array(this.V).fill(false); // To mark vertices as visited
    const isArticulation = new Array(this.V).fill(false); // To mark vertices as articulation points
    const bridges = []; // List to store bridges

    // Start DFS from all vertices
    for (let i = 0; i < this.V; i++) {
      if (!visited[i]) {
        this.dfs(i, -1, disc, low, visited, isArticulation, bridges);
      }
    }

    // Output the results
    console.log("Bridges:");
    if (bridges.length === 0) {
      console.log("No bridges found.");
    } else {
      for (const bridge of bridges) {
        console.log(bridge);
      }
    }

    console.log("Articulation Points:");
    let articulationCount = 0;
    for (let i = 0; i < this.V; i++) {
      if (isArticulation[i]) {
        console.log(i);
        articulationCount++;
      }
    }
    if (articulationCount === 0) {
      console.log("No articulation points found.");
    }
  }
}

// Test cases
const graph1 = new Graph(5);
graph1.addEdge(1, 0);
graph1.addEdge(0, 2);
graph1.addEdge(2, 1);
graph1.addEdge(0, 3);
graph1.addEdge(3, 4);
console.log("Graph 1:");
graph1.findBridgesAndArticulationPoints();

const graph2 = new Graph(4);
graph2.addEdge(0, 1);
graph2.addEdge(1, 2);
graph2.addEdge(2, 3);
console.log("\nGraph 2:");
graph2.findBridgesAndArticulationPoints();

const graph3 = new Graph(7);
graph3.addEdge(0, 1);
graph3.addEdge(1, 2);
graph3.addEdge(2, 0);
graph3.addEdge(1, 3);
graph3.addEdge(1, 4);
graph3.addEdge(1, 6);
graph3.addEdge(3, 5);
graph3.addEdge(4, 5);
console.log("\nGraph 3:");
graph3.findBridgesAndArticulationPoints();
