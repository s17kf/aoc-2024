#!/usr/bin/env python3

import numpy as np

import common


def get_antennas_coordinates_dict(matrix):
    antennas_coordinates = np.argwhere(matrix != ".")
    antennas_coordinates_dict = {}
    for x, y in antennas_coordinates:
        if matrix[x, y] not in antennas_coordinates_dict:
            antennas_coordinates_dict[matrix[x, y]] = []
        antennas_coordinates_dict[matrix[x, y]].append((x, y))
    return antennas_coordinates_dict


def try_add_antinode(antinodes, x, y):
    if x < 0 or y < 0:
        return False
    try:
        antinodes[x, y] = 1
        return True
    except IndexError:
        return False


def fill_antinodes(antinodes, one_type_antennas_coordinates):
    for i, (x1, y1) in enumerate(one_type_antennas_coordinates):
        for x2, y2 in one_type_antennas_coordinates[i + 1:]:
            dx, dy = x2 - x1, y2 - y1
            for x, y in [(x1 - dx, y1 - dy), (x2 + dx, y2 + dy)]:
                try_add_antinode(antinodes, x, y)


def fill_antinodes2(antinodes, one_type_antennas_coordinates):
    for i, (x1, y1) in enumerate(one_type_antennas_coordinates):
        for x2, y2 in one_type_antennas_coordinates[i + 1:]:
            dx, dy = x2 - x1, y2 - y1
            for x, y, dx, dy in [(x1, y1, -dx, -dy), (x2, y2, dx, dy)]:
                while try_add_antinode(antinodes, x, y):
                    x, y = x + dx, y + dy


def main():
    input_lines = common.init_day(8)
    if input_lines is None:
        exit(1)

    antennas_matrix = np.array([list(map(str, line)) for line in input_lines])
    antinodes = np.zeros(antennas_matrix.shape, dtype=int)
    antinodes2 = np.zeros(antennas_matrix.shape, dtype=int)

    antennas_coords_dict = get_antennas_coordinates_dict(antennas_matrix)

    for antenna_type in antennas_coords_dict:
        fill_antinodes(antinodes, antennas_coords_dict[antenna_type])
        fill_antinodes2(antinodes2, antennas_coords_dict[antenna_type])

    result1 = np.sum(antinodes)
    result2 = np.sum(antinodes2)

    print(f"task1: {result1}")
    print(f"task2: {result2}")


main()
