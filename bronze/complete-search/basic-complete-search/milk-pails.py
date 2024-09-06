from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

# sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
# sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")

sys.stdin = open("pails.in", "r")
sys.stdout = open("pails.out", "w")
MOD = 10**9 + 7

X,Y,M=map(int,input().split())
ans=0
for i in range(M+1):
    for j in range(M+1):
        if(i*X+j*Y<=M):
            ans=max(ans,i*X+j*Y)

print(ans)