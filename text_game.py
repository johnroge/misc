#!/usr/bin/env python3
"""
simple text game similar to dungeons and dragons
useful for practicing with classes, methods and flow control
v2.6
"""

from game_characters import Wizard, Creature, LargeCreature,\
    MagicalCreature, Dragon
import random
import time
import os
# TODO: **  intermittent bug exists where user input is ignored    **
# TODO: **  and the program jumps to the next creature             **

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
    creature_count = number_creatures()
    creatures = get_creatures(creature_count)
    game_loop(player, creatures)


def number_creatures():
    """
    Let player choose number of creatures to battle
    :return: Integer
    """
    while True:
        choice = input('Please enter a number between 5 and 100: ')
        choice = int(choice)
        if 5 <= choice <= 100:
            return choice
        else:
            print('Please enter a number between 5 and 100.')


def display_monster(creature):
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
    print('                                   v2.6')
    print('-' * 40)
    print()
    time.sleep(2)


def get_creatures(number):
    """
    Generate master list of available creatures to hunt
    :return: List of creature instances
    """

    # TODO: randomize the creature stats within a certain range
    creature_menu = [
        # name, level, health, defense, armor
        Creature('dire wolf', 5, 50, 5, 1),
        Creature('giant spider', 2, 15, 5, 1),
        Creature('poisonous snake', 1, 5, 2, 1),
        Creature('black bear', 8, 90, 9, 5),
        # name, level, health, defense, armor, magic
        MagicalCreature('goblin', 9, 50, 4, 2, 8),
        MagicalCreature('dark elf', 10, 90, 10, 5, 16),
        MagicalCreature('beholder', 11, 40, 10, 4, 14),
        MagicalCreature('mind flayer', 12, 40, 8, 4, 20),
        MagicalCreature('golem', 13, 90, 5, 10, 9),
        MagicalCreature('lich', 9, 40, 2, 2, 10),
        MagicalCreature('skeleton', 8, 30, 2, 3, 10),
        MagicalCreature('zombie', 10, 60, 1, 3, 8),
        MagicalCreature('air elemental', 8, 30, 15, 5, 10),
        MagicalCreature('death knight', 15, 100, 20, 20, 20),
        # name, level, health, defense, armor
        LargeCreature('frost giant', 15, 90, 15, 10),
        LargeCreature('orc', 12, 100, 12, 10),
        LargeCreature('troll', 14, 90, 15, 10),
        # name, level, health, defense, armor, fire
        Dragon('Red Dragon', 20, 800, 20, 40, True),
        Dragon('Black Dragon', 15, 600, 15, 25, False)
    ]

    # TODO: weight the creatures so fewer dragons, more lower level
    creatures = []
    while number >= 1:
        creatures.append(random.choice(creature_menu))
        number -= 1

    return creatures


def get_player_info():
    """
    Get user input for new player
    :return: return an instance of Wizard as player
    """
    # TODO: Let player choose character class and roll for starting stats
    name = input('What is your name, hero? ')
    name = name.capitalize()
    player = Wizard(name,
                    15,   # level
                    300,  # max health
                    5,    # defense
                    6,    # armor
                    10,    # magic
                    8,    # wisdom
                    300)  # current health

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
        display_monster(active_creature)
        cmd = user_action()

        if cmd == 'a':
            battle_loop(player, active_creature, creatures)
        elif cmd == 'r':
            print(f'{player.name} bravely runs away!')
        elif cmd == 'l':
            look_around(player, creatures)
        elif cmd == 'h':
            rest(player)
        elif cmd == 'v':
            print(player.__repr__())
        elif cmd == 'x':
            game_exit()
        else:
            print('Please enter a, r, l, h, v or x to continue: ')

        if not creatures:
            game_won()


def rest(player):
    """
    Give player chance to regain health by resting.
    :param player: current active player
    :return: N/A
    """
    clear_screen()
    print('Our hero finds a place to rest and restore his health...')
    time.sleep(10)

    health_gain = round(player.current_health * .10)
    if player.current_health + health_gain <= player.health:
        player.current_health += health_gain
    else:
        player.current_health = player.health

    print(f'{player.name} has regained {health_gain} points of '
          f'health by resting...')
    time.sleep(3)
    print(player.__repr__())


def user_action():
    """
    Current menu for player choices
    :return: cmd
    """
    # TODO: create sub-menu for other actions?
    # TODO: add feature for loading and saving game
    cmd = input('--> Do you [A]ttack, [H]eal, [R]un away, [L]ook around, '
                '[V]iew current stats or e[X]it game: ')
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

    win_bonus = round(active_creature.level * .2)
    while player.current_health >= 0 and active_creature.health >= 0:
        player_attack(player, active_creature)
        if active_creature.health <= 0:
            creatures.remove(active_creature)
            print(f'The {active_creature.name} has released its mortal coil.')
        else:
            creature_attack(active_creature, player)

        if player.current_health <= 0:
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
        elif player.current_health <= round(player.health * .20):
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
    damage = player_roll - active_creature.armor

    print(f'Our hero has attacked the {active_creature.name}!')
    time.sleep(1)
    print(f'{player.name} rolls a {player_roll}, while the'
          f' {active_creature.name} rolls a {creature_roll} in defense...')
    time.sleep(2)

    if player_roll >= creature_roll:
        print(f'The creature sustains {damage} points of damage!')
        active_creature.health -= damage
        time.sleep(2)
    else:
        print(f'The wiley {active_creature.name} has dodged our attack...')
        time.sleep(2)

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
    damage = creature_roll - player.armor
    print(f'The {active_creature.name} fights back!')
    time.sleep(1)
    print(f'The {active_creature.name} has rolled a {creature_roll}, '
          f'while our hero {player.name} rolls a {player_roll}!')
    time.sleep(2)

    if creature_roll >= player_roll:
        print(f'{player.name} has taken {damage} points of damage!')
        player.current_health -= damage
        time.sleep(2)
    else:
        print(f'Our hero {player.name} manages to parry the attack...')
        time.sleep(2)

    clear_screen()


if __name__ == '__main__':
    main()

