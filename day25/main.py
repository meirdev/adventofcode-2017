import collections
import enum
import re
from typing import DefaultDict, NamedTuple


class Move(enum.IntEnum):
    LEFT = -1
    RIGHT = 1


class State(NamedTuple):
    write: int
    move: Move
    next: str


class Blueprints(NamedTuple):
    begin: str
    diagnostic: int
    states: dict[str, dict[int, State]]


def parse_input(input: str) -> Blueprints:
    begin = re.search(r"Begin in state (\w).", input)
    if begin is None:
        raise ValueError("begin")

    diagnostic = re.search(r"Perform a diagnostic checksum after (\d+) steps.", input)
    if diagnostic is None:
        raise ValueError("diagnostic")

    states: dict[str, dict[int, State]] = {}

    for key, value in re.findall(r"In state (\w):(.*?)\n\n", input + "\n\n", re.DOTALL):
        states[key] = {}

        for i, (write, move, next) in enumerate(
            zip(
                re.findall(r"Write the value (\d+)", value),
                re.findall(r"Move one slot to the (\w+)", value),
                re.findall(r"Continue with state (\w)", value),
            )
        ):
            states[key][i] = State(
                int(write), Move.RIGHT if move == "right" else Move.LEFT, next
            )

    return Blueprints(begin.group(1), int(diagnostic.group(1)), states)


def part1(input: str) -> int:
    blueprints = parse_input(input)

    tape: DefaultDict[int, int] = collections.defaultdict(int)

    current, diagnostic, states, cursor = *blueprints, 0

    for _ in range(diagnostic):
        s = states[current][tape[cursor]]
        tape[cursor] = s.write
        cursor += s.move
        current = s.next

    return list(tape.values()).count(1)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))


if __name__ == "__main__":
    main()
