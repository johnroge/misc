#!/usr/bin/env python3
"""
simple text game similar to dungeons and dragons
useful for practicing with classes, methods and flow control
"""

from game_characters import Wizard, Creature
import random
import time


def main():
    """

    :return:
    """
    print_header()
    game_loop()


def print_header():
    print()
    print('-' * 40)
    print('         WIZARD GAME APP')
    print('-' * 40)
    print()


def game_loop():
    creatures = [
        Creature('wolf', 5, 10),
        Creature('orc', 10, 20),
        Creature('goblin', 10, 15),
        Creature('dark elf', 15, 30),
        Creature('dragon', 20, 50),
    ]

    hero = Wizard('Gandolf', 20, 100)

    while True:

        active_creature = random.choice(creatures)
        print(f'A level {active_creature.level} {active_creature.name} '
              f'appears in the clearing...')

        cmd = input('--> Do you [A]ttack, [R]un away, or [L]ook around?')
        cmd = cmd.lower()
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                time.sleep(2)
                print('Our hero runs and hides to recover his wounds..')
                time.sleep(5)
                print()
                print('Our hero has returned, rested and ready for'
                      ' adventure!')
        elif cmd == 'r':
            print('Our hero runs away to fight another day!')
        elif cmd == 'l':
            print('The Wizard looks around and sees: ')
            for c in creatures:
                print(f' * A {c.name} of level {c.level}')
        else:
            print('Exiting game...')
            break


if __name__ == '__main__':
    main()
