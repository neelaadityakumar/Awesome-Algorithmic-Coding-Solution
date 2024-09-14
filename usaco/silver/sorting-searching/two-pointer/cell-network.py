import sys

external = 0
useLocal = 1
if external == 1:
    if useLocal == 1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open(
            "/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("pairup.in", "r")
        sys.stdout = open("pairup.out", "w")
n, m = map(int, input().split())

# We remove all the duplicate cities and towers
cities = sorted(list(set(map(int, input().split()))))
towers = sorted(list(set(map(int, input().split()))))

"""
We start at the first city. For each city, we calculate the distance to towers
until the selected tower's position is greater than the city's position. (As
then, the distance will only increase). Then, we continue for the next city
starting at the current tower. We choose the minimum distance to a tower for
each city, and the maximum of which will be our answer.
"""

max_dist = 0
city_ptr = 0
tower_ptr = 0

while city_ptr < len(cities):

    while tower_ptr+1 < len(towers) and abs(cities[city_ptr] - towers[tower_ptr]) > abs(cities[city_ptr] - towers[tower_ptr+1]):
        tower_ptr += 1

    dist = abs(cities[city_ptr] - towers[tower_ptr])
    max_dist = max(max_dist, dist)

    city_ptr += 1


print(max_dist)
