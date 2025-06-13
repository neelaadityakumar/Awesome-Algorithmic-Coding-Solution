const input = require("fs").readFileSync("/dev/stdin", "utf8").trim();
const n = Number(input);
const dp = Array(n + 1).fill(-1);
function removeDigits(n) {
  dp[0] = 0;

  for (let i = 1; i <= n; i++) {
    for (let ch of String(i)) {
      const digit = Number(ch);
      if (digit > 0) {
        dp[i] = Math.min(dp[i], 1 + dp[i - digit]);
      }
    }
  }
  return dp[n];
}

function removeDigits(n) {
  if (n === 0) return 0;
  if (dp[n] !== -1) return dp[n];

  let minSteps = Infinity;
  for (let ch of String(n)) {
    const digit = Number(ch);
    if (digit > 0) {
      minSteps = Math.min(minSteps, 1 + removeDigits(n - digit));
    }
  }

  return (dp[x] = minSteps);
}

console.log(removeDigits(n));
