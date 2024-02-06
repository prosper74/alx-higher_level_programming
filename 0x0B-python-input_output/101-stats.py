#!/usr/bin/python3
"""
This module is part of the Python Input Output project.
Reads stdin line by line and computes metrics
"""


import sys


def print_metrics(total_size, status_codes):
    """
    A function that reads stdin line by line and computes metrics
    :param total_size: total size of the file.
    :param status_codes: status codes of the file
    """
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


try:
    count = 0
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0,
                    '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

    for line in sys.stdin:
        count += 1
        parts = line.split()
        total_size += int(parts[-1])
        status_codes[parts[-2]] += 1

        if count % 10 == 0:
            print_metrics(total_size, status_codes)

    print_metrics(total_size, status_codes)

except KeyboardInterrupt:
    print_metrics(total_size, status_codes)
