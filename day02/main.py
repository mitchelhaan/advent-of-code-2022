import enum
from typing import List, Tuple

# https://adventofcode.com/2022/day/2


class Move(enum.Enum):
    rock = 1
    paper = 2
    scissors = 3


class Result(enum.Enum):
    loss = 0
    draw = 3
    win = 6


moves_result = {
    (Move.rock, Move.rock): Result.draw,
    (Move.rock, Move.paper): Result.win,
    (Move.rock, Move.scissors): Result.loss,
    (Move.paper, Move.rock): Result.loss,
    (Move.paper, Move.paper): Result.draw,
    (Move.paper, Move.scissors): Result.win,
    (Move.scissors, Move.rock): Result.win,
    (Move.scissors, Move.paper): Result.loss,
    (Move.scissors, Move.scissors): Result.draw,
}


def score_round(round: Tuple[Move, Move]) -> int:
    opponent_move, your_move = round
    return your_move.value + moves_result.get(round).value


def part1(rounds: List[Tuple[Move, Move]]) -> int:
    """What would your total score be if everything goes exactly according to your strategy guide?"""
    return sum(score_round(r) for r in rounds)


def part2(rounds: List[Tuple[Move, Move]]) -> int:
    """Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?"""
    return sum(score_round(r) for r in rounds)


def parse_move(val: str) -> Move:
    if val in "AX":
        return Move.rock
    if val in "BY":
        return Move.paper
    if val in "CZ":
        return Move.scissors


def parse_result(val: str) -> Result:
    if val == "X":
        return Result.loss
    if val == "Y":
        return Result.draw
    if val == "Z":
        return Result.win


def your_move_for_result(opponent_move: Move, result: Result) -> Move:
    for m, r in moves_result.items():
        if opponent_move == m[0] and result == r:
            return m[1]


def parse_round_as_moves(round: str) -> Tuple[Move, Move]:
    return tuple(map(parse_move, round.split()))


def parse_round_as_move_result(round: str) -> Tuple[Move, Move]:
    # The input here is Move, Result...
    # but backtracking to Move, Move to reuse scoring from part 1
    move_str, result_str = round.split()
    move, result = parse_move(move_str), parse_result(result_str)
    return move, your_move_for_result(move, result)


def parse_input_part1(data: str) -> List[Tuple[Move, Move]]:
    return list(map(parse_round_as_moves, data.strip().splitlines()))


def parse_input_part2(data: str) -> List[Tuple[Move, Move]]:
    return list(map(parse_round_as_move_result, data.strip().splitlines()))
