const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const [n, m] = input[0].split(" ").map(Number);
const mod = Math.pow(10, 9) + 7;
let dp = Array.from({ length: n }).map(() => Array(m).fill(0));
let mat = [];
for (let i = 1; i <= n; i++) {
  const cell = input[i].split("");
  mat.push(cell);
}

dp[0][0] = 1;

for (let j = 1; j < m; j++) {
  if (mat[0][j] == ".") {
    dp[0][j] = dp[0][j - 1];
  }
}
for (let i = 1; i < n; i++) {
  if (mat[i][0] == ".") {
    dp[i][0] = dp[i - 1][0];
  }
}
for (let i = 1; i < n; i++) {
  for (let j = 1; j < m; j++) {
    if (mat[i][j] === ".") {
      dp[i][j] += ((dp[i - 1][j] % mod) + (dp[i][j - 1] % mod)) % mod;
      dp[i][j] % mod;
    }
  }
}

console.log(dp[n - 1][m - 1] % mod);
