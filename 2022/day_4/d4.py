def read_lines():
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
    result = []
    for line in lines:
        result.append(line.strip('\n'))
    return result


def get_search_zones(x):
    start = int(x.split('-')[0])
    end = int(x.split('-')[1])
    stuff = {start}
    i = start + 1
    while i <= end:
        stuff.add(i)
        i += 1
    return stuff


def part_one():
    lines = read_lines()
    total = 0
    for line in lines:
        pairs = line.split(',')
        elf_one = get_search_zones(pairs[0])
        elf_two = get_search_zones(pairs[1])
        if elf_one.issubset(elf_two) or elf_two.issubset(elf_one):
            total += 1
    print(total)


def part_two():
    lines = read_lines()
    total = 0
    for line in lines:
        pairs = line.split(',')
        elf_one = get_search_zones(pairs[0])
        elf_two = get_search_zones(pairs[1])
        if elf_one.intersection(elf_two):
            total += 1
    print(total)


part_one()
part_two()
