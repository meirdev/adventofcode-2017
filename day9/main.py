def parse_input(input: str) -> str:
    return input.strip()


def solution(input: str) -> tuple[int, int]:
    puzzle = parse_input(input)

    garbage, ignore = False, False

    total_score, depth = 0, 0

    garbage_chars = 0

    for i in range(len(puzzle)):
        if ignore:
            ignore = False
        elif puzzle[i] == "!":
            ignore = True
        elif garbage:
            if puzzle[i] == ">":
                garbage = False
            else:
                garbage_chars += 1
        elif puzzle[i] == "<":
            garbage = True
        elif puzzle[i] == "{":
            depth += 1
        elif puzzle[i] == "}":
            total_score += depth
            depth -= 1

    return total_score, garbage_chars


def part1(input: str) -> int:
    return solution(input)[0]


def part2(input: str) -> int:
    return solution(input)[1]


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
