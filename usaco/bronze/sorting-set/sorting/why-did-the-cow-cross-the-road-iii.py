import sys
sys.setrecursionlimit(10**9)

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("cowqueue.in", "r")
        sys.stdout = open("cowqueue.out", "w")

n= int(input())
time=[ list(map(int,input().split())) for i in range(n)]
time.sort(reverse=True)

ans=0
last=0
while len(time)>0:
    start,duration=time.pop()
    if start<last:
        start+=last-start
    last=start+duration
    ans=max(ans,last)

print(ans)