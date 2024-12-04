#!/usr/bin/env python3

import common


def check_diagonal(x, y, dx, dy, word_len, matrix, word):
    rows, cols = len(matrix), len(matrix[0])
    for i in range(word_len):
        if not 0 <= x < rows or not 0 <= y < cols or matrix[x][y] != word[i]:
            return False
        x += dx
        y += dy
    return True


def search_word(matrix, word):
    rows, cols = len(matrix), len(matrix[0])
    words_found = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]:
                words_found += 1 if check_diagonal(x, y, dx, dy, len(word), matrix, word) else 0
    return words_found


def search_crossed_word(matrix, word):
    if len(word) != 3:
        return None
    rows = len(matrix)
    cols = len(matrix[0])
    words_found = 0
    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            crossed_words = 0
            if matrix[x][y] == word[1]:
                for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    if matrix[x + dx][y + dy] == word[0] and matrix[x - dx][y - dy] == word[2]:
                        crossed_words += 1
            words_found += 1 if crossed_words == 2 else 0
    return words_found


input_lines = common.init_day(4)
if input_lines is None:
    exit(1)

print(f"task1: {search_word(input_lines, "XMAS")}")
print(f"task2: {search_crossed_word(input_lines, "MAS")}")
