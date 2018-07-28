#!/usr/bin/env python3

import time
from misc.Characters import *


def main():
    print_header()
    get_hero_name()
    game_loop()


def print_header():
    print('*' * 70)
    print('*' * 70)
    print('  wizard game')
    print('*' * 70)
    print('*' * 70)
    print()


def get_hero_name():
    pass


def game_loop():
    """
    Core game loop; identifies all the characters in play
    along with the main player (hero) and manages the end
    to end game play
    :return:
    """

    # TODO: generate a random, ongoing list of creatures based on %
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

    # TODO: get hero name from user
    hero = Wizard('Stanly', 20, 50, 20, 30, 30)

    while True:
        """
        Pulls a random creature from the creatures list and then
        gives the hero 3 options - look, run, attack
        """

        active_creature = random.choice(creatures)
        print('\nA level {} {} has appeared at the edge of the forest..'
              .format(active_creature.level, active_creature.name))
        print()

        # TODO: sanitize user input
        cmd = input('Do you [A]ttack [R]un or [L]ook? \n')
        if cmd == 'a':
            if battle(hero, active_creature):
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
            # TODO: implement a specific exit along with game stats
            print('exiting game')
            break

        if not creatures:
            print('\n\nThe forest has been cleared by the hero!')
            print()
            break


def battle(hero, creature):
    """
    Main battle function, called by hero's attack
    :param hero: current player
    :param creature: active creature
    :return:
    """
    # get everyone's roll first and store in a variable
    creature_defense = creature.get_defensive_roll()
    creature_attack = creature.attack()
    hero_attack = hero.attack()
    hero_defense = hero.get_defensive_roll()

    print('Our hero attacks the {}!'.format(creature.name))
    print('You roll a: {}'.format(hero_attack))
    print('{} rolls a: {}'.format(creature.name, creature_defense))

    # call the hit_success function to determine a hit
    successful_hit = hit_success(hero_attack, creature_defense)
    if successful_hit:
        print('Hero successfully hits the {} for {} points of damage!'
              .format(creature.name, hero_attack))
        # TODO: reduce X health in damage from creature
        # TODO: if creature health >=0, eliminate creature
        # TODO:    -> then assign exp points to hero and return to main
        # TODO: else: creature now attacks hero

    else:
        print('Hero misses!')
        # TODO: creature attacks hero


def hit_success(attack_roll, defensive_roll):
    if attack_roll >= defensive_roll:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
