import sys
sys.setrecursionlimit(10**9)
external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("breedflip.in", "r")
        sys.stdout = open("breedflip.out", "w")

n=int(input())
a=input()
b=input()
count=0
i=0
while i<n:
    c=0
    while a[i]!=b[i]:
        c+=1
        i+=1
    if c>0:
        count+=1

    i+=1
print(count)