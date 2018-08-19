#!/usr/bin/env python3

# sell movie tickets; age 3 and under are free, 4 - 12 is $10,
# and 13+ is $20.
# Get user age, number of tickets, which showing
# print out unique ID for receipt


def get_user_input():
    age = input('\n What is your age? ')
    age = int(age)
    ticket_count = input('\n How many tickets would you like? ')
    ticket_count = int(ticket_count)
    show_time = input('\ Which showing? ')
    return age, ticket_count, show_time


def check_age(age):
    if age <= 3:
        return 0
    elif age <= 12:
        return 10
    else:
        return 20


def check_movie_time():
    pass


def get_ticket_price():
    pass


def main():
    pass


if __name__ == '__main__':
    main()