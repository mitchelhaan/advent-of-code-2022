from .main import parse_input_part1, parse_input_part2, part1, part2

sample_input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

sample_data = parse_input_part1(sample_input)


def test_parse_input_part1():
    assert len(sample_data) == 5
    assert sum(sample_data[0]) == 6000
    assert sum(sample_data[1]) == 4000
    assert sum(sample_data[2]) == 11000
    assert sum(sample_data[3]) == 24000
    assert sum(sample_data[4]) == 10000


def test_part1():
    assert part1(sample_data) == 24000


def test_part2():
    assert part2(sample_data) == 45000
