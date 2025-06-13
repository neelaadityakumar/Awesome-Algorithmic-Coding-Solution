const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const n = Number(input[0]);
const p = input[1].split(" ").map(Number);

function expectedMoves(plates) {
  const n = plates.length;
  const dp = Array.from({ length: n + 1 }, () =>
    Array.from({ length: n + 1 }, () => Array(n + 1).fill(-1))
  );

  function go(c1, c2, c3) {
    if (c1 < 0 || c2 < 0 || c3 < 0) return 0;
    if (c1 === 0 && c2 === 0 && c3 === 0) return 0;
    if (dp[c1][c2][c3] >= 0) return dp[c1][c2][c3];

    let ans = 1;

    if (c1 > 0) ans += (c1 / n) * go(c1 - 1, c2, c3);
    if (c2 > 0) ans += (c2 / n) * go(c1 + 1, c2 - 1, c3);
    if (c3 > 0) ans += (c3 / n) * go(c1, c2 + 1, c3 - 1);

    const p0 = (n - c1 - c2 - c3) / n;
    ans /= 1 - p0;

    dp[c1][c2][c3] = ans;
    return ans;
  }

  const count = [0, 0, 0, 0];
  for (const x of plates) count[x]++;

  return go(count[1], count[2], count[3]);
}

console.log(expectedMoves(p).toFixed(10));
