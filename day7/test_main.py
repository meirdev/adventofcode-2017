from .main import part1, part2


INPUT = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""


def test_part1():
    assert part1(INPUT) == "tknk"


def test_part2():
    assert part2(INPUT) == 60


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == "ahnofa"
    assert part2(input) == 802
