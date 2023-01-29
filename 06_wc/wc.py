#!/usr/bin/env python3
"""
Author : runner <runner@7741a07f3dbe>
Date   : 2023-01-28
Purpose: Rock the Casbah
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        help='Inout Files',
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    total_lines, total_bytes, total_words = 0, 0, 0
    for fh in args.file:
        num_lines, num_bytes, num_words = 0, 0, 0
        for line in fh:
            num_lines += 1
            num_bytes += len(line)
            num_words += len(line.split())

        total_lines += num_lines
        total_bytes += num_bytes
        total_words += num_words

        print(f'{num_lines:8}{num_words:8},{num_bytes:8} {fh.name}')

    if len(args.file) > 1:
        print(f'{total_lines:8}{total_words:8},{total_bytes:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
