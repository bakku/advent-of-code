import numpy as np
from numpy.typing import NDArray

from aopy_2025.utils import get_puzzle_input


def _parse_puzzle_input(input_: str) -> NDArray[np.str_]:
    return np.array([list(line) for line in input_.splitlines()])


def _count_paper_rolls(grid: NDArray[np.str_]) -> int:
    return np.sum(grid == "@")


def _get_removable_paper_roll_positions(
    grid: NDArray[np.str_],
) -> list[tuple[int, int]]:
    positions: list[tuple[int, int]] = []

    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell != "@":
                continue

            grid_copy = grid.copy()

            grid_copy[row_idx, col_idx] = "#"

            start_row = max(0, row_idx - 1)
            end_row = row_idx + 2

            start_col = max(0, col_idx - 1)
            end_col = col_idx + 2

            subgrid = grid_copy[start_row:end_row, start_col:end_col]

            if _count_paper_rolls(subgrid) < 4:
                positions.append((row_idx, col_idx))

    return positions


def _part1(grid: NDArray[np.str_]):
    print(f"day 04 - part 01: {len(_get_removable_paper_roll_positions(grid))}")


def _apply_removals(
    grid: NDArray[np.str_], removable_positions: list[tuple[int, int]]
) -> None:
    for row, col in removable_positions:
        grid[row, col] = "x"


def _part2(grid: NDArray[np.str_]):
    amount_removes = 0

    while removable_positions := _get_removable_paper_roll_positions(grid):
        amount_removes += len(removable_positions)
        _apply_removals(grid, removable_positions)

    print(f"day 04 - part 02: {amount_removes}")


def day04() -> None:
    puzzle_input = _parse_puzzle_input(get_puzzle_input(4))
    _part1(puzzle_input)
    _part2(puzzle_input)
