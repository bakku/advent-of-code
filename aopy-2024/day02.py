from pathlib import Path


def parse_puzzle_input(puzzle_input):
    reports = []

    for line in puzzle_input.split("\n"):
        levels = [int(level) for level in line.split(" ")]

        reports.append(levels)

    return reports


def is_increasing(report):
    for idx in range(len(report) - 1):
        difference = report[idx + 1] - report[idx]

        if not (1 <= difference and difference <= 3):
            return False

    return True


def is_safe(report):
    return is_increasing(report) or is_increasing(list(reversed(report)))


def shrink_report(report, idx):
    return report[:idx] + report[idx + 1 :]


def is_lax_safe(report):
    fully_safe_check = is_safe(report)

    partial_safe_checks = [
        is_safe(shrink_report(report, idx)) for idx in range(len(report))
    ]

    return fully_safe_check or any(partial_safe_checks)


def part01(puzzle_input):
    reports = parse_puzzle_input(puzzle_input)

    return sum([1 for report in reports if is_safe(report)])


def part02(puzzle_input):
    reports = parse_puzzle_input(puzzle_input)

    return sum([1 for report in reports if is_lax_safe(report)])


if __name__ == "__main__":
    puzzle_input = Path("input/day02.txt").read_text().rstrip("\n")

    print("Part 01: %d" % part01(puzzle_input))
    print("Part 02: %d" % part02(puzzle_input))
