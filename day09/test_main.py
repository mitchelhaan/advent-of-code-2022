import json
import sys
from itertools import product
from .main import (
    parse_input_part1,
    parse_input_part2,
    part1,
    part2,
    perform_action,
    Action,
    State,
    Point,
)

sample_input1 = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

sample_input2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

sample_data1 = parse_input_part1(sample_input1)
sample_data2 = parse_input_part2(sample_input2)


def test_parse_input_part1():
    json.dump(sample_data1, sys.stdout, indent=2, default=repr)

    assert len(sample_data1) == 8
    assert sample_data1[0] == Action("R", 4)


def test_perform_action():
    state = State()
    for action in sample_data1:
        perform_action(state, action)

    json.dump(state, sys.stdout, indent=2, default=repr)

    assert state.rope_position[0] == Point(2, 2)


def test_point_adjacency():
    # Square from (-2, -2) to (2, 2)
    square_around_origin = list(product(range(-2, 3), range(-2, 3)))

    # Square from (-1, -1) to (1, 1)
    adjacent_to_origin = list(product(range(-1, 2), range(-1, 2)))

    # Check adjacency to the origin point
    for x, y in square_around_origin:
        if (x, y) in adjacent_to_origin:
            assert Point(0, 0).is_adjacent_to(Point(x, y))
        else:
            assert not Point(0, 0).is_adjacent_to(Point(x, y))


def test_point_movement():
    # Test movement on a single axis
    assert Point(0, 0).move_toward(Point(5, 0)) == Point(1, 0)
    assert Point(0, 0).move_toward(Point(-5, 0)) == Point(-1, 0)
    assert Point(0, 0).move_toward(Point(0, 5)) == Point(0, 1)
    assert Point(0, 0).move_toward(Point(0, -5)) == Point(0, -1)

    # Test movement on both axes
    assert Point(0, 0).move_toward(Point(5, 5)) == Point(1, 1)
    assert Point(0, 0).move_toward(Point(-5, 5)) == Point(-1, 1)
    assert Point(0, 0).move_toward(Point(5, -5)) == Point(1, -1)
    assert Point(0, 0).move_toward(Point(-5, -5)) == Point(-1, -1)


def test_part1():
    assert part1(sample_data1) == 13


def test_part2():
    assert part2(sample_data1) == 1
    assert part2(sample_data2) == 36
