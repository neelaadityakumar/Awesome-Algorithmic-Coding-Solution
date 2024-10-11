import heapq

with open("pump.in", "r") as infile:
    n, m = map(int, infile.readline().split())

    graph = [[] for _ in range(n)]
    flow_rates = []

    for _ in range(m):
        a, b, c, f = map(int, infile.readline().split())
        graph[a - 1].append((b - 1, c, f))
        graph[b - 1].append((a - 1, c, f))
        flow_rates.append(f)


def dijkstra(flow_rate: int) -> float:

    cost = [float("inf")] * n
    cost[0] = 0  # start at FJ's farm
    queue = [(0, 0)]
    completed = set()

    while queue:
        curr_cost, curr_node = heapq.heappop(queue)

        if curr_node in completed:
            continue
        completed.add(curr_node)

        for adj_node, pipe_cost, pipe_flow in graph[curr_node]:
            # we ignore all routes with flow rates less than our set rate
            if pipe_flow < flow_rate:
                continue
            new_cost = curr_cost + pipe_cost
            if new_cost < cost[adj_node]:
                cost[adj_node] = new_cost
                heapq.heappush(queue, (cost[adj_node], adj_node))

    return 0 if cost[n - 1] == float("inf") else flow_rate / cost[n - 1]


max_worth = 0
for flow_rate in flow_rates:
    worth = dijkstra(flow_rate)
    if worth > max_worth:
        max_worth = worth

print(int(max_worth * 10**6), file=open("pump.out", "w"))
