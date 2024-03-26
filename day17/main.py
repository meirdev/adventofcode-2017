import collections
from typing import Deque


def parse_input(input: str) -> int:
    return int(input)


def solution(input: str, spinlock: int) -> Deque[int]:
    steps = parse_input(input)

    queue = collections.deque([0])

    for i in range(1, spinlock):
        queue.rotate(-((steps + 1) % len(queue)))
        queue.appendleft(i)

    return queue


def part1(input: str) -> int:
    queue = solution(input, 2018)

    return queue[1]


def part2(input: str) -> int:
    queue = solution(input, 5_000_000)

    queue.rotate(-queue.index(0))

    return queue[1]


def main() -> None:
    input = "363"

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
