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
n, m, k = map(int, input().split())
applicants = sorted(list(map(int, input().split())))
apartments = sorted(list(map(int, input().split())))
ans = 0

i = 0  # Applicant pointer
j = 0  # Apartment pointer
ans = 0
while i < n and j < m:
    applicant = applicants[i]
    apartment = apartments[j]
    if abs(applicant - apartment) <= k:
        ans += 1
        i += 1
        j += 1
    elif applicant - apartment > k:
        j += 1
    else:
        i += 1

print(ans)
