#!/usr/bin/env python3
import sys


class File:
    def __init__(self, name: str, size: int):
        self.size = size
        self.name = name


class Directory:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.directorys = []
        self.files = []

    def add_directory(self, sub: "Directory"):
        self.directorys.append(sub)

    def add_file(self, file: File):
        self.files.append(file)

    def get_sizes(self, storage: set) -> tuple[int, int]:
        file_sizes = sum((x.size for x in self.files))
        dir_sizes = file_sizes
        for x in self.directorys:
            x_size, x_total = x.get_sizes(storage)
            dir_sizes += x_total
        storage.add((self.name, file_sizes, dir_sizes))
        return (file_sizes, dir_sizes)


class Explorer:
    def __init__(self):
        self.base = Directory("/", None)
        self.current = self.base

    def add_values(self, values: list[str]):
        for output_line in values:
            thing, name = output_line.split()
            if thing == "dir":
                self.current.add_directory(Directory(name, self.current))
            else:
                self.current.add_file(File(name, int(thing)))

    def change_dir(self, directory: str):
        if directory == "/":
            self.current = self.base
        elif directory == "..":
            self.current = self.current.parent
        else:
            for i in self.current.directorys:
                if i.name == directory:
                    self.current = i

    def process(self, input: list[str]):
        output = []
        for line in input:
            if line.startswith("$"):
                if len(output) > 0:
                    self.add_values(output)
                output = []
                cmd = line.split()
                if cmd[1] == "cd":
                    self.change_dir(cmd[2])
            else:
                output.append(line)
        if len(output) > 0:
            self.add_values(output)

    def get_sizes(self):
        values = set()
        _, top_total = self.base.get_sizes(values)
        return top_total, values


def main():
    exp = Explorer()
    with open(sys.argv[1]) as f:
        exp.process(f.readlines())
    value = 0
    used, a_set = exp.get_sizes()
    free = 70000000 - used
    smalles = 70000000
    needed = 30000000 - free
    for name, _, total in a_set:
        if total < 100000:
            value += total
        if total > needed:
            print(total, name)
    print(value)


if __name__ == "__main__":
    main()
