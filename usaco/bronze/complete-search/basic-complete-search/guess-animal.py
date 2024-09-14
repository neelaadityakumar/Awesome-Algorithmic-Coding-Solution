# https://usaco.org/index.php?page=viewproblem2&cpid=893
import sys
sys.setrecursionlimit(10**9)

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("guess.in", "r")
        sys.stdout = open("guess.out", "w")
MOD = 10**9 + 7

n= int(input())
p=[ input().split() for i in range(n)]
ans=0
for i in range(n-1):
    animal1=set(p[i][2:])
    for j in range(i+1,n):
        animal2=set(p[j][2:])
        ans=max(ans,len(animal1.intersection(animal2)))
print(ans+1)