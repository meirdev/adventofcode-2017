import collections
import re
from typing import DefaultDict, Iterator, NamedTuple

import more_itertools


class Op(NamedTuple):
    register: str
    op: str
    value: int


class Condition(NamedTuple):
    register: str
    cmp: str
    value: int


class Instruction(NamedTuple):
    op: Op
    condition: Condition


def parse_input(input: str) -> list[Instruction]:
    instructions = []

    for line in input.strip().splitlines():
        match = re.match(
            r"(?P<reg_a>\w+) (?P<op>\w+) (?P<val_a>-?\d+) if (?P<reg_b>\w+) (?P<cmp>.*?) (?P<val_b>-?\d+)",
            line,
        )

        if match is None:
            raise ValueError(line)

        op = Op(match.group("reg_a"), match.group("op"), int(match.group("val_a")))
        condition = Condition(
            match.group("reg_b"), match.group("cmp"), int(match.group("val_b"))
        )

        instructions.append(Instruction(op, condition))

    return instructions


def solution(input: str) -> Iterator[DefaultDict[str, int]]:
    instructions = parse_input(input)

    registers: DefaultDict[str, int] = collections.defaultdict(int)

    for op, condition in instructions:
        if eval(f"{registers[condition.register]} {condition.cmp} {condition.value}"):
            if op.op == "inc":
                registers[op.register] += op.value
            else:
                registers[op.register] -= op.value
            yield registers


def part1(input: str) -> int:
    instructions = solution(input)

    return max(more_itertools.last(instructions).values())


def part2(input: str) -> int:
    instructions = solution(input)

    return max(max(i.values()) for i in instructions)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
