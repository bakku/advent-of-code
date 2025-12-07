import math
import re
from itertools import zip_longest
from typing import TypedDict

from aopy_2025.utils import get_puzzle_input


class Problem(TypedDict):
    numbers: list[int]
    operation: str


def _parse_puzzle_input1(input_: str) -> list[Problem]:
    raw_tokens: list[list[str]] = [
        re.split(r"\s+", line.strip()) for line in input_.splitlines()
    ]

    raw_numbers: list[list[str]] = [list(col) for col in zip(*raw_tokens[:-1])]
    parsed_numbers = [list(map(int, problem)) for problem in raw_numbers]

    raw_full_problems = list(zip(parsed_numbers, raw_tokens[-1]))

    return [
        {"numbers": numbers, "operation": operation}
        for [numbers, operation] in raw_full_problems
    ]


def _parse_puzzle_input2(input_: str) -> list[Problem]:
    matrix = [list(line) for line in input_.splitlines()]

    transposed_input = list(zip_longest(*matrix, fillvalue=" "))
    cleaned_transposed_input = list(
        map(lambda x: list(filter(lambda y: y != " ", x)), transposed_input)
    )

    raw_problems: list[list[list[str]]] = []
    curr_problem: list[list[str]] = []

    for row in cleaned_transposed_input:
        if row:
            curr_problem.append(row)
        else:
            raw_problems.append(curr_problem)
            curr_problem = []

    raw_problems.append(curr_problem)

    problems: list[Problem] = []

    for problem in raw_problems:
        operation = problem[0][-1]

        problem[0].remove(operation)

        numbers = [int("".join(number)) for number in problem]

        problems.append({"numbers": numbers, "operation": operation})

    return problems


def _calc_problem(problem: Problem) -> int:
    if problem["operation"] == "*":
        return math.prod(problem["numbers"])

    return sum(problem["numbers"])


def _part1(problems: list[Problem]) -> None:
    print(f"day 06 - part 1: {sum(_calc_problem(problem) for problem in problems)}")


def _part2(problems: list[Problem]) -> None:
    print(f"day 06 - part 2: {sum(_calc_problem(problem) for problem in problems)}")


def day06() -> None:
    _part1(_parse_puzzle_input1(get_puzzle_input(6)))
    _part2(_parse_puzzle_input2(get_puzzle_input(6)))
