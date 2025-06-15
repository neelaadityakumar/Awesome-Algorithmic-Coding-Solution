const input = require("fs").readFileSync("/dev/stdin", "utf8").trim();
const freq = new Array(26).fill(0);

for (const ch of input) {
  freq[ch.charCodeAt(0) - 65]++;
}

const n = input.length;
const maxFreq = Math.max(...freq);
if (maxFreq > Math.floor((n + 1) / 2)) {
  console.log(-1);
  return;
}

let res = "";
let prev = -1;

for (let i = 0; i < n; i++) {
  for (let c = 0; c < 26; c++) {
    if (freq[c] === 0 || c === prev) continue;

    // try placing this char
    freq[c]--;
    const remaining = n - i - 1;
    const maxRem = Math.max(...freq);

    if (maxRem <= Math.floor((remaining + 1) / 2)) {
      res += String.fromCharCode(c + 65);
      prev = c;
      break;
    }

    freq[c]++; // revert if leads to invalid
  }
}

console.log(res);
