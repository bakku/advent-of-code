from pathlib import Path


def parse_puzzle_input(puzzle_input):
    equations = []

    for line in puzzle_input.split("\n"):
        result, numbers_as_str = line.split(": ")

        numbers = [int(number) for number in numbers_as_str.split(" ")]

        equations.append([int(result), numbers])

    return equations


def solve(result, numbers, curr_result, with_concat):
    if len(numbers) == 0:
        if result == curr_result:
            return True
        else:
            return False

    next_num = numbers[0]
    rest_nums = numbers[1:]

    if solve(result, rest_nums, curr_result + next_num, with_concat):
        return True

    if solve(result, rest_nums, curr_result * next_num, with_concat):
        return True

    if with_concat:
        if solve(result, rest_nums, int(str(curr_result) + str(next_num)), with_concat):
            return True

    return False


def is_solvable(equation, with_concat=False):
    result, numbers = equation

    first_num = numbers[0]
    rest_nums = numbers[1:]

    return solve(result, rest_nums, first_num, with_concat)


def part01(puzzle_input):
    equations = parse_puzzle_input(puzzle_input)

    solvable_equations = [equation for equation in equations if is_solvable(equation)]

    relevant_results = [result for result, _ in solvable_equations]

    return sum(relevant_results)


def part02(puzzle_input):
    equations = parse_puzzle_input(puzzle_input)

    solvable_equations = [equation for equation in equations if is_solvable(equation, with_concat=True)]

    relevant_results = [result for result, _ in solvable_equations]

    return sum(relevant_results)


if __name__ == "__main__":
    puzzle_input = Path("input/day07.txt").read_text().rstrip("\n")

    print("Part 01: %d" % part01(puzzle_input))
    print("Part 02: %d" % part02(puzzle_input))
