#!/usr/bin/env python3


def main():
    print_header()
    run_event_loop()


def print_header():
    print('-' * 50)
    print('    Journal App')
    print('-' * 50)


def run_event_loop():

    print('What would you like to do?')
    cmd = None

    while cmd != 'x':
        cmd = input('[L]ist, [A]dd or e[X]it? ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            print('l')
        elif cmd == 'a':
            print('a')
        elif cmd == 'x':
            print("sorry, we can't understand '{}'.".format(cmd))

    print('all done, have a nice day')


def list_entries():
    pass


def add_entry():
    pass


if __name__ == '__main__':
    main()
