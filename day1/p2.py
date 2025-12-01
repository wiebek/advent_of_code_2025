#!/usr/bin/env python

import sys


def main(file_name: str):
    """
    Find the times that the dial pasted 0
    Part2 between: 5719 - 6492
    answer: 5963
    """
    rotations = []
    point = 50
    code = 0

    with open(file_name) as f:
        for line in f:
            line = line.strip()
            rotations.append(line)

    for line in rotations:
        steps = int(line[1:])
        for _ in range(steps, 0, -1):
            point += -1 if line[0] == "L" else 1
            if point % 100 == 0:
                code += 1

    print(code)


if __name__ == "__main__":
    main(sys.argv[1])
