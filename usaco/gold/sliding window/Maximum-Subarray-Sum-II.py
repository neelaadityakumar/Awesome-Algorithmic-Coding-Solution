from sortedcontainers import SortedList

# Constants
LINF = 10**18  # Equivalent of long long max value

# Input reading
N, A, B = map(int, input().split())

# Prefix sum array
pfx = [0] * (N + 1)
for i in range(1, N + 1):
    a = int(input())  # Reading each element
    pfx[i] = pfx[i - 1] + a  # Constructing the prefix sum array

# Variables initialization
ret = -LINF
ms = SortedList()  # Python equivalent of multiset

# Sliding window approach for subarray sums between A and B
for i in range(A, N + 1):
    # If subarray size exceeds B, remove the leftmost element from the window
    if i > B:
        ms.remove(pfx[i - B - 1])

    # Insert the current prefix sum into the sorted multiset
    ms.add(pfx[i - A])

    # Calculate the maximum sum by subtracting the smallest prefix sum in the set
    ret = max(ret, pfx[i] - ms[0])

# Output the result
print(ret)
