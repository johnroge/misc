#!/usr/bin/env python3
# practice file for checking for missing subnets


def main():
    a_file = get_file_a()
    b_file = get_file_b()
    write_out = get_outfile()

    with open(a_file, 'r') as file1:
        with open(b_file, 'r') as file2:
            same = set(file1).difference(file2)

    same.discard('\n')

    with open(write_out, 'w') as file_out:
        for line in same:
            file_out.write(line)


def get_file_a():
    file_a = input('File A to check: ')
    return file_a


def get_file_b():
    file_b = input('File B to check: ')
    return file_b


def get_outfile():
    outfile = input('File to write to: ')
    return outfile


if __name__ == '__main__':
    main()