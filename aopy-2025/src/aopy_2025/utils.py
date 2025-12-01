from pathlib import Path


def get_puzzle_input(day: int) -> str:
    path = (
        Path(__file__).parent.parent.parent / "inputs" / f"day{str(day).zfill(2)}.txt"
    )

    return path.read_text()
