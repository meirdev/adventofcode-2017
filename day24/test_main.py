from .main import part1, part2


INPUT = """
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
"""


def test_part1():
    assert part1(INPUT) == 31


def test_part2():
    assert part2(INPUT) == 19


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 2006
    assert part2(input) == 1994
