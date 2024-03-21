from .main import part1, part2


INPUT = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""


def test_part1():
    assert part1(INPUT) == 6


def test_part2():
    assert part2(INPUT) == 2


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 175
    assert part2(input) == 213
