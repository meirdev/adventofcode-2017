import itertools


def parse_input(input: str) -> dict[int, int]:
    return dict(
        tuple(map(int, line.split(": "))) for line in input.strip().splitlines()  # type: ignore
    )


def scanner(range: int, time: int) -> int:
    offset = time % ((range - 1) * 2)

    return 2 * (range - 1) - offset if offset > range - 1 else offset


def part1(input: str) -> int:
    layers = parse_input(input)

    return sum(
        depth * range for depth, range in layers.items() if scanner(range, depth) == 0
    )


def part2(input: str) -> int:
    layers = parse_input(input)

    return next(
        wait
        for wait in itertools.count()
        if not any(scanner(range, wait + depth) == 0 for depth, range in layers.items())
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
