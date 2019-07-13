#!/usr/bin/env python3
"""
simple text game similar to dungeons and dragons
useful for practicing with classes, methods and flow control
"""


def main():
    """

    :return:
    """
    print_header()
    game_loop()


def print_header():
    print('-' * 60)
    print('         WIZARD GAME APP')
    print('-' * 60)
    print()


def game_loop():

    while True:

        cmd = input('Do you [A]ttack, [R]un away, or [L]ook around?')
        cmd = cmd.lower()
        if cmd == 'a':
            print('attack pressed')
        elif cmd == 'r':
            print('run pressed')
        elif cmd == 'l':
            print('looks around')
        else:
            print('Exiting game...')


if __name__ == '__main__':
    main()
