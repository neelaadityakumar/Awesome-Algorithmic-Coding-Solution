class BIT:
	"""
	Short for "binary indexed tree",
	this data structure supports point update and range sum
	queries like a segment tree.
	"""

	def __init__(self, len_: int) -> None:
		self.bit = [0] * (len_ + 1)
		self.arr = [0] * len_
		self.len = len_

	def set(self, ind: int, val: int):
		"""Sets the value at ind to val"""
		self.add(ind, val - self.arr[ind])

	def add(self, ind: int, val: int):
		"""Adds val to the element at index ind."""
		self.arr[ind] += val
		ind += 1
		while ind <= self.len:
			self.bit[ind] += val
			ind += ind & -ind

	def pref_sum(self, ind: int):
		""":return: The sum of all values in [0, ind]."""
		ind += 1
		sum_ = 0
		while ind > 0:
			sum_ += self.bit[ind]
			ind -= ind & -ind
		return sum_


arr_len, query_num = map(int, input().split())
arr = list(map(int, input().split()))

bit = BIT(arr_len)
for i, v in enumerate(arr):
	bit.add(i, v)

for _ in range(query_num):
	q_type, arg1, arg2 = map(int, input().split())
	if q_type == 1:
		bit.set(arg1 - 1, arg2)
	elif q_type == 2:
		print(bit.pref_sum(arg2 - 1) - bit.pref_sum(arg1 - 2))