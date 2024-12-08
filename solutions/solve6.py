#!/usr/bin/env python3

import numpy as np

import common


def move_out(x, y, direction, matrix):
    if direction == 0:
        matrix[:x + 1, y] = 'X'
    elif direction == 1:
        matrix[x, y:] = 'X'
    elif direction == 2:
        matrix[x:, y] = 'X'
    elif direction == 3:
        matrix[x, :y + 1] = 'X'


def move(x, y, direction, matrix):
    # direction: 0 - up, 1 - right, 2 - down, 3 - left
    try:
        if direction == 0:
            first_obstacle_x = np.where(matrix[0:x, y] == '#')[0][-1]
            # matrix[first_obstacle_x + 1:x + 1, y] = 'X'
            matrix[first_obstacle_x + 1:x + 1, y] = np.where(matrix[first_obstacle_x + 1:x + 1, y] == '.', 'X',
                                                             matrix[first_obstacle_x + 1:x + 1, y])
            x = first_obstacle_x + 1
        elif direction == 1:
            first_obstacle_y = np.where(matrix[x, y:] == '#')[0][0] + y
            # matrix[x, y:first_obstacle_y] = 'X'
            matrix[x, y:first_obstacle_y] = np.where(matrix[x, y:first_obstacle_y] == '.', 'X',
                                                     matrix[x, y:first_obstacle_y])
            y = first_obstacle_y - 1
        elif direction == 2:
            first_obstacle_x = np.where(matrix[x:, y] == '#')[0][0] + x
            # matrix[x:first_obstacle_x, y] = 'X'
            matrix[x:first_obstacle_x, y] = np.where(matrix[x:first_obstacle_x, y] == '.', 'X',
                                                     matrix[x:first_obstacle_x, y])
            x = first_obstacle_x - 1
        elif direction == 3:
            first_obstacle_y = np.where(matrix[x, 0:y] == '#')[0][-1]
            # matrix[x, first_obstacle_y + 1:y + 1] = 'X'
            matrix[x, first_obstacle_y + 1:y + 1] = np.where(matrix[x, first_obstacle_y + 1:y + 1] == '.', 'X',
                                                             matrix[x, first_obstacle_y + 1:y + 1])
            y = first_obstacle_y + 1
    except IndexError:
        move_out(x, y, direction, matrix)
        return x, y, None

    direction = (direction + 1) % 4
    return x, y, direction


def main():
    input_lines = common.init_day(6)
    if input_lines is None:
        exit(1)

    result2 = 0

    matrix = np.array([list(map(str, line)) for line in input_lines])

    x, y = np.where(matrix == '^')
    x, y = x[0], y[0]

    direction = 0
    while direction is not None:
        x, y, direction = move(x, y, direction, matrix)

    result1 = np.sum((matrix == 'X') | (matrix == '^'))

    print(matrix)
    print(x, y, direction)

    print(f"task1: {result1}")
    print(f"task2: {result2}")


main()
