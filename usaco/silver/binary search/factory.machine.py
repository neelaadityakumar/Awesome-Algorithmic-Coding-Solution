# https://cses.fi/problemset/task/1620

n, t = map(int, input().split())
machines = list(map(int, input().split()))


def products_made(t, arr):
    return sum(t // x for x in arr)


left = 0
right = max(machines) * t

while left < right:
    mid = left + (right - left) // 2

    if products_made(mid, machines) >= t:
        right = mid
    else:
        left = mid + 1

print(left)
