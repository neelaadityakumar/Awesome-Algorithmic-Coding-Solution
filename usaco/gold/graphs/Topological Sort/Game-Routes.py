from collections import defaultdict, deque
from typing import DefaultDict


# taking n,m number of levels and number of edges
n, m = [int(x) for x in input().split()]


graph = defaultdict(list)
dp = defaultdict(int)
back = defaultdict(list)
inDegree = defaultdict(int)


# building the graph
for _ in range(m):
    x, y = [int(x) for x in input().split()]
    graph[x].append(y)
    back[y].append(x)
    inDegree[y] += 1

level = deque([])

# adding into the queue nodes which doesn't have outgoing edges
for i in range(1, n+1):
    if not inDegree[i]:
        level.append(i)

# doing topological sort and changing  all the number of paths
dp[1] = 1
while level:
    node = level.popleft()
    for val in graph[node]:
        inDegree[val] -= 1
        if inDegree[val] == 0:
            level.append(val)
    for val in back[node]:
        dp[node] = (dp[node]+dp[val]) % (1000000007)
print(dp[n])
