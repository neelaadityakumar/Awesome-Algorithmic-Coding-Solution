const input = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split("\n");

const [n, x] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);

// Store value and original index
const indexedArr = arr.map((val, idx) => ({ val, idx: idx + 1 }));

// Sort by value
indexedArr.sort((a, b) => a.val - b.val);

function twoSum(start, end, target) {
  while (start < end) {
    const sum = indexedArr[start].val + indexedArr[end].val;
    if (sum === target) {
      return [indexedArr[start].idx, indexedArr[end].idx];
    } else if (sum < target) {
      start++;
    } else {
      end--;
    }
  }
  return -1;
}

let result = -1;

for (let i = 0; i < n - 2; i++) {
  const a = indexedArr[i].val;
  const rem = x - a;

  const pair = twoSum(i + 1, n - 1, rem);
  if (pair !== -1) {
    result = [indexedArr[i].idx, ...pair];
    break;
  }
}

if (result === -1) {
  console.log("IMPOSSIBLE");
} else {
  result.sort((a, b) => a - b);
  console.log(result.join(" "));
}
