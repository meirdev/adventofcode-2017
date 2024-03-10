from .main import part1, part2


def test_part1():
    for input, expected in (
        ("1122", 3),
        ("1111", 4),
        ("1234", 0),
        ("91212129", 9),
    ):
        assert part1(input) == expected


def test_part2():
    for input, expected in (
        ("1212", 6),
        ("1221", 0),
        ("123425", 4),
        ("123123", 12),
        ("12131415", 4),
    ):
        assert part2(input) == expected


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 1251
    assert part2(input) == 1244
