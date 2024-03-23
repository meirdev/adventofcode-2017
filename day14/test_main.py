from .main import part1, part2


INPUT = "flqrgnkx"


def test_part1():
    assert part1(INPUT) == 8108


def test_part2():
    assert part2(INPUT) == 1242


def test_input():
    input = "vbqugkhl"

    assert part1(input) == 8148
    assert part2(input) == 1180
