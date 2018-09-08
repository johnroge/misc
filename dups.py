#!/usr/bin/env python3
"""
putting together a rough framework to find duplicate files
v0.2 September 2018
"""
import os


# todo: take list of files that have equal size and compare their hash
def main():
    '''
    Get user input for two folders and then search for duplicate files
    based on file size; next will implement a hash check
    :return: Return a list of duplicate files
    '''
    folder_one = get_folder()
    folder_two = get_folder()
    duplicates = []
    files_1 = get_file_path(folder_one)
    files_2 = get_file_path(folder_two)
    for file in files_1:
        for item in files_2:
            if os.path.getsize(file) == os.path.getsize(item):
                duplicates.append(file)
                duplicates.append(item)
            else:
                continue

    print(duplicates)


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