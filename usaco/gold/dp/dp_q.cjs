const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");

const n = +input[0];
const height = input[1].split(" ").map(Number);
const a = input[2].split(" ").map(Number);
const MOD = 1e9 + 7;

const dp = new Map();

function solve(i, prev) {
  if (i >= n) return 0;
  const key = `${i},${prev}`;
  if (dp.has(key)) return dp.get(key);

  // Option 1: skip this element → pay nothing
  let res = solve(i + 1, prev);

  // Option 2: include this element if height[i] > prev
  if (height[i] > prev) {
    res = Math.max(res, a[i] + solve(i + 1, height[i]));
  }

  dp.set(key, res);
  return res;
}

const retained = solve(0, -1);
console.log(retained);
