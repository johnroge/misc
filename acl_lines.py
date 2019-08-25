#!/usr/bin/env python3
"""
quick script to renumber acl lines in multiple of 10
Author: JohnR
Last Touched: 8/20/2019
Version .01
"""


def main():
    """
    flow control
    :return: None - output new file with a numbered ACL list
    """
    infile, outfile = get_user_input()
    convert_file(infile, outfile)


def get_user_input():
    """
    Get user input for file to convert and file to write to
    :return: two variables, input file and results file
    """
    input_file = input('File to convert: ')
    output_file = input('New file to write results to: ')

    return input_file, output_file


def convert_file(file_input, file_output):
    """
    Should be able to do all conversion in one function, at least to start
    :return: None - writes to a results file
    """
    with open(file_input, 'r') as fin, open(file_output, 'w') as fout:
        # getting closer but need to split on something else
        # guessing: split into bytearray or similiar, check isdigit, then remove?
        for line in fin.readlines():
            line.split()
            tmp_line = line[2:]
            fout.write(tmp_line)


if __name__ == '__main__':
    main()
