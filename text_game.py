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
        # name, level, health, defense
        Creature('wolf', 5, 100, 5),
        Creature('poisonous snake', 3, 25, 2),
        Creature('elk', 5, 300, 5),
        # name, level, health, defense, magic
        MagicalCreature('goblin', 10, 350, 9, 8),
        MagicalCreature('dark elf', 15, 450, 15, 10),
        # name, level, health, defense, armor
        LargeCreature('orc', 10, 500, 12, 10),
        LargeCreature('dragon', 20, 4_000, 50, 50),
    ]

    return creatures


def get_player_info():
    player_name = input('What is your name, hero? ')
    return player_name.capitalize()


def game_loop():
    creatures = get_creatures()
    name = get_player_info()

    # name, level, health, defense, magic, wisdom
    player_1 = Wizard(name, 20, 500, 10, 50, 10)

    while True:

        active_creature = random.choice(creatures)
        print()
        print(f'A level {active_creature.level} {active_creature.name} '
              f'appears in the clearing...')

        cmd = input('--> Do you [A]ttack, [R]un away, or [L]ook around?')
        cmd = cmd.lower()
        if cmd == 'a':
            battle(player_1, active_creature)
            # TODO: determine results and next steps
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
            print('-' * 45)
            print('The forest has been cleared of creatures!')
            print('-' * 45)


def battle(player, creature):
    # TODO: remove creature from list if defeated
    # TODO: give player chance to run if below threshold
    # TODO: slow down game play and provide more detail

    while player.health >= player.health * .3:
        hero_attack = player.attack()
        creature_defense = creature.defensive_roll()
        if hero_attack >= creature_defense:
            print(f'You have inflicted {hero_attack} point of damage '
                  f'on the {creature.name}!')
            creature.health -= hero_attack
            if creature.health <= 0:
                print(f'You have killed the {creature.name}!')
                break
        else:
            print(f'The {creature.name} has dodged your attack...')

        creature_attack = creature.attack()
        player_defense = player.defensive_roll()
        if creature_attack >= player_defense:
            print(f'The {creature.name} has hit you with {creature_attack}'
                  f' points of damage!')
            player.health -= creature_attack
            if player.health <= 0:
                print(f'Our hero {player.name} has been mortally wounded; '
                      f' will he be able to survive to fight another day?')
                player.health = 1
                break
        else:
            print(f'{player.name} has dodged the attack!')


if __name__ == '__main__':
    main()
