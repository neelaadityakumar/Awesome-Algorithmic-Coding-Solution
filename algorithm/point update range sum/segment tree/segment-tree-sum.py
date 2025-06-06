class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build_tree(nums, 0, self.n - 1, 0)

    def build_tree(self, nums, left, right, index):
        if left == right:
            self.tree[index] = nums[left]
            return

        mid = (left + right) // 2
        self.build_tree(nums, left, mid, 2 * index + 1)
        self.build_tree(nums, mid + 1, right, 2 * index + 2)
        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def sum_range(self, left, right, index, qleft, qright):
        if qright < left or qleft > right:
            return 0

        if qleft <= left and right <= qright:
            return self.tree[index]

        mid = (left + right) // 2
        return self.sum_range(left, mid, 2 * index + 1, qleft, qright) + \
               self.sum_range(mid + 1, right, 2 * index + 2, qleft, qright)

    def update(self, left, right, index, pos, val):
        if left == right:
            self.tree[index] = val
            return

        mid = (left + right) // 2
        if pos <= mid:
            self.update(left, mid, 2 * index + 1, pos, val)
        else:
            self.update(mid + 1, right, 2 * index + 2, pos, val)

        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]


class NumArray:
    def __init__(self, nums):
        self.seg_tree = SegmentTree(nums)

    def update(self, index, val):
        self.seg_tree.update(0, self.seg_tree.n - 1, 0, index, val)

    def sumRange(self, left, right):
        return self.seg_tree.sum_range(0, self.seg_tree.n - 1, 0, left, right)
