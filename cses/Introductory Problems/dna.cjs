const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const arr = input[0].split("");

let res = 1;
let cnt = 1;
for (let i = 1; i < arr.length; i++) {
  if (arr[i] == arr[i - 1]) {
    cnt++;
    res = Math.max(res, cnt);
  } else {
    cnt = 1;
  }
}

console.log(res);
