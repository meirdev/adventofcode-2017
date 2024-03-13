def parse_input(input: str) -> list[list[str]]:
    return [line.split(" ") for line in input.strip().splitlines()]


def part1(input: str) -> int:
    passphrases = parse_input(input)

    return sum(1 for i in passphrases if len(set(i)) == len(i))


def part2(input: str) -> int:
    passphrases = parse_input(input)

    return sum(1 for i in passphrases if len(set(map(tuple, map(sorted, i)))) == len(i))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
