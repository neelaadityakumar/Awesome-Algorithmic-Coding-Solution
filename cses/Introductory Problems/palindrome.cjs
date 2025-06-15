const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");
const str = input[0];
const freq = {};

for (const ch of str) {
  freq[ch] = freq[ch] || 0;
  freq[ch] += 1;
}
let odd = 0;
for (const ch in freq) {
  odd += freq[ch] % 2 == 1;
}
let last = "",
  res = "";
if (odd > 1) {
  console.log("NO SOLUTION");
} else {
  for (const ch in freq) {
    if (freq[ch] % 2 == 1) {
      last = ch.repeat(freq[ch]);
    } else {
      const half = Math.floor(freq[ch] / 2);
      res += ch.repeat(half);
    }
  }

  const result = res + last + [...res].reverse().join("");
  console.log(result);
}
