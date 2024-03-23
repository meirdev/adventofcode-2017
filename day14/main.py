import functools
import itertools


def knot_hash(s: str) -> str:
    lengths = list(map(ord, s.strip())) + [17, 31, 73, 47, 23]

    elements = list(range(256))

    position = 0
    skip_size = 0

    for _ in range(64):
        for length in lengths:
            for i, rev in zip(
                range(position, position + length),
                reversed(
                    [
                        elements[j % len(elements)]
                        for j in range(position, position + length)
                    ]
                ),
            ):
                elements[i % len(elements)] = rev
            position = (position + length + skip_size) % len(elements)
            skip_size += 1

    return "".join(
        f"{i:02x}"
        for i in map(
            lambda i: functools.reduce(lambda a, b: a ^ b, i),
            itertools.batched(elements, 16),
        )
    )


def to_bits(hash: str) -> str:
    return "".join(f"{int(i, 16):04b}" for i in hash)


def get_grid(input: str) -> list[str]:
    return [to_bits(knot_hash(f"{input}-{i}")) for i in range(128)]


def part1(input: str) -> int:
    return sum(i.count("1") for i in get_grid(input))


def part2(input: str) -> int:
    disk_defragmenter = get_grid(input)

    visited = set()

    def rec(i: tuple[int, int]):
        y, x = i

        if disk_defragmenter[y][x] == "0":
            return

        if i in visited:
            return

        visited.add(i)

        for y_, x_ in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            y_ += y
            x_ += x

            if 0 <= y_ < 128 and 0 <= x_ < 128:
                rec((y_, x_))

    regions = 0

    for i in itertools.product(range(128), range(128)):
        before = len(visited)

        rec(i)

        if before < len(visited):
            regions += 1

    return regions


def main() -> None:
    input = "vbqugkhl"

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
