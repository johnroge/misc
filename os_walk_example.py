#!/usr/bin/env python

import os


def walk_tree(starting_folder):
    for root, dirs, files in os.walk(starting_folder, topdown=True):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))


def main():
    f1 = input('Starting folder? ')
    walk_tree(f1)


if __name__ == '__main__':
    main()
