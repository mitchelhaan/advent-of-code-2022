from typing import List

# https://adventofcode.com/2022/day/8


def parse_input_part1(data: str) -> List[str]:
    return [list(map(int, line)) for line in data.strip().splitlines()]


parse_input_part2 = parse_input_part1


def is_tree_visible(grid: List[List[int]], x: int, y: int) -> bool:
    # All of the trees around the edge of the grid are visible
    if x == 0 or y == 0 or x == len(grid[0]) - 1 or y == len(grid) - 1:
        return True

    # Other trees are only visible if all of the other trees between it and an edge of the grid are shorter than it.
    # Only consider trees in the same row or column.
    height = grid[y][x]

    visible_from_left = all(grid[y][test_x] < height for test_x in range(0, x))
    visible_from_right = all(
        grid[y][test_x] < height for test_x in range(x + 1, len(grid[0]))
    )
    visible_from_top = all(grid[test_y][x] < height for test_y in range(0, y))
    visible_from_bottom = all(
        grid[test_y][x] < height for test_y in range(y + 1, len(grid))
    )

    return (
        visible_from_left
        or visible_from_right
        or visible_from_top
        or visible_from_bottom
    )


def view_distance_up(grid, x, y) -> int:
    height = grid[y][x]
    view_distance = 0

    for test_y in range(y - 1, -1, -1):
        view_distance += 1
        if grid[test_y][x] >= height:
            break

    return view_distance


def view_distance_left(grid, x, y) -> int:
    height = grid[y][x]
    view_distance = 0

    for test_x in range(x - 1, -1, -1):
        view_distance += 1
        if grid[y][test_x] >= height:
            break

    return view_distance


def view_distance_right(grid, x, y) -> int:
    height = grid[y][x]
    view_distance = 0

    for test_x in range(x + 1, len(grid[y])):
        view_distance += 1
        if grid[y][test_x] >= height:
            break

    return view_distance


def view_distance_down(grid, x, y) -> int:
    height = grid[y][x]
    view_distance = 0

    for test_y in range(y + 1, len(grid)):
        view_distance += 1
        if grid[test_y][x] >= height:
            break

    return view_distance


def tree_scenic_score(grid, x, y) -> int:
    return (
        view_distance_up(grid, x, y)
        * view_distance_left(grid, x, y)
        * view_distance_right(grid, x, y)
        * view_distance_down(grid, x, y)
    )


def part1(grid: List[List[int]]) -> int:
    """Consider your map; how many trees are visible from outside the grid?"""
    return sum(
        is_tree_visible(grid, x, y)
        for x in range(len(grid[0]))
        for y in range(len(grid))
    )


def part2(grid: List[List[int]]) -> int:
    return max(
        tree_scenic_score(grid, x, y)
        for x in range(len(grid[0]))
        for y in range(len(grid))
    )
