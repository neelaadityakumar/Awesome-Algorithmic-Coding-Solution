
# https://usaco.org/index.php?page=viewproblem2&cpid=1276
import sys
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


n,m=map(int,input().split())

cows= [list(map(int, input().split())) for _ in range(n)]
acs= [list(map(int, input().split())) for _ in range(m)]
ans = float('inf')

# Function to check if a set of air conditioners (given by bitmask) satisfies the cooling requirements of the cows
def check(bitmask):
    # Cooling array for stalls from 1 to 100
    cooling = [0] * 101
    cost = 0

    # Add cooling from each air conditioner in the current bitmask
    for i in range(m):
        if bitmask & (1 << i):  # If the i-th air conditioner is included
            a, b, p, cost_i = acs[i]
            cost += cost_i
            for j in range(a, b + 1):
                cooling[j] += p

    # Check if all cows are sufficiently cooled
    for s, t, c in cows:
        for j in range(s, t + 1):
            if cooling[j] < c:
                return float('inf')  # Not enough cooling

    return cost

# Iterate over all possible subsets of air conditioners using bitmasking
for bitmask in range(1 << m):
    ans = min(ans, check(bitmask))

# Print the minimum cost found
print(ans)