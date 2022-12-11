from .main import parse_input_part1, parse_input_part2, part1, part2

sample_input = """
a
b
c
d
"""

sample_data1 = parse_input_part1(sample_input)
sample_data2 = parse_input_part2(sample_input)


def test_parse_input_part1():
    assert len(sample_data1) == 4


def test_parse_input_part2():
    assert len(sample_data2) == 4


def test_part1():
    assert part1(sample_data1) == 4


def test_part2():
    assert part2(sample_data2) == 4
