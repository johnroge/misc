# character classes for text_game.py
import random


class Wizard:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def attack(self, creature):
        print(f'The Wizard {self.name} attacks the {creature.name}!')

        my_roll = random.randint(1, 10) * self.level
        creature_roll = random.randint(1, 10) * creature.level

        print(f'You roll a {my_roll} versus the {creature.name} rolling'
              f' a {creature_roll}.')

        if my_roll >= creature_roll:
            print(f'You have killed the {creature.name}!')
            return True
        else:
            print(f'Sadly you have been defeated by the {creature.name}..')


class Creature:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def __repr__(self):
        return "Creature {} of {} level and {} health.".format(
            self.name,
            self.level,
            self.health
        )


