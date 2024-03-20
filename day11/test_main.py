from .main import part1, part2


def test_part1():
    for input, expected in (
        ("ne,ne,ne", 3),
        ("ne,ne,sw,sw", 0),
        ("ne,ne,s,s", 2),
        ("se,sw,se,sw,sw", 3),
    ):
        assert part1(input) == expected


def test_part2():
    assert part2("ne,ne,sw,sw") == 2


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 812
    assert part2(input) == 1603
