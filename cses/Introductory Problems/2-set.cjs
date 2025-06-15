const n = +require("fs").readFileSync("/dev/stdin", "utf8").trim();

const total = (n * (n + 1)) / 2;

if (total % 2 !== 0) {
  console.log("NO");
} else {
  console.log("YES");
  let a = [],
    b = [];
  let sumA = 0,
    sumB = 0;

  for (let i = n; i >= 1; i--) {
    if (sumA <= sumB) {
      a.push(i);
      sumA += i;
    } else {
      b.push(i);
      sumB += i;
    }
  }

  console.log(a.length);
  console.log(a.join(" "));
  console.log(b.length);
  console.log(b.join(" "));
}

// Backtracking version
let found = false;
let ansA = [],
  ansB = [];

function twoSet(i, sumA, sumB, a, b) {
  if (found) return;

  if (i > n) {
    if (sumA === sumB) {
      ansA = [...a];
      ansB = [...b];
      found = true;
    }
    return;
  }

  // Try adding i to set A
  twoSet(i + 1, sumA + i, sumB, [...a, i], b);
  // Try adding i to set B
  twoSet(i + 1, sumA, sumB + i, a, [...b, i]);
}

if (total % 2 !== 0) {
  console.log("NO");
} else {
  twoSet(1, 0, 0, [], []);
  console.log("YES");
  console.log(ansA.length);
  console.log(ansA.join(" "));
  console.log(ansB.length);
  console.log(ansB.join(" "));
}
