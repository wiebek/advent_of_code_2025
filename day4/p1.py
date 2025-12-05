#!/usr/bin/env python

import sys


def main(file_name):
    """
    Find all rolls of paper adjacent to each roll. If fewer than 4 than a forklift can reach it.
    @ = paper roll
    Yes:
    ..@@.
    ..@..
    .....

    No:
    ...@.
    ..@..
    .@.@.

    Answer: 1564
    """
    lines = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            lines.append([c for c in line])

    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            n = 0
            # check if position is paper roll
            if lines[i][j] != "@":
                continue

            # look left + right
            if j - 1 >= 0 and lines[i][j - 1] == "@":  # left
                n += 1
            if j + 1 < len(lines[i]) and lines[i][j + 1] == "@":  # right
                n += 1

            # look up and down
            if i - 1 >= 0 and lines[i - 1][j] == "@":  # up
                n += 1
            if i + 1 < len(lines) and lines[i + 1][j] == "@":  # down
                n += 1

            # look diagonal
            if i - 1 >= 0 and j - 1 >= 0 and lines[i - 1][j - 1] == "@":  # left up
                n += 1
            if (
                i - 1 >= 0 and j + 1 < len(lines[i]) and lines[i - 1][j + 1] == "@"
            ):  # right up
                n += 1
            if (
                i + 1 < len(lines) and j - 1 >= 0 and lines[i + 1][j - 1] == "@"
            ):  # left down
                n += 1
            if (
                i + 1 < len(lines)
                and j + 1 < len(lines[i])
                and lines[i + 1][j + 1] == "@"
            ):  # right down
                n += 1

            if n < 4:
                total += 1

    print(total)


if __name__ == "__main__":
    main(sys.argv[1])
