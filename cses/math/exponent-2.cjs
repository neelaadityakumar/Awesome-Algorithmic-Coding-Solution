// Fermat's Little Theorem
// When MOD is prime (which 1e9 + 7 is), Fermat’s Little Theorem tells us:
// a^k ≡ a^(k % (MOD - 1)) mod MOD
// That means:
// a^(b^c) mod MOD ≡ a^(b^c % (MOD - 1)) mod MOD
// So instead of computing b^c directly, we compute it modulo MOD - 1:

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
const MOD = 1000000007;

const output = [];

for (let i = 1; i <= t; i++) {
  const [a, b, c] = input[i].split(" ").map(Number);
  output.push(modPow(a, modPow(b, c, MOD - 1), MOD));
}

console.log(output.join("\n"));
