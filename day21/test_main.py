from .main import part1, part2


INPUT = """
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
"""


def test_part1():
    assert part1(INPUT, 2) == 12


def test_part2():
    pass


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 203
    assert part2(input) == 3342470
