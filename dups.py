#!/usr/bin/env python3
"""
putting together a rough framework to find duplicate files
v0.1 August 2018
"""
import optparse


def main():
    # show user instructions
    # get user input of two folders to check
    # allow user to request sub-directories for either/ both folders
    # first look for common file sizes for a given file
    # from the resulting set of files that have the same size,
    # check for a common file hash
    # print out list of duplicate files for the end user


def get_user_input():
    # sample code for getting input and arguments
    parser = optparse.OptionParser()
    parser.add_option('-s', '--subdirectories',
                      help='include subdirectories of the folder')
    (options, arguments) = parser.parse_args()
    return options


def check_file_size(file01, file02):
    # use list comprehension and generator here
    pass


def check_file_hash(file01, file02):
    # use list comprehension and generator here
    pass


if __name__ == '__main__':
    main()
