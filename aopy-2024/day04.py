from pathlib import Path
import re
import numpy as np


def parse_puzzle_input(puzzle_input):
    return [list(line) for line in puzzle_input.split("\n")]


def transpose(grid):
    return np.transpose(grid)


def get_diagonals(grid):
    matrix = np.array(grid)
    n, m = matrix.shape

    return [matrix.diagonal(i).tolist() for i in range(-n + 1, m)]


def count_pattern_horizontally(letter_grid, pattern):
    occurrences = 0

    for letter_line in letter_grid:
        occurrences += len(re.findall(pattern, "".join(letter_line)))

    return occurrences


def part01(puzzle_input):
    letter_grid = parse_puzzle_input(puzzle_input)

    return sum(
        [
            # horizontally forwards
            count_pattern_horizontally(letter_grid, "XMAS"),
            # horizontally backwards
            count_pattern_horizontally(letter_grid, "SAMX"),
            # vertically forwards
            count_pattern_horizontally(transpose(letter_grid), "XMAS"),
            # vertically backwards
            count_pattern_horizontally(transpose(letter_grid), "SAMX"),
            # diagonally top-left -> bottom right forward
            count_pattern_horizontally(get_diagonals(letter_grid), "XMAS"),
            # diagonally top-left -> bottom right backwards
            count_pattern_horizontally(get_diagonals(letter_grid), "SAMX"),
            # diagonally top-right -> bottom left forward
            count_pattern_horizontally(
                get_diagonals(np.fliplr(np.array(letter_grid))), "XMAS"
            ),
            # diagonally top-right -> bottom left backwards
            count_pattern_horizontally(
                get_diagonals(np.fliplr(np.array(letter_grid))), "SAMX"
            ),
        ]
    )


def is_x_mas_at_point(letter_grid, x, y):
    if x == 0 or x == len(letter_grid[0]) - 1 or y == 0 or y == len(letter_grid):
        # we are at the border, so there cannot be MAS
        return False

    matrix = np.array(letter_grid)

    sub_matrix = matrix[y - 1 : y + 2, x - 1 : x + 2]

    tl_br_diagonal = sub_matrix.diagonal(0).tolist()
    tr_bl_diagonal = np.fliplr(sub_matrix).diagonal(0).tolist()

    is_tl_br_diagonal_mas = "".join(tl_br_diagonal) in ["MAS", "SAM"]
    is_tr_bl_diagonal_mas = "".join(tr_bl_diagonal) in ["MAS", "SAM"]

    return is_tl_br_diagonal_mas and is_tr_bl_diagonal_mas


def part02(puzzle_input):
    letter_grid = parse_puzzle_input(puzzle_input)

    return sum(
        [
            1
            for y in range(0, len(letter_grid))
            for x in range(0, len(letter_grid[y]))
            if is_x_mas_at_point(letter_grid, x, y)
        ]
    )


if __name__ == "__main__":
    puzzle_input = Path("input/day04.txt").read_text().rstrip("\n")

    print("Part 01: %d" % part01(puzzle_input))
    print("Part 02: %d" % part02(puzzle_input))
