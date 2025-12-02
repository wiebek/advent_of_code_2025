#!/usr/bin/env python

import sys


def main(file_name: str):
    """
    Find all integers that are repeated twice in a integer
    ie. 123123 or 18851885
    """
    f = open(file_name)
    product_id_ranges = f.readline().strip().split(",")
    f.close()

    p1_answer = 0

    for r in product_id_ranges:
        n, m = list(map(int, r.split("-")))
        # n, m = r.split("-")
        # valid_ids.add(n)
        for ra in list(range(n, m + 1)):
            ra_str = str(ra)
            if ra_str[int(len(ra_str) / 2) :] == ra_str[: int(len(ra_str) / 2)]:
                p1_answer += int(ra_str)

    print(p1_answer)


if __name__ == "__main__":
    main(sys.argv[1])
