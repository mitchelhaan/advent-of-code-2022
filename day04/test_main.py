from .main import (
    parse_input_part1,
    range_contained,
    ranges_overlap,
)

test_data = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

assignments = parse_input_part1(test_data)
# rucksack_groups = parse_input_part2(test_data)


def test_parse_input_part1():
    assert len(assignments) == 6
    assert assignments[0] == (range(2, 5), range(6, 9))

    assert sum(range_contained(*x) for x in assignments) == 2


def test_range_inclusive():
    assert not range_contained(*assignments[0])
    assert not range_contained(*assignments[1])
    assert not range_contained(*assignments[2])
    assert range_contained(*assignments[3])
    assert range_contained(*assignments[4])
    assert not range_contained(*assignments[5])


def test_range_overlapping():
    assert not ranges_overlap(*assignments[0])
    assert not ranges_overlap(*assignments[1])
    assert ranges_overlap(*assignments[2])
    assert ranges_overlap(*assignments[3])
    assert ranges_overlap(*assignments[4])
    assert ranges_overlap(*assignments[5])
