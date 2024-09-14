import sys

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("bcount.in", "r")
        sys.stdout = open("bcount.out", "w")

n,q=map(int,input().split())
arr=[int(input()) for _ in range(n)]
dic={
    1:0,
    2:0,
    3:0,
}
counter1=[0]*(n+1)
counter2=[0]*(n+1)
counter3=[0]*(n+1)

for i in range(1,n+1):
    counter1[i]=counter1[i-1]+(1 if arr[i-1]==1 else 0)
    counter2[i]=counter2[i-1]+(1 if arr[i-1]==2 else 0)
    counter3[i]=counter3[i-1]+(1 if arr[i-1]==3 else 0)


for _ in range(q):
    l,r=map(int,input().split())

    print(counter1[r]-counter1[l-1],counter2[r]-counter2[l-1],counter3[r]-counter3[l-1])

