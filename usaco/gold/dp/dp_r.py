MOD = 10**9 + 7

def mat_mult(A, B, N):
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
    return result

# DP-style matrix exponentiation with memoization
def mat_pow_dp(A, K, N, memo):
    if K in memo:
        return memo[K]
    if K == 1:
        return A
    if K % 2 == 0:
        half = mat_pow_dp(A, K // 2, N, memo)
        memo[K] = mat_mult(half, half, N)
    else:
        half = mat_pow_dp(A, K // 2, N, memo)
        half_squared = mat_mult(half, half, N)
        memo[K] = mat_mult(half_squared, A, N)
    return memo[K]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    N = int(data[idx]); idx += 1
    K = int(data[idx]); idx += 1

    A = []
    for _ in range(N):
        row = [int(data[idx + j]) for j in range(N)]
        A.append(row)
        idx += N

    memo = {}
    result = mat_pow_dp(A, K, N, memo)
    total_paths = sum(sum(row) for row in result) % MOD
    print(total_paths)

if __name__ == "__main__":
    main()
