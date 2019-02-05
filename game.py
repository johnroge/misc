#!/usr/bin/env python3
"""
D&D game
name, level, speed, exp
"""

from characters import *
import random
import time


def main():

    creatures = [
       Dragon('Red Dragon', 400, 20, 20, 20, 20, breaths_fire=True),
       Dragon('White Dragon', 300, 15, 15, 14, 13, breaths_fire=False),
       Dragon('Black Dragon', 300, 12, 11, 16, 4, breaths_fire=True),
       Paladin('Paladin named Rose', 200, 9, 12, 11, 1.2),
       Paladin('Paladin named BraveHeart', 240, 5, 4, 6, 1.1),
       Cleric('Cleric named Sam', 90),
       Infantry('Soldier', 140, 9, 8, 7, 1.2),
       Infantry('Soldier', 150, 5, 6, 3, 1.1),
       Infantry('Soldier', 134, 6, 7, 8, 1.1),
       Ranger('Ranger Rick', 200, 11, 11, 11, 10, 12),
       Ranger('Ranger Dan', 240, 11, 11, 11, 16, 12),
       Jedi('Rogue Jedi', 220, 10, 10, 10, 40),
       Jedi('Rogue Jedi', 300, 12, 10, 10, 50),
       Elf('Elf', 340, 11, 19, 16, 30),
       Elf('Elf', 500, 10, 20, 15, 10),
       RogueWarrior('Rogue Warrior', 220, 11, 11, 15, 1.3),
       RogueWarrior('Rogue Warrior', 290, 10, 12, 15, 1.2),
       Archer('trained archer', 100, 9, 8, 8, 1.1),
       Archer('trained archer', 100, 8, 8, 9, 1.2),
       Thief('sneaky thief', 100, 7, 7, 9, 1.3),
       Thief('sneaky thief', 100, 8, 7, 6, 1.2),
       Thief('sneaky thief', 120, 11, 9, 12, 1.4),
       SmallAnimal('Toad', 30, 1, 2, 1),
       SmallAnimal('Bat', 40, 2, 3, 1),
       Dwarf('Dwarf', 300, 13, 5, 14, 20),
       Dwarf('Dwarf', 400, 16, 6, 16, 30),
       Creature('Raccoon', 50, 5, 2, 5),
       Creature('Coyote', 60),
       Creature('Grey Wolf', 70),
       Creature('Brown Bear', 230, 15, 12, 15),
       Creature('Mountain Lion', 190, 12, 25, 12),
       Wizard('Evil Wizard Sauron', 500, level=11, speed=13, exp=10, magic=1.2)
    ]

    name = input('What is your name, hero? ')
    hero = Wizard(name, health=450, level=25, speed=26, exp=23, magic=1.4)

    print_header(name)
    game_loop(creatures, hero)


def print_header(name):
    print('-' * 60)
    print(f'          Get ready, {name.capitalize()}!')
    print('-' * 60)


def game_loop(creatures, hero):

    while hero.health > 0:

        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level}'
              f' has appeared on the edge of the clearing - what does'
              f' our hero {hero.name} do?')

        cmd = input('[E]xit game, [A]ttack, [L]ook or [R]un away: ')
        cmd = cmd.lower()
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                time.sleep(5)
                print()
                print(f'{hero.name} has returned to health!')
        elif cmd == 'l':
            print(f'{hero.name} looks around the clearing and sees: ')
            for c in creatures:
                print(f'A level {c.level} {c.name}.')
        elif cmd == 'r':
            print()
            print('!' * 50)
            print('!!!!!! tucking tail and hitting the trail !!!!!!!!')
            print('!' * 50)
            print()
        else:
            print('exiting game')
            raise SystemExit

        if not creatures:
            print()
            print(f'Congratulations, {hero.name}, you have'
                  f' cleared the forest!')
            print('GAME OVER')
            break


if __name__ == '__main__':
    main()