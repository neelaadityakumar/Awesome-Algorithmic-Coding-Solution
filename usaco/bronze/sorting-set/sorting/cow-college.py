import sys
sys.setrecursionlimit(10**9)

external=0
useLocal=1
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("cowqueue.in", "r")
        sys.stdout = open("cowqueue.out", "w")

n= int(input())
fee = sorted(int(i) for i in input().split())

optimalFee=0
totalFee=0
for i in range(n):
    currFee=fee[i]
    profit=currFee*(n-i)
    if profit>totalFee:
        totalFee=profit
        optimalFee=currFee



print(totalFee,optimalFee)