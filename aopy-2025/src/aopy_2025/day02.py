import itertools
from collections.abc import Callable
from typing import TypedDict

from aopy_2025.utils import flatten, get_puzzle_input


class Range(TypedDict):
    start: int
    end: int


def _parse_puzzle_input(puzzle_input: str) -> list[Range]:
    return [
        {"start": int(range_.split("-")[0]), "end": int(range_.split("-")[1])}
        for range_ in puzzle_input.split(",")
    ]


def _is_invalid_id1(num: int) -> bool:
    num_as_str = str(num)

    if len(num_as_str) % 2 == 1:
        return False

    middle = len(num_as_str) // 2

    return num_as_str[:middle] == num_as_str[middle:]


def _is_invalid_id2(num: int) -> bool:
    num_as_str = str(num)

    middle = len(num_as_str) // 2

    for n in range(1, middle + 1):
        batches = list(itertools.batched(num_as_str, n=n))

        first = batches[0]

        if all(batch == first for batch in batches):
            return True

    return False


def _get_invalid_ids(range_: Range, is_invalid_id: Callable[[int], bool]) -> list[int]:
    return [
        num for num in range(range_["start"], range_["end"] + 1) if is_invalid_id(num)
    ]


def _part1(ranges: list[Range]) -> None:
    invalid_ids = flatten(
        [_get_invalid_ids(range_, _is_invalid_id1) for range_ in ranges]
    )

    print(f"day 02 - part 01: {sum(invalid_ids)}")


def _part2(ranges: list[Range]) -> None:
    invalid_ids = flatten(
        [_get_invalid_ids(range_, _is_invalid_id2) for range_ in ranges]
    )

    print(f"day 02 - part 02: {sum(invalid_ids)}")


def day02() -> None:
    ranges = _parse_puzzle_input(get_puzzle_input(2))
    _part1(ranges)
    _part2(ranges)
