import sys

from aopy_2025.day01 import day01
from aopy_2025.day02 import day02
from aopy_2025.day03 import day03
from aopy_2025.day04 import day04
from aopy_2025.day05 import day05
from aopy_2025.day06 import day06
from aopy_2025.day07 import day07

DAYS = {
    1: day01,
    2: day02,
    3: day03,
    4: day04,
    5: day05,
    6: day06,
    7: day07,
}


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: uv run aopy-2025 <day>")
        sys.exit(-1)

    day = int(sys.argv[1])

    if day not in DAYS:
        print(f"day {day} was not implemented yet")
        sys.exit(-1)

    DAYS[day]()
