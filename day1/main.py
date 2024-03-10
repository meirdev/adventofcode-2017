import itertools


def parse_input(input: str) -> str:
    return input.strip()


def part1(input: str) -> int:
    captcha = parse_input(input)

    return sum(int(a) for a, b in itertools.pairwise(captcha + captcha[0]) if a == b)


def part2(input: str) -> int:
    captcha = parse_input(input)

    return sum(
        int(captcha[i])
        for i in range(len(captcha))
        if captcha[i] == captcha[(i + len(captcha) // 2) % len(captcha)]
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
