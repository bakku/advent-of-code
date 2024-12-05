from pathlib import Path
import math


def parse_puzzle_input(puzzle_input):
    rule_definitions_raw, pages_to_print_raw = puzzle_input.split("\n\n")

    rule_definitions = [r.split("|") for r in rule_definitions_raw.split("\n")]
    pages_to_print = [p.split(",") for p in pages_to_print_raw.split("\n")]

    return rule_definitions, pages_to_print


def build_rules_map(rule_definitions):
    rules_map = {}

    for before, after in rule_definitions:
        if before not in rules_map:
            rules_map[before] = {"before": [], "after": []}

        rules_map[before]["after"].append(after)

        if after not in rules_map:
            rules_map[after] = {"before": [], "after": []}

        rules_map[after]["before"].append(before)

    return rules_map


def is_page_valid(pages_before, pages_after, value, rules_map):
    for page_before in pages_before:
        if page_before in rules_map[value]["after"]:
            return False

    for page_after in pages_after:
        if page_after in rules_map[value]["before"]:
            return False

    return True


def is_page_set_valid(page_set, rules_map):
    for i in range(len(page_set)):
        before, after = page_set[:i], page_set[i + 1 :]

        if not is_page_valid(
            pages_before=before,
            pages_after=after,
            value=page_set[i],
            rules_map=rules_map,
        ):
            return False

    return True


def part01(puzzle_input):
    rule_definitions, pages_to_print = parse_puzzle_input(puzzle_input)

    rules_map = build_rules_map(rule_definitions)

    valid_page_sets = [
        page_set
        for page_set in pages_to_print
        if is_page_set_valid(page_set, rules_map)
    ]

    return sum(
        [int(page_set[math.floor(len(page_set) / 2)]) for page_set in valid_page_sets]
    )


def find_faulty_index(page_set, rules_map, except_):
    for i in range(len(page_set)):
        before, after = page_set[:i], page_set[i + 1 :]

        if (
            not is_page_valid(
                pages_before=before,
                pages_after=after,
                value=page_set[i],
                rules_map=rules_map,
            )
            and i not in except_
        ):
            return i


def find_valid_page_set(page_set, value, rules_map):
    for i in range(len(page_set) + 1):
        page_set_copy = page_set.copy()

        page_set_copy.insert(i, value)

        before, after = page_set_copy[:i], page_set_copy[i + 1 :]

        if is_page_valid(
            pages_before=before,
            pages_after=after,
            value=page_set_copy[i],
            rules_map=rules_map,
        ):
            return page_set_copy


def fix_page_sets(invalid_page_sets, rules_map):
    valid_page_sets = []

    for invalid_page_set in invalid_page_sets:
        page_set = invalid_page_set.copy()
        exceptions = []

        while not is_page_set_valid(page_set, rules_map):
            faulty_index = find_faulty_index(page_set, rules_map, except_=exceptions)

            page_set_without_faulty = (
                page_set[:faulty_index] + page_set[faulty_index + 1 :]
            )

            potential_next_page_set = find_valid_page_set(
                page_set_without_faulty, page_set[faulty_index], rules_map
            )

            if potential_next_page_set is None:
                # No position found for the current faulty_index, so skip it for now.
                exceptions.append(faulty_index)
            else:
                exceptions = []
                page_set = potential_next_page_set

        valid_page_sets.append(page_set)

    return valid_page_sets


def part02(puzzle_input):
    rule_definitions, pages_to_print = parse_puzzle_input(puzzle_input)

    rules_map = build_rules_map(rule_definitions)

    invalid_page_sets = [
        page_set
        for page_set in pages_to_print
        if not is_page_set_valid(page_set, rules_map)
    ]

    valid_page_sets = fix_page_sets(invalid_page_sets, rules_map)

    return sum(
        [int(page_set[math.floor(len(page_set) / 2)]) for page_set in valid_page_sets]
    )


if __name__ == "__main__":
    puzzle_input = Path("input/day05.txt").read_text().rstrip("\n")

    print("Part 01: %d" % part01(puzzle_input))
    print("Part 02: %d" % part02(puzzle_input))
