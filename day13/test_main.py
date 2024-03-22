from .main import part1, part2


INPUT = """
0: 3
1: 2
4: 4
6: 4
"""


def test_part1():
    assert part1(INPUT) == 24


def test_part2():
    assert part2(INPUT) == 10


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 648
    assert part2(input) == 3933124
