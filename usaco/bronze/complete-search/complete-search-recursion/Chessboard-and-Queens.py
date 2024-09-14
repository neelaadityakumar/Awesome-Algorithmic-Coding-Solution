# https://cses.fi/problemset/task/1624

import sys
sys.setrecursionlimit(10**9)

external=0
useLocal=1
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("lifeguards.in", "r")
        sys.stdout = open("lifeguards.out", "w")
MOD = 10**9 + 7
n=8
board = [[j for j in input()] for _ in range(n)]
ans=0
col=[0]*n
diag_1=[0]*(2*n-1)
diag_2=[0]*(2*n-1)
def solve(row=0):
    if row==n:
        global ans
        ans+=1
        return
    for i in range(n):
        if col[i]==0 and diag_1[row-i+n-1]==0 and diag_2[row+i]==0 and board[row][i]!="*":
            col[i]=1
            diag_1[row-i+n-1]=1
            diag_2[row+i]=1
            solve(row+1)
            col[i]=0
            diag_1[row-i+n-1]=0
            diag_2[row+i]=0


solve()

print(ans)