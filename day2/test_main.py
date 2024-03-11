from .main import part1, part2


INPUT_PART_1 = """
5 1 9 5
7 5 3
2 4 6 8
"""

INPUT_PART_2 = """
5 9 2 8
9 4 7 3
3 8 6 5
"""


def test_part1():
    assert part1(INPUT_PART_1) == 18


def test_part2():
    assert part2(INPUT_PART_2) == 9


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 32020
    assert part2(input) == 236
