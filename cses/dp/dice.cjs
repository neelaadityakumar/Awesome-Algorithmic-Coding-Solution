const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");

const n = +input[0];
const mod = 1e9 + 7;

const dp = Array(n + 1).fill(0);
dp[0] = 1;

for (let i = 1; i <= n; i++) {
  for (let j = 1; j <= 6 && j <= i; j++) {
    dp[i] = ((dp[i] % mod) + (dp[i - j] % mod)) % mod;
  }
}

console.log(dp[n]);
