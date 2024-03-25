from .main import part1, part2


INPUT = "s1,x3/4,pe/b"


def test_part1():
    assert part1(INPUT, "abcde") == "baedc"


def test_part2():
    assert part2(INPUT, "abcde") == "baedc"


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == "fnloekigdmpajchb"
    assert part2(input) == "amkjepdhifolgncb"
