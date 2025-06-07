n,k=map(int,input().split())
arr=list(map(int,input().split()))
dp=[float('inf')]*n
dp[0]=0
dp[1]=abs(arr[1]-arr[0])
for i in range(2,n):
    for j in range(1,k+1):
        if i-j>=0:
            dp[i]=min(dp[i],dp[i-j]+abs(arr[i]-arr[i-j]))
print(dp[-1])