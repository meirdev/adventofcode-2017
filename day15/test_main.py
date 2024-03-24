from .main import part1, part2


INPUT = """
Generator A starts with 65
Generator B starts with 8921
"""


def test_part1():
    assert part1(INPUT) == 588


def test_part2():
    assert part2(INPUT) == 309


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 600
    assert part2(input) == 313
