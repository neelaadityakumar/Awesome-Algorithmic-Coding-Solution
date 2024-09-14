import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
external=0
useLocal=1
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("whereami.in", "r")
        sys.stdout = open("whereami.out", "w")


from collections import defaultdict

# List of zodiac years in order
years = "Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, Pig, Rat".split(", ")
# Map each zodiac year to its index (1-based)
yearMap = {year: i for i, year in enumerate(years)}

# Dictionary to store the birth year difference of each cow relative to Bessie
birth_year_diff = defaultdict(int)

# Set Bessie's zodiac year as Ox
birth_year = {"Bessie": "Ox"}

# Read the number of relationships
n = int(input())

# Process each relationship
for _ in range(n):
    statement = input().split()
    from_cow = statement[0]     # The cow whose year we are defining
    direction = statement[3]    # 'previous' or 'next'
    zodiac = statement[4]       # Zodiac year
    to_cow = statement[-1]      # The cow relative to which we are defining the year

    # Find the current year position of the target cow
    current_year_pos = yearMap[birth_year[to_cow]]
    target_year_pos = yearMap[zodiac]

    # Calculate the difference in years based on the zodiac cycle
    if direction == "previous":
        # Find the closest previous zodiac year
        if target_year_pos < current_year_pos:
            year_diff = current_year_pos - target_year_pos
        else:
            year_diff = current_year_pos - target_year_pos + 12
        birth_year_diff[from_cow] = birth_year_diff[to_cow] - year_diff
    else:
        # Find the closest next zodiac year
        if target_year_pos > current_year_pos:
            year_diff = target_year_pos - current_year_pos
        else:
            year_diff = target_year_pos - current_year_pos + 12
        birth_year_diff[from_cow] = birth_year_diff[to_cow] + year_diff

    # Update the birth year of the cow
    birth_year[from_cow] = zodiac

# Output the absolute difference in years between Bessie and Elsie
print(abs(birth_year_diff["Elsie"]))

