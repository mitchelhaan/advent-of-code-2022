from .main import (
    parse_input_part1,
    perform_shuffle_move,
    perform_bulk_move,
    top_crates,
)

test_data = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def test_parse_input_part1():
    stacks, moves = parse_input_part1(test_data)

    assert len(stacks) == 3
    assert len(moves) == 4
    assert len(stacks[0]) == 2
    assert len(stacks[1]) == 3
    assert len(stacks[2]) == 1
    assert stacks[0].pop() == "N"


def test_perform_shuffle_move():
    stacks, moves = parse_input_part1(test_data)

    perform_shuffle_move(stacks, moves[0])
    assert stacks[0] == ["Z", "N", "D"]
    assert stacks[1] == ["M", "C"]
    assert stacks[2] == ["P"]


def test_top_crates():
    stacks, moves = parse_input_part1(test_data)
    assert top_crates(stacks) == "NDP"


def test_perform_bulk_move():
    stacks, moves = parse_input_part1(test_data)

    perform_bulk_move(stacks, moves[0])
    assert stacks[0] == ["Z", "N", "D"]
    assert stacks[1] == ["M", "C"]
    assert stacks[2] == ["P"]

    perform_bulk_move(stacks, moves[1])
    assert stacks[0] == []
    assert stacks[1] == ["M", "C"]
    assert stacks[2] == ["P", "Z", "N", "D"]
