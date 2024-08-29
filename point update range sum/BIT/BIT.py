class MinSegmentTree:
	"""A data structure that can answer point update & range minimum queries."""

	def __init__(self, len_: int):
		self.len = len_
		self.tree = [0] * (2 * len_)

	def set(self, ind: int, val: int) -> None:
		"""Sets the value at ind to val."""
		ind += self.len
		self.tree[ind] = val

		while ind > 1:
			self.tree[ind // 2] = min(self.tree[ind], self.tree[ind ^ 1])
			ind //= 2

	def range_min(self, start: int, end: int) -> int:
		""":return: the minimum element of all elements in [start, end)"""
		start += self.len
		end += self.len
		min_ = float("inf")
		while start < end:
			if start % 2 == 1:
				min_ = min(min_, self.tree[start])
				start += 1
			if end % 2 == 1:
				end -= 1
				min_ = min(min_, self.tree[end])

			start //= 2
			end //= 2
		return min_


arr_len, query_num = map(int, input().split())
arr = list(map(int, input().split()))

segtree = MinSegmentTree(arr_len)
for i, v in enumerate(arr):
	segtree.set(i, v)

for _ in range(query_num):
	type_, arg1, arg2 = map(int, input().split())
	if type_ == 1:
		segtree.set(arg1 - 1, arg2)
	elif type_ == 2:
		print(segtree.range_min(arg1 - 1, arg2))