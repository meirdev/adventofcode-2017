import itertools
from typing import TypeAlias

Grid: TypeAlias = tuple[str, ...]

START: Grid = (".#.", "..#", "###")


def parse_input(input: str) -> dict[Grid, Grid]:
    rules = {}

    for line in input.strip().splitlines():
        from_, to = line.split(" => ")

        rules[tuple(from_.split("/"))] = tuple(to.split("/"))

    return rules


def rotate(grid: Grid) -> Grid:
    return tuple("".join(row[::-1]) for row in zip(*grid))


def flip(grid: Grid) -> Grid:
    return grid[::-1]


def get_orientations(grid: Grid) -> list[Grid]:
    grids = [grid]

    for _ in range(3):
        grids.append(rotate(grids[-1]))

    grids.append(flip(grid))

    for _ in range(3):
        grids.append(rotate(grids[-1]))

    return grids


def get_square(grid: Grid, x: int, y: int, size: int) -> Grid:
    return tuple(
        "".join(grid[yi][xi] for xi in range(x * size, x * size + size))
        for yi in range(y * size, y * size + size)
    )


def solution(input: str, iterations) -> int:
    rules = parse_input(input)

    all_rules = dict(
        (rule, to) for from_, to in rules.items() for rule in get_orientations(from_)
    )

    pattern: Grid = START

    for _ in range(iterations):
        size = 2 if len(pattern) % 2 == 0 else 3

        new_pattern: list[str] = []

        for x, y in itertools.product(
            range(len(pattern) // size), range(len(pattern) // size)
        ):
            square = all_rules[get_square(pattern, x, y, size)]

            for n, line in enumerate(square):
                if y * len(square) + n >= len(new_pattern):
                    new_pattern.append("")
                new_pattern[y * len(square) + n] += line

        pattern = tuple(new_pattern)

    return sum(row.count("#") for row in pattern)


def part1(input: str, iterations: int = 5) -> int:
    return solution(input, iterations)


def part2(input: str) -> int:
    return solution(input, 18)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
