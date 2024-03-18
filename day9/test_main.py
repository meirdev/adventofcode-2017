from .main import part1, part2


def test_part1():
    for input, expected in (
        ("{}", 1),
        ("{{{}}}", 6),
        ("{{},{}}", 5),
        ("{{{},{},{{}}}}", 16),
        ("{<a>,<a>,<a>,<a>}", 1),
        ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
        ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
        ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3),
    ):
        assert part1(input) == expected


def test_part2():
    for input, expected in (
        ("<>", 0),
        ("<random characters>", 17),
        ("<<<<>", 3),
        ("<{!>}>", 2),
        ("<!!>", 0),
        ("<!!!>>", 0),
        ("<{o\"i!a,<{i<a>", 10),
    ):
        assert part2(input) == expected


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 17537
    assert part2(input) == 7539
