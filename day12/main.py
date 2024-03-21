from typing import Iterator


def parse_input(input: str) -> dict[str, list[str]]:
    graph = {}

    for line in input.strip().splitlines():
        program, connects = line.split(" <-> ")

        graph[program] = connects.split(", ")

    return graph


def solution(input: str) -> Iterator[set[str]]:
    graph = parse_input(input)

    visited: set[str] = set()

    def inner(key: str):
        if key in visited:
            return False

        visited.add(key)

        for k in graph[key]:
            inner(k)

    while len(graph):
        key = next(iter(graph.keys()))

        visited = set()

        inner(key)

        yield visited

        for key in visited:
            graph.pop(key)


def part1(input: str) -> int:
    return next(len(visited) for visited in solution(input) if "0" in visited)


def part2(input: str) -> int:
    return sum(1 for _ in solution(input))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
