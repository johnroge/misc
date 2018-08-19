#!/usr/bin/env python3
import csv
import os


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('*' * 55)
    print('                 REAL ESTATE APP')
    print('*' * 55)


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                 'SacramentoTransactions.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        for row in reader:
            print(type(row), row)
            print("Bed count: {}".format(row['beds']))


def query_data(data):
    pass


if __name__ == '__main__':
    main()
