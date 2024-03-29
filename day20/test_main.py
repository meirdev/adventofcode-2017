from .main import part1, part2


INPUT_PART_1 = """
p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>
"""

INPUT_PART_2 = """
p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>    
p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>
"""


def test_part1():
    assert part1(INPUT_PART_1) == 0


def test_part2():
    assert part2(INPUT_PART_2) == 1


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 150
    assert part2(input) == 657
