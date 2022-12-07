from typing import List

# https://adventofcode.com/2022/day/1


def parse_input_part1(data: str):
    # Elves are separated by a blank line
    each_elf = data.strip().split("\n\n")
    return [list(map(int, x.split())) for x in each_elf]


def part1(elf_calories: List[List[int]]) -> int:
    """Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?"""
    return max(map(sum, elf_calories))


parse_input_part2 = parse_input_part1


def part2(elf_calories: List[List[int]]) -> int:
    """Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?"""
    return sum(sorted(map(sum, elf_calories))[-3:])
