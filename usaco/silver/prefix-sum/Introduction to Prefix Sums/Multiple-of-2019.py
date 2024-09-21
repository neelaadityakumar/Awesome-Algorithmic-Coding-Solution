from collections import defaultdict
import sys

external = 1
useLocal = 1
if external == 1:
    if useLocal == 1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open(
            "/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("maxcross.in", "r")
        sys.stdout = open("maxcross.out", "w")
MOD = 2019
string = input()

count = [0] * MOD
count[0] = 1

cur_num = 0
power = 1
ans = 0
for c in reversed(string):
    # find the remainder of the current number MOD 2019
    cur_num = (int(c) * power + cur_num) % MOD
    # increase the power of 10
    power = (power * 10) % MOD
    # increase the count of this remainder
    ans += count[cur_num]
    count[cur_num] += 1


print(ans)
