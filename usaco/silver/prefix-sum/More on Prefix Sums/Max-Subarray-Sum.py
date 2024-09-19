size = int(input())
arr = [int(i) for i in input().split()]
assert len(arr) == size

max_subarray_sum = arr[0]
min_pref_sum = 0
running_pref_sum = 0
for i in arr:
    running_pref_sum += i
    max_subarray_sum = max(max_subarray_sum, running_pref_sum - min_pref_sum)
    min_pref_sum = min(min_pref_sum, running_pref_sum)
print(max_subarray_sum)
