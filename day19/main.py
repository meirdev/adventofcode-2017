import string


DIRECTION = {
    "u": (-1, 0),
    "d": (1, 0),
    "r": (0, 1),
    "l": (0, -1),
}


def parse_input(input: str) -> dict[tuple[int, int], str]:
    return {
        (y, x): col
        for y, row in enumerate(input.strip("\n\r").splitlines())
        for x, col in enumerate(row)
        if col != " "
    }


def solution(input: str) -> tuple[str, int]:
    map = parse_input(input)

    visited: set[tuple[int, int]] = set()

    letters: list[str] = []

    direction = "d"
    position = next((y, x) for y, x in map if y == 0)

    steps = 0

    while len(visited) != len(map):
        steps += 1

        visited.add(position)

        if map[position] in string.ascii_uppercase:
            letters.append(map[position])

        if map[position] == "+":
            for direction, dir in DIRECTION.items():
                next_position = (position[0] + dir[0], position[1] + dir[1])
                if next_position in map and next_position not in visited:
                    position = next_position
                    break
        else:
            position = (
                position[0] + DIRECTION[direction][0],
                position[1] + DIRECTION[direction][1],
            )

    return "".join(letters), steps


def part1(input: str) -> str:
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
