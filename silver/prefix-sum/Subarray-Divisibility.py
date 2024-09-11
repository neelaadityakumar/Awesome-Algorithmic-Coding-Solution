n = int(input())
arr = list(map(int, input().split()))
freq = [0 for _ in range(n)]
ans, cur, freq[0] = 0, 0, 1
for x in arr:
    cur = (n + (cur + x) % n) % n
    ans += freq[cur]
    freq[cur] += 1
print(ans)