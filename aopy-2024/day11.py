from pathlib import Path


def parse_puzzle_input(puzzle_input):
    return [stone for stone in puzzle_input.split(" ")]


def next_blink(stones_dict):
    next_stones_dict = {}

    for stone, amount in stones_dict.items():
        if stone == "0":
            next_stones_dict["1"] = next_stones_dict.get("1", 0) + amount
        elif len(stone) % 2 == 0:
            middle = int(len(stone) / 2)

            # removes leading zeros
            left = str(int(stone[0:middle]))
            right = str(int(stone[middle:]))

            next_stones_dict[left] = next_stones_dict.get(left, 0) + amount
            next_stones_dict[right] = next_stones_dict.get(right, 0) + amount
        else:
            next_stone = str(int(stone) * 2024)

            next_stones_dict[next_stone] = next_stones_dict.get(next_stone, 0) + amount

    return next_stones_dict


def blink(stones_dict, n):
    for i in range(n):
        stones_dict = next_blink(stones_dict)

    return stones_dict


def part01(puzzle_input):
    stones = parse_puzzle_input(puzzle_input)
    stones_dict = {stone: stones.count(stone) for stone in set(stones)}

    return sum([amount for _, amount in blink(stones_dict, n=25).items()])


def part02(puzzle_input):
    stones = parse_puzzle_input(puzzle_input)
    stones_dict = {stone: stones.count(stone) for stone in set(stones)}

    return sum([amount for _, amount in blink(stones_dict, n=75).items()])


if __name__ == "__main__":
    puzzle_input = Path("input/day11.txt").read_text().rstrip("\n")

    print("Part 01: %d" % part01(puzzle_input))
    print("Part 02: %d" % part02(puzzle_input))
