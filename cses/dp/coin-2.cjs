const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const [n, x] = input[0].split(" ").map(Number);
const coins = input[1].split(" ").map(Number);
const mod = 1e9 + 7;

const dp = new Uint32Array(x + 1); // Fast, typed array
dp[0] = 1;

for (let i = 1; i <= x; i++) {
  for (let j = 0; j < n; j++) {
    const coin = coins[j];
    if (i >= coin) {
      dp[i] = (dp[i] + dp[i - coin]) % mod;
    }
  }
}

console.log(dp[x]);
