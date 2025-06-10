const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const n = Number(input[0]);
const a = input[1].split(" ").map(Number);
const dp = Array(n + 1)
  .fill(null)
  .map(() => Array(n + 1).fill(null));

const solve = (s, e) => {
  if (s > e || e >= n || s >= n) {
    return 0;
  }

  if (dp[s][e] !== null) {
    return dp[s][e];
  }

  const pickLeft = a[s] - solve(s + 1, e);

  const pickRight = a[e] - solve(s, e - 1);

  dp[s][e] = Math.max(pickLeft, pickRight);
  return dp[s][e];
};

const result = solve(0, n - 1);
console.log(result);
