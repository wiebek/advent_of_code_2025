#!/usr/bin/env python

import sys


def main(file_name: str):
    """
    Find the voltage of all batteries when only being able to turn on the 12 highest values

    answer: 172167155440541
    """
    with open(file_name) as f:
        lines = f.read().splitlines()

    total = 0
    for l in lines:
        l = list(map(int, [i for i in l]))
        n = len(l)

        d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12 = (
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        )
        for i, battery in enumerate(l[:-1]):
            if battery > d1 and n - i > 11:
                d1 = battery
                d2 = 0
            elif battery > d2 and n - i > 10:
                d2 = battery
                d3 = 0
            elif battery > d3 and n - i > 9:
                d3 = battery
                d4 = 0
            elif battery > d4 and n - i > 8:
                d4 = battery
                d5 = 0
            elif battery > d5 and n - i > 7:
                d5 = battery
                d6 = 0
            elif battery > d6 and n - i > 6:
                d6 = battery
                d7 = 0
            elif battery > d7 and n - i > 5:
                d7 = battery
                d8 = 0
            elif battery > d8 and n - i > 4:
                d8 = battery
                d9 = 0
            elif battery > d9 and n - i > 3:
                d9 = battery
                d10 = 0
            elif battery > d10 and n - i > 2:
                d10 = battery
                d11 = 0
            elif battery > d11 and n - i > 1:
                d11 = battery
                d12 = 0
            elif battery > d12 and n - i > 0:
                d12 = battery

        if l[-1] > d12:
            d12 = l[-1]

        total += int(f"{d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}{d9}{d10}{d11}{d12}")

    print(total)


if __name__ == "__main__":
    main(sys.argv[1])
