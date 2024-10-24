#!/usr/bin/python3
""" 0. Log parsing """
import sys
import re


def print_stats(file_size_sum, status_count):
    """Print the file size and status code"""
    print(f"File size: {file_size_sum}")
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")


total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

pattren = (r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} -'
           r' \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\]'
           r' "GET /projects/260 HTTP/1\.1" \d+ \d+')
try:
    for line in sys.stdin:
        if re.match(pattren, line):

            parts = line.split()
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            total_size += file_size

            if status_code in status_count:
                status_count[status_code] += 1

            line_count += 1

            if line_count == 10:
                print_stats(total_size, status_count)
                line_count = 0

except KeyboardInterrupt:

    pass

finally:

    print_stats(total_size, status_count)
