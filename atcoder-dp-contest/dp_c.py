n=int(input())
arr=[]
dp=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
    dp.append([float('-inf'),float('-inf'),float('-inf')])

dp[0]=arr[0]
for i in range(1,n):
    dp[i][0]=max(dp[i-1][1]+arr[i][0],dp[i-1][2]+arr[i][0])
    dp[i][1]=max(dp[i-1][0]+arr[i][1],dp[i-1][2]+arr[i][1])
    dp[i][2]=max(dp[i-1][0]+arr[i][2],dp[i-1][1]+arr[i][2])

print(max(dp[-1]))