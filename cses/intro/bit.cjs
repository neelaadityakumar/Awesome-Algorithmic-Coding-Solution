const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const n = BigInt(input[0]);
const MOD = 1000000007n;

function modPow(base, exponent, mod) {
  let result = 1n;
  base = base % mod;

  while (exponent > 0n) {
    if (exponent % 2n === 1n) {
      result = (result * base) % mod;
    }
    base = (base * base) % mod;
    exponent = exponent / 2n;
  }

  return result;
}

console.log(modPow(2n, n, MOD).toString());
