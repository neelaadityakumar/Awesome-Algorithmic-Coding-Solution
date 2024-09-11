# https://usaco.org/index.php?page=viewproblem2&cpid=963
import sys
sys.setrecursionlimit(10**9)

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("gymnastics.in", "r")
        sys.stdout = open("gymnastics.out", "w")
MOD = 10**9 + 7

k,n=map(int,input().split())

sessions= [list(map(int, input().split())) for _ in range(k)]
ans=0
for i in range(1,n):
    for j in range(i+1,n+1):
        c1=0
        c2=0
        for session in sessions:
            ii=session.index(i)
            jj=session.index(j)
            # print(session,i,j,ii,jj,i>=jj)
            if ii>jj:
                c1+=1
            else:
                c2+=1

        if c1==k or c2==k:
            ans+=1
print(ans)







