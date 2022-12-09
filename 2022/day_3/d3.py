def prioritize(ch):
    is_upper = ch.isupper()
    alpha_pos = (ord(ch.upper()) - 64)
    priority = alpha_pos + 26 if is_upper else alpha_pos
    return priority


def read_lines():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
    result = []
    for line in lines:
        result.append(line.strip('\n'))
    return result


def part_one():
    lines = read_lines()
    total = 0
    for line in lines:
        compartment_size = int(len(line) / 2)
        compartment_one = set(line[:compartment_size])
        compartment_two = set(line[compartment_size:])
        common_item = compartment_one.intersection(compartment_two)
        total += prioritize(list(common_item)[0])
    print(total)


def part_two():
    lines = read_lines()
    i = 0
    total = 0
    while i < len(lines):
        rucksack_one = set(lines[i])
        rucksack_two = set(lines[i + 1])
        rucksack_three = set(lines[i + 2])
        common_item = rucksack_one.intersection(rucksack_two).intersection(rucksack_three)
        total += prioritize(list(common_item)[0])
        i += 3
    print(total)


part_one()
part_two()
