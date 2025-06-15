const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");

const [n, s] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);

const prefixSumCount = new Map();
prefixSumCount.set(0, 1); // Empty prefix sum
let ans = 0;
let sum = 0;

for (const num of arr) {
  sum += num;
  if (prefixSumCount.has(sum - s)) {
    ans += prefixSumCount.get(sum - s);
  }
  prefixSumCount.set(sum, (prefixSumCount.get(sum) || 0) + 1);
}

console.log(ans);
