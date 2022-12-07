import re
from functools import reduce
from typing import List, Iterable


def chunk(items: List, count: int) -> Iterable[List]:
    for x in range(0, len(items), count):
        yield items[x : x + count]


def compartment_contents(rucksack: str) -> List[str]:
    return list(chunk(rucksack, int(len(rucksack) / 2)))


def duplicates(contents: List[str]) -> str:
    # Find the intersection (common items) of each rucksack/compartment contents
    return "".join(reduce(set.intersection, map(set, contents)))


def item_priority(item: str) -> int:
    if re.match("[a-z]", item):
        return ord(item) - ord("a") + 1
    if re.match("[A-Z]", item):
        return ord(item) - ord("A") + 27


def item_priorities(items: str):
    return [item_priority(x) for x in items]


def parse_input_part1(data: str) -> List[List[str]]:
    return [compartment_contents(r) for r in data.strip().splitlines()]


def parse_input_part2(data: str) -> List[List[str]]:
    return list(chunk(data.strip().splitlines(), 3))


def part1(rucksacks: List[List[str]]) -> int:
    """Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?"""
    dupes = [duplicates(r) for r in rucksacks]
    return sum(item_priorities(dupes))


def part2(rucksack_groups: List[List[str]]) -> int:
    """Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?"""
    badges = [duplicates(g) for g in rucksack_groups]
    return sum(item_priorities(badges))
