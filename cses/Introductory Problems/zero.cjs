const input = require("fs").readFileSync("/dev/stdin", "utf8").trim();
let n = BigInt(input);
let count = 0n;

for (let i = 5n; i <= n; i *= 5n) {
  count += n / i;
}

console.log(count.toString());
