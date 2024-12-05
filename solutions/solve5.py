#!/usr/bin/env python3

from functools import cmp_to_key

import common


def validate_update(rules, pages):
    for i, page in enumerate(pages):
        if page not in rules:
            continue
        for following in rules[page]:
            if following in pages[:i]:
                return False
    return True


def fix_update(rules, rules_inverted, pages):
    def compare_pages(page1, page2):
        if page1 in rules and page2 in rules[page1]:
            return -1
        if page2 in rules_inverted and page1 in rules_inverted[page2]:
            return 1
        return 0

    pages.sort(key=cmp_to_key(compare_pages))


def main():
    input_lines = common.init_day(5)
    if input_lines is None:
        exit(1)

    rules = {}
    rules_inverted = {}
    updates = []
    parsing_rules = True
    for line in input_lines:
        if line == "":
            parsing_rules = False
            continue
        if parsing_rules:
            first, second = line.split("|")
            if first in rules:
                rules[first].append(second)
            else:
                rules[first] = [second]
            if second in rules_inverted:
                rules_inverted[second].append(first)
            else:
                rules_inverted[second] = [first]
        else:
            updates.append(line)

    correct_middle_sum = 0
    fixed_middle_sum = 0

    for update in updates:
        pages = update.split(",")
        if validate_update(rules, pages):
            correct_middle_sum += int(pages[len(pages) // 2])
            continue
        fix_update(rules, rules_inverted, pages)
        fixed_middle_sum += int(pages[len(pages) // 2])

    print(f"task1: {correct_middle_sum}")
    print(f"task2: {fixed_middle_sum}")


main()
