import sys

n = int(input())
cows = [int(i) for i in input().split()]

odd = 0
even = 0
for i in range(n):
    if cows[i] % 2 == 0:
        even += 1
    else:
        odd += 1

while odd > even:
    odd -= 2
    even += 1

if odd == even:
    print(odd * 2)
else:
    print(odd * 2 + 1)