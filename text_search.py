#!/usr/bin/env python3

"""
Search for a given text string in a given folder
Uses yield generator to reduce memory footprint and improve speed.
version 1.1
Aug 2018

NOTES:
Changed utf-8 encoding to latin-1 and it works; unclear on the difference
More info here:
http://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html
"""
import os
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')


def main():
    """
    Core program logic, gets user input and then counts number of matches
    :return: Total number of matches, but not location or context
    """
    print_header()
    folder = get_folder()
    if not folder:
        print('Sorry, we cannot find that location.')
        return

    text = get_search_text()
    if not text:
        print('We need a search phrase, please.')
        return

    matches = search_folders(folder, text)
    match_count = 0
    for m in matches:
        match_count += 1

    print("Found {:,} matches.".format(match_count))


def print_header():
    print('*' * 40)
    print('     file search app')
    print('*' * 40)
    print()


def get_folder():
    """
    Get user input for top level folder to search.
    :return: Return absolute path of that folder to main()
    """
    folder = input('Folder to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text():
    """
    Get single text string to search for and convert to lower case.
    :return: Return lower case text string to main()
    """
    text = input('Text to search for: ')
    return text.lower()


def search_folders(folder, text):
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, text)
        else:
            yield from search_file(full_item, text)


def search_file(filename, search_text):
    with open(filename, 'r', encoding='latin-1') as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line=line_num, file=filename, text=line)
                yield m


if __name__ == '__main__':
    main()