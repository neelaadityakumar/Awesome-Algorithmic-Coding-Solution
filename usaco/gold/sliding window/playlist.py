n = int(input().strip())
nums = [int(v) for v in input().split(" ")]

ans = -float("inf")
left, right = 0, 0
unique_songs = set()

while right < n:
    # Notice that all the songs in unique_songs are unique in each iteration.
    # We keep this property by shrinking the window before inserting nums[right].
    while nums[right] in unique_songs:
        unique_songs.remove(nums[left])
        left += 1

    unique_songs.add(nums[right])
    ans = max(ans, right - left+1)

    right += 1


print(ans)
