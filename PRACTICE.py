#!/usr/bin/env python3
import os
import cat_service


def main():
    print_header()
    folder = get_folder()
    print('found or created folder: ' + folder)
    download(folder)


def print_header():
    print('-' * 40)
    print('               TEST FILE')
    print('-' * 40)


def get_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'TEST_FOLDER'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download(folder):
    print('Connecting to server to download cats..')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat {}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)

    print('....done.')


if __name__ == '__main__':
    main()