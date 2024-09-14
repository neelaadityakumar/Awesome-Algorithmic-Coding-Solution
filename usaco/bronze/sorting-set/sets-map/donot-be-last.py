import sys

sys.stdin = open("notlast.in", "r")
sys.stdout = open("notlast.out", "w")

# taking input
n = int(input())
data = [input().split() for a in range(n)]

# creating a dictionary to store the amount of milk produced by each cow
cows = {'Annabelle':0, 'Bessie':0, 'Daisy':0, 'Elsie':0, 'Gertie':0, 'Henrietta':0, 'Maggie':0}
for c in data:
    cows[c[0]] += int(c[1])

# if all cows produced same amount then print Tie
if len(set(cows.values())) == 1:
    print("Tie")
# else find the second minimum value and find how many cows produced that much amount
else:
    secondMin = sorted(set(cows.values()))[1]
    count = 0
    for key, value in cows.items():
        if value == secondMin:
            ans = key
            count += 1
        # if more than 1 cow produced that amount print Tie
        if count > 1:
            ans = "Tie"
            break
    print(ans)