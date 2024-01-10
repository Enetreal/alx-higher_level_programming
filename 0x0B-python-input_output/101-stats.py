#!/usr/bin/python3


import sys
from collections import defaultdict

def compute_metrics():
    """
    Reads stdin line by line and computes metrics.
    Prints total file size and number of lines by status code every 10 lines or after a keyboard interruption.
    """
    total_file_size = 0
    status_code_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) >= 9:
                file_size = int(parts[-1])
                total_file_size += file_size
                status_code = parts[-2]
                status_code_counts[status_code] += 1

            if line_count % 10 == 0:
                print(f"Total file size: {total_file_size}")
                for code in sorted(status_code_counts.keys()):
                    print(f"{code}: {status_code_counts[code]}")

    except KeyboardInterrupt:
        print(f"Total file size: {total_file_size}")
        for code in sorted(status_code_counts.keys()):
            print(f"{code}: {status_code_counts[code]}")

if __name__ == "__main__":
    compute_metrics()
