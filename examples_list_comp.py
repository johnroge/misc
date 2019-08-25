#!/usr/bin/env python3
"""
list comprehensions, lambda, map, filter and reduce
NOTES: ord will return the ASCII code for a character
"""


def main():
    """
    flow control to demonstrate some basic functions
    :return: none
    """
    # create some standard variables to be used - string, range, etc.
    some_string = 'spamspamspam'
    number_range = range(1, 102)
    matrix_alpha = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
    matrix_beta = [[2, 2, 2, 2],
                    [3, 3, 3, 3],
                    [4, 4, 4, 4]]

    # run each example once
    basic_list_comp(some_string)
    use_map(some_string)
    collect_squares()
    use_lambda()
    use_filter()
    nested_for_loop_comp()
    fizz_buzz(number_range)
    get_diagonal(matrix_alpha)


def use_map(string_value):
    """
    use map instead of a list comp to convert characters to ASCII
    :param string_value: any string value
    :return: none
    """
    print('*' * 55)
    print('using map: ')
    map_results = list(map(ord, string_value))
    print(map_results)
    print()


def basic_list_comp(string_value):
    """
    use a list comp to replace characters in a string with their ASCII
    equivalent
    :param string_value: any string value
    :return: none
    """
    print('*' * 55)
    print('basic list comprehension: ')
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


def fizz_buzz(some_range):
    """
    fizzbuzz exercise, but using filter and lambda to find the numbers
    :param some_range: any range of integers
    :return: None
    """
    print('*' * 55)
    print('fizzbuzz exercise using map and lambda to find divisible numbers: ')
    div_5 = list(filter((lambda x: x % 5 == 0), some_range))
    div_3 = list(filter((lambda x: x % 3 == 0), some_range))
    for x in some_range:
        if x in div_5 and x in div_3:
            print('fizzbuzz')
        elif x in div_3:
            print('fizz')
        elif x in div_5:
            print('buzz')
        else:
            print(x)


def get_diagonal(matrix):
    """
    use list comp to pull diagonal numbers from a given matrix
    :param matrix: matrix list of numbers
    :return: none
    """
    print('*' * 55)
    print('use list comp to print the diagonal numbers from a matrix:')
    print([matrix[i][i] for i in range(len(matrix))])
    print([matrix[i][len(matrix)-1-i] for i in range(len(matrix))])


if __name__ == '__main__':
    main()