const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const n = +input[0];
const total = Math.floor(n * (n + 1) * 0.5);
const sum = input[1]
  .split(" ")
  .map(Number)
  .reduce((prev, curr) => prev + curr, 0);

console.log(total - sum);
