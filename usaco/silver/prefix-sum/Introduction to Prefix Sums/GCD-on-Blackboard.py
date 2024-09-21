from math import gcd

n = int(input())
arr = list(map(int, input().split()))

ans = 0

prefix_gcd = [0] * n
prefix_gcd[0] = arr[0]

suffix_gcd = [0] * n
suffix_gcd[n - 1] = arr[n - 1]

# prefix_gcd[i] = GCD of a[0], a[1], ..., a[i]
for i in range(1, n):
    prefix_gcd[i] = gcd(prefix_gcd[i - 1], arr[i])

# suffix_gcd[i] = GCD of a[n - 1], a[n - 2], ..., a[i]
for i in range(n - 2, -1, -1):
    suffix_gcd[i] = gcd(suffix_gcd[i + 1], arr[i])

# Calculate the answer if we replace an element with index between 1 and n - 2
for i in range(1, n - 1):
    ans = max(ans, gcd(prefix_gcd[i - 1], suffix_gcd[i + 1]))

# Calculate the answer if we replace the first element in the array
ans = max(ans, suffix_gcd[1])
# Calculate the answer if we replace the last element in the array
ans = max(ans, prefix_gcd[n - 2])

print(ans)
