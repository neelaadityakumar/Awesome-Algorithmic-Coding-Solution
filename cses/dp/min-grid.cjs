const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const n = +input[0];
const grid = input.slice(1).map((row) => row.split(""));

const score = (c) => c.charCodeAt(0) - "A".charCodeAt(0) + 1;

const dp = Array.from({ length: n }, () => Array(n).fill(null));

dp[0][0] = {
  cost: score(grid[0][0]),
  path: grid[0][0],
};

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (i === 0 && j === 0) continue;

    const curChar = grid[i][j];
    const curScore = score(curChar);

    let options = [];

    if (i > 0) {
      const { cost, path } = dp[i - 1][j];
      options.push({ cost: cost + curScore, path: path + curChar });
    }

    if (j > 0) {
      const { cost, path } = dp[i][j - 1];
      options.push({ cost: cost + curScore, path: path + curChar });
    }

    // Choose min cost first, then lex smallest path
    options.sort((a, b) =>
      a.cost !== b.cost ? a.cost - b.cost : a.path.localeCompare(b.path)
    );

    dp[i][j] = options[0];
  }
}

console.log(dp[n - 1][n - 1].path);
