const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const [n, k] = input[0].split(" ").map(Number);
const a = input[1].split(" ").map(Number);
const dp = Array(k + 1).fill(-1);

const solve = (stones) => {
  if (stones <= 0) return 0;
  if (dp[stones] !== -1) return dp[stones];

  for (let i = 0; i < n; i++) {
    if (stones - a[i] >= 0 && solve(stones - a[i]) === 0) {
      return (dp[stones] = 1); // found a winning move
    }
  }

  return (dp[stones] = 0); // no winning move found
};

console.log(solve(k) ? "First" : "Second");
