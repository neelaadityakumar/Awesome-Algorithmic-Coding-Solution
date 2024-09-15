from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
external = 0
useLocal = 1
if external == 1:
    if useLocal == 1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open(
            "/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("factory.in", "r")
        sys.stdout = open("factory.out", "w")


def dfs(node, color):
    # Assign the current node to a team (color)
    team[node] = color

    # Traverse all the friends of the current node
    for neighbor in adj[node]:
        if team[neighbor] == -1:
            # Assign the opposite color to the neighbor
            if not dfs(neighbor, 3 - color):
                return False
        elif team[neighbor] == team[node]:
            # If the neighbor has the same color as the current node, it's impossible
            return False
    return True


# Input
n, m = map(int, input().split())

# Initialize adjacency list for the graph and team array
adj = [[] for _ in range(n + 1)]
team = [-1] * (n + 1)  # -1 means unvisited, 1 for team 1, 2 for team 2

# Build the adjacency list from the friendships
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# Try to assign teams using DFS
for i in range(1, n + 1):
    if team[i] == -1:  # If the pupil has not been assigned to a team yet
        if not dfs(i, 1):  # Start DFS with team 1
            print("IMPOSSIBLE")
            sys.exit()

# If the process succeeds, print the team assignments
print(" ".join(map(str, team[1:])))
