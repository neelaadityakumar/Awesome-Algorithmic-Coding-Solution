N, M = map(int, input().split())

S = list(map(int, input().split()))

for i in range(1, N):
    if S[i] - S[i - 1] > M:
        S[i - 1] = S[i] - M
    elif S[i - 1] - S[i] > M:
        S[i] = S[i - 1] - M


for i in range(N-1, 0, -1):
    if S[i] - S[i - 1] > M:
        S[i - 1] = S[i] - M
    elif S[i - 1] - S[i] > M:
        S[i] = S[i - 1] - M

print(" ".join(map(str, S)))
