from pathlib import Path


def parse_puzzle_input(puzzle_input):
    return [int(num) for num in list(puzzle_input)]


def digits_to_blocks(digits):
    blocks = []
    curr_file_id = 0

    for i in range(len(digits)):
        if i % 2 == 0:
            next_blocks = [curr_file_id] * digits[i]
            curr_file_id += 1
        else:
            next_blocks = ["."] * digits[i]

        blocks += next_blocks

    return blocks


def is_compact(blocks):
    free_space_visited = False

    for block in blocks:
        if block == ".":
            free_space_visited = True
        else:
            if free_space_visited:
                return False

    return True


def compact_single(blocks):
    next_blocks = blocks.copy()

    first_free_space_idx = 0
    last_file_block_idx = 0

    for i in range(len(blocks)):
        if blocks[i] == ".":
            first_free_space_idx = i
            break

    for i in range(len(blocks) - 1, -1, -1):
        if blocks[i] != ".":
            last_file_block_idx = i
            break

    next_blocks[first_free_space_idx] = next_blocks[last_file_block_idx]
    next_blocks[last_file_block_idx] = "."

    return next_blocks


def compact(blocks):
    while not is_compact(blocks):
        blocks = compact_single(blocks)

    return blocks


def checksum(blocks):
    sum_ = 0

    for i in range(len(blocks)):
        if blocks[i] != ".":
            sum_ = sum_ + (int(blocks[i]) * i)

    return sum_


def part01(puzzle_input):
    digits = parse_puzzle_input(puzzle_input)

    blocks = digits_to_blocks(digits)

    compact_blocks = compact(blocks)

    return checksum(compact_blocks)


def part02(puzzle_input):
    equations = parse_puzzle_input(puzzle_input)

    return 1


if __name__ == "__main__":
    puzzle_input = Path("input/day09.txt").read_text().rstrip("\n")

    print("Part 01: %d" % part01(puzzle_input))
    print("Part 02: %d" % part02(puzzle_input))
