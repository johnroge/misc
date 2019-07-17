#!/usr/bin/env python3
"""
simple text game similar to dungeons and dragons
useful for practicing with classes, methods and flow control
v2.0
"""

from game_characters import Wizard, Creature, LargeCreature,\
    MagicalCreature, Dragon
import random
import time
import os
# TODO: create random items that can be used in game play
# TODO: create decorator for sanitizing input
# TODO: use recursion
# TODO: use lambda function
# TODO: use list comp
# TODO: use generator
# TODO: use *args and *kwargs


def main():
    """
    Initial flow control that initiates the game
    :return: None
    """
    print_header()
    player = get_player_info()
    creatures = get_creatures()
    game_loop(player, creatures)


def current_monster(creature):
    """
    Info regarding current active creature faced by player
    :param creature: active creature
    :return: None
    """
    print()
    print(f'A level {creature.level} {creature.name} '
          f'appears in the clearing...')


def print_header():
    """
    Generic game header
    :return: None
    """
    clear_screen()
    print()
    print('-' * 40)
    print('   WELCOME TO THE WIZARD GAME APP')
    print('                                   v2.0')
    print('-' * 40)
    print()


def get_creatures():
    """
    Generate master list of available creatures to hunt
    :return: List of creature instances
    """
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
        # name, level, health, defense, armor, fire
        Dragon('Red Dragon', 20, 800, 20, 20, True),
        Dragon('Black Dragon', 15, 600, 15, 15, False)
    ]

    return creatures


def get_player_info():
    """
    Get user input for new player
    :return: return an instance of Wizard as player
    """
    # TODO: Need to randomize some of these characteristics or provide
    # TODO: more options to the user, maybe other character classes
    name = input('What is your name, hero? ')
    name = name.capitalize()
    player = Wizard(name,
                    20,  # level
                    300, # health
                    5,   # defense
                    5,   # magic
                    5)   # wisdom

    return player


def game_loop(player, creatures):
    """
    Core game logic representing player actions and consequences
    :param player: current player
    :param creatures: list of available creatures
    :return: None
    """
    while True:
        active_creature = random.choice(creatures)
        current_monster(active_creature)
        cmd = user_action()

        if cmd == 'a':
            battle_loop(player, active_creature, creatures)
        elif cmd == 'r':
            print(f'{player.name} bravely runs away!')
        elif cmd == 'l':
            look_around(player, creatures)
        elif cmd == 'v':
            print(player.__repr__())
        else:
            game_exit()

        if not creatures:
            game_won()


def user_action():
    """
    Current menu for player choices
    :return: cmd
    """
    # TODO: create real menu
    # TODO: give player chance to rest and heal by % current health
    # TODO: add feature for loading and saving game
    cmd = input('--> Do you [A]ttack, [R]un away, [L]ook around or '
                '[V]iew current player stats?\n ---> Press any '
                'other key to exit game to console: ')
    cmd = cmd.lower()
    return cmd


def game_exit():
    """
    Exit game
    :return: None
    """
    # TODO: add save feature
    raise SystemExit


def battle_loop(player, active_creature, creatures):
    """
    Flow control for player - creature fight
    :param player: current active player
    :param active_creature: current creature being attacked
    :param creatures: full list of available creatures
    :return: None
    """

    win_bonus = round(active_creature.level * .5)
    while player.health >= 0 and active_creature.health >= 0:
        player_attack(player, active_creature)
        if active_creature.health <= 0:
            creatures.remove(active_creature)
            print(f'The {active_creature.name} has released its mortal coil.')
        else:
            creature_attack(active_creature, player)

        if player.health <= 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(2)
            print(f'{player.name} has heroically died in battle...')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('-' * 45)
            print('       GAME OVER')
            print('-' * 45)
            time.sleep(6)
            game_exit()
        elif player.health <= 30:
            print(f'{player.name} has been critically wounded, but manages '
                  f'to escape with his life.')
            time.sleep(5)
            break
        else:
            pass

    player.level += win_bonus


def look_around(player, creatures):
    """
    View all current creatures
    :param player: current player
    :param creatures: all available creatures
    :return: None
    """
    print(f'{player.name} looks around and sees: ')
    for c in creatures:
        print(f' * A {c.name} of level {c.level}')


def game_won():
    """
    Game over, player has defeated all creatures
    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-' * 45)
    print('Congratulations!')
    print('The forest has been cleared of creatures!')
    print('-' * 45)
    time.sleep(6)
    raise SystemExit


def clear_screen():
    """
    Clear the current screen of data
    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def player_attack(player, active_creature):
    """
    Flow control for player attacking a creature
    :param player: current player
    :param active_creature: Creature being attacked by player
    :return: None
    """
    clear_screen()
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

    clear_screen()


def creature_attack(active_creature, player):
    """
    Active creature attacking current player
    :param active_creature: Current creature of melee
    :param player: current player
    :return: None
    """
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

    clear_screen()


if __name__ == '__main__':
    main()

