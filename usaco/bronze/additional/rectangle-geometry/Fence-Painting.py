import sys
sys.setrecursionlimit(10**9)
external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("paint.in", "r")
        sys.stdout = open("paint.out", "w")

x1,x2=map(int,input().split(" "))
x3,x4,=map(int,input().split(" "))

total=(x2-x1)+(x4-x3)
inter=max(0,min(x2,x4)-max(x1,x3))
print(total-inter)
