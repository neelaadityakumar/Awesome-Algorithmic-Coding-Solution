const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");

const n = +input[0];
const MOD = 1e9 + 7;

// build undirected tree
const graph = Array.from({ length: n + 1 }, () => []);
for (let i = 1; i < n; i++) {
  const [u, v] = input[i].split(" ").map(Number);
  graph[u].push(v);
  graph[v].push(u);
}

// dp[u][c]: number of ways to color subtree rooted at u with color c (0 = white, 1 = black)
const dp = Array.from({ length: n + 1 }, () => Array(2).fill(-1));

function dfs(u, c, parent) {
  if (dp[u][c] !== -1) return dp[u][c];

  let res = 1;
  for (const v of graph[u]) {
    if (v === parent) continue;

    if (c === 0) {
      // if current is white, child can be black or white
      const childWays = (dfs(v, 0, u) + dfs(v, 1, u)) % MOD;
      res = (res * childWays) % MOD;
    } else {
      // if current is black, child must be white
      res = (res * dfs(v, 0, u)) % MOD;
    }
  }

  return (dp[u][c] = res);
}

const result = (dfs(1, 0, -1) + dfs(1, 1, -1)) % MOD;
console.log(result);
/// if x ways & y ways then total=x*y ways
