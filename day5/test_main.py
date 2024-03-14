from .main import part1, part2


INPUT = """
0
3
0
1
-3
"""


def test_part1():
    assert part1(INPUT) == 5


def test_part2():
    assert part2(INPUT) == 10


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 381680
    assert part2(input) == 29717847
