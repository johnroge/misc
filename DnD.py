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
    name = input('What is your character name? ')
    name = name.title()
    # name, level, exp, weapon, health, defense, magic
    hero = Wizard(name, 9, 10, 3, 400, 2, 8)

    while True:
        active_creature = npc()
        print('\nA level {} {} has appeared at the edge of the forest..'
              .format(active_creature.level, active_creature.name))
        print()

        cmd = input('Do you [A]ttack, [R]un, [I]nventory or [W]ait')
        cmd = cmd.lower()
        if cmd == 'a':
            battle(hero, active_creature)
            if hero.is_alive:
                print('****** Our hero has killed the {}! *******'.format
                      (active_creature.name))
            else:
                print('OH NO! THE {} has killed our hero, {}!'.format(
                    active_creature.name, hero.name
                ))
                print('GAME OVER')
                break
        elif cmd == 'r':
            print('Our hero sneaks away to fight another day.')
        elif cmd == 'i':
            print('You currently have {} health and {} experience.'.format(
                hero.health, hero.exp
            ))
        elif cmd == 'w':
            print('The hero has decided to rest their wounds for a bit.')
            time.sleep(15)
            hero.health = hero.health * 1.2
        else:
            # TODO: implement a specific exit along with game stats
            print('exiting game')
            break


def npc():
    # shortcuts for common dice rolls
    r_3 = random.randint(1, 3)
    r_5 = random.randint(2, 5)
    r_8 = random.randint(2, 8)
    r_10 = random.randint(2, 10)
    r_13 = random.randint(3, 13)
    r_15 = random.randint(3, 15)
    r_20 = random.randint(3, 20)
    r_25 = random.randint(3, 25)
    r_30 = random.randint(4, 30)
    r_60 = random.randint(10, 60)
    r_100 = random.randint(20, 100)
    r_150 = random.randint(30, 150)
    r_200 = random.randint(40, 200)

    #        name - level - exp - weapon - health - defense
    creatures = [
        SmallAnimal('Toad', r_3, r_5, r_3, r_10, r_3),
        LargeAnimal('Tiger', r_8, r_13, r_10, r_100, r_15),
        Dragon('Red Dragon', r_15, r_30, r_15, r_200, r_60, fire=True),
        MedNPC('Ogre', r_5, r_5, r_8, r_60, r_20),
        MedNPC('Troll', r_8, r_8, r_8, r_100, r_25),
        MedNPC('Assassin', r_10, r_10, r_20, r_100, r_20),
        MedNPC('Soldier', r_8, r_8, r_8, r_60, r_15),
        MedNPC('Dwarf', r_15, r_20, r_25, r_100, r_30),
    ]
    creature = random.choice(creatures)
    return creature


def battle(hero, creature):
    """
    battle function calls match function if creature is still alive
    to fight, removes from main list of creatures if killed
    :param hero: current player
    :param creature: active creature
    :return: Winner of the battle, hero or the creature
    """
    while hero.is_alive and creature.is_alive:
        match(hero, creature)
        if creature.is_alive:
            match(creature, hero)
        else:
            hero.exp = hero.exp + creature.exp


def match(fighter1, fighter2):
    """
    main fighting function, called by battle function above
    :param fighter1: current player
    :param fighter2: active creature
    :return: Successful hit and damage or a miss
    """

    # get the respective attack and defense rolls
    fighter1_attack = fighter1.attack()
    fighter2_defense = fighter2.get_defensive_roll()

    # show user the results of the attack
    print('{} attacks {}!'.format(fighter1.name, fighter2.name))
    print('{} rolls a {}'.format(fighter1.name, fighter1_attack))
    time.sleep(2)
    print('{} rolls a {}'.format(fighter2.name, fighter2_defense))
    time.sleep(2)

    # call the hit_success function to determine a hit
    successful_hit = hit_success(fighter1_attack, fighter2_defense)
    if successful_hit:
        # show damage to user and deduct from loser's health
        print()
        print('***** {} successfully hits {} for {} points of damage!'
              .format(fighter1.name, fighter2.name, fighter1_attack))
        fighter2.take_damage(fighter1_attack)
        fighter1.exp += 1
        time.sleep(2)
    else:
        print()
        print('{} misses!'.format(fighter1.name))
        time.sleep(2)


def hit_success(attack_roll, defensive_roll):
    # determine hit success by pitting size of attack roll against
    # defensive roll
    if attack_roll >= defensive_roll:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
