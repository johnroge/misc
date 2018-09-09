#!/usr/bin/env python3
"""
Find duplicate files between two given folders first based on file size
and then based on md5 hash of each file.
Using file size first to increase speed when searching very large folders.
v0.2 September 2018
"""
import os
import hashlib


def main():
    '''
    :return: Return a list of duplicate files
    '''
    folder_one = get_folder()
    folder_two = get_folder()
    list_one = []
    list_two = []
    final_list = []
    files_1 = get_file_path(folder_one)
    files_2 = get_file_path(folder_two)
    for file in files_1:
        for item in files_2:
            if os.path.getsize(file) == os.path.getsize(item):
                list_one.append(file)
                list_two.append(item)
            else:
                continue

    for file in list_one:
        for item in list_two:
            if get_hash(file) == get_hash(item):
                final_list.append(file)
                final_list.append(item)

    print(final_list)


def get_hash(file):
    hash = hashlib.md5()
    with open(file, 'rb') as afile:
        buf = afile.read()
        hash.update(buf)

    return hash.hexdigest()


def get_file_path(directory):
    '''
    :param directory: folder to iterate
    :return: return full path of each file in folder
    '''
    file_paths = []

    for root, directories, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_paths.append(file_path)

    return file_paths


# todo: sanitize user input, give syntax
def get_folder():
    '''
    :return: Return absolute path of a chosen folder
    '''
    folder = input('Folder to search: ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


if __name__ == '__main__':
    main()