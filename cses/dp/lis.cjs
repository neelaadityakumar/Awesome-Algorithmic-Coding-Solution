const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);

const tails = [];

for (let num of arr) {
  let left = 0,
    right = tails.length;
  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    if (tails[mid] < num) left = mid + 1;
    else right = mid;
  }
  tails[left] = num;
}

console.log(tails.length);
