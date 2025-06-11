const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const s1 = input[0];
const s2 = input[1];
const n = s1.length;
const m = s2.length;

let prev = Array(m + 1).fill(0);
let curr = Array(m + 1).fill(0);

for (let j = 0; j <= m; j++) prev[j] = j;

for (let i = 1; i <= n; i++) {
  curr[0] = i;
  for (let j = 1; j <= m; j++) {
    if (s1[i - 1] === s2[j - 1]) {
      curr[j] = prev[j - 1];
    } else {
      curr[j] =
        1 +
        Math.min(
          prev[j], // delete
          curr[j - 1], // insert
          prev[j - 1] // replace
        );
    }
  }
  [prev, curr] = [curr, prev]; // reuse arrays
}

console.log(prev[m]);
