side_len, query_num = [int(i) for i in input().split()]
tree_prefixes = [[0 for _ in range(side_len + 1)] for _ in range(side_len + 1)]
for r in range(side_len):
    for ci, c in enumerate(input()):
        tree = c == "*"
        tree_prefixes[r + 1][ci + 1] += (
            tree_prefixes[r][ci + 1]
            + tree_prefixes[r + 1][ci]
            - tree_prefixes[r][ci]
            + tree
        )

for _ in range(query_num):
    from_row, from_col, to_row, to_col = [int(i) for i in input().split()]
    print(
        tree_prefixes[to_row][to_col]
        - tree_prefixes[to_row][from_col - 1]
        - tree_prefixes[from_row - 1][to_col]
        + tree_prefixes[from_row - 1][from_col - 1]
    )
