#!/usr/bin/env python3

import bisect

import common


def count_checksum1(mem):
    first_empty = mem.index(None)
    last_not_empty = len(mem) - 1
    while mem[last_not_empty] is None:
        last_not_empty -= 1

    while first_empty < last_not_empty:
        mem[first_empty], mem[last_not_empty] = mem[last_not_empty], None
        first_empty = mem.index(None, first_empty)
        while mem[last_not_empty] is None:
            last_not_empty -= 1

    checksum = i = 0
    while mem[i] is not None:
        checksum += i * mem[i]
        i += 1
    return checksum


def count_checksum2(mem, files, empty_spaces):
    for size in empty_spaces:
        empty_spaces[size].reverse()
    files.reverse()

    for id, size, pos in files:
        possible_spaces = []
        for space_size in range(size, 10):
            if len(empty_spaces[space_size]) == 0:
                continue
            if empty_spaces[space_size][-1] > pos:
                empty_spaces[space_size] = []
                continue
            possible_spaces.append((empty_spaces[space_size][-1], space_size))
        possible_spaces.sort()

        if len(possible_spaces) == 0:
            for i in range(pos, pos + size):
                mem[i] = id
            continue

        space_pos, space_size = possible_spaces[0]
        empty_spaces[space_size].pop()
        for i in range(space_pos, space_pos + size):
            mem[i] = id
        if size != space_size:
            bisect.insort_left(empty_spaces[space_size - size], space_pos + size, key=lambda x: -x)

    checksum = 0
    for i, id in enumerate(mem):
        if id is None:
            continue
        checksum += i * id
    return checksum


def main():
    input_lines = common.init_day(9)
    if input_lines is None:
        exit(1)

    mem = []
    empty_spaces = {i: [] for i in range(1, 10)}
    files = []

    for i, c in enumerate(input_lines[0]):
        size = int(c)
        if size == 0:
            continue
        if i % 2 == 0:
            id = i // 2
            files.append((id, size, len(mem)))
            mem.extend([id]*size)
        else:
            empty_spaces[size].append(len(mem))
            mem.extend([None] * size)

    checksum1 = count_checksum1(mem)
    checksum2 = count_checksum2([None for _ in range(len(mem))], files, empty_spaces)

    print(f"task1: {checksum1}")
    print(f"task2: {checksum2}")


main()
