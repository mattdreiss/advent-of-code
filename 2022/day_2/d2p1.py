with open("input.txt", "r") as inputFile:
    lines = inputFile.readlines()

selections = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
my_total_score = 0

for line in lines:
    round_selections = line.split()
    opponent_score = selections[round_selections[0]]
    my_score = selections[round_selections[1]]

    if opponent_score == my_score:
        my_score += 3
    elif (my_score == 2 and opponent_score == 1) or (my_score == 3 and opponent_score == 2) or (my_score == 1 and opponent_score == 3):
        my_score += 6

    my_total_score += my_score


print(my_total_score)