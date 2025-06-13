const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const [n, x] = input[0].split(" ").map(Number);
const prices = input[1].split(" ").map(Number);
const pages = input[2].split(" ").map(Number);

const dp = new Array(x + 1).fill(0);

for (let i = 0; i < n; i++) {
  for (let j = x; j >= prices[i]; j--) {
    dp[j] = Math.max(dp[j], dp[j - prices[i]] + pages[i]);
  }
}

console.log(dp[x]);
