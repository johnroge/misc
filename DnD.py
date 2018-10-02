#!/usr/bin/env python3

import time
from Characters import *


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
        SmallAnimal('Toad', 1, 2, 1, 5, 1),
        LargeAnimal('Tiger', 10, 20, 8, 150, 1),
        Dragon('Red Dragon', 50, 75, 60, 300, 5),
        MedNPC('Ogre', 30, 15, 10, 200, 1),
        MedNPC('Troll', 10, 15, 10, 240, 1),
        MedNPC('Assassin', 30, 50, 10, 100, 1),
        MedNPC('Soldier', 20, 30, 15, 150, 1),
        MedNPC('Dwarf', 25, 40, 20, 200, 1),
    ]

    # TODO: get hero name from user
    hero = Wizard('Stanly', 20, 50, 20, 30, 30, 5)

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
            battle(hero, active_creature, creatures)
            if hero.is_alive:
                print('Our hero has killed the {} '.format
                      (active_creature.name))
            else:
                print("Crap ..... the creature ate the hero")
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


def battle(hero, creature, creatures):
    """
    Main battle function, called by hero's attack
    :param hero: current player
    :param creature: active creature
    :return:
    """
    match(hero, creature)
    if creature.is_alive:
        match(creature, hero)
    else:
        creatures.remove(creature)


def match(fighter1, fighter2):
    """
    Main battle function, called by hero's attack
    :param hero: current player
    :param creature: active creature
    :return:
    """
    fighter1_attack = fighter1.attack()
    fighter2_defense = fighter2.get_defensive_roll()

    time.sleep(2)
    print('{} attacks the {}!'.format(fighter1.name, fighter2.name))
    print('{} rolls a {}'.format(fighter1.name, fighter1_attack))
    print('{} rolls a {}'.format(fighter2.name, fighter2_defense))

    # call the hit_success function to determine a hit
    successful_hit = hit_success(fighter1_attack, fighter2_defense)
    if successful_hit:
        print('{} successfully hits the {} for {} points of damage!'
              .format(fighter1.name, fighter2.name, fighter1_attack))
        fighter2.take_damage(fighter1_attack)
    else:
        print('{} misses!'.format(fighter1.name))


def hit_success(attack_roll, defensive_roll):
    if attack_roll >= defensive_roll:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
