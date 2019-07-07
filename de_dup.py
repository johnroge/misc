#!/usr/bin/env python3
"""
traverse a given directory structure and identify duplicate files
version .1
last updated 3/2019
"""


def main():
    """
    create a dict using each file hash as key and value is full file path
    :return: main program loop
    """
    main_db = {}
    directory = get_directory()

    for file in directory:
        file_hash = get_file_hash(file)
        if file_hash in main_db:
            main_db.setdefault(file_hash, []).append(file)




def get_directory():
    """
    Need to get the correct file path with sys or os
    :return: properly formatted directory path
    """
    my_dir = input('Please enter a folder: ')
    return my_dir


def get_file_hash(some_file):
    """
    run a distinct file through the md5 checksum
    :return: md5 checksum value
    """
    check_sum =
    return check_sum


def write_results():
    """
    Give an option to either print or save results to a file
    :return: None
    """
    pass


if __name__ == '__main__':
    main()
