#!/usr/bin/env python3

import re

import common


def sum_muls(data):
    regex = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    return sum([int(match[0]) * int(match[1]) for match in re.findall(regex, data)])


input_lines = common.init_day(3)
if input_lines is None:
    exit(1)

all_lines = "".join(input_lines)

result1 = sum_muls(all_lines)

remove_regex = re.compile(r"don't\(\)(.*?)do\(\)|don't\(\)(.*)$")
result2 = sum_muls(remove_regex.sub("", all_lines))

print(f"task1: {result1}")
print(f"task2: {result2}")
