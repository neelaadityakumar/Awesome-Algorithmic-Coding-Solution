# https://usaco.org/index.php?page=viewproblem2&cpid=639
import sys
sys.setrecursionlimit(10**9)

# sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
# sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")

sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")
MOD = 10**9 + 7

n, k = map(int, input().split())
diamond_arr = []
for i in range(n):
    size = int(input())
    diamond_arr.append(size)

result = 0
for i in range(n):
    count = 0
    for j in range(i, n):
        if diamond_arr[j] >= diamond_arr[i] and diamond_arr[j] <= diamond_arr[i] + k:
            count += 1
        result = max(result, count)

print(result)