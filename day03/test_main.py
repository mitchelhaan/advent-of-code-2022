from .main import (
    parse_input_part1,
    parse_input_part2,
    duplicates,
    item_priorities,
)

test_data = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

rucksacks = parse_input_part1(test_data)
rucksack_groups = parse_input_part2(test_data)


def test_parse_input_part1():
    assert len(rucksacks) == 6
    compartments = rucksacks[0]
    assert compartments[0] == "vJrwpWtwJgWr"
    assert compartments[1] == "hcsFMMfFFhFp"


def test_duplicates():
    assert duplicates(rucksacks[0]) == "p"
    assert duplicates(rucksacks[1]) == "L"
    assert duplicates(rucksacks[2]) == "P"
    assert duplicates(rucksacks[3]) == "v"
    assert duplicates(rucksacks[4]) == "t"
    assert duplicates(rucksacks[5]) == "s"


def test_priority():
    assert item_priorities("pLPvts") == [16, 38, 42, 22, 20, 19]


def test_example1():
    assert duplicates(rucksack_groups[0]) == "r"


def test_example2():
    assert duplicates(rucksack_groups[1]) == "Z"
