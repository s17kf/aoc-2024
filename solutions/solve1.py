#!/usr/bin/env python3

from collections import Counter

import common

input_lines = common.init_day(1)
if input_lines is None:
    exit(1)

left = []
right = []
right_counter = Counter()

for line in input_lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))
    right_counter[int(r)] += 1

left.sort()
right.sort()

distances_sum = 0
similarity_score = 0

for i, l in enumerate(left):
    r = right[i]
    distances_sum += abs(l - r)
    similarity_score += l * right_counter[l]

result1 = distances_sum
result2 = similarity_score

print(f"task1: {result1}")
print(f"task2: {result2}")
