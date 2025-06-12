// import fs from "fs";

const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const s = input[1].split(" ").map(Number);
const t = input[2].split(" ").map(Number);

const INF = 1e16;
const memo = Array.from({ length: n }, () => Array(m).fill(-1));

function dp(i, j) {
  if (i < 0 || j < 0) return 0;
  if (memo[i][j] !== -1) return memo[i][j];

  let res = dp(i - 1, j);
  res = Math.max(res, dp(i, j - 1));
  if (s[i] == t[j]) {
    res = Math.max(res, 1 + dp(i - 1, j - 1));
  }
  memo[i][j] = res;
  return res;
}

let ans = dp(n - 1, m - 1);
console.log(ans);

if (ans === 0) {
  console.log("");
} else {
  ans = [];
  let [i, j] = [n - 1, m - 1];
  while (i >= 0 && j >= 0) {
    if (s[i] === t[j]) {
      ans.push(s[i]);
      i--;
      j--;
    } else if (j > 0 && memo[i][j] == memo[i][j - 1]) {
      j--;
    } else {
      i--;
    }
  }

  console.log(ans.reverse().join(" "));
}
