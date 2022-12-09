with open("input.txt", "r") as inputFile:
    lines = inputFile.readlines()

current_elf_calories = 0
max_elf_calories = 0
elves = []

for line in lines:
    if line == "\n":
        elves.append(current_elf_calories)
        current_elf_calories = 0
    else:
        current_elf_calories += int(line)

elves.sort(reverse=True)
print("part 1: ", elves[0])
print("part 2: ", elves[0] + elves[1] + elves[2])
