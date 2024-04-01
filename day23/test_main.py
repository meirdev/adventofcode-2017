from .main import part1, part2


def test_part1():
    pass


def test_part2():
    pass


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 4225
    assert part2(input) == 905
