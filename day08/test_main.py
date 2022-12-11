from .main import (
    is_tree_visible,
    parse_input_part1,
    part1,
    part2,
    tree_scenic_score,
    view_distance_down,
    view_distance_left,
    view_distance_right,
    view_distance_up,
)

sample_input = """
30373
25512
65332
33549
35390
"""

sample_data1 = parse_input_part1(sample_input)


def test_parse_input_part1():
    assert len(sample_data1) == 5
    assert sample_data1[0] == [3, 0, 3, 7, 3]


def test_is_tree_visible():
    # Top row
    assert all(is_tree_visible(sample_data1, x, 0) for x in range(len(sample_data1[0])))

    # Left column
    assert all(is_tree_visible(sample_data1, 0, y) for y in range(len(sample_data1)))

    # Bottom row
    assert all(
        is_tree_visible(sample_data1, x, len(sample_data1) - 1)
        for x in range(len(sample_data1[0]))
    )

    # Right column
    assert all(
        is_tree_visible(sample_data1, len(sample_data1[0]) - 1, y)
        for y in range(len(sample_data1))
    )

    assert is_tree_visible(sample_data1, 1, 1)
    assert not is_tree_visible(sample_data1, 3, 1)


def test_view_distance():
    tree1 = (2, 1)
    assert view_distance_up(sample_data1, *tree1) == 1
    assert view_distance_left(sample_data1, *tree1) == 1
    assert view_distance_right(sample_data1, *tree1) == 2
    assert view_distance_down(sample_data1, *tree1) == 2

    tree2 = (2, 3)
    assert view_distance_up(sample_data1, *tree2) == 2
    assert view_distance_left(sample_data1, *tree2) == 2
    assert view_distance_right(sample_data1, *tree2) == 2
    assert view_distance_down(sample_data1, *tree2) == 1


def test_tree_scenic_score():
    assert tree_scenic_score(sample_data1, 2, 1) == 4
    assert tree_scenic_score(sample_data1, 2, 3) == 8


def test_part1():
    assert part1(sample_data1) == 21


def test_part2():
    assert part2(sample_data1) == 8
