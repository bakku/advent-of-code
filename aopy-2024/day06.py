from pathlib import Path
import math

UP_MARKER = "^"
RIGHT_MARKER = ">"
DOWN_MARKER = "v"
LEFT_MARKER = "<"
ANY_MARKER = [UP_MARKER, RIGHT_MARKER, DOWN_MARKER, LEFT_MARKER]


def parse_puzzle_input(puzzle_input):
    return [list(line) for line in puzzle_input.split("\n")]


def get_current_point(map_):
    for i in range(len(map_)):
        for j in range(len(map_[i])):
            if map_[i][j] in ANY_MARKER:
                return i, j


def calc_next_point(map_, i, j):
    if map_[i][j] == UP_MARKER:
        if i == 0:
            return -1, j, UP_MARKER

        if map_[i - 1][j] == "#":
            return i, j, RIGHT_MARKER

        return i - 1, j, UP_MARKER

    if map_[i][j] == RIGHT_MARKER:
        if j == len(map_[i]) - 1:
            return i, len(map_[i]), RIGHT_MARKER

        if map_[i][j + 1] == "#":
            return i, j, DOWN_MARKER

        return i, j + 1, RIGHT_MARKER

    if map_[i][j] == DOWN_MARKER:
        if i == len(map_) - 1:
            return len(map_), j, DOWN_MARKER

        if map_[i + 1][j] == "#":
            return i, j, LEFT_MARKER

        return i + 1, j, DOWN_MARKER

    if j == 0:
        return i, -1, LEFT_MARKER

    if map_[i][j - 1] == "#":
        return i, j, UP_MARKER

    return i, j - 1, LEFT_MARKER


def is_guard_leaving_map(map_, i, j):
    return i == -1 or i == len(map_) or j == -1 or j == len(map_[i])


def count_guard_positions(map_):
    return sum([line.count("X") for line in map_])


def part01(puzzle_input):
    map_ = parse_puzzle_input(puzzle_input)

    while True:
        curr_i, curr_j = get_current_point(map_)
        next_i, next_j, marker = calc_next_point(map_, curr_i, curr_j)

        map_[curr_i][curr_j] = "X"

        if is_guard_leaving_map(map_, next_i, next_j):
            break
        else:
            map_[next_i][next_j] = marker

    return count_guard_positions(map_)


def part02(puzzle_input):
    map_ = parse_puzzle_input(puzzle_input)

    return 1


if __name__ == "__main__":
    puzzle_input = Path("input/day06.txt").read_text().rstrip("\n")

    print("Part 01: %d" % part01(puzzle_input))
    print("Part 02: %d" % part02(puzzle_input))
