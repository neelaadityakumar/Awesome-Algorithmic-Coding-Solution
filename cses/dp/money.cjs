const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const n = +input[0];
const coins = input[1].split(" ").map(Number);

const memo = new Array(n + 1).fill(0).map(() => ({}));
const sums = new Set();

function dfs(i, currSum) {
  if (i === n) {
    if (currSum > 0) sums.add(currSum);
    return;
  }

  if (memo[i][currSum]) return;

  // Don't take current coin
  dfs(i + 1, currSum);

  // Take current coin
  dfs(i + 1, currSum + coins[i]);

  memo[i][currSum] = true;
}

dfs(0, 0);

const result = Array.from(sums).sort((a, b) => a - b);
console.log(result.length);
console.log(result.join(" "));
