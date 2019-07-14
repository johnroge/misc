#!/usr/bin/env python3
"""
simple text game similar to dungeons and dragons
useful for practicing with classes, methods and flow control
v1.3
"""

from game_characters import Wizard, Creature, LargeCreature,\
    MagicalCreature
import random
import time
import os


def main():
    print_header()
    game_loop()


def print_header():
    print()
    print('-' * 40)
    print('   WELCOME TO THE WIZARD GAME APP')
    print('                                   v1.3')
    print('-' * 40)
    print()


def get_creatures():
    # TODO: create a randomized set of creatures based on probability
    # TODO: randomize the creature stats within a certain range
    creatures = [
        # name, level, health, defense
        Creature('wolf', 5, 50, 5),
        Creature('poisonous snake', 3, 5, 2),
        Creature('elk', 5, 60, 5),
        # name, level, health, defense, magic
        MagicalCreature('goblin', 10, 70, 9, 8),
        MagicalCreature('dark elf', 15, 90, 15, 10),
        # name, level, health, defense, armor
        LargeCreature('orc', 10, 100, 12, 10),
        LargeCreature('dragon', 20, 500, 50, 50),
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
    player_1 = Wizard(name, 20, 200, 6, 5, 5)

    while True:

        active_creature = random.choice(creatures)
        print()
        print(f'A level {active_creature.level} {active_creature.name} '
              f'appears in the clearing...')

        cmd = input('--> Do you [A]ttack, [R]un away, [L]ook around or '
                    '[V]iew current player stats?\n ---> Press any '
                    'other key to exit game to console: ')
        cmd = cmd.lower()
        if cmd == 'a':
            os.system('cls' if os.name == 'nt' else 'clear')
            battle_loop(player_1, active_creature, creatures)
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


def battle_loop(player, active_creature, creatures):
    # TODO: give player chance to run if below threshold
    # TODO: provide more detail in game play
    # TODO: increase player level based on winning

    while player.health >= 0 and active_creature.health >= 0:
        player_attack(player, active_creature)
        if active_creature.health <= 0:
            creatures.remove(active_creature)
            print(f'The {active_creature.name} has released its mortal coil.')
        else:
            creature_attack(active_creature, player)

        # TODO: end game if health below 0
        if player.health <= 0:
            print(f'{player.name} has been killed in battle.')
            print('-' * 45)
            print('       GAME OVER')
            print('-' * 45)
            time.sleep(6)
            raise SystemExit
        elif player.health <= 30:
            print(f'{player.name} has been critically wounded, but manages '
                  f'to escape with his life.')
            time.sleep(5)
            break
        else:
            pass


def player_attack(player, active_creature):
    player_roll = player.attack_roll()
    creature_roll = active_creature.defensive_roll()
    print(f'Our hero has attacked the {active_creature.name}!')
    time.sleep(1)
    print(f'{player.name} rolls a {player_roll}, while the'
          f' {active_creature.name} rolls a {creature_roll} in defense...')
    time.sleep(1)

    if player_roll >= creature_roll:
        print(f'The creature sustains {player_roll} points of damage!')
        active_creature.health -= player_roll
    else:
        print(f'The wiley {active_creature.name} has dodged our attack...')

    os.system('cls' if os.name == 'nt' else 'clear')


def creature_attack(active_creature, player):
    creature_roll = active_creature.attack_roll()
    player_roll = player.defensive_roll()
    print(f'The {active_creature.name} fights back!')
    time.sleep(1)
    print(f'The {active_creature.name} has rolled a {creature_roll}, '
          f'while our hero {player.name} rolls a {player_roll}!')
    time.sleep(1)

    if creature_roll >= player_roll:
        print(f'{player.name} has taken {creature_roll} points of damage!')
        player.health -= creature_roll
    else:
        print(f'Our hero {player.name} manages to parry the attack...')

    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main()
