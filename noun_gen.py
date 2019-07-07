#!/usr/bin/env python3
# generate a list of nouns for memory test

import time
import os


def menu(prompt):

    while True:
        response = input(prompt)
        if response == '1':
            exit_program()
        elif response == '2':
            new_session()
        elif response == '3':
            show_all()
        else:
            print('Please enter a number between 1 and 3')


def options():
    user_prompt = (
        "\nWelcome to memory test\n"
        "Please choose from the following options:\n"
        "1: exit the program\n"
        "2: start a new session\n"
        "3: show the current list in full\n"
        ">>>>> "
    )

    return user_prompt


def exit_program():
    print("exiting program.....")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    raise SystemExit


def new_session():
    file_location = input('Please enter a source file:')
    number_nouns = input('How many words would you like to try?')




def show_all():
    pass


def get_noun_file():
    pass


def extract_nouns():
    pass


if __name__ == '__main__':
    current_words = []
    menu(options())
