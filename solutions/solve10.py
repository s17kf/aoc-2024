#!/usr/bin/env python3

import queue

import numpy as np

import common

DELTAS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def add_nexts_bfs(t_map, nexts, visited, x, y):
    for dx, dy in DELTAS:
        new_x, new_y = x + dx, y + dy
        if new_x < 0 or new_y < 0:
            continue
        try:
            if t_map[new_x, new_y] == t_map[x, y] - 1 and not visited[new_x, new_y]:
                nexts.put((new_x, new_y))
                visited[new_x, new_y] = True
        except IndexError:
            pass


def add_scores_for_reachable_zeros(t_map, scores, x, y):
    nexts = queue.Queue()
    visited = np.zeros(t_map.shape, dtype=bool)
    add_nexts_bfs(t_map, nexts, visited, x, y)
    while not nexts.empty():
        x, y = nexts.get()
        if t_map[x, y] == 0:
            scores[x, y] += 1
            continue
        add_nexts_bfs(t_map, nexts, visited, x, y)


def to_int(x):
    try:
        return int(x)
    except ValueError:
        return -1


def main():
    input_lines = common.init_day(10)
    if input_lines is None:
        exit(1)

    topographic_map = np.array([list(map(to_int, line)) for line in input_lines])

    scores = np.zeros(topographic_map.shape, dtype=int)
    h9 = np.where(topographic_map == 9)

    for x, y in zip(*h9):
        add_scores_for_reachable_zeros(topographic_map, scores, x, y)
    result1 = np.sum(scores)

    # PART 2:
    scores2 = np.zeros(topographic_map.shape, dtype=int)
    for x, y in zip(*h9):
        scores2[x, y] = 1
    for h in range(9, 0, -1):
        for x, y in zip(*np.where(topographic_map == h)):
            for dx, dy in DELTAS:
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_y < 0:
                    continue
                try:
                    if topographic_map[new_x, new_y] == h - 1:
                        scores2[new_x, new_y] += scores2[x, y]
                except IndexError:
                    pass

    h0 = np.where(topographic_map == 0)
    result2 = scores2[h0].sum()

    print(f"task1: {result1}")
    print(f"task2: {result2}")


main()
