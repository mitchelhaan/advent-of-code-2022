from copy import copy
from dataclasses import dataclass, field
import dataclasses
from typing import List, Literal

# https://adventofcode.com/2022/day/9


@dataclass
class Point:
    x: int = 0
    y: int = 0

    def up(self, count: int = 1):
        self.y += count

    def down(self, count: int = 1):
        self.y -= count

    def left(self, count: int = 1):
        self.x -= count

    def right(self, count: int = 1):
        self.x += count

    def is_adjacent_to(self, other: "Point") -> bool:
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    def move_toward(self, other: "Point"):
        # Other point is left/right
        if self.x == other.x:
            self.y += 1 if other.y > self.y else -1
        # Other point is up/down
        elif self.y == other.y:
            self.x += 1 if other.x > self.x else -1
        # Other is diagonal up/left
        elif self.x > other.x and self.y < other.y:
            self.x -= 1
            self.y += 1
        # Other is diagonal up/right
        elif self.x < other.x and self.y < other.y:
            self.x += 1
            self.y += 1
        # Other is diagonal down/right
        elif self.x < other.x and self.y > other.y:
            self.x += 1
            self.y -= 1
        # Other is diagonal down/left
        elif self.x > other.x and self.y > other.y:
            self.x -= 1
            self.y -= 1

        return self


@dataclass
class Action:
    direction: Literal["U", "D", "L", "R"]
    count: int


@dataclass
class State:
    rope_position: List[Point] = field(default_factory=list)
    tail_history: List[Point] = field(default_factory=list)
    rope_length: int = 2


def parse_action(data: str) -> Action:
    direction, count = data.split()
    return Action(direction, int(count))


def perform_action(state: State, action: Action):
    if len(state.rope_position) == 0:
        state.rope_position = [Point(0, 0) for _ in range(state.rope_length)]

    # Move one step at a time
    for _ in range(action.count):
        # Move the head of the rope
        if action.direction == "U":
            state.rope_position[0].up()
        elif action.direction == "D":
            state.rope_position[0].down()
        elif action.direction == "L":
            state.rope_position[0].left()
        elif action.direction == "R":
            state.rope_position[0].right()

        # Trickle the motion down the rope
        for knot in range(1, len(state.rope_position)):
            if not state.rope_position[knot - 1].is_adjacent_to(
                state.rope_position[knot]
            ):
                state.rope_position[knot].move_toward(state.rope_position[knot - 1])

        state.tail_history.append(copy(state.rope_position[-1]))


def parse_input_part1(data: str) -> List[Action]:
    return [parse_action(action) for action in data.strip().splitlines()]


def part1(actions: List[Action]) -> int:
    state = State()

    for action in actions:
        perform_action(state, action)

    return len(set([dataclasses.astuple(x) for x in state.tail_history]))


parse_input_part2 = parse_input_part1


def part2(actions: List[Action]) -> int:
    state = State(rope_length=10)

    for action in actions:
        perform_action(state, action)

    return len(set([dataclasses.astuple(x) for x in state.tail_history]))
