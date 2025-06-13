// const input = require("fs")
//   .readFileSync("/dev/stdin", "utf8")
//   .trim()
//   .split("\n");
// const n = +input[0];
// let res = [];
// function permute(ind, curr) {
//   if (ind >= n) {
//     if (curr.length == n) {
//       res = [...curr];
//       return true;
//     }
//     return false;
//   }
//   for (let i = 1; i <= n; i++) {
//     if (curr.includes(i) || Math.abs(curr[curr.length - 1] - i) == 1) continue;
//     if (permute(ind + 1, [...curr, i])) return true;
//   }
//   return false;
// }

// permute(0, []);
// if (res.length === n) console.log(res.join(" "));
// else console.log("NO SOLUTION");
const input = require("fs").readFileSync("/dev/stdin", "utf8").trim();
const n = +input;

if (n === 2 || n === 3) {
  console.log("NO SOLUTION");
} else {
  const res = [];
  for (let i = 2; i <= n; i += 2) res.push(i);
  for (let i = 1; i <= n; i += 2) res.push(i);
  console.log(res.join(" "));
}
