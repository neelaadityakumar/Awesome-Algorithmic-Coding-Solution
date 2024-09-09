import sys
sys.setrecursionlimit(10**9)

external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("angry.in", "r")
        sys.stdout = open("angry.out", "w")

def explode_right(target, r):
    # Find bales within the explosion range to the right
    in_range = [b for b in bales if target < b <= target + r]
    if len(in_range) == 0:
        return
    # Add the exploded bales to the set
    total_exploded.update(in_range)
    # Recur for the rightmost bale in the current explosion range
    explode_right(in_range[-1], r + 1)


def explode_left(target, r):
    # Find bales within the explosion range to the left
    in_range = [b for b in bales if target - r <= b < target]
    if len(in_range) == 0:
        return
    # Add the exploded bales to the set
    total_exploded.update(in_range)
    # Recur for the leftmost bale in the current explosion range
    explode_left(in_range[0], r + 1)


# Read number of hay bales
N = int(input())
# Read the positions of the hay bales
bales = sorted(int(input()) for _ in range(N))  # Sort to ensure correct ordering

ans = 0
# Try exploding from each hay bale
for i in bales:
    # Use a set to avoid duplicate counting of the same bale
    total_exploded = {i}
    explode_right(i, 1)
    explode_left(i, 1)
    # Update the maximum number of explosions
    ans = max(len(total_exploded), ans)

# Print the maximum number of explosions
print(ans)


