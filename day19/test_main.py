from .main import part1, part2


INPUT = """
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
"""


def test_part1():
    assert part1(INPUT) == "ABCDEF"


def test_part2():
    assert part2(INPUT) == 38


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == "AYRPVMEGQ"
    assert part2(input) == 16408
