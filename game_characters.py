# character classes for text_game.py
import random


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

    def defensive_roll(self):
        return random.randint(1, 10) * self.level


class LargeCreature(Creature):
    def __init__(self, name, level, health, armor):
        super().__init__(name, level, health)
        self.armor = armor

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.armor
        return base_roll + modifier


class MagicalCreature(Creature):
    def __init__(self, name, level, health, magic):
        super().__init__(name, level, health)
        self.magic = magic

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.magic
        return base_roll + modifier


class Wizard(Creature):
    def __init__(self, name, level, health, magic):
        super().__init__(name, level, health)
        self.magic = magic

    def attack(self, creature):
        print(f'The Wizard {self.name} attacks the {creature.name}!')

        modifier = self.magic
        my_roll = self.defensive_roll() + modifier
        creature_roll = creature.defensive_roll()

        print(f'You roll a {my_roll} versus the {creature.name} rolling'
              f' a {creature_roll}.')

        if my_roll >= creature_roll:
            print(f'You have killed the {creature.name}!')
            return True
        else:
            print(f'Sadly you have been defeated by the {creature.name}..')
