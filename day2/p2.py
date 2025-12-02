#!/usr/bin/env python

import sys


def main(file_name: str):
    """
    Find all integers that have repeats in an integer
    ie.
    """
    f = open(file_name)
    product_id_ranges = f.readline().strip().split(",")
    f.close()

    p2_answer = 0

    for r in product_id_ranges:
        n, m = list(map(int, r.split("-")))
        # n, m = r.split("-")
        # valid_ids.add(n)
        for ra in list(range(n, m + 1)):
            ra_str = str(ra)
            chunks = len(ra_str)
            if len(set(ra_str)) == 1 and len(ra_str) > 1:
                p2_answer += ra
            else:
                for ra2 in list(range(1, int(len(ra_str) / 2) + 1)):
                    chunk_size = len(ra_str) // ra2
                    z = [
                        ra_str[i : i + chunk_size] for i in range(0, chunks, chunk_size)
                    ]
                    if len(set(z)) == 1 and len(z) > 1:
                        p2_answer += int(ra_str)
                        break

    print(p2_answer)


if __name__ == "__main__":
    main(sys.argv[1])
