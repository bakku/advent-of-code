import sys

from aopy_2025.day01 import day01
from aopy_2025.day02 import day02
from aopy_2025.day03 import day03

DAYS = {
    1: day01,
    2: day02,
    3: day03,
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
