# character classes for text_game.py
import random


class Creature:
    def __init__(self, name, level, health, defense):
        self.name = name
        self.level = level
        self.health = health
        self.defense = defense

    def __repr__(self):
        return "Creature {} of {} level and {} health.".format(
            self.name,
            self.level,
            self.health
        )

    def attack(self):
        return random.randint(1, 10) + self.level

    def defensive_roll(self):
        return random.randint(1, 10) + self.defense


class LargeCreature(Creature):
    def __init__(self, name, level, health, defense, armor):
        super().__init__(name, level, health, defense)
        self.armor = armor

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.armor
        return base_roll + modifier


class MagicalCreature(Creature):
    def __init__(self, name, level, health, defense, magic):
        super().__init__(name, level, health, defense)
        self.magic = magic

    def attack(self):
        base_attack = super().attack()
        modifier = self.magic
        return base_attack + modifier

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.magic
        return base_roll + modifier


class Wizard(MagicalCreature):
    def __init__(self, name, level, health, defense, magic, wisdom):
        super().__init__(name, level, health, defense, magic)
        self.wisdom = wisdom

    def attack(self):
        base_attack = super().attack()
        modifier = self.wisdom
        return base_attack + modifier

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.wisdom
        return base_roll + modifier
