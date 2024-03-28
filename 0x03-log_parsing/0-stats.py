#!/usr/bin/python3
"""
A Python script that reads stdin line by line and computes metrics
"""

import sys
import re
import signal


line_count = 0
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}


def print_statistics():
    """
    Print statistics based on accumulated data
    """
    print(f'File size: {total_file_size}')
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f'{code}: {status_code_counts[code]}')


def signal_handler(sig, frame):
    """
    Handle keyboard interruption
    (CTRL + C)
    """
    print_statistics()
    sys.exit(0)


# setup signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
for line in sys.stdin:
    line = line.strip()

    match = re.match(
        r'^(\S+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$', line
    )

    if match:
        ip_address, status_code, file_size = match.groups()
        status_code = int(status_code)
        file_size = int(file_size)

        # Update metrics
        line_count += 1
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()
