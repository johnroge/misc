#!/usr/bin/env python3
"""
Shamelessly stolen from stackoverflow (at least the important bits)
Last updated: 8/14/2019
Author: JohnR
Version 1.0
"""


def main():
    """
    flow control
    :return: none - writes to an output file for missing lines
    """
    a_file = get_file_a()
    b_file = get_file_b()
    write_out = get_outfile()

    with open(a_file, 'r') as file1:
        with open(b_file, 'r') as file2:
            difference = set(file1).difference(file2)

    difference.discard('\n')

    with open(write_out, 'w') as file_out:
        for line in difference:
            file_out.write(line)


def get_file_a():
    """
    first file to compare
    :return: file a
    """
    file_a = input('File A to check: ')
    return file_a


def get_file_b():
    """
    second file for comparison
    :return: file b
    """
    file_b = input('File B to check: ')
    return file_b


def get_outfile():
    """
    new file to write to for results of what is missing in second file
    :return: output file
    """
    outfile = input('File to write to: ')
    return outfile


if __name__ == '__main__':
    main()