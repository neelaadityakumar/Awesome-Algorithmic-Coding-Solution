
# https://codeforces.com/problemset/problem/581/D
import sys

sys.setrecursionlimit(10**9)



# Read input values for the dimensions of the three logos
a, b, c, d, e, f = list(map(int, input().split()))

# Calculate the total area needed by the logos
total_area = a * b + c * d + e * f

# Find the smallest possible side length n of the square billboard that can fit the total area
n = 1
while n ** 2 < total_area:
    n += 1

# If the area of the square is greater than the total area needed, it's impossible to fit
if n ** 2 > total_area:
    print(-1)
    exit()

# Prepare the logos' dimensions in sorted order by their largest side first
logos = sorted([[max(a, b), min(a, b), 'A'],
                [max(c, d), min(c, d), 'B'],
                [max(e, f), min(e, f), 'C']])

# The largest logo must fit exactly along one side of the square
if logos[2][0] != n:
    print(-1)
    exit()

# Start building the billboard layout string with the largest logo placed on the square
layout = str(n) + '\n' + (logos[2][2] * n + '\n') * logos[2][1]

# Check if the other two logos can fit the remaining space in the billboard
if logos[0][0] == n and logos[1][0] == n:
    # Both remaining logos should fit side by side
    for i in range(2):
        layout += (logos[i][2] * n + '\n') * logos[i][1]
else:
    # The remaining logos must fit in the remaining space
    remaining_height = n - logos[2][1]

    # Check if the remaining height matches one of the dimensions of the other logos
    if remaining_height not in logos[0] or remaining_height not in logos[1]:
        print(-1)
        exit()

    # Arrange the two logos in the remaining space
    x = logos[0][1] if logos[0][0] == remaining_height else logos[0][0]
    y = logos[1][1] if logos[1][0] == remaining_height else logos[1][0]

    # Add the arrangement of the remaining logos to the layout
    layout += (logos[0][2] * x + logos[1][2] * y + '\n') * remaining_height

# Print the final layout
print(layout)

