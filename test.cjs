const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const n = +input[0];
const coins = input[1].split(" ").map(Number);

let possible = new Set([0]);

for (let coin of coins) {
  const next = new Set();
  for (let sum of possible) {
    next.add(sum + coin);
  }
  for (let sum of next) possible.add(sum);
}

possible.delete(0);
const result = [...possible].sort((a, b) => a - b);

console.log(result.length);
console.log(result.join(" "));
