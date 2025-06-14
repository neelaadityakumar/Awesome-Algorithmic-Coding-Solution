function modPow(base, exp, mod) {
  if (base === 0 && exp === 0) return 1;

  let result = 1;
  base = base % mod;

  while (exp > 0) {
    if (exp & 1) result = (result * base) % mod;
    base = (base * base) % mod;
    exp = exp >> 1;
  }

  return result;
}

const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const t = +input[0];
const mod = 1000000007;

const output = [];

for (let i = 1; i <= t; i++) {
  const [aStr, bStr] = input[i].split(" ");
  let a = +aStr;
  let b = +bStr;

  output.push(modPow(a, b, mod));
}

console.log(output.join("\n"));
