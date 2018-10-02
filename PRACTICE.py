#!/usr/bin/env python3

import os


def main():
    folder = get_folder()
    if not folder:
        print('Sorry we cannot search that location.')
        return

    text = get_text()
    if not text:
        print('need to search for something....')
        return

    search_file(folder, text)


def get_folder():
    folder = input('What folder would you like to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_text():
    text = input('Search phrase ')
    return text


def search_file(folder, text):
    print('would search {} for {}.'.format(folder, text))


if __name__ == '__main__':
    main()
