n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

updates = []
for _ in range(m):
    updates.append(list(map(int, input().split())))

s = [0] * (m + 2)
add = [0] * (n + 2)

for _ in range(k):
    x, y = map(int, input().split())
    s[x] += 1
    s[y + 1] -= 1

for i in range(1, m + 1):
    # Apply prefix sums
    s[i] += s[i - 1]

    # At the same time compute the second difference array
    add[updates[i - 1][0]] += s[i] * updates[i - 1][2]
    add[updates[i - 1][1] + 1] -= s[i] * updates[i - 1][2]

for i in range(1, n + 1):
    # Apply prefix sums
    add[i] += add[i - 1]
    print(add[i] + arr[i - 1], end=" ")
