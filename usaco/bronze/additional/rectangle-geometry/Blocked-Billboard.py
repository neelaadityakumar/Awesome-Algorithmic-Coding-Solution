import sys
sys.setrecursionlimit(10**9)
external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("billboard.in", "r")
        sys.stdout = open("billboard.out", "w")

x1,y1,x2,y2=map(int,input().split(" "))
x3,y3,x4,y4=map(int,input().split(" "))
x5,y5,x6,y6=map(int,input().split(" "))

def area(x1,y1,x2,y2):
    if x1 > x2 or y1 > y2:
        return 0
    return (x2 - x1) * (y2 - y1)
area1=area(x1,y1,x2,y2)
area2=area(x3,y3,x4,y4)
area3_intersect=area(max(x1,x5),max(y1,y5),min(x2,x6),min(y2,y6))
area4_intersect=area(max(x3,x5),max(y3,y5),min(x4,x6),min(y4,y6))

print(area1+area2-area3_intersect-area4_intersect)
