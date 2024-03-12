from .main import part1, part2


def test_part1():
    assert part1("1024") == 31


def test_part2():
    assert part2("5") == 10


def test_input():
    input = "277678"

    assert part1(input) == 475
    assert part2(input) == 279138
