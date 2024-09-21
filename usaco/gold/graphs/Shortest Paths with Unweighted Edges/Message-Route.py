from collections import deque, defaultdict

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

# BFS setup
queue = deque([1])
distance = [-1] * (n + 1)
parent = [-1] * (n + 1)
distance[1] = 0

while queue:
    node = queue.popleft()

    for neighbor in graph[node]:
        if distance[neighbor] == -1:  # If neighbor is not visited
            distance[neighbor] = distance[node] + 1
            parent[neighbor] = node
            queue.append(neighbor)
            if neighbor == n:  # If we reach the destination
                # Reconstruct the path
                path = []
                current = n
                while current != -1:
                    path.append(current)
                    current = parent[current]
                path.reverse()

                print(len(path))
                print(" ".join(map(str, path)))
                exit()

# If no path found
print("IMPOSSIBLE")
