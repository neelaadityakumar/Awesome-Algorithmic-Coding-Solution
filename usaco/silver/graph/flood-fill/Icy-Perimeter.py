import sys

file_input = open("perimeter.in")
file_output = open("perimeter.out", "w")
sys.stdin, sys.stdout = file_input, file_output


def flood_fill(x, y):
    global visited

    to_visit = {(x, y)}
    area = 0
    perimeter = 0
    while to_visit:
        x, y = to_visit.pop()
        if (x, y) not in visited:
            visited.add((x, y))
            area += 1
            neighbour_count = 0
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= nx < length and 0 <= ny < length and graph[nx][ny] == "#":
                    to_visit.add((nx, ny))
                    neighbour_count += 1
            perimeter += 4 - neighbour_count
    return area, perimeter


length = int(sys.stdin.readline())
graph = sys.stdin.readlines()

terminate = False
for row in graph:
    if row.count(".") != 0:
        break
else:
    print(length ** 2, length * 4)
    terminate = True

if not terminate:
    visited = set()
    max_area = 0
    min_perimeter = 0
    for row in range(length):
        for col in range(length):
            if graph[row][col] == "#":
                area, perimeter = flood_fill(row, col)
                if area > max_area or (area == max_area and perimeter < min_perimeter):
                    max_area = area
                    min_perimeter = perimeter
    print(max_area, min_perimeter)
