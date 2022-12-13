from dataclasses import dataclass, field
from typing import List

# https://adventofcode.com/2022/day/10


@dataclass
class State:
    register_x: int = 1
    register_x_history: List[int] = field(default_factory=list)


def process_instruction(state: State, instruction: str):
    if instruction == "noop":
        state.register_x_history.append(state.register_x)
    elif instruction.startswith("addx"):
        state.register_x_history.append(state.register_x)
        state.register_x_history.append(state.register_x)
        state.register_x += int(instruction.split()[-1])


def signal_strength(state: State, cycle: int):
    return cycle * state.register_x_history[cycle - 1]


def is_sprite_visible(cycle: int, register_x: int, screen_width: int = 40) -> bool:
    return abs((cycle % screen_width) - register_x) <= 1


def generate_image(state: State, width: int = 40) -> str:
    image = ""
    for cycle, val in enumerate(state.register_x_history):
        image += "#" if is_sprite_visible(cycle, val, width) else "."
        if (cycle + 1) % width == 0:
            image += "\n"
    return image


def parse_input_part1(data: str) -> List[str]:
    return data.strip().splitlines()


def part1(instructions: List[str]) -> int:
    state = State()
    for instruction in instructions:
        process_instruction(state, instruction)

    cycles = len(state.register_x_history)
    return sum(signal_strength(state, x) for x in range(20, cycles, 40))


parse_input_part2 = parse_input_part1


def part2(instructions: List[str]) -> str:
    state = State()
    for instruction in instructions:
        process_instruction(state, instruction)

    return "\n\n" + generate_image(state).replace(".", " ")
