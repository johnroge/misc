#!/usr/bin/env python3
"""
Author: JohRoge
Last Updated: 10/14/2019
version: .1
Notes: test file - walk a directory, find files over a certain size,
       use defaultdic, yield, lambda where possible
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
    # TODO: add default parameters below?
    menu_dict = {'1': scan_folder(),
                 '2': save_report(),
                 '3': largest_files(),
                 'q': exit_script()}

    main_text = '\n'.join((
        'Choose from the following:',
        '"1" - scan a folder,',
        '"2" - save a Report,',
        '"3" - see largest files',
        '"q" to Quit: '
      ))
    # TODO: fix this, look for better examples
    while True:
        print('\nMain Menu:')
        response = input(main_text)
        print()
        try:
            if response == 'q':
                print('exiting program.')
                menu_dict[response]()
        except KeyError:
            print('\nThat selection is invalid. Please try again.')


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


def largest_files(database, number_entries=5):
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