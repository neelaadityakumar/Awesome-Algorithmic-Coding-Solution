import sys

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("div7.in", "r")
        sys.stdout = open("div7.out", "w")

n=int(input())
k=7
arr=[int(input()) for _ in range(n)]
ans, cur= 0, 0
index={}
for i in range(len(arr)):
    x=arr[i]
    cur = (k + (cur + x) % k) % k
    if cur in index:
        ans =max(ans,i-index[cur])
    else:
        index[cur]=i


print(ans)