const MOD = 1e9 + 7;

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const K = input[0].trim(); // large number as string
const D = +input[1];

const n = K.length;
const memo = new Map();

function dfs(pos, sumMod, tight) {
  const key = `${pos},${sumMod},${tight}`;
  if (memo.has(key)) return memo.get(key);

  if (pos === n) return sumMod === 0 ? 1 : 0;

  const maxDigit = tight ? Number(K[pos]) : 9;
  let res = 0;

  for (let digit = 0; digit <= maxDigit; digit++) {
    const newTight = tight && digit === maxDigit;
    res = (res + dfs(pos + 1, (sumMod + digit) % D, newTight)) % MOD;
  }

  memo.set(key, res);
  return res;
}

let ans = dfs(0, 0, true);
ans = (ans - 1 + MOD) % MOD; // subtract 1 to exclude 0
console.log(ans);
