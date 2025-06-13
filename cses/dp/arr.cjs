const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const mod = 1e9 + 7;
const [n, m] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);

// dp[i][j] = ways to build array up to i-th index with value j at i
const dp = Array.from({ length: n }, () => Array(m + 2).fill(0));

if (arr[0] === 0) {
  for (let j = 1; j <= m; j++) dp[0][j] = 1;
} else {
  dp[0][arr[0]] = 1;
}

for (let i = 1; i < n; i++) {
  for (let j = 1; j <= m; j++) {
    if (arr[i] == 0 || arr[i] == j) {
      dp[i][j] =
        ((dp[i - 1][j - 1] || 0) +
          (dp[i - 1][j] || 0) +
          (dp[i - 1][j + 1] || 0)) %
        mod;
    }
  }
}

// Final answer = sum of dp[n-1][j] for valid j
let result = 0;
if (arr[n - 1] == 0) {
  for (let j = 1; j <= m; j++) {
    result = (result + dp[n - 1][j]) % mod;
  }
} else {
  result = dp[n - 1][arr[n - 1]] % mod;
}
console.log(result);
