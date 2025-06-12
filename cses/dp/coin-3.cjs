const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [n, x] = input[0].split(" ").map(Number);
const coins = input[1].split(" ").map(Number);
const mod = 1e9 + 7;

const dp = Array(x + 1).fill(0);
dp[0] = 1;

for (let coin of coins) {
  for (let i = coin; i <= x; i++) {
    dp[i] = (dp[i] + dp[i - coin]) % mod;
  }
}

console.log(dp[x]);
