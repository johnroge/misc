#!/usr/bin/env python3
"""
Important bits stolen from stackoverflow - sue them, not me.
Checks file a against file b to see what is missing from file b, then
writes results of missing lines to output file.
Last updated: 8/14/2019
Author: JohnR
Version 1.0
"""


def main():
    """
    flow control and core logic
    :return: none - writes to an output file for missing lines
    """
    a_file = get_file_a()
    b_file = get_file_b()
    write_out = get_outfile()
    compare_files(a_file, b_file, write_out)


def compare_files(file1, file2, output_file):
    with open(file1, 'r') as file_1:
        with open(file2, 'r') as file_2:
            difference = set(file_1).difference(file_2)

    difference.discard('\n')

    with open(output_file, 'w') as file_out:
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
