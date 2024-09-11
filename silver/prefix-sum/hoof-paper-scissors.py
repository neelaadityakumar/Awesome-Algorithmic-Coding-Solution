with open("hps.in") as r:
	n = int(r.readline().strip())
	hooves = [0 for _ in range(n + 1)]
	paper = [0 for _ in range(n + 1)]
	scissors = [0 for _ in range(n + 1)]

	for i in range(1, n + 1):
		hooves[i] += hooves[i - 1]
		paper[i] += paper[i - 1]
		scissors[i] += scissors[i - 1]

		action = r.readline().strip()
		if action == "H":
			paper[i] += 1
		elif action == "P":
			scissors[i] += 1
		elif action == "S":
			hooves[i] += 1

max_wins = 0
for i in range(n + 1):
	before_wins = max(hooves[i], paper[i], scissors[i])
	after_wins = max(
		hooves[n] - hooves[i], paper[n] - paper[i], scissors[n] - scissors[i]
	)
	max_wins = max(max_wins, before_wins + after_wins)

print(max_wins, file=open("hps.out", "w"))