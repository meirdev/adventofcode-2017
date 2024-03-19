import functools
import itertools


def parse_input(input: str) -> str:
    return input.strip()


def knot(lengths: list[int], rounds: int, numbers: int = 256) -> list[int]:
    elements = list(range(numbers))

    position = 0
    skip_size = 0

    for _ in range(rounds):
        for length in lengths:
            for i, rev in zip(
                range(position, position + length),
                reversed(
                    [
                        elements[j % len(elements)]
                        for j in range(position, position + length)
                    ]
                ),
            ):
                elements[i % len(elements)] = rev
            position = (position + length + skip_size) % len(elements)
            skip_size += 1

    return elements


def part1(input: str, numbers: int = 256) -> int:
    lengths = parse_input(input)

    elements = knot(list(map(int, lengths.split(","))), 1, numbers)

    return elements[0] * elements[1]


def part2(input: str) -> str:
    lengths = parse_input(input)

    elements = knot(list(map(ord, lengths)) + [17, 31, 73, 47, 23], 64)

    return "".join(
        f"{i:02x}"
        for i in map(
            lambda i: functools.reduce(lambda a, b: a ^ b, i),
            itertools.batched(elements, 16),
        )
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
