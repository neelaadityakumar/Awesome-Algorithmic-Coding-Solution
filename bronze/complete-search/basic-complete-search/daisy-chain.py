import sys
sys.setrecursionlimit(10**9)

external=0
useLocal=1
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("diamond.in", "r")
        sys.stdout = open("diamond.out", "w")
MOD = 10**9 + 7

n= int(input())
p=[int(i) for i in input().split()]
count=0
for i in range(n):
    for j in range(i,n):
         avg=sum(p[i : j + 1]) / (j - i + 1)
         for k in range(i,j+1):
            if(p[k]==avg):
                count+=1
                break

print(count)