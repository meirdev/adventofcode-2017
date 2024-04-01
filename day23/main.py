import collections
from typing import DefaultDict, Iterator, NamedTuple


class Process(NamedTuple):
    pc: int
    instruction: str
    registers: DefaultDict[str, int]


def parse_input(input: str) -> list[list[str]]:
    return [line.split(" ") for line in input.strip().splitlines()]


def run(input: str, debug: bool = False) -> Iterator[Process]:
    instructions = parse_input(input)

    registers = collections.defaultdict(int)

    if debug:
        registers["a"] = 1

    def get(op: str) -> int:
        if op.isalpha():
            return registers[op]
        return int(op)

    i = 0

    while i < len(instructions):
        yield Process(i, instructions[i][0], registers)

        match instructions[i]:
            case "set", x, y:
                registers[x] = get(y)
            case "sub", x, y:
                registers[x] -= get(y)
            case "mul", x, y:
                registers[x] *= get(y)
            case "jnz", x, y:
                if get(x) != 0:
                    i += get(y)
                    continue
        i += 1


def part1(input: str) -> int:
    return sum(1 for _, instruction, _ in run(input) if instruction == "mul")


def part2(input: str) -> int:
    for pc, _, registers in run(input, debug=True):
        if pc == 11:
            return sum(
                1
                for b in range(registers["b"], registers["c"] + 1, 17)
                if any(b % d == 0 for d in range(2, int(b**0.5)))
            )

    return -1


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
