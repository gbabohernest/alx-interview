#!/usr/bin/python3
"""
A Python script that reads stdin line by line and computes metrics
"""

import sys


def parse_line(input_line):
    """
    Parse a line of input and extract the status code and file size.

    Args:
        input_line (str): A line of input in the specified format.

    Returns:
        tuple or None: A tuple containing the status code and file size
        if the line is in the correct format,
        otherwise None.
    """
    try:
        parts = input_line.split(" ")

        if len(parts) > 4:
            status_code = int(parts[-2])  # Convert status code to integer
            file_size = int(parts[-1])

            return status_code, file_size

    except (IndexError, ValueError):
        pass

    return None


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


lines_processed = 0
size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        # skip lines that don't match expected format
        result = parse_line(line.strip())

        if result is None:
            continue

        status_code, file_size = result

        # update metrics
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        size += file_size
        lines_processed += 1

        # print stats every 10 lines
        if lines_processed % 10 == 0:
            lines_processed = 0
            print_statistics(status_code_counts, size)

except KeyboardInterrupt:
    print_statistics(status_code_counts, size)
    raise
