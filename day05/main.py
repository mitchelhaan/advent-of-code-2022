from dataclasses import dataclass
import re
from functools import reduce
from typing import List, Iterable, Optional, Tuple


@dataclass
class Move:
    count: int
    from_stack: int
    to_stack: int


def parse_stacks(stack_defs: List[str]) -> List[List[str]]:
    # find out how many stacks we have
    stack_count = len(stack_defs.pop().split())
    stacks = [[] for _ in range(stack_count)]

    while len(stack_defs) > 0:
        s = stack_defs.pop()
        for x in range(stack_count):
            val = s[1 + x * 4]
            if len(val) > 0 and val != " ":
                stacks[x].append(val)

    return stacks


def parse_move(instruction: str) -> Move:
    match = re.match(r"move (\d+) from (\d+) to (\d+)", instruction)
    return Move(
        count=int(match.group(1)),
        from_stack=int(match.group(2)),
        to_stack=int(match.group(3)),
    )


def parse_moves(move_lines: List[str]) -> List[Move]:
    return [parse_move(x) for x in move_lines]


def parse_input_part1(data: str) -> Tuple[List[List[str]], List[Move]]:
    stack_lines = []
    move_lines = []

    for line in data.splitlines():
        if line.startswith("move"):
            move_lines.append(line)
        elif line != "":
            stack_lines.append(line)

    return (parse_stacks(stack_lines), parse_moves(move_lines))


def perform_shuffle_move(stacks: List[List[str]], move: Move):
    for _ in range(move.count):
        stacks[move.to_stack - 1].append(stacks[move.from_stack - 1].pop())


def perform_bulk_move(stacks: List[List[str]], move: Move):
    stacks[move.to_stack - 1].extend(stacks[move.from_stack - 1][-move.count :])
    del stacks[move.from_stack - 1][-move.count :]


def top_crates(stacks: List[List[str]]) -> str:
    return "".join([x[-1] for x in stacks])


parse_input_part2 = parse_input_part1


def part1(data: Tuple[List[List[str]], List[Move]]) -> str:
    """After the rearrangement procedure completes, what crate ends up on top of each stack?"""
    stacks, moves = data
    for move in moves:
        perform_shuffle_move(stacks, move)

    return top_crates(stacks)


def part2(data: Tuple[List[List[str]], List[Move]]) -> str:
    """After the rearrangement procedure completes, what crate ends up on top of each stack?"""
    stacks, moves = data
    for move in moves:
        perform_bulk_move(stacks, move)

    return top_crates(stacks)
