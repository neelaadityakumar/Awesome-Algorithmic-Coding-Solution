const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
let n = +input[0];
let res = [];
while (n > 1) {
  res.push(n);

  if (n & 1) {
    n *= 3;
    n++;
  } else {
    n = Math.floor(n / 2);
  }
}
res.push(n);
console.log(res.join(" "));
