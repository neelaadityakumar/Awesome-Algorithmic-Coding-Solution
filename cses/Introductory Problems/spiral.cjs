const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const n = +input[0];
function numberSpiral(Y, X) {
  // If Y is greater than X, implying Yth row is the outer boundary
  if (Y > X) {
    // Compute the area of the inner square
    let ans = (Y - 1) * (Y - 1);
    let add = 0;

    // Check parity of Y to determine if numbers are in increasing or decreasing order
    if (Y % 2 !== 0) {
      // Add X to the area if Yth row is odd
      add = X;
    } else {
      // Add 2*Y - X to the area if Yth row is even
      add = 2 * Y - X;
    }

    // Print the final result
    console.log(ans + add);
  }
  // If X is greater than or equal to Y, implying Xth column is the outer boundary
  else {
    // Compute the area of the inner square
    let ans = (X - 1) * (X - 1);
    let add = 0;

    // Check parity of X to determine if numbers are in increasing or decreasing order
    if (X % 2 === 0) {
      // Add Y to the area if Xth column is even
      add = Y;
    } else {
      // Add 2*X - Y to the area if Xth column is odd
      add = 2 * X - Y;
    }

    // Print the final result
    console.log(ans + add);
  }
}

for (let i = 1; i <= n; i++) {
  const [y, x] = input[i].split(" ").map(Number);
  numberSpiral(y, x);
}
