import fs from "fs";

const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const [n, W] = input[0].split(" ").map(Number);
const weights = [0],
  values = [0];
for (let i = 1; i <= n; i++) {
  const [w, v] = input[i].split(" ").map(Number);
  weights[i] = w;
  values[i] = v;
}

const INF = 1e16;
const VMAX = 100001;
const memo = Array.from({ length: n + 1 }, () => Array(VMAX).fill(-1));

function dp(i, v) {
  if (v < 0) return INF;
  if (i === 0) return v === 0 ? 0 : INF;
  if (memo[i][v] !== -1) return memo[i][v];

  let res = dp(i - 1, v); // skip
  if (v >= values[i]) {
    res = Math.min(res, dp(i - 1, v - values[i]) + weights[i]); // take
  }

  memo[i][v] = res;
  return res;
}

let ans = 0;
for (let v = 0; v < VMAX; v++) {
  if (dp(n, v) <= W) ans = v;
}
console.log(ans);
