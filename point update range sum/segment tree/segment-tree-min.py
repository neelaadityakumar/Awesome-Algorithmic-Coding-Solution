import sys
import math
sys.stdin = open("../../_test/test.in", "r")
sys.stdout = open("../../_test/test.out", "w")

# Constants
N = int(2e5 + 5)
INF = math.inf

# Global variables
n, q = 0, 0
x = [0] * N
segment_tree = [0] * (N << 2)

def build(tree_index, left, right):
    """Builds the segment tree."""
    if left == right:
        segment_tree[tree_index] = x[left]
        return
    mid = (left + right) // 2
    build(tree_index * 2 + 1, left, mid)
    build(tree_index * 2 + 2, mid + 1, right)
    segment_tree[tree_index] = min(segment_tree[tree_index * 2 + 1], segment_tree[tree_index * 2 + 2])

def get(tree_index, left, right, query_left, query_right):
    """Gets the minimum value in the range [query_left, query_right]."""
    if query_right < left or right < query_left:
        return INF
    if query_left <= left and right <= query_right:
        return segment_tree[tree_index]
    mid = (left + right) // 2
    left_min = get(tree_index * 2 + 1, left, mid, query_left, query_right)
    right_min = get(tree_index * 2 + 2, mid + 1, right, query_left, query_right)
    return min(left_min, right_min)

def update(tree_index, left, right, position):
    """Updates the segment tree when an element at 'position' changes."""
    if left == right:
        segment_tree[tree_index] = x[position]
        return
    mid = (left + right) // 2
    if position <= mid:
        update(tree_index * 2 + 1, left, mid, position)
    else:
        update(tree_index * 2 + 2, mid + 1, right, position)
    segment_tree[tree_index] = min(segment_tree[tree_index * 2 + 1], segment_tree[tree_index * 2 + 2])

def main():
    """Main function to handle input and output."""
    global n, q, x

    n, q = map(int, input().split())
    x = list(map(int, input().split()))  # Input for array 'x', zero-based indexing

    build(0, 0, n - 1)

    for _ in range(q):
        t, a, b = map(int, input().split())

        if t == 1:
            # Update operation (zero-based index for a)
            x[a - 1] = b
            update(0, 0, n - 1, a - 1)
        else:
            # Range minimum query operation (zero-based indices for a and b)
            print(get(0, 0, n - 1, a - 1, b - 1))

if __name__ == "__main__":
    main()
