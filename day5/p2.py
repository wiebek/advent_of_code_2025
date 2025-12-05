#!/usr/bin/env python

import sys
from collections import defaultdict


def parse_file(file_name: str):
    """
    Parse the file by checking for the empty line
    """
    flag = True
    ingredients = []
    ranges = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if line == "":
                flag = False
                continue
            if flag:
                ranges.append(line)
            else:
                ingredients.append(line)
    return ranges, ingredients


def all_numbers_in_range(ranges: list):
    """
    Calculate the amount of id's that are fresh.
    Overlapping regions must be merged.
    """
    d = defaultdict(int)
    for r in ranges:
        n, m = list(map(int, r.split("-")))
        l = list(range(n, m + 1))
        [d[i] + 1 for i in l]
    return d


def main(file_name):
    """
    Find all the ingredients that are not spoiled
    351.192.334.583.397 too high
    351.192.334.583.393 too high
    """
    ranges, _ = parse_file(file_name)
    ranges_int = sorted([list(map(int, r.split("-"))) for r in ranges])

    print(f"Making all ranges")
    # all_ranges = all_numbers_in_range(ranges)
    total = 0
    for i, r in enumerate(ranges_int):
        print(r)
        n, m = r
        if i == 0:
            total += len(range(n, m + 1))
        else:
            m_prev = ranges_int[i - 1][1]
            print(f"Current start: {n} vs previous stop: {m_prev}: {n < m_prev}")
            if m == m_prev:
                continue
            if n < m_prev:
                print(f"New range: {range(m_prev + 1, m + 1)}")
                total += len(range(m_prev + 1, m + 1))
            else:
                total += len(range(n, m + 1))

    print(f"Total for part 2: {total}")


if __name__ == "__main__":
    main(sys.argv[1])
