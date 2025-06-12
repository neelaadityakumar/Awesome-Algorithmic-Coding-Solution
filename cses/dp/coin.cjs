const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [n, x] = input[0].split(" ").map(Number);
const coins = input[1].split(" ").map(Number);
const INF = 1e9;
const dp = Array(x + 1).fill(INF);
dp[0] = 0;

for (let coin of coins) {
  for (let i = coin; i <= x; i++) {
    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
  }
}

console.log(dp[x] === INF ? -1 : dp[x]);
