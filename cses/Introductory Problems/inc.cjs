const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const n = +input[0];
const arr = input[1].split(" ").map(Number);
let res = 0;

let last = arr[0];

for (let i = 1; i < n; i++) {
  if (arr[i] >= last) {
    last = arr[i];
  } else {
    res += last - arr[i];
  }
}

console.log(res);
