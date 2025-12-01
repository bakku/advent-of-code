import sys

from aopy_2025.day01 import day01


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: uv run aopy-2025 <day>")
        sys.exit(-1)

    day = int(sys.argv[1])

    if day == 1:
        day01()
