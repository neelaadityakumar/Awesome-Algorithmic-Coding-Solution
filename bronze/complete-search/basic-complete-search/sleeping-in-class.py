# https://usaco.org/index.php?page=viewproblem2&cpid=1203

import sys
sys.setrecursionlimit(10**9)
external=0
useLocal=1
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("balancing.in", "r")
        sys.stdout = open("balancing.out", "w")

def solve():
    n=int(input())
    arr=list(map(int,input().split()))
    sums=sum(arr)
    ans=n-1
    if sums==0:
        print(0)
        return

    for sum1 in range(1, sums + 1):
        if sums % sum1 == 0:
            curr_sum = 0
            valid_partition = True  # Flag to check if partitioning is successful

            for s in arr:
                curr_sum += s
                if curr_sum > sum1:
                    valid_partition = False  # Partitioning failed
                    break
                elif curr_sum == sum1:
                    curr_sum = 0  # Reset current sum for a new partition

            if valid_partition:  # Check if partitioning was successful
                print(n - sums // sum1)
                return

t=int(input())
for _ in range(t):
    solve()

