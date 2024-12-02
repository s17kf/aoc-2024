#!/usr/bin/env python3

import common


def is_safe(report):
    if len(report) == 1:
        return True
    if report[0] == report[1]:
        return False
    multiplier = 1 if report[1] > report[0] else -1
    for i, second in enumerate(report[1:]):
        first = report[i]
        diff = (second - first) * multiplier
        if not 0 < diff <= 3:
            return False
    return True


input_lines = common.init_day(2)
if input_lines is None:
    exit(1)

result1 = 0
result2 = 0
for line in input_lines:
    line = [int(num) for num in line.split()]
    if is_safe(line):
        result1 += 1
        result2 += 1
    elif any(is_safe(line[:i] + line[i + 1:]) for i in range(len(line))):
        result2 += 1

print(f"task1: {result1}")
print(f"task2: {result2}")
