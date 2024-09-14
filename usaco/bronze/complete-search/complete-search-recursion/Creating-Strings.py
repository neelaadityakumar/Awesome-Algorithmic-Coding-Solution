# https://cses.fi/problemset/task/1622

import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

external=0
useLocal=1
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("lifeguards.in", "r")
        sys.stdout = open("lifeguards.out", "w")
MOD = 10**9 + 7


string = [i for i in input()]
n= len(string)
perm=[]
count_dic=defaultdict(int)
for s in string:
    count_dic[s]+=1
def solve(index=0,str=[]):
    if index==n:
        perm.append("".join(str))
        return
    for i in range(ord("a"),ord("z")+1):
        if count_dic[chr(i)]>0:
            count_dic[chr(i)]-=1
            str.append(chr(i))
            solve(index+1,str)
            count_dic[chr(i)]+=1
            str.pop()

solve()
size=len(perm)
print(size)
for i in range(size):
    print(perm[i])
