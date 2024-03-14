from typing import Callable


def parse_input(input: str) -> list[int]:
    return list(map(int, input.strip().splitlines()))


def solution(input: str, jump: Callable[[int], int]) -> int:
    instructions = parse_input(input)

    i = 0
    steps = 0

    while i < len(instructions):
        temp, i = i, i + instructions[i]
        instructions[temp] += jump(instructions[temp])
        steps += 1

    return steps


def part1(input: str) -> int:
    return solution(input, lambda _: 1)


def part2(input: str) -> int:
    return solution(input, lambda x: -1 if x >= 3 else 1)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
