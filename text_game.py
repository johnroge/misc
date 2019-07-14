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
    print('                                   v1.2')
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
    # TODO: give player change to rest and heal by % current health
    # TODO: create random items that can be used in game play
    # TODO: break some of these into discrete functions
    creatures = get_creatures()
    name = get_player_info()

    # name, level, health, defense, magic, wisdom
    player_1 = Wizard(name, 20, 500, 1, 1, 1)

    while True:

        active_creature = random.choice(creatures)
        print()
        print(f'A level {active_creature.level} {active_creature.name} '
              f'appears in the clearing...')

        cmd = input('--> Do you [A]ttack, [R]un away, [L]ook around or '
                    '[V]iew current player stats?')
        cmd = cmd.lower()
        if cmd == 'a':
            battle(player_1, active_creature, creatures)
        elif cmd == 'r':
            print(f'{player_1.name} bravely runs away!')
        elif cmd == 'l':
            print(f'{player_1.name} looks around and sees: ')
            for c in creatures:
                print(f' * A {c.name} of level {c.level}')
        elif cmd == 'v':
            print(f'NAME: {player_1.name}')
            print(f'LEVEL: {player_1.level}')
            print(f'HEALTH: {player_1.health}')
            print(f'DEFENSE: {player_1.defense}')
            print(f'MAGIC: {player_1.magic}')
            print(f'WISDOM: {player_1.wisdom}')
        else:
            print('Exiting game...')
            break

        if not creatures:
            print('-' * 45)
            print('The forest has been cleared of creatures!')
            print('-' * 45)


def battle(player, active_creature, creatures):
    # TODO: give player chance to run if below threshold
    # TODO: provide more detail in game play
    # TODO: increase player level based on winning

    while player.health >= 0 and active_creature.health >= 0:
        time.sleep(2)
        hero_attack = player.attack()
        creature_defense = active_creature.defensive_roll()
        if hero_attack >= creature_defense:
            print(f'You have inflicted {hero_attack} point of damage '
                  f'on the {active_creature.name}!')
            active_creature.health -= hero_attack
            if active_creature.health <= 0:
                creatures.remove(active_creature)
                print(f'You have killed the {active_creature.name}!')
                break
        else:
            print(f'The {active_creature.name} has dodged your attack...')

        time.sleep(2)
        creature_attack = active_creature.attack()
        player_defense = player.defensive_roll()
        if creature_attack >= player_defense:
            print(f'The {active_creature.name} has hit you with {creature_attack}'
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
