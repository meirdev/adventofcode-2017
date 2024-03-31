import collections
import enum


class Node(enum.StrEnum):
    CLEAN = "."
    WEAKENED = "W"
    INFECTED = "#"
    FLAGGED = "F"


class Virus:
    def __init__(self, grid: list[list[Node]]) -> None:
        self._state = {
            (y, x): grid[y][x] for y in range(len(grid)) for x in range(len(grid[y]))
        }

        center = len(grid) // 2

        self._y = center
        self._x = center

        self._dir = collections.deque([(-1, 0), (0, 1), (1, 0), (0, -1)])

        self._infections = 0

    @property
    def current(self) -> Node:
        return self._state.get((self._y, self._x), Node.CLEAN)

    @property
    def infections(self) -> int:
        return self._infections

    def change(self, node: Node) -> None:
        if node == Node.INFECTED:
            self._infections += 1
        self._state[self._y, self._x] = node

    def turn_left(self) -> None:
        self._dir.rotate(1)

    def turn_right(self) -> None:
        self._dir.rotate(-1)

    def turn_reverse(self) -> None:
        self._dir.rotate(2)

    def forward(self) -> None:
        self._y += self._dir[0][0]
        self._x += self._dir[0][1]


def parse_input(input: str) -> list[list[Node]]:
    return [list(map(Node, line)) for line in input.strip().splitlines()]


def part1(input: str) -> int:
    grid = parse_input(input)

    virus = Virus(grid)

    for _ in range(10_000):
        if virus.current == Node.INFECTED:
            virus.turn_right()
            virus.change(Node.CLEAN)
        else:
            virus.turn_left()
            virus.change(Node.INFECTED)

        virus.forward()

    return virus.infections


def part2(input: str) -> int:
    grid = parse_input(input)

    virus = Virus(grid)

    for _ in range(10_000_000):
        if virus.current == Node.CLEAN:
            virus.turn_left()
            virus.change(Node.WEAKENED)
        elif virus.current == Node.WEAKENED:
            virus.change(Node.INFECTED)
        elif virus.current == Node.INFECTED:
            virus.turn_right()
            virus.change(Node.FLAGGED)
        elif virus.current == Node.FLAGGED:
            virus.turn_reverse()
            virus.change(Node.CLEAN)

        virus.forward()

    return virus.infections


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
