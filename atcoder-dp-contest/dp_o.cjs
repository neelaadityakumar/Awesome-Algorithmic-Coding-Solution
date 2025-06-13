const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const MOD = 1e9 + 7;

const n = +input[0];
const a = input.slice(1).map((line) => line.split(" ").map(Number));
const dp = Array(1 << n).fill(-1);

function countWays(man, mask) {
  if (mask === (1 << n) - 1) return 1;
  if (dp[mask] !== -1) return dp[mask];
  let total = 0;
  for (let w = 0; w < n; w++) {
    if (!(mask & (1 << w)) && a[man][w] === 1) {
      total = (total + countWays(man + 1, mask | (1 << w))) % MOD;
    }
  }
  return (dp[mask] = total);
}

console.log(countWays(0, 0));
