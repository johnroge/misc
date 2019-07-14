#!/usr/bin/env python3
"""
simple text game similar to dungeons and dragons
useful for practicing with classes, methods and flow control
v1.0
"""

from game_characters import Wizard, Creature, LargeCreature,\
    MagicalCreature
import random
import time


def main():
    print_header()
    game_loop()


def print_header():
    print()
    print('-' * 40)
    print('   WELCOME TO THE WIZARD GAME APP')
    print('                                   v1.0')
    print('-' * 40)
    print()


def get_creatures():
    # TODO: create a randomized set of creatures based on probability
    # TODO: randomize the creature stats within a certain range
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

    return creatures


def get_player_info():
    # TODO: track player health
    player_name = input('What is your name, hero? ')
    return player_name.capitalize()


def game_loop():

    creatures = get_creatures()
    name = get_player_info()

    # name, level, health, magic
    player_1 = Wizard(name, 20, 100, 50)

    while True:

        active_creature = random.choice(creatures)
        print(f'A level {active_creature.level} {active_creature.name} '
              f'appears in the clearing...')

        cmd = input('--> Do you [A]ttack, [R]un away, or [L]ook around?')
        cmd = cmd.lower()
        if cmd == 'a':
            if player_1.attack(active_creature):
                creatures.remove(active_creature)
            else:
                time.sleep(2)
                print(f'Our hero {player_1.name} runs and hides to '
                      f'recover his wounds..')
                time.sleep(5)
                print()
                print(f'Our hero {player_1.name} has returned, rested '
                      f'and ready for another adventure!')
        elif cmd == 'r':
            print(f'{player_1.name} bravely runs away!')
        elif cmd == 'l':
            print(f'{player_1.name} looks around and sees: ')
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
