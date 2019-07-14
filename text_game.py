#!/usr/bin/env python3
"""
simple text game similar to dungeons and dragons
useful for practicing with classes, methods and flow control
"""

from game_characters import Wizard, Creature, LargeCreature,\
    MagicalCreature
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
        # name, level, health
        Creature('wolf', 5, 10),
        Creature('poisonous snake', 3, 5),
        Creature('elk', 5, 10),
        # name, level, health, magic
        MagicalCreature('goblin', 10, 15, 10),
        MagicalCreature('dark elf', 15, 30, 15),
        # name, level, health, magic
        LargeCreature('orc', 10, 20, 5),
        LargeCreature('dragon', 20, 50, 30),
    ]

    # name, level, health, magic
    hero = Wizard('Gandolf', 20, 100, 50)

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

        if not creatures:
            print('The forest has been cleared of creatures!')
            print()


if __name__ == '__main__':
    main()
