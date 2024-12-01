import numpy
import common


def get_matrix_from_string_lines(lines, typ=int, parse_function=common.return_int_arg):
    matrix = numpy.zeros((len(lines), len(lines[0])), typ)
    for i, line in enumerate(lines):
        matrix[i] = ([parse_function(char) for char in line])
        matrix[i] = ([parse_function(char) for char in line])
    return matrix


def size(matrix):
    return len(matrix), len(matrix[0])


def turn_right_90(matrix):
    size_x, _ = size(matrix)
    new_matrix = matrix.copy()
    for x, row in enumerate(matrix):
        for y, item in enumerate(row):
            new_matrix[y, size_x - x - 1] = item
    return new_matrix


def turn_180(matrix):
    size_x, _ = size(matrix)
    new_matrix = matrix.copy()
    for x, row in enumerate(matrix):
        for y, item in enumerate(row):
            new_matrix[size_x - x - 1, size_x - y - 1] = item
    return new_matrix


def turn_left_90(matrix):
    size_x, _ = size(matrix)
    new_matrix = matrix.copy()
    for x, row in enumerate(matrix):
        for y, item in enumerate(row):
            new_matrix[size_x - y - 1, x] = item
    return new_matrix


def flip_up_down(matrix):
    size_x, _ = size(matrix)
    new_matrix = matrix.copy()
    for x, row in enumerate(reversed(matrix)):
        new_matrix[x] = row
    return new_matrix


def flip_right_left(matrix):
    size_x, _ = size(matrix)
    new_matrix = matrix.copy()
    for x, row in enumerate(matrix):
        for y, item in enumerate(reversed(row)):
            new_matrix[x, y] = item
    return new_matrix
