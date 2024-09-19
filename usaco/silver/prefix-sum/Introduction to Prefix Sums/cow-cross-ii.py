from collections import defaultdict
import sys

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("maxcross.in", "r")
        sys.stdout = open("maxcross.out", "w")

# Input reading
n, k, b = map(int, input().split())
broken_signals = [int(input()) for _ in range(b)]

# Initialize an array where 1 represents working signal and 0 represents broken signal
arr = [1] * n
for i in broken_signals:
    arr[i - 1] = 0

# Use sliding window to find the minimum repairs needed
current_broken_count = sum(arr[:k])  # Count working signals in the first window of size k
min_repairs = k - current_broken_count  # Initial repairs needed

for i in range(k, n):
    # Slide the window right by one
    current_broken_count += arr[i] - arr[i - k]
    repairs_needed = k - current_broken_count
    min_repairs = min(min_repairs, repairs_needed)

print(min_repairs)
