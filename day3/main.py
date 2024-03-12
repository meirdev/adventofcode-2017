import collections
import itertools
import math
from typing import DefaultDict


def parse_input(input: str) -> int:
    return int(input)


def part1(input: str) -> int:
    square = parse_input(input)

    size = math.ceil(square**0.5)
    center = math.ceil((size - 1) / 2)

    return max(0, center - 1 + abs(center - square % size))


def part2(input: str) -> int:
    square = parse_input(input)

    matrix: DefaultDict[tuple[int, int], int] = collections.defaultdict(int)

    x, y = 0, 0
    matrix[x, y] = 1

    moves = (0, 1, 0), (0, 0, -1), (1, -1, 0), (1, 0, 1)

    for i in itertools.count(1, 2):
        for i_, x_, y_ in moves:
            for _ in range(i + i_):
                x += x_
                y += y_
                matrix[x, y] = sum(
                    matrix[k]
                    for k in itertools.product(range(x - 1, x + 2), range(y - 1, y + 2))
                )
                if matrix[x, y] > square:
                    return matrix[x, y]

    return -1


def main() -> None:
    input = "277678"

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
