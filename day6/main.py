import re


def parse_input(input: str) -> list[int]:
    return list(map(int, re.split(r"\s+", input.strip())))


def solution(input: str) -> tuple[int, int]:
    banks = parse_input(input)

    cycles = 0
    seen: dict[tuple[int, ...], int] = {}

    while True:
        if (key := tuple(banks)) in seen:
            return cycles, cycles - seen[key]

        seen[key] = cycles

        max_index = max(range(len(banks)), key=lambda i: banks[i])

        blocks, banks[max_index] = banks[max_index], 0

        i = max_index + 1
        while blocks:
            banks[i % len(banks)] += 1
            blocks -= 1
            i += 1

        cycles += 1


def part1(input: str) -> int:
    return solution(input)[0]


def part2(input: str) -> int:
    return solution(input)[1]


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
