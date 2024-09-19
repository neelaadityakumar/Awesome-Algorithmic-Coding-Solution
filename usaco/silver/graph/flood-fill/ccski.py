
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
        sys.stdin = open("ccski.in", "r")
        sys.stdout = open("ccski.out", "w")

# Directions for movement: up, left, down, right
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
MAX_N = 500

# Initialize grid, waypoints, and mark arrays
grid = [[0] * MAX_N for _ in range(MAX_N)]
wp = [[False] * MAX_N for _ in range(MAX_N)]
mark = [[False] * MAX_N for _ in range(MAX_N)]

# Floodfill to mark all reachable nodes given an elevation difference `d`


def floodfill(d, m, n, wy, wx):
    stack = [(wy, wx)]  # Stack for DFS
    mark[wy][wx] = True

    while stack:
        y, x = stack.pop()  # Pop from stack for DFS

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < m and 0 <= nx < n:
                if not mark[ny][nx] and abs(grid[y][x] - grid[ny][nx]) <= d:
                    stack.append((ny, nx))  # Push to stack for DFS
                    mark[ny][nx] = True


# Checks if all waypoints are reachable with the given elevation difference `d`


def reachable(d, m, n, wy, wx):
    # Reset the mark grid for each search
    global mark
    mark = [[False] * n for _ in range(m)]

    floodfill(d, m, n, wy, wx)

    # Check if all waypoints are reachable
    for i in range(m):
        for j in range(n):
            if wp[i][j] and not mark[i][j]:
                return False
    return True


def main():
    m, n = map(int, input().split())
    diff = 0
    mx = 0
    mn = sys.maxsize
    # Read the grid of elevations
    for i in range(m):
        grid[i][:n] = map(int, input().split())
        mx = max(mx, max(grid[i][:n]))
        mn = min(mn, min(grid[i][:n]))
        diff = max(diff, mx - mn)

    # Read the waypoints and set the starting waypoint
    wy, wx = 0, 0
    for i in range(m):
        waypoint_row = map(int, input().split())
        for j, is_waypoint in enumerate(waypoint_row):
            wp[i][j] = is_waypoint != 0
            if wp[i][j]:
                wy, wx = i, j

    # Binary search for the minimum elevation difference
    l, r = 0, int(diff+1)
    while l < r:
        d = (l + r) // 2
        if reachable(d, m, n, wy, wx):
            r = d
        else:
            l = d + 1

    # Write output to 'ccski.out'
    print(l)


if __name__ == "__main__":
    main()
