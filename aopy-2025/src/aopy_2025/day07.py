from aopy_2025.utils import get_puzzle_input


def _parse_puzzle_input(input_: str) -> list[list[str]]:
    return [list(line) for line in input_.splitlines()]


def _print_grid(grid: list[list[str]]) -> None:
    print("\n".join(["".join(row) for row in grid]))


def _tachyon_manifold_playthrough(grid: list[list[str]]) -> list[list[str]]:
    modified_grid = [row.copy() for row in grid]

    for row_idx, row in enumerate(modified_grid):
        for col_idx, cell in enumerate(row):
            if (
                cell == "S"
                and (row_idx + 1) < len(modified_grid)
                and modified_grid[row_idx + 1][col_idx] != "|"
            ):
                modified_grid[row_idx + 1][col_idx] = "|"

            if cell == "|" and (row_idx + 1) < len(modified_grid):
                if modified_grid[row_idx + 1][col_idx] == "^":
                    if (col_idx + 1) < len(modified_grid[row_idx + 1]):
                        modified_grid[row_idx + 1][col_idx + 1] = "|"

                    if (col_idx - 1) >= 0:
                        modified_grid[row_idx + 1][col_idx - 1] = "|"
                else:
                    modified_grid[row_idx + 1][col_idx] = "|"

    return modified_grid


def _count_splits(grid: list[list[str]]) -> int:
    count = 0

    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == "^":
                if (col_idx - 1) < 0 or grid[row_idx][col_idx - 1] != "|":
                    continue

                if (col_idx + 1) >= len(grid[row_idx]) or grid[row_idx][
                    col_idx + 1
                ] != "|":
                    continue

                if (row_idx - 1) < 0 or grid[row_idx - 1][col_idx] != "|":
                    continue

                count += 1

    return count


def _part1(grid: list[list[str]]) -> None:
    new_grid = _tachyon_manifold_playthrough(grid)
    print(f"day 07 - part 1: {_count_splits(new_grid)}")


def _find_starting_point(grid: list[list[str]]) -> tuple[int, int]:
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == "S":
                return row_idx, col_idx

    raise ValueError("starting point not found")


def _count_timelines(grid: list[list[str]], row_idx: int, col_idx: int) -> int:
    print(row_idx, col_idx)

    # Reached the end of the grid
    if row_idx + 1 >= len(grid):
        return 0

    # No split, just move down
    if grid[row_idx][col_idx] != "^":
        return _count_timelines(grid, row_idx + 1, col_idx)

    count = 0

    if col_idx - 1 >= 0:
        count += _count_timelines(grid, row_idx, col_idx - 1) + 1

    if col_idx + 1 < len(grid[row_idx]):
        count += _count_timelines(grid, row_idx, col_idx + 1) + 1

    return count


def _part2(grid: list[list[str]]) -> None:
    row_idx, col_idx = _find_starting_point(grid)
    print(f"day 07 - part 2: {_count_timelines(grid, row_idx, col_idx)}")


def day07() -> None:
    grid = _parse_puzzle_input(get_puzzle_input(7))
    _part1(grid)
    _part2(grid)
