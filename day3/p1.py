#!/usr/bin/env python

import sys


def main(file_name: str):
    """
    Find the voltage of all batteries when only being able to turn on the 2 highest values

    answer: 17443
    """
    with open(file_name) as f:
        lines = f.read().splitlines()

    total = 0
    for l in lines:
        l = list(map(int, [i for i in l]))

        d1, d2 = 0, 0
        for battery in l[:-1]:
            if battery > d1:
                d1 = battery
                d2 = 0
            elif battery > d2:
                d2 = battery
        if l[-1] > d2:
            d2 = l[-1]

        total += d1 * 10 + d2

    print(total)


if __name__ == "__main__":
    main(sys.argv[1])
