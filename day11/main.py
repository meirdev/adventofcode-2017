from typing import Iterator

import more_itertools


def parse_input(input: str) -> list[str]:
    return input.strip().split(",")


def solution(input: str) -> Iterator[int]:
    steps = parse_input(input)

    x, y = 0, 0

    for step in steps:
        match step:
            case "n":
                y -= 2
            case "ne":
                y -= 1
                x += 1
            case "nw":
                y -= 1
                x -= 1
            case "s":
                y += 2
            case "se":
                y += 1
                x += 1
            case "sw":
                y += 1
                x -= 1

        yield max(abs(x), abs(y) // 2 + abs(y) % 2)


def part1(input: str) -> int:
    return more_itertools.last(solution(input))


def part2(input: str) -> int:
    return max(solution(input))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
