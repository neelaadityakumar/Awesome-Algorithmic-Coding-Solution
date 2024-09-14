import sys

sys.stdin = open("../../_test/test.in", "r")
sys.stdout = open("../../_test/test.out", "w")

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
	input_parts = input().split()
	q_type = int(input_parts[0])
	arg = list(map(int, input_parts[1:]))
	if q_type == 1:
		for i in range(arg[0] - 1, arg[1]):
			bit.add(i, arg[2])
	elif q_type == 2:
		print(bit.pref_sum(arg[0] - 1) - bit.pref_sum(arg[0] - 2))
