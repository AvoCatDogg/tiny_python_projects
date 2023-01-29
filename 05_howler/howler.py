#!/usr/bin/env python3
"""
Author : runner <runner@00c093ba08f3>
Date   : 2023-01-26
Purpose: Rock the Casbah
"""
import os
import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler.py (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        help='Output filename',
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + '\n')
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
