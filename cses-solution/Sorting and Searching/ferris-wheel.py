import sys

external = 0
useLocal = 1
if external == 1:
    if useLocal == 1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open(
            "/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("pairup.in", "r")
        sys.stdout = open("pairup.out", "w")
n, x = map(int, input().split())
children = sorted(list(map(int, input().split())))
ans = 0

i = 0  # Applicant pointer
j = n-1  # Apartment pointer
ans = 0
while i < n and j >= 0 and i <= j:
    left = children[i]
    right = children[j]
    # print(i, j, left, right, ans)
    if abs(left + right) <= x:
        i += 1
        j -= 1
    elif left > right:
        i += 1
    else:
        j -= 1

    ans += 1
print(ans)
