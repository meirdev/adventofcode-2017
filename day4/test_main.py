from .main import part1, part2


INPUT_PART_1 = """
aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa
"""

INPUT_PART_2 = """
abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio
"""


def test_part1():
    assert part1(INPUT_PART_1) == 2


def test_part2():
    assert part2(INPUT_PART_2) == 3


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 455
    assert part2(input) == 186
