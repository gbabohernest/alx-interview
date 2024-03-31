#!/usr/bin/python3
"""
A Python script that reads stdin line by line and computes metrics
"""

import sys


def print_statistics(status_code_counts_dict, total_size):
    """
    Print the computed statistics based on
    status code counts and total file size.

    Args:
        status_code_counts_dict (dict): A dictionary containing
        the counts of different status codes.
        total_size (int): The total size of all files processed.
    """
    print(f'File size: {total_size}')
    for code in sorted(status_code_counts_dict.keys()):
        if status_code_counts_dict[code] != 0:
            print(f"{code}: {status_code_counts_dict[code]}")


status_code_counts = {"200": 0, "301": 0, "400": 0, "401": 0,
                      "403": 0, "404": 0, "405": 0, "500": 0}

lines_processed = 0
size = 0

try:
    for line in sys.stdin:
        input_list = line.split()

        if len(input_list) < 7:
            continue

        lines_processed += 1

        try:
            size += int(input_list[-1])
        except ValueError:
            pass

        try:
            status_code = input_list[-2]
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
        except ValueError:
            pass

        if lines_processed % 10 == 0:
            print_statistics(status_code_counts, size)

    print_statistics(status_code_counts, size)

except KeyboardInterrupt:
    print_statistics(status_code_counts, size)
    raise
