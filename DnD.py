#!/usr/bin/env python3

import time
from Characters import *


def print_header():
    print('*' * 40)
    print('*' * 40)
    print('               wizard game')
    print('*' * 40)
    print('*' * 40)
    print()


def main():
    """
    Core game loop; identifies all the characters in play
    along with the main player (hero) and manages the end
    to end game play
    :return:
    """
    print_header()

    # TODO: generate a random, ongoing list of creatures based on %
    # name, level, exp, weapon, health, defense
    creatures = [
        SmallAnimal('Toad', 1, 2, 1, 5, 1),
        LargeAnimal('Tiger', 10, 20, 8, 300, 1),
        Dragon('Red Dragon', 50, 75, 60, 1000, 5, fire=True),
        MedNPC('Ogre', 30, 15, 10, 200, 1),
        MedNPC('Troll', 10, 15, 10, 300, 1),
        MedNPC('Assassin', 30, 50, 10, 400, 1),
        MedNPC('Soldier', 20, 30, 15, 150, 1),
        MedNPC('Dwarf', 25, 40, 20, 300, 1),
    ]

    name = input('What is your character name? ')
    # name, level, exp, weapon, health, defense, magic
    hero = Wizard(name, 20, 50, 20, 800, 30, 5)

    while True:
        """
        Pulls a random creature from the creatures list and then
        gives the hero 3 options - look, run, attack
        """

        active_creature = random.choice(creatures)
        print('You currently have {} health left.'.format(hero.health))
        print('\nA level {} {} has appeared at the edge of the forest..'
              .format(active_creature.level, active_creature.name))
        print()

        cmd = input('Do you [A]ttack [R]un or [L]ook? \n')
        cmd = cmd.lower()
        if cmd == 'a':
            battle(hero, active_creature, creatures)
            if hero.is_alive:
                print('Our hero has killed the {}!'.format
                      (active_creature.name))
            else:
                print('OH NO! THE {} has killed our hero, {}!'.format(
                    active_creature.name, hero.name
                ))
                print('GAME OVER')
                break
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
            print('YOU WIN!')
            print()
            break


def battle(hero, creature, creatures):
    """
    battle function calls match function if creature is still alive
    to fight, removes from main list of creatures if killed
    :param hero: current player
    :param creature: active creature
    :param creatures: full list of creatures to battle
    :return:
    """
    match(hero, creature)
    if creature.is_alive:
        match(creature, hero)
    else:
        creatures.remove(creature)


def match(fighter1, fighter2):
    """
    main fighting function, called by battle function above
    :param fighter1: current player
    :param fighter2: active creature
    :return:
    """
    fighter1_attack = fighter1.attack()
    fighter2_defense = fighter2.get_defensive_roll()

    print('{} attacks the {}!'.format(fighter1.name, fighter2.name))
    print('{} rolls a {}'.format(fighter1.name, fighter1_attack))
    time.sleep(2)
    print('{} rolls a {}'.format(fighter2.name, fighter2_defense))
    time.sleep(2)

    # call the hit_success function to determine a hit
    successful_hit = hit_success(fighter1_attack, fighter2_defense)
    if successful_hit:
        print('{} successfully hits the {} for {} points of damage!'
              .format(fighter1.name, fighter2.name, fighter1_attack))
        fighter2.take_damage(fighter1_attack)
        time.sleep(2)
    else:
        print('{} misses!'.format(fighter1.name))
        time.sleep(2)


def hit_success(attack_roll, defensive_roll):
    if attack_roll >= defensive_roll:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
