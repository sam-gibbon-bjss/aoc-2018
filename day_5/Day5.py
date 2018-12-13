def read_input():
    with open('input.txt') as f:
        return f.readline().strip()


def will_react(unit1, unit2):
    return unit1 != unit2 and unit1.upper() == unit2.upper()


def react_iteration(polymer):
    for i in range(0, len(polymer)-1):
        # loop may skip some positions if we delete a character pair so can result in index out of range,
        # but it's much less efficient to immediately break after one deletion
        try:
            if will_react(polymer[i], polymer[i + 1]):
                polymer = polymer[:i] + polymer[i + 2:]
        except IndexError:
            break

    return polymer


def react(polymer):
    previous_polymer = None
    iterations = 0
    while polymer != previous_polymer:
        iterations += 1
        previous_polymer = polymer
        polymer = react_iteration(polymer)
        # print("Reaction {}: {} -> {}".format(iterations, previous_polymer, polymer))
        print("Reaction {}: {} -> {}".format(iterations, len(previous_polymer), len(polymer)))

    return polymer


def part1():
    polymer = react(read_input())

    print("Final polymer: {}".format(polymer))
    print("Remaining units: {}".format(len(polymer)))


def part2():
    polymer = read_input()

    polymer_chars = set(polymer.upper())

    reduced_polymer_lengths = {}
    for char in polymer_chars:
        reduced_polymer = polymer.replace(char, "").replace(char.lower(), "")
        reduced_reacted_polymer = react(reduced_polymer)
        reduced_polymer_lengths[char] = len(reduced_reacted_polymer)

    print(reduced_polymer_lengths)


if __name__ == '__main__':
    part1()
    part2()
