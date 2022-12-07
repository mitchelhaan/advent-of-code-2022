from .main import parse_input_part1, parse_input_part2, part1, part2, score_round

sample_input = """
A Y
B X
C Z
"""

sample_data1 = parse_input_part1(sample_input)


def test_parse_input_part1():
    assert len(sample_data1) == 3
    assert score_round(sample_data1[0]) == 8
    assert score_round(sample_data1[1]) == 1
    assert score_round(sample_data1[2]) == 6


def test_part1():
    assert part1(sample_data1) == 15


sample_data2 = parse_input_part2(sample_input)


def test_parse_input_part1():
    assert len(sample_data2) == 3
    assert score_round(sample_data2[0]) == 4
    assert score_round(sample_data2[1]) == 1
    assert score_round(sample_data2[2]) == 7


def test_part2():
    assert part2(sample_data2) == 12
