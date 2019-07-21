# character classes for text_game.py
import random
# TODO: create some decorators, start with @property
# TODO: add some magic methods
# TODO: create new methods


class Creature:
    """
    Base level class that applies to all characters
    """
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

    def attack_roll(self):
        return random.randint(1, 10) + self.level

    def defensive_roll(self):
        return random.randint(1, 10) + self.defense


class LargeCreature(Creature):
    """
    Large, NPC character class
    """
    def __init__(self, name, level, health, defense, armor):
        super().__init__(name, level, health, defense)
        self.armor = armor

    def __repr__(self):
        return 'Large'

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.armor
        return base_roll + modifier


class Dragon(LargeCreature):
    """
    Special class for dragons - may or may not breath fire
    """
    def __init__(self, name, level, health, defense, armor, fire):
        super().__init__(name, level, health, defense, armor)
        self.fire = fire

    def __repr__(self):
        return 'Dragon'

    def attack_roll(self):
        base_attack = super().attack_roll()
        fire_modifier = 20 if self.fire else 0

        return base_attack + fire_modifier


class MagicalCreature(Creature):
    """
    NPC magical class of characters
    """
    def __init__(self, name, level, health, defense, magic):
        super().__init__(name, level, health, defense)
        self.magic = magic

    def __repr__(self):
        return 'Magical'

    def attack_roll(self):
        base_attack = super().attack_roll()
        modifier = self.magic
        return base_attack + modifier

# TODO: Character class - Ranger
# TODO: Character class - Cleric
# TODO: Character class - Barbarian
# TODO: Character class - Fighter


class Wizard(MagicalCreature):
    """
    Currently only available to game player
    """
    def __init__(self, name, level, health, defense, magic,
                 wisdom, current_health):
        super().__init__(name, level, health, defense, magic)
        self.wisdom = wisdom
        self.current_health = current_health

    def __repr__(self):
        return f'{self.name} is a level {self.level} wizard with ' \
            f'{self.current_health} health, {self.magic} magic, and' \
            f' {self.wisdom} wisdom.'

    def attack_roll(self):
        base_attack = super().attack_roll()
        modifier = self.wisdom
        return base_attack + modifier

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.wisdom
        return base_roll + modifier
