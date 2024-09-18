from collections import deque
import sys
sys.setrecursionlimit(10**9)
external = 1
useLocal = 0
if external == 1:
    if useLocal == 1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open(
            "/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("revegetate.in", "r")
        sys.stdout = open("revegetate.out", "w")


def main():
    # Open input and output files
    n, m = map(int, input().split())

    adj = [[] for _ in range(n)]

    for _ in range(m):
        line = input().split()
        type = line[0]
        u, v = int(line[1]) - 1, int(line[2]) - \
            1  # Convert to 0-based index

        # 'S' means same grass, 'D' means different grass
        adj[u].append((v, type == 'S'))
        adj[v].append((u, type == 'S'))

    component_num = 0
    impossible = False
    color = [-1] * n  # -1 means unvisited

    for i in range(n):
        # If this node has not been visited, process it
        if color[i] == -1:
            component_num += 1
            todo = deque([(i, True)])  # BFS queue with (node, grass type)

            while todo:
                nxt, grass_type = todo.popleft()

                # Set grass type for the current node
                color[nxt] = grass_type

                # Process adjacent nodes
                for neighbor, same_grass in adj[nxt]:
                    expected_type = grass_type if same_grass else not grass_type

                    # If the neighbor hasn't been visited
                    if color[neighbor] == -1:
                        todo.append((neighbor, expected_type))
                    # If there's a contradiction in the grass type assignment
                    elif color[neighbor] != expected_type:
                        impossible = True
                        break

            if impossible:
                break

    if impossible:
        print("0")
    else:
        # Output 2^component_num in the form of '1' followed by component_num '0's
        print(f"1{'0' * component_num}")


if __name__ == "__main__":
    main()
