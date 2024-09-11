# https://dmoj.ca/problem/ccc08s4

import sys
sys.setrecursionlimit(10**9)

external=0
useLocal=1
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("lifeguards.in", "r")
        sys.stdout = open("lifeguards.out", "w")
MOD = 10**9 + 7
def solve(cards, max_value):
    if len(cards) == 1:
        if cards[0] > max_value and cards[0] <= 24:
            return cards[0]
        return max_value

    n = len(cards)
    new_max = max_value

    for i in range(n):
        for j in range(i + 1, n):
            card1 = cards[i]
            card2 = cards[j]

            # Create new list of cards with card1 and card2 removed
            new_cards = [cards[k] for k in range(n) if k != i and k != j]

            # Addition
            new_max = max(new_max, solve(new_cards + [card1 + card2], new_max))

            # Subtraction
            new_max = max(new_max, solve(new_cards + [card1 - card2], new_max))
            new_max = max(new_max, solve(new_cards + [card2 - card1], new_max))

            # Multiplication
            new_max = max(new_max, solve(new_cards + [card1 * card2], new_max))

            # Division
            if card2 != 0 and card1 % card2 == 0:
                new_max = max(new_max, solve(new_cards + [card1 // card2], new_max))
            if card1 != 0 and card2 % card1 == 0:
                new_max = max(new_max, solve(new_cards + [card2 // card1], new_max))

    return new_max

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    num_cases = int(data[index])
    index += 1

    results = []

    for _ in range(num_cases):
        cards = [int(data[index]), int(data[index + 1]), int(data[index + 2]), int(data[index + 3])]
        index += 4
        result = solve(cards, 0)
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()

