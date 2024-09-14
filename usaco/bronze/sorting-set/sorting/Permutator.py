n = int(input())
a = list(map(int, input().split()))
b = sorted(list(map(int, input().split())), reverse = True)
res = 0
temp = []
for i in range(n):
	temp.append((a[i] * (i + 1) * (n - i)))
temp.sort()
for i in range(n):
	res += (temp[i] * b[i])
print(res)