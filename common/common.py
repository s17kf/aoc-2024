import sys

TAB = "    "


def is_empty(array):
    return len(array) == 0


def get_last_element(array):
    return array[len(array) - 1]


def print_array_line_by_line(array):
    for line in array:
        print(line)


def get_list_of_groups_divided_empty_line(lines, delimiter=" "):
    groups = []
    last_group = ""

    for line in lines:
        if is_empty(line):
            groups.append(last_group.lstrip(delimiter))
            last_group = ""
            continue
        last_group += delimiter + line
    if last_group != "":
        groups.append(last_group.lstrip(delimiter))
    return groups


def return_arg(arg):
    return arg


def return_int_arg(arg):
    return int(arg)


def get_matrix_from_string_lines(lines, parse_function=return_arg):
    matrix = []
    for line in lines:
        matrix.append([parse_function(char) for char in line])
    return matrix


def get_matrix_size(matrix):
    return len(matrix), len(matrix[0])


def generate_empty_matrix(rows, columns, empty_value=None):
    matrix = []
    for row in range(rows):
        matrix.append([empty_value for i in range(columns)])
    return matrix


def print_matrix(matrix, borders='|', delimiter=''):
    for row in matrix:
        print(f"{borders}{delimiter.join(row)}{borders}")


def add_or_increase_for_key(my_dict, key, default_value=1, value_to_increase=1):
    if key in my_dict:
        my_dict[key] += value_to_increase
    else:
        my_dict[key] = default_value
    return my_dict


def print_dict_line_by_line(dictionary):
    [print(f"{key}: {value}") for key, value in dictionary.items()]
