import itertools
import re


def parse_input(input: str) -> list[list[int]]:
    return [
        list(map(int, re.split(r"\s+", line))) for line in input.strip().splitlines()
    ]


def part1(input: str) -> int:
    spreadsheet = parse_input(input)

    return sum(max(nums) - min(nums) for nums in spreadsheet)


def part2(input: str) -> int:
    spreadsheet = parse_input(input)

    return sum(
        next(
            n1 // n2
            for n1, n2 in itertools.product(nums, repeat=2)
            if n1 > n2 and n1 % n2 == 0
        )
        for nums in spreadsheet
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
