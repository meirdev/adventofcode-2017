import collections
from typing import NamedTuple

PROGRAMS = "abcdefghijklmnop"


class Spin(NamedTuple):
    x: int


class Exchange(NamedTuple):
    a: int
    b: int


class Partner(NamedTuple):
    a: str
    b: str


def parse_input(input: str) -> list[NamedTuple]:
    moves: list[NamedTuple] = []

    for line in input.strip().split(","):
        match line[0]:
            case "s":
                moves.append(Spin(int(line[1:])))
            case "x":
                a, b = line[1:].split("/")
                moves.append(Exchange(int(a), int(b)))
            case "p":
                a, b = line[1:].split("/")
                moves.append(Partner(a, b))

    return moves


def solution(input: str, times: int, programs: str) -> str:
    moves = parse_input(input)

    queue = collections.deque(programs)

    seen: dict[str, int] = {}

    for i in range(times):
        for move in moves:
            if isinstance(move, Spin):
                queue.rotate(move.x)
            elif isinstance(move, Exchange):
                queue[move.a], queue[move.b] = queue[move.b], queue[move.a]
            elif isinstance(move, Partner):
                a, b = queue.index(move.a), queue.index(move.b)
                queue[a], queue[b] = queue[b], queue[a]

        result = "".join(queue)

        if result in seen:
            index = times % (i - seen[result]) - 1
            if index < 0:
                index = 0
            return next(j for j in seen if seen[j] == index)
        else:
            seen[result] = i

    return result


def part1(input: str, programs: str = PROGRAMS) -> str:
    return solution(input, 1, programs)


def part2(input: str, programs: str = PROGRAMS) -> str:
    return solution(input, 1_000_000_000, programs)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
