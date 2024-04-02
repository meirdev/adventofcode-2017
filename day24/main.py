import collections
import functools
from typing import DefaultDict, NamedTuple


class Component(NamedTuple):
    port1: int
    port2: int


def parse_input(input: str) -> list[Component]:
    return [
        Component(*map(int, line.split("/"))) for line in input.strip().splitlines()
    ]


@functools.cache
def solution(input: str) -> list[tuple[int, int]]:
    components = parse_input(input)

    graph: DefaultDict[int, set[int]] = collections.defaultdict(set)

    for i, component in enumerate(components, start=1):
        graph[component.port1].add(i)
        graph[component.port2].add(-i)

    def bridge_strength(s):
        return sum(sum(components[abs(i) - 1]) for i in s)

    bridges: list[tuple[int, int]] = []

    def rec(bridge: list[int]) -> tuple[int, int]:
        component = components[abs(bridge[-1]) - 1]

        port = component.port1 if bridge[-1] < 0 else component.port2

        bridges.extend(
            rec(bridge + [i])
            for i in graph[port]
            if i not in bridge and -i not in bridge
        )

        return len(bridge), bridge_strength(bridge)

    bridges.extend(rec([i]) for i in graph[0])

    return bridges


def part1(input: str) -> int:
    return max(solution(input), key=lambda i: i[1])[1]


def part2(input: str) -> int:
    return max(solution(input), key=lambda i: i[0])[1]


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
