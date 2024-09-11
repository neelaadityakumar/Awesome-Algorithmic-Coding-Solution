import sys
sys.setrecursionlimit(10**9)
external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("square.in", "r")
        sys.stdout = open("square.out", "w")

x1,y1,x2,y2=map(int,input().split(" "))
x3,y3,x4,y4=map(int,input().split(" "))

x_min,x_max=min(x1,x3),max(x2,x4)
y_min,y_max=min(y1,y3),max(y2,y4)
length=max(y_max-y_min,x_max-x_min)
print(length**2)