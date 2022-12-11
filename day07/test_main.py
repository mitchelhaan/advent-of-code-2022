from .main import (
    all_dir_sizes,
    build_directory_tree,
    part1,
    part2,
    print_directory_tree,
    sort_dirs_by_size,
    total_size,
)

test_data = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

root = build_directory_tree(test_data.strip())


def test_build_directory_tree():
    print_directory_tree(root)

    assert len(root.children) == 4
    assert root.children["a"].children["e"].children["i"].size == 584


def test_total_size():
    assert total_size(root.children["a"].children["e"]) == 584
    assert total_size(root) == 48381165


def test_all_dir_sizes():
    dir_sizes = all_dir_sizes(root)

    assert len(dir_sizes) == 4
    assert dir_sizes["/"] == 48381165
    assert dir_sizes["/a/e"] == 584
    assert dir_sizes["/a"] == 94853
    assert dir_sizes["/d"] == 24933642


def test_sort_dirs_by_size():
    sorted_dirs = sort_dirs_by_size(all_dir_sizes(root))

    assert len(sorted_dirs) > 0
    assert sorted_dirs[0] < sorted_dirs[-1]


def test_part1():
    assert part1(test_data.strip()) == 95437


def test_part2():
    assert part2(test_data.strip()) == 24933642
