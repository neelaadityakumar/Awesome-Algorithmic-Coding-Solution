import sys
sys.setrecursionlimit(10**9)
external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("billboard.in", "r")
        sys.stdout = open("billboard.out", "w")


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
# we'll be using one-indexing to make things more obvious
x = [0, x1, x2, x3, x4]
y = [0, y1, y2, y3, y4]

# Case 1
if x[4] >= x[2] and x[3] <= x[1] and y[4] >= y[2] and y[3] <= y[1]:
	print(str(0))
# Case 2
elif x[3] <= x[1] and y[3] <= y[1] and y[4] > y[1] and x[4] >= x[2]:
	print(str((x[2] - x[1]) * (y[2] - y[4])))
# Case 3
elif y[3] < y[2] and x[3] <= x[1] and y[4] >= y[2] and x[4] >= x[2]:
	print(str((x[2] - x[1]) * (y[3] - y[1])))
# Case 4
elif x[4] > x[1] and x[3] <= x[1] and y[4] >= y[2] and y[3] <= y[1]:
	print(str((x[2] - x[4]) * (y[2] - y[1])))
# Case 5
elif x[3] < x[2] and x[4] >= x[2] and y[4] >= y[2] and y[3] <= x[1]:
	print(str((x[3] - x[1]) * (y[2] - y[1])))
# Case 6 and the corner case
else:
	print(str((x[2] - x[1]) * (y[2] - y[1])))