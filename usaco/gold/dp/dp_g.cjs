const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const [n, m] = input[0].split(" ").map(Number);
let graph = {};
let dp = Array.from({ length: n + 1 }).fill(-1);
for (let i = 1; i <= m; i++) {
  const [u, v] = input[i].split(" ").map(Number);
  graph[u] = graph[u] || [];
  graph[u].push(v);
}

function dfs(u) {
  if (dp[u] != -1) return dp[u];
  let mx = 0;
  for (const v of graph[u] || []) {
    mx = Math.max(mx, 1 + dfs(v));
  }
  dp[u] = mx;
  return mx;
}
let max = 0;
for (let u = 1; u <= n; u++) {
  max = Math.max(max, dfs(u));
}
console.log(max);
