const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const n = +input[0];
const a = input[1].split(" ").map(Number);

const prefix = [a[0]];
for (let i = 1; i < n; i++) {
  prefix[i] = prefix[i - 1] + a[i];
}
const getSum = (l, r) => {
  if (l === 0) return prefix[r];
  return prefix[r] - prefix[l - 1];
};

const dp = Array.from({ length: n }, () => Array(n).fill(-1));

function solve(i, j) {
  if (i === j) return 0;
  if (dp[i][j] !== -1) return dp[i][j];

  let minCost = Infinity;
  for (let k = i; k < j; k++) {
    const cost = solve(i, k) + solve(k + 1, j) + getSum(i, j);
    minCost = Math.min(minCost, cost);
  }
  return (dp[i][j] = minCost);
}

console.log(solve(0, n - 1));
