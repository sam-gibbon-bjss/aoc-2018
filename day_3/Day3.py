from parse import compile


def read_input():
    with open('input.txt') as f:
        return f.readlines()


def part1():
    claims = read_input()

    claim_format = compile("#{} @ {},{}: {}x{}")

    squares = {}

    for claim in claims:
        id, claim_x, claim_y, width, height = claim_format.parse(claim)

        for x in range(int(claim_x), int(claim_x) + int(width)):
            for y in range(int(claim_y), int(claim_y) + int(height)):
                square = (x, y)
                if square in squares:
                    squares[square] += 1
                else:
                    squares[square] = 1

    dupe_squares = {k: v for k, v in squares.items() if v > 1}
    print("There are {} squares in two or more claims".format(len(dupe_squares)))

    for claim in claims:
        id, claim_x, claim_y, width, height = claim_format.parse(claim)

        has_overlap = False

        for x in range(int(claim_x), int(claim_x) + int(width)):
            for y in range(int(claim_y), int(claim_y) + int(height)):
                if (x, y) in dupe_squares:
                    has_overlap = True
                    break

        if not has_overlap:
            print("Claim {} does not overlap other claims".format(id))


if __name__ == '__main__':
    part1()
