#!/usr/bin/env python3
"""
Author : runner <runner@d54b9702764e>
Date   : 2023-01-28
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        help='letter(s)',
                        nargs='+',
                        type=str)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_name = args.file
    line_dict = {}
    for line in file_name:
        line_dict[line[0].upper()] = line.rstrip()

    for letter in args.letter:
        if letter.upper() in line_dict:
            print(line_dict[letter.upper()])
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
