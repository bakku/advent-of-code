from pathlib import Path
import re


def parse_puzzle_input(puzzle_input):
    return "".join(puzzle_input.split("\n"))


def part01(puzzle_input):
    memory = parse_puzzle_input(puzzle_input)

    matches = re.findall(r"mul\(\d+,\d+\)", memory)

    result = 0

    for match in matches:
        [n, m] = match.replace("mul(", "").replace(")", "").split(",")

        result += int(n) * int(m)

    return result


def part02(puzzle_input):
    memory = parse_puzzle_input(puzzle_input)

    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", memory)

    result = 0
    mul_enabled = True

    for match in matches:
        if match == "do()":
            mul_enabled = True
        elif match == "don't()":
            mul_enabled = False
        else:
            if mul_enabled:
                [n, m] = match.replace("mul(", "").replace(")", "").split(",")

                result += int(n) * int(m)

    return result


if __name__ == "__main__":
    puzzle_input = Path("input/day03.txt").read_text().rstrip("\n")

    print("Part 01: %d" % part01(puzzle_input))
    print("Part 02: %d" % part02(puzzle_input))
