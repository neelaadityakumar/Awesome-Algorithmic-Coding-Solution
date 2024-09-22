from collections import deque

city_num, flight_num = list(map(int, input().split(" ")))
flights = [[] for _ in range(city_num)]
back_edge = [[] for _ in range(city_num)]
for _ in range(flight_num):
    a, b = list(map(int, input().split(" ")))
    a, b = a - 1, b - 1
    flights[a].append(b)
    back_edge[b].append(a)

# Use Kahn's algorithm to do a topological sort
in_degree = [0] * city_num
for nodes in flights:
    for node in nodes:
        in_degree[node] += 1

queue = deque([i for i, in_deg in enumerate(in_degree) if in_deg == 0])
top_sort = []
while queue:
    curr = queue.popleft()
    top_sort.append(curr)
    for next_ in flights[curr]:
        in_degree[next_] -= 1
        if in_degree[next_] == 0:
            queue.append(next_)

# Compute the dist array in topological order
parent = [-1] * city_num
dist = [-float("inf")] * city_num
dist[0] = 1
for i in range(len(top_sort)):
    b = top_sort[i]
    for prev in back_edge[b]:
        if dist[prev] + 1 > dist[b]:
            dist[b] = dist[prev] + 1
            parent[b] = prev

if dist[city_num - 1] == -float("inf"):
    print("IMPOSSIBLE")
else:
    # dist[city_num - 1] denotes the length of the longest path
    # ending at the final city. i.e. Lehmälä
    print(dist[city_num - 1])

    # Begin from the final city, trace the parent pointer
    # to construct the entire path backward
    at = city_num - 1
    route = []
    while parent[at] != -1:
        route.append(at)
        at = parent[at]
    route.append(0)

    # Print the route in the correct order
    print(*[c + 1 for c in route[::-1]])
