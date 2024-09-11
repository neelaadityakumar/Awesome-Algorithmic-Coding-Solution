
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
INF = float('inf')

# Check if current cooling setup meets the requirements of all cows
def all_cows_satisfied(cooling):
    for s, t, c in cows:
        for j in range(s, t + 1):
            if cooling[j] < c:
                return False
    return True

# Recursive function to explore all combinations of air conditioners
def solve(i, cost, cooling):
    # Base case: if all air conditioners have been considered
    if i == m:
        # Check if all cows are satisfied with current cooling
        return cost if all_cows_satisfied(cooling) else INF



    # Option 1: Do not use the current air conditioner
    min_cost = solve(i + 1, cost, cooling)

    # Option 2: Use the current air conditioner
    a, b, p, cost_i = acs[i]
    new_cooling = cooling[:]  # Create a copy of the current cooling state
    for j in range(a, b + 1):
        new_cooling[j] += p  # Add cooling effect of the current air conditioner

    # Recursively calculate cost if using the current air conditioner
    min_cost = min(min_cost, solve(i + 1, cost + cost_i, new_cooling))

    # Store result in memo and return
    return min_cost



# Initial call to the recursive function
initial_cooling = [0] * 101  # No cooling applied at the start
answer = solve(0, 0, initial_cooling)

print(answer)