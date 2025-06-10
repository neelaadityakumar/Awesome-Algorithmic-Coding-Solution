const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const n = Number(input[0]);
const p = input[1].split(" ").map(Number);

const leastHeads = Math.floor(n / 2) + 1;

const dp = Array.from({ length: n }, () => Array(n + 1).fill(0));
dp[0][0] = 1 - p[0]; // 0 heads from first coin (tail)
dp[0][1] = p[0]; // 1 head from first coin

for (let i = 1; i < n; i++) {
  for (let j = 0; j <= i + 1; j++) {
    if (j > 0) dp[i][j] += dp[i - 1][j - 1] * p[i]; // get head
    dp[i][j] += dp[i - 1][j] * (1 - p[i]); // get tail
  }
}

let result = 0;
for (let j = leastHeads; j <= n; j++) {
  result += dp[n - 1][j]; // n-1 is the last coin index
}

console.log(result.toFixed(10));
