from .main import part1, part2


INPUT = "3"


def test_part1():
    assert part1(INPUT) == 638


def test_input():
    input = "363"

    assert part1(input) == 136
    assert part2(input) == 1080289
