from typing import Literal, TypedDict

from aopy_2025.utils import get_puzzle_input

Direction = Literal["left", "right"]


class Rotation(TypedDict):
    direction: Direction
    amount: int


def _parse_puzzle_input0101(puzzle_input: str) -> list[Rotation]:
    return [
        {"direction": "left" if line[0] == "L" else "right", "amount": int(line[1:])}
        for line in puzzle_input.splitlines()
    ]


def _p0101(rotations: list[Rotation]) -> None:
    curr_pos = 50

    positions: list[int] = []

    for rotation in rotations:
        step = (
            -rotation["amount"]
            if rotation["direction"] == "left"
            else rotation["amount"]
        )
        curr_pos = (curr_pos + step) % 100
        positions.append(curr_pos)

    print(f"day 01 - part 01: {positions.count(0)}")


def _p0102(rotations: list[Rotation]) -> None:
    curr_pos = 50

    amount_zeros = 0

    for rotation in rotations:
        step = -1 if rotation["direction"] == "left" else 1

        for _ in range(rotation["amount"]):
            curr_pos = (curr_pos + step) % 100

            if curr_pos == 0:
                amount_zeros += 1

    print(f"day 01 - part 02: {amount_zeros}")


def day01() -> None:
    rotations = _parse_puzzle_input0101(get_puzzle_input(1))

    _p0101(rotations)
    _p0102(rotations)
