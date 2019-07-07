#!/usr/bin/env python3
# generate a list of nouns for memory test

import time
import os
import random


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
    print("\nexiting program.....")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    raise SystemExit


def new_session():
    file_location = input('Please enter a source file:')
    number_nouns = int(input('How many words would you like to try?'))

    words = extract_nouns(file_location, number_nouns)

    os.system('cls' if os.name == 'nt' else 'clear')
    print('Ready? Starting in 3..')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    for word in words:
        print(word)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')


def show_all():
    pass


def extract_nouns(file_location, number_nouns):
    noun_list = []
    current_words = []
    with open(file_location, 'r') as infile:
        for line in infile.readlines():
            noun_list.append(line.strip("\n"))

    counter = number_nouns
    while counter >= 1:
        current_words.append(random.choice(noun_list))
        counter -= 1

    return current_words


if __name__ == '__main__':
    menu(options())
