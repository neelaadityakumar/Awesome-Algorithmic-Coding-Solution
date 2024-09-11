import math
import sys

sys.stdin = open("../_test/test.in", "r")
sys.stdout = open("../_test/test.out", "w")



input = sys.stdin.read
data = input().split()

def build_sparse_table(v, n):
    # Determine the maximum power of 2 that fits the range
    lg = 20  # As in the C++ code
    fa = [[float('inf')] * lg for _ in range(5000005 + 1)]

    # Initialize the sparse table
    for i in range(1, n + 1):
        fa[i][0] = v[i - 1]

    # Build the sparse table
    for j in range(1, lg):
        for i in range(1, n - (1 << (j - 1)) + 1):
            fa[i][j] = min(fa[i][j - 1], fa[i + (1 << (j - 1))][j - 1])

    return fa

def query(fa, a, b):
    a += 1  # Adjusting for 1-based index to 0-based index in Python
    dif = b - a + 1
    mn = fa[a][0]
    curr = a
    for i in range(30):
        if (1 << i) <= dif:
            mn = min(mn, fa[curr][i])
            curr += (1 << i)
    return mn

def main():
    idx = 0

    # Read n and q
    n = int(data[idx])
    idx += 1
    q = int(data[idx])
    idx += 1

    # Read the array values
    v = [int(data[i]) for i in range(idx, idx + n)]
    idx += n

    # Build the sparse table
    fa = build_sparse_table(v, n)

    results = []

    # Process each query
    for _ in range(q):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        results.append(query(fa, a, b))

    # Output results
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
