import re

FACTORS = {
    "A": 16807,
    "B": 48271,
}


def parse_input(input: str) -> dict[str, int]:
    return {i: int(s) for i, s in re.findall(r"Generator (\w).*?(\d+)", input)}


def solution(input: str, pairs: int, multiples: dict[str, int]) -> int:
    generators = parse_input(input)

    def f(i):
        while True:
            generators[i] = generators[i] * FACTORS[i] % 2147483647
            if generators[i] % multiples[i] == 0:
                yield generators[i]

    return sum(bin(next(f("A")))[-16:] == bin(next(f("B")))[-16:] for _ in range(pairs))


def part1(input: str) -> int:
    return solution(input, 40_000_000, {"A": 1, "B": 1})


def part2(input: str) -> int:
    return solution(input, 5_000_000, {"A": 4, "B": 8})


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
