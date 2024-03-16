import collections
import functools
import re
from typing import NamedTuple


class Program(NamedTuple):
    weight: int
    above: set[str]


def parse_input(input: str) -> dict[str, Program]:
    towers = {}

    for line in input.strip().splitlines():
        if "->" in line:
            program, above = line.split(" -> ")
        else:
            program, above = line, ""

        match = re.match(r"(\w+) \((\d+)\)", program)

        if match is None:
            raise ValueError(line)

        name, weight = match.group(1), int(match.group(2))

        towers[name] = Program(weight, set(above.split(", ")) if above else set())

    return towers


def get_bottom_program(towers: dict[str, Program]) -> str:
    return functools.reduce(
        lambda a, b: a - b.above, towers.values(), set(towers)
    ).pop()


def part1(input: str) -> str:
    towers = parse_input(input)

    return get_bottom_program(towers)


def part2(input: str) -> int:
    towers = parse_input(input)

    bottom_program = get_bottom_program(towers)

    def rec(k):
        if len(towers[k].above) == 0:
            return towers[k].weight

        above = [rec(i) for i in towers[k].above]

        if len(set(above)) == 1:
            return towers[k].weight + sum(above)

        current = [towers[i].weight for i in towers[k].above]

        nums = collections.Counter(above)

        min_index = above.index(min(nums, key=nums.get))
        max_index = above.index(max(nums, key=nums.get))

        raise ValueError(current[min_index] - abs(above[min_index] - above[max_index]))

    try:
        rec(bottom_program)
    except ValueError as error:
        return error.args[0]

    return -1


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
