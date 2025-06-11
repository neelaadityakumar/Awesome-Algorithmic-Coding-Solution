const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const MOD = 1e9 + 7;

const [nStr, kStr] = input[0].split(" ");
const n = +nStr;
let K = BigInt(kStr);

const A = input.slice(1).map((line) => line.split(" ").map(Number));

// Matrix multiplication: (A × B) % MOD
function multiply(A, B) {
  const res = Array.from({ length: n }, () => Array(n).fill(0));
  for (let i = 0; i < n; i++)
    for (let k = 0; k < n; k++)
      for (let j = 0; j < n; j++)
        res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD;
  return res;
}

// Matrix exponentiation: A^k % MOD
function matrixPower(mat, k) {
  let res = Array.from({ length: n }, (_, i) =>
    Array.from({ length: n }, (_, j) => (i === j ? 1 : 0))
  ); // Identity matrix
  while (k > 0n) {
    if (k % 2n === 1n) res = multiply(res, mat);
    mat = multiply(mat, mat);
    k >>= 1n;
  }
  return res;
}

const Ak = matrixPower(A, K);

// Sum of all elements in A^K
let total = 0;
for (let i = 0; i < n; i++)
  for (let j = 0; j < n; j++) total = (total + Ak[i][j]) % MOD;

console.log(total);
