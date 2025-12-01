#!/usr/bin/env python

import sys


def main(file_name: str):
    """
    Find the amount of times the dial is exactly on zero.
    Answer: 1043
    """
    dial = [i for i in range(100)]
    index = 50
    code = 0

    with open(file_name) as f:
        for line in f:
            line = line.strip()
            d = line[0]
            n = int(line[1:])

            if index == 0:
                code += 1

            if d == "L":
                n = n % 100
                index = dial[index - n]
            elif d == "R":
                n = n % 100
                index = index + n - 100
                index = dial[index]

    print(code)


if __name__ == "__main__":
    main(sys.argv[1])
