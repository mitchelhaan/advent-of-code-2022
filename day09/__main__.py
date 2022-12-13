import pytest
import sys
from pathlib import Path

from .main import parse_input_part1, parse_input_part2, part1, part2

current_dir = Path(__file__).parent

pytest.main(["-v", current_dir])

if len(sys.argv) >= 2:
    file = sys.argv[1]
else:
    file = current_dir / "input.txt"

with open(file) as f:
    data = f.read()

    print()
    print(f"Part1: result is {part1(parse_input_part1(data))}")
    print(f"Part2: result is {part2(parse_input_part2(data))}")
    print()
