import collections
from typing import Deque, Iterator


class Queue(collections.deque[int]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0

    def append(self, value: int) -> None:
        self.counter += 1
        return super().append(value)


def parse_input(input: str) -> list[list[str]]:
    return [line.split(" ") for line in input.strip().splitlines()]


def run(
    instructions: list[list[str]],
    id: int,
    out_queue: Deque[int],
    in_queue: Deque[int] | None = None,
) -> Iterator[bool]:
    registers = collections.defaultdict(int)
    registers["p"] = id

    def get(op: str) -> int:
        if op.isalpha():
            return registers[op]
        return int(op)

    i = 0

    while i < len(instructions):
        match instructions[i]:
            case "snd", x:
                out_queue.append(get(x))
            case "set", x, y:
                registers[x] = get(y)
            case "add", x, y:
                registers[x] += get(y)
            case "mul", x, y:
                registers[x] *= get(y)
            case "mod", x, y:
                registers[x] %= get(y)
            case "rcv", x:
                if in_queue is None:
                    if get(x) != 0:
                        return
                else:
                    if len(in_queue) > 0:
                        registers[x] = in_queue.popleft()
                        yield False
                    else:
                        yield True
                        continue
            case "jgz", x, y:
                if get(x) > 0:
                    i += get(y)
                    continue
        i += 1


def part1(input: str) -> int:
    instructions = parse_input(input)

    q = Queue()

    next(run(instructions, 0, q), None)

    return q.pop()


def part2(input: str) -> int:
    instructions = parse_input(input)

    q0 = Queue()
    q1 = Queue()

    a = run(instructions, 0, q0, q1)
    b = run(instructions, 1, q1, q0)

    wait: dict[Iterator[bool], bool | None] = {a: False, b: False}

    while not all(wait.values()):
        wait = {a: next(a, None), b: next(b, None)}

        if all(wait[i] is None for i in wait):
            break

    return q1.counter


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
