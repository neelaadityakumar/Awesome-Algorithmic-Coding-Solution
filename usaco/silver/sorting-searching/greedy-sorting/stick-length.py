import sys
import statistics

external=0
useLocal=1
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("pairup.in", "r")
        sys.stdout = open("pairup.out", "w")
N = int(input())
nums = [int(i) for i in input().split()]
m= statistics.median(nums)


print(int(sum([abs(i-m) for i in nums])))