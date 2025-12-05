from typing import TypedDict

from aopy_2025.utils import get_puzzle_input


class Database(TypedDict):
    fresh_id_ranges: list[tuple[int, int]]
    ingredient_ids: list[int]


def _parse_puzzle_input(input_: str) -> Database:
    [raw_id_ranges, raw_ingredient_ids] = input_.split("\n\n")

    fresh_id_ranges: list[tuple[int, int]] = []

    for id_range in raw_id_ranges.splitlines():
        [start, end] = id_range.split("-")

        fresh_id_ranges.append((int(start), int(end)))

    ingredient_ids = [
        int(ingredient_id) for ingredient_id in raw_ingredient_ids.splitlines()
    ]

    return {"fresh_id_ranges": fresh_id_ranges, "ingredient_ids": ingredient_ids}


def _is_fresh(id_: int, fresh_id_ranges: list[tuple[int, int]]) -> bool:
    return any(start <= id_ <= end for start, end in fresh_id_ranges)


def _part1(database: Database) -> None:
    result = sum(
        _is_fresh(ingredient_id, database["fresh_id_ranges"])
        for ingredient_id in database["ingredient_ids"]
    )

    print(f"day 05 - part 1: {result}")


def _clip_range(
    ranges: list[tuple[int, int]], range_: tuple[int, int]
) -> tuple[int, int]:
    start, end = range_

    for r_start, r_end in ranges:
        if r_start <= start <= r_end:
            start = r_end + 1
        if r_start <= end <= r_end:
            end = r_start - 1

    return start, end


def _preprocess_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    final_ranges: list[tuple[int, int]] = []

    for range_ in ranges:
        modified_range = _clip_range(final_ranges, range_)

        if modified_range[0] <= modified_range[1]:
            final_ranges.append(modified_range)

    return final_ranges


def _postprocess_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    final_ranges: list[tuple[int, int]] = []

    for outer_idx, outer_range in enumerate(ranges):
        is_contained = any(
            inner_range[0] <= outer_range[0] and outer_range[1] <= inner_range[1]
            for inner_idx, inner_range in enumerate(ranges)
            if outer_idx != inner_idx
        )

        if not is_contained:
            final_ranges.append(outer_range)

    return final_ranges


def _part2(database: Database) -> None:
    ranges = database["fresh_id_ranges"]
    normalized_ranges = _postprocess_ranges(_preprocess_ranges(ranges))

    result = sum(range_[1] - range_[0] + 1 for range_ in normalized_ranges)

    print(f"day 05 - part 2: {result}")


def day05() -> None:
    database = _parse_puzzle_input(get_puzzle_input(5))
    _part1(database)
    _part2(database)
