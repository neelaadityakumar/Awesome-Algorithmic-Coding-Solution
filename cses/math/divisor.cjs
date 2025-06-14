const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const t = +input[0];

const output = [];

function count(n) {
  let res = 0;
  for (let i = 1; i * i <= n; i++) {
    if (n % i === 0) {
      res += 1;
      if (i !== Math.floor(n / i)) res += 1; // count n/i only if it's different
    }
  }
  return res;
}

for (let i = 1; i <= t; i++) {
  const n = +input[i];

  output.push(count(n));
}

console.log(output.join("\n"));
