from .main import part1, part2


INPUT = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""


def test_part1():
    assert part1(INPUT) == 1


def test_part2():
    assert part2(INPUT) == 10


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 4448
    assert part2(input) == 6582
