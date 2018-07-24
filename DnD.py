#!/usr/bin/env python3
import random
import time
from misc.Characters import Wizard, SmallAnimal, LargeAnimal, MedNPC


def main():
    print_header()
    game_loop()


def print_header():
    print('*' * 70)
    print('  wizard game')
    print('*' * 70)
    print()


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1, 2, 1, 5),
        LargeAnimal('Tiger', 10, 20, 8, 150),
        Dragon('Red Dragon', 50, 75, 60, 300, 20, True),
        MedNPC('Ogre', 30, 15, 10, 200),
        MedNPC('Troll', 10, 15, 10, 240),
        MedNPC('Assassin', 30, 50, 10, 100),
        MedNPC('Soldier', 20, 30, 15, 150),
        MedNPC('Dwarf', 25, 40, 20, 200),
    ]

    # TODO: keep score for health
    hero = Wizard('Stanly', 20, 50, 20, 30, 30)

    while True:

        active_creature = random.choice(creatures)
        print('\nA level {} {} has appeared at the edge of the forest..'
              .format(active_creature.level, active_creature.name))
        print()

        cmd = input('Do you [A]ttack [R]un or [L]ook? \n')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                time.sleep(3)
                print('Our hero barely manages to escape to recover...')
                time.sleep(5)
                print('The hero is ready again for battle.')
        elif cmd == 'r':
            print('Our hero sneaks away to fight another day.')
        elif cmd == 'l':
            print('Our hero looks around the forest and sees:')
            for c in creatures:
                print(' A {} of level {}.'.format(c.name, c.level))
                time.sleep(2)
        else:
            print('exiting game')
            break

        if not creatures:
            print('\n\nThe forest has been cleared by the hero!')
            print()
            break


if __name__ == '__main__':
    main()
