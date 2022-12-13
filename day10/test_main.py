from .main import (
    generate_image,
    is_sprite_visible,
    parse_input_part1,
    parse_input_part2,
    part1,
    part2,
    State,
    process_instruction,
    signal_strength,
)


def test_parse_input_part1():
    assert len(sample_data1) == 146


def test_process_instruction():
    state = State()

    process_instruction(state, "noop")
    assert state.register_x == 1
    assert state.register_x_history == [1]

    process_instruction(state, "addx 3")
    assert state.register_x == 4
    assert state.register_x_history == [1, 1, 1]

    process_instruction(state, "addx -5")
    assert state.register_x == -1
    assert state.register_x_history == [1, 1, 1, 4, 4]


def test_signal_strength():
    state = State()
    for instruction in sample_data1:
        process_instruction(state, instruction)

    assert signal_strength(state, 20) == 420
    assert signal_strength(state, 60) == 1140
    assert signal_strength(state, 100) == 1800
    assert signal_strength(state, 140) == 2940
    assert signal_strength(state, 180) == 2880
    assert signal_strength(state, 220) == 3960

    assert (
        sum(
            signal_strength(state, x)
            for x in range(20, len(state.register_x_history), 40)
        )
        == 13140
    )


def test_is_sprite_visible():
    assert is_sprite_visible(1, 1)
    assert is_sprite_visible(2, 1)
    assert not is_sprite_visible(3, 16)
    assert not is_sprite_visible(4, 16)


def test_generate_image():
    state = State()
    for instruction in sample_data1:
        process_instruction(state, instruction)

    assert generate_image(state).splitlines() == sample_image.splitlines()


sample_input = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

sample_data1 = parse_input_part1(sample_input)

sample_image = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
""".strip()
