const n = +require("fs").readFileSync("/dev/stdin", "utf8").trim();
const mod = 1e9 + 7;

const total = (n * (n + 1)) / 2;
if (total % 2 !== 0) {
  console.log(0);
} else {
  const target = Math.floor(total / 2);
  const dp = Array(target + 1).fill(0);
  dp[0] = 1;

  for (let num = 1; num <= n; num++) {
    for (let sum = target; sum >= num; sum--) {
      dp[sum] = (dp[sum] + dp[sum - num]) % mod;
    }
  }

  const inv2 = 500000004; // Modular inverse of 2 under mod 1e9+7
  console.log((dp[target] * inv2) % mod);
}
