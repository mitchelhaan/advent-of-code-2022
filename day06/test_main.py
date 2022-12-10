from .main import find_start_of_packet, find_start_of_message

test_data = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
"""

packets = test_data.strip().splitlines()


def test_find_start_of_packet():
    assert find_start_of_packet(packets[0]) == 7
    assert find_start_of_packet(packets[1]) == 5
    assert find_start_of_packet(packets[2]) == 6
    assert find_start_of_packet(packets[3]) == 10
    assert find_start_of_packet(packets[4]) == 11


def test_find_start_of_message():
    assert find_start_of_message(packets[0]) == 19
    assert find_start_of_message(packets[1]) == 23
    assert find_start_of_message(packets[2]) == 23
    assert find_start_of_message(packets[3]) == 29
    assert find_start_of_message(packets[4]) == 26
