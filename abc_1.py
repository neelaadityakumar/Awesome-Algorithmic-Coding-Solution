import sys
# from itertools import combinations

# sys.stdin = open("abc.in", "r")
# sys.stdout = open("abc.out", "w")
sys.stdin = open("planting.in", "r")
sys.stdout = open("planting.out", "w")

field_num = int(input())
deg = [0 for _ in range(field_num + 1)]  # 1-indexed
for _ in range(field_num - 1):
	field1, field2 = [int(i) for i in input().split()]
	deg[field1] += 1
	deg[field2] += 1

max_deg = max(deg)
print(max_deg + 1)
