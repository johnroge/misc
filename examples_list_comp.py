#!/usr/bin/env python3
"""
list comprehensions, map, filter and reduce
NOTES: ord will return the ASCII code for a character
"""


def main():
    """
    flow control to demonstrate some basic functions
    :return: none
    """
    some_string = 'spam'
    list_comp(some_string)
    use_map(some_string)
    expression(some_string)
    collect_squares()
    use_lambda()
    use_filter()
    nested_for_loop_comp()


def list_comp(string_value):
    results = []
    print('*' * 55)
    print('basic for loop: ')
    for x in string_value:
        results.append(ord(x))
        print(results)
        print()


def use_map(string_value):
    print('*' * 55)
    print('using map: ')
    map_results = list(map(ord, string_value))
    print(map_results)
    print()


def expression(string_value):
    print('*' * 55)
    print('using an expression: ')
    results = [ord(x) for x in string_value]
    print(results)
    print()


def collect_squares():
    print('*' * 55)
    print('print the square of a range of numbers: ')
    results = [x ** 2 for x in range(10)]
    print(results)
    print()


def use_lambda():
    print('*' * 55)
    print('print squares using a lambda instead: ')
    results = list(map((lambda x: x ** 2), range(10)))
    print(results)
    print()


def use_filter():
    print('*' * 55)
    print('using filter and lambda to pick out even numbers: ')
    results = list(filter((lambda x: x % 2 == 0), range(18)))
    print(results)
    print()


def nested_for_loop_comp():
    print('*' * 55)
    print('nesting a for loop in a list comprehension: ')
    results = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
    print(results)
    print()


if __name__ == '__main__':
    main()