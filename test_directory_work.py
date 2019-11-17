#!/usr/bin/env python3
"""
Author: JohRoge
Last Updated: 10/14/2019
version: .1
Notes: test file - walk a directory, find files over a certain size,
       use defaultdict, yield, lambda where possible
       write test case for each function
       use try/except wherever possible
"""
from collections import defaultdict


def main():
    """
    control flow for program
    :return: n/a
    """
    # TODO: create a placeholder database to pass through?
    pass


def main_menu():
    """
    user main menu
    :return: variable - option selected
    """
    # use dict as switch to build a menu
    switch_func_dict = {
        1: search_logic(),
        2: viewing_logic(),
        3: save_logic(),
        4: exit_script(),
    }

    print('Choose 1 - 4')
    print('1 search a folder')
    print('2 view results')
    print('3 save results')
    print('4 exit script')
    selection = input('>>> ')


def search_logic():
    """
    flow control for searching a directory
    :return: n/a - shows results to screen and then exits to main_menu
    """
    search_directory = get_search_folder()
    try:
        test_folder_path(search_directory)
    except ValueError:
        print('not a valid path')
        main_menu()

    scan_results = scan_folder(search_directory)
    display_largest_files(scan_results)
    main_menu()


def viewing_logic():
    """
    flow control for viewing results
    :return: n/a - show results to screen and exit to main_menu
    """
    pass


def save_logic():
    """
    flow control for saving offline data
    :return: n/a, saves to file and exits back to main_menu
    """
    pass


def get_search_folder():
    """
    get folder to search from user
    :return: variable - valid directory path
    """
    pass


def test_folder_path():
    """
    make sure path given by user is a valid path
    :return: boolean
    """
    pass


def scan_folder(folder):
    """
    scan folder and yield file names, sizes
    :param folder: folder to search
    :return: defaultdict (presumably)
    """
    pass


def display_largest_files(database, number_entries=5):
    """
    show largest files in a database, default to top 5 largest
    :param database: defaultdict
    :param number_entries: int
    :return: display largest N files
    """
    pass


def exit_script(database):
    """
    exit and save data if requested
    :param database: defaultdict
    :return: system exit
    """
    pass


def save_report(database):
    """
    save copy of current report
    :param database: defaultdict
    :return: boolean
    """
    pass


if __name__ == '__main__':
    main()