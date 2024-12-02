from pathlib import Path


def parse_puzzle_input(puzzle_input):
    pairs = [pair.split("   ") for pair in puzzle_input.split("\n")]
    left_unsorted = [int(l) for (l, _) in pairs]
    right_unsorted = [int(r) for (_, r) in pairs]

    left = sorted(left_unsorted)
    right = sorted(right_unsorted)

    return left, right


def part01(puzzle_input):
    left, right = parse_puzzle_input(puzzle_input)

    distances = [max(l, r) - min(l, r) for (l, r) in zip(left, right)]

    return sum(distances)


def part02(puzzle_input):
    left, right = parse_puzzle_input(puzzle_input)

    similarities = [n * right.count(n) for n in left]

    return sum(similarities)


if __name__ == "__main__":
    puzzle_input = Path("input/day01.txt").read_text().rstrip("\n")

    print("Part 01: %d" % part01(puzzle_input))
    print("Part 02: %d" % part02(puzzle_input))
