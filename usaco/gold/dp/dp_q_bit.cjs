const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const n = +input[0];
const h = input[1].split(" ").map(Number);
const a = input[2].split(" ").map(Number);

const BIT = Array(n + 2).fill(0);

function update(s, x) {
  for (let i = s; i <= n; i += i & -i) BIT[i] = Math.max(BIT[i], x);
}

function query(s) {
  let ans = 0;
  for (let i = s; i > 0; i -= i & -i) ans = Math.max(ans, BIT[i]);
  return ans;
}

for (let i = 0; i < n; i++) {
  const maxSoFar = query(h[i] - 1); // max value for any height less than h[i]
  update(h[i], maxSoFar + a[i]);
}

console.log(query(n));
