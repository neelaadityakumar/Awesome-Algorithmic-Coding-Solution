const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const [n, k] = input[0].split(" ").map(Number);
const a = input[1].split(" ").map(Number);

// dp[i][j] will store the number of ways to distribute 'j' candies
// among children from index 'i' to 'n-1'.
// Initialize with -1 to denote uncomputed states.
const dp = Array(n)
  .fill(null)
  .map(() => Array(k + 1).fill(-1));

const MOD = 1000000007;

const solve = (childIndex, remainingCandies) => {
  if (remainingCandies === 0) {
    return 1;
  }

  if (childIndex >= n) {
    return 0;
  }

  if (dp[childIndex][remainingCandies] !== -1) {
    return dp[childIndex][remainingCandies];
  }

  let ways = 0;

  if (remainingCandies > 0) {
    ways = (ways + solve(childIndex, remainingCandies - 1)) % MOD;
  }

  // current child (`childIndex`) takes 0 candies,
  ways = (ways + solve(childIndex + 1, remainingCandies)) % MOD;

  // Term 3: `- dp[childIndex + 1][remainingCandies - a[childIndex] - 1]`
  // This term corrects for overcounting. When we add `solve(childIndex, remainingCandies - 1)`,
  // we implicitly assume the current child could take any number of candies up to `remainingCandies`.
  // However, the current child can only take up to `a[childIndex]` candies.
  // So, we subtract the ways where the current child takes *more than* `a[childIndex]` candies.
  // This happens when `(remainingCandies - a[childIndex] - 1)` is the remaining candies for the next child,
  // indicating the current child would have taken `a[childIndex] + 1` or more.
  if (remainingCandies - a[childIndex] - 1 >= 0) {
    ways =
      (ways -
        solve(childIndex + 1, remainingCandies - a[childIndex] - 1) +
        MOD) %
      MOD; // Add MOD to ensure positive result before modulo
  }

  // Store the computed result to avoid re-computation
  dp[childIndex][remainingCandies] = ways;
  return ways;
};

// Initiate the recursion from the first child (index 0) with all 'k' candies
console.log(solve(0, k));
