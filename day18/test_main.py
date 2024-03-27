from .main import part1, part2


INPUT_PART_1 = """
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
"""

INPUT_PART_2 = """
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
"""


def test_part1():
    assert part1(INPUT_PART_1) == 4


def test_part2():
    assert part2(INPUT_PART_2) == 3


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 4601
    assert part2(input) == 6858
