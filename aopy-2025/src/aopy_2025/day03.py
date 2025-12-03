import itertools

from aopy_2025.utils import get_puzzle_input


def _parse_puzzle_input(input_: str) -> list[list[str]]:
    return [list(line) for line in input_.splitlines()]


def _get_largest_joltage_naive(bank: list[str], n: int) -> int:
    return max(int("".join(x)) for x in itertools.combinations(bank, n))


def _get_largest_joltage_fast(bank: list[str], length: int) -> int:
    joltage = bank.copy()

    while len(joltage) > length:
        possibilities = [joltage[:i] + joltage[i + 1 :] for i in range(len(joltage))]

        max_possibility = max(int("".join(x)) for x in possibilities)
        joltage = list(str(max_possibility))

    return int("".join(joltage))


def _part1(banks: list[list[str]]) -> None:
    joltages = [_get_largest_joltage_naive(bank, 2) for bank in banks]

    print(f"day 03 - part 01: {sum(joltages)}")


def _part2(banks: list[list[str]]) -> None:
    joltages = [_get_largest_joltage_fast(bank, 12) for bank in banks]

    print(f"day 03 - part 02: {sum(joltages)}")


def day03() -> None:
    banks = _parse_puzzle_input(get_puzzle_input(3))
    _part1(banks)
    _part2(banks)
