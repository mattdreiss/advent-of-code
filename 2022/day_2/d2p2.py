with open("input.txt", "r") as inputFile:
    lines = inputFile.readlines()

selections = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}
my_total_score = 0

for line in lines:
    round_selections = line.split()
    opponent_selection = selections[round_selections[0]]
    my_outcome = round_selections[1]

    if my_outcome == "X":
        my_total_score += 3 if opponent_selection == 1 else opponent_selection - 1
    elif my_outcome == "Y":
        my_total_score += opponent_selection + 3
    else:
        my_total_score += (1 if opponent_selection == 3 else opponent_selection + 1) + 6

print(my_total_score)
