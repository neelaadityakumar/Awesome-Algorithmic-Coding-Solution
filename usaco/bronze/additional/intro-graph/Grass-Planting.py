with open("planting.in") as read:
    field_num = int(read.readline())
    deg = [0 for _ in range(field_num + 1)]  # 1-indexed
    for _ in range(field_num - 1):
        field1, field2 = [int(i) for i in read.readline().split()]
        deg[field1] += 1
        deg[field2] += 1

max_deg = max(deg)
print(max_deg + 1, file=open("planting.out", "w"))
