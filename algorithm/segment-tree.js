class SegmentTree {
  constructor(nums) {
    this.n = nums.length;
    this.tree = new Array(4 * this.n).fill(0);
    this.buildTree(nums, 0, this.n - 1, 0);
  }

  buildTree(nums, left, right, index) {
    if (left === right) {
      this.tree[index] = nums[left];
      return;
    }

    const mid = Math.floor((left + right) / 2);
    this.buildTree(nums, left, mid, 2 * index + 1);
    this.buildTree(nums, mid + 1, right, 2 * index + 2);
    this.tree[index] = this.tree[2 * index + 1] + this.tree[2 * index + 2];
  }

  sumRange(left, right, index, qleft, qright) {
    if (qright < left || qleft > right) {
      return 0;
    }

    if (qleft <= left && right <= qright) {
      return this.tree[index];
    }

    const mid = Math.floor((left + right) / 2);
    return (
      this.sumRange(left, mid, 2 * index + 1, qleft, qright) +
      this.sumRange(mid + 1, right, 2 * index + 2, qleft, qright)
    );
  }

  update(left, right, index, pos, val) {
    if (left === right) {
      this.tree[index] = val;
      return;
    }

    const mid = Math.floor((left + right) / 2);
    if (pos <= mid) {
      this.update(left, mid, 2 * index + 1, pos, val);
    } else {
      this.update(mid + 1, right, 2 * index + 2, pos, val);
    }

    this.tree[index] = this.tree[2 * index + 1] + this.tree[2 * index + 2];
  }
}

class NumArray {
  constructor(nums) {
    this.segTree = new SegmentTree(nums);
  }

  update(index, val) {
    this.segTree.update(0, this.segTree.n - 1, 0, index, val);
  }

  sumRange(left, right) {
    return this.segTree.sumRange(0, this.segTree.n - 1, 0, left, right);
  }
}
// Example usage:
const nums = [1, 3, 5];
const numArray = new NumArray(nums);
console.log(numArray.sumRange(0, 2)); // Output: 9
numArray.update(1, 2);
console.log(numArray.sumRange(0, 2)); // Output: 8
