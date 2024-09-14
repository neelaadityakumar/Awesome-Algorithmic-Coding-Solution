import sys
sys.setrecursionlimit(10**9)
external=1
useLocal=0
if external==1:
    if useLocal==1:
        sys.stdin = open("/Users/aditya.kumar/Desktop/code/_test/test.in", "r")
        sys.stdout = open("/Users/aditya.kumar/Desktop/code/_test/test.out", "w")
    else:
        sys.stdin = open("tttt.in", "r")
        sys.stdout = open("tttt.out", "w")

# read input
board = []
for _ in range(3):
  board.append(list(input()))

def check_winners(c1, c2, c3):
  winners = {c1, c2, c3}
  if len(winners) == 3:
    return []
  else:
    return sorted(list(winners))

def check_individual_winners_and_team_winners(individuals_winners, team_winners, winners):
  if len(winners) == 1:
    individuals_winners.add(winners[0])
  elif len(winners) == 2:
    # convert list to tuple so that it can be hashed and added into set
    team_winners.add(tuple(winners))

def check_num_of_winners(board):
  individuals_winners = set()
  team_winners = set()

  # check each row
  for row in board:
    winners = check_winners(*row)
    check_individual_winners_and_team_winners(individuals_winners, team_winners, winners)

  # check each column
  for i in range(3):
    winners = check_winners(board[0][i], board[1][i], board[2][i])
    check_individual_winners_and_team_winners(individuals_winners, team_winners, winners)

  # check diagonals
  winners = check_winners(board[0][0], board[1][1], board[2][2])
  check_individual_winners_and_team_winners(individuals_winners, team_winners, winners)
  winners = check_winners(board[0][2], board[1][1], board[2][0])
  check_individual_winners_and_team_winners(individuals_winners, team_winners, winners)

  return len(individuals_winners), len(team_winners)

result = check_num_of_winners(board)
print(result[0])
print(result[1])
