from typing import List, Tuple


def range_contained(range1: range, range2: range) -> bool:
    """True if one range is fully contained within the other"""
    return all(x in range2 for x in range1) or all(x in range1 for x in range2)


def ranges_overlap(range1: range, range2: range) -> bool:
    """True if there is any overlap between the ranges"""
    return any(x in range2 for x in range1) or any(x in range1 for x in range2)


def parse_range(range_str: str) -> range:
    start, end = map(int, range_str.split("-"))
    return range(start, end + 1)


def parse_input_part1(data: str) -> List[Tuple]:
    ranges = []
    for elf1, elf2 in (x.split(",") for x in data.strip().splitlines()):
        ranges.append((parse_range(elf1), parse_range(elf2)))
    return ranges


parse_input_part2 = parse_input_part1


def part1(assignments: List[Tuple[range]]) -> int:
    """In how many assignment pairs does one range fully contain the other?"""
    return sum(range_contained(*x) for x in assignments)


def part2(assignments: List[Tuple[range]]) -> int:
    """In how many assignment pairs do the ranges overlap?"""
    return sum(ranges_overlap(*x) for x in assignments)
