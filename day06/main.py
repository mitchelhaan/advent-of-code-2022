def find_start(data: str, unique_count: int) -> int:
    for x in range(unique_count, len(data)):
        if len(set(data[x - unique_count : x])) == unique_count:
            return x


def find_start_of_packet(data: str) -> int:
    return find_start(data, 4)


def find_start_of_message(data: str) -> int:
    return find_start(data, 14)


def parse_input_part1(data: str) -> str:
    return data.strip()


parse_input_part2 = parse_input_part1


def part1(data: str) -> int:
    """How many characters need to be processed before the first start-of-packet marker is detected?"""
    return find_start_of_packet(data)


def part2(data: str) -> int:
    """How many characters need to be processed before the first start-of-message marker is detected?"""
    return find_start_of_message(data)
