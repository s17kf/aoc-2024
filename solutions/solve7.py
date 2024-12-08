#!/usr/bin/env python3

import common


def check_numbers(numbers, expected_result, operators):
    if len(numbers) == 1:
        return numbers[0] == expected_result
    last, second_last = numbers.pop(), numbers.pop()
    for operator in operators:
        if check_numbers(numbers + [operator(last, second_last)], expected_result, operators):
            return True
    return False


def main():
    input_lines = common.init_day(7)
    if input_lines is None:
        exit(1)

    result1 = 0
    result2 = 0

    for line in input_lines:
        values = line.split()
        expected_result = int(values[0].rstrip(":"))
        numbers = [int(v) for v in reversed(values[1:])]

        operators = [lambda x, y: x + y, lambda x, y: x * y]
        if check_numbers(numbers.copy(), expected_result, operators):
            result1 += expected_result

        operators.append(lambda x, y: int(f"{x}{y}"))
        if check_numbers(numbers.copy(), expected_result, operators):
            result2 += expected_result

    print(f"task1: {result1}")
    print(f"task2: {result2}")


main()
