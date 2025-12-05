#!/usr/bin/env python

import sys

PAPER_ROLL = "@"


def check_left(y: int = 0, y_len: int = 1):
    """
    Check if there is a paper roll left of the position
    """
    pass


def check_right(y, y_len):
    """
    Check if there is a paper roll right of the position
    """
    pass


def check_up(x, x_len):
    """
    Check if there is a paper roll up of the position
    """
    pass


def check_down(x, x_len):
    """
    Check if there is a paper roll down from the position
    """
    pass


def loop(lines):
    total = 0
    new_lines = []
    for i in range(len(lines)):
        new_line = []
        for j in range(len(lines[i])):
            n = 0
            # check if position is paper roll
            if lines[i][j] != "@":
                new_line.append(".")
                continue

            # look left + right
            # check_left(j, y_len)
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
                new_line.append(".")
            else:
                new_line.append("@")

        new_lines.append(new_line)

    return (total, new_lines)


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

    Go through the warehouse several times until you cannot remove any more paper rolls.
    Answer: 9401
    """
    lines = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            lines.append([c for c in line])

    total = 0
    while True:
        tmp_total, new_lines = loop(lines)
        if tmp_total == 0:
            break
        total += tmp_total
        lines = new_lines
    print(total)


if __name__ == "__main__":
    main(sys.argv[1])
