from dataclasses import dataclass, field
import enum
import re
from typing import List, Mapping, Optional, Tuple


class EntryKind(enum.Enum):
    directory = "dir"
    file = "file"


@dataclass
class DirEntry:
    name: str
    kind: EntryKind = EntryKind.directory
    size: int = 0
    parent: Optional["DirEntry"] = None
    children: Mapping[str, "DirEntry"] = field(default_factory=dict)

    def __repr__(self) -> str:
        if self.kind == EntryKind.directory:
            desc = f"dir, total_size={total_size(self)}"
        else:
            desc = f"file, size={self.size}"
        return f"{self.name} ({desc})"


def build_directory_tree(console_output: str):
    root = DirEntry("/")
    curdir = root

    for line in console_output.splitlines():
        if m := re.match(r"\$\s+(\w+)\s*(.*)", line):
            cmd, arg = m.groups()
            if cmd == "cd":
                if arg == "/":
                    curdir = root
                elif arg == "..":
                    curdir = curdir.parent
                else:
                    curdir = curdir.children[arg]
        else:
            size, name = line.split()
            if size == "dir":
                size = 0
                kind = EntryKind.directory
            else:
                size = int(size)
                kind = EntryKind.file
            curdir.children[name] = DirEntry(
                name=name, kind=kind, size=size, parent=curdir
            )

    return root


def print_directory_tree(entry: DirEntry, indent=2):
    print(f"{'-':>{indent}} {entry}")
    for x in entry.children.values():
        print_directory_tree(x, indent + 2)


def total_size(entry: DirEntry) -> int:
    return entry.size + sum(total_size(e) for e in entry.children.values())


def all_dir_sizes(entry: DirEntry, path: str = "", results=None) -> Mapping[str, int]:
    results = results or {}

    if entry.parent:
        path = f"{path}/{entry.name}"

    results[path or "/"] = total_size(entry)

    for x in entry.children.values():
        if x.kind == EntryKind.directory:
            all_dir_sizes(x, path, results)

    return results


def sort_dirs_by_size(dir_sizes: Mapping[str, int]) -> List[Tuple[int, str]]:
    return sorted((size, name) for name, size in dir_sizes.items())


def parse_input_part1(data: str) -> str:
    return data.strip()


parse_input_part2 = parse_input_part1


def part1(console_output: str) -> int:
    """Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?"""
    root = build_directory_tree(console_output)
    dir_sizes = all_dir_sizes(root)

    return sum(x for x in dir_sizes.values() if x <= 100000)


def part2(console_output: str) -> int:
    """Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?"""
    total_disk_space = 70000000
    needed_disk_space = 30000000

    root = build_directory_tree(console_output)
    dir_sizes = all_dir_sizes(root)

    used_disk_space = dir_sizes["/"]

    for (size, name) in sort_dirs_by_size(dir_sizes):
        if total_disk_space - (used_disk_space - size) > needed_disk_space:
            return size
