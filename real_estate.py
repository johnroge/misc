#!/usr/bin/env python3
"""
basic data manipulation using a csv file containing historical
real-estate data
"""
import csv
import os
from data_types import Purchase
try:
    import statistics
except:
    import py2_statistics as statistics


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('*' * 65)
    print('*' * 65)
    print('       Real Estate Data Mining App')
    print('*' * 65)
    print('*' * 65)
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoTransactions.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


def query_data(data):
    data.sort(key= lambda p: p.price)
    high_purchase = data[-1]
    print('The most expensive house is ${:,} with {} beds and {} baths.'
          .format(high_purchase.price, high_purchase.beds, high_purchase.
                  baths))
    low_purchase = data[0]
    print('The least expensive house is ${:,} with {} beds and {} baths'
          .format(low_purchase.price, low_purchase.beds, low_purchase.baths))

    prices = [
        p.price
        for p in data
    ]

    avg_price = statistics.mean(prices)
    print('Average home price is ${:,}'.format(int(avg_price)))

    two_bed_homes = [
        p
        for p in data
        if p.beds == 2
    ]

    avg_price = statistics.mean([p.price for p in two_bed_homes])
    avg_baths = statistics.mean([p.baths for p in two_bed_homes])
    avg_sqft = statistics.mean([p.sq__ft for p in two_bed_homes])
    print('Average 2 bedroom home is ${:,}, baths={}, sq ft={:,}'
          .format(int(avg_price), round(avg_baths, 1), round(avg_sqft, 1)))


if __name__ == '__main__':
    main()


