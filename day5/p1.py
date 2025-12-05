#!/usr/bin/env python

import sys


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
    From all ranges given create one list with all numbers within the range.
    """
    l = []
    for r in ranges:
        n, m = list(map(int, r.split("-")))
        l.append(range(n, m + 1))
    return l


def main(file_name):
    """
    Find all the ingredients that are not spoiled
    """
    ranges, ingredients_ids = parse_file(file_name)
    print(f"Making all ranges")
    all_ranges = all_numbers_in_range(ranges)

    print(f"Calculating total")
    total = 0
    # total = sum([total + 1 for i in ingredients_ids for j in all_ranges if i in j])
    for id in ingredients_ids:
        for range_ in all_ranges:
            if int(id) in range_:
                total += 1
                break

    print(total)


if __name__ == "__main__":
    main(sys.argv[1])
