# character classes for text_game.py
import random

# TODO: create some decorators, start with @property
# TODO: add some magic methods
# TODO: create new methods


class Creature:
    """
    Base level class that applies to all characters
    """

    def __init__(self, name, level, health, defense, armor):
        self.name = name
        self.level = level
        self.health = health
        self.defense = defense
        self.armor = armor

    def __repr__(self):
        return (
            f"A {self.name} of {self.level} level, {self.health} "
            f"health, {self.defense} and {self.armor} armor."
        )

    def attack_roll(self):
        modifier = round(random.randint(1, self.level) * 0.5)
        return random.randint(1, 15) + modifier

    def defensive_roll(self):
        modifier = round(random.randint(1, self.defense) * 0.5)
        return random.randint(1, 15) + modifier


class LargeCreature(Creature):
    """
    Large, NPC character class
    """

    def __init__(self, name, level, health, defense, armor):
        super().__init__(name, level, health, defense, armor)

    def attack_roll(self):
        modifier = round(random.randint(1, self.level))
        return random.randint(1, 20) + modifier

    def defensive_roll(self):
        modifier = round(random.randint(1, self.defense))
        return random.randint(1, 20) + modifier


class Dragon(LargeCreature):
    """
    Special class for dragons - may or may not breath fire
    """

    def __init__(self, name, level, health, defense, armor, fire):
        super().__init__(name, level, health, defense, armor)
        self.fire = fire

    def attack_roll(self):
        base_attack = super().attack_roll()
        fire_modifier = random.randint(1, 20) if self.fire else 0
        return base_attack + fire_modifier

    def defensive_roll(self):
        base_defense = super().defensive_roll()
        return base_defense + random.randint(1, 20)


class MagicalCreature(Creature):
    """
    NPC magical class of characters
    """

    def __init__(self, name, level, health, defense, armor, magic):
        super().__init__(name, level, health, defense, armor)
        self.magic = magic

    def attack_roll(self):
        modifier = round(random.randint(1, self.magic))
        return random.randint(1, 20) + modifier + self.level

    def defensive_roll(self):
        modifier = round(random.randint(1, self.defense))
        return random.randint(1, 20) + modifier


# TODO: Character class - Ranger
# TODO: Character class - Cleric
# TODO: Character class - Barbarian
# TODO: Character class - Fighter


class Wizard(MagicalCreature):
    """
    Currently only available to game player
    """

    def __init__(
        self,
        name,
        level,
        health,
        defense,
        armor,
        magic,
        wisdom,
        current_health,
        strength,
        items,
        spells,
    ):
        super().__init__(name, level, health, defense, armor, magic)
        self.wisdom = wisdom
        self.current_health = current_health
        self.strength = strength
        self.items = items
        self.spells = spells

    def __repr__(self):
        return (
            f"{self.name} is a level {self.level} wizard with "
            f"{self.current_health} health, {self.magic} magic, "
            f"{self.wisdom} wisdom and {self.armor} armor."
        )

    def attack_roll(self):
        base_attack = super().attack_roll()
        modifier = self.wisdom
        return base_attack + modifier

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.wisdom
        return base_roll + modifier


class Item:
    """
    Physical objects to be used by player
    """

    def __init__(self, name, cost, weight):
        self.name = name
        self.cost = cost
        self.weight = weight

    def __repr__(self):
        return (
            f"A {self.name} which costs {self.cost} gold and weighs "
            f"{self.weight} pounds."
        )


class Weapon(Item):
    def __init__(self, name, cost, weight, damage):
        super().__init__(name, cost, weight)
        self.damage = damage


class Armor(Item):
    def __init__(self, name, cost, weight, defense):
        super().__init__(name, cost, weight)
        self.defense = defense


class Potion(Item):
    def __init__(self, name, cost, weight, effect):
        super().__init__(name, cost, weight)
        self.effect = effect


class Spell:
    """
    Spells to be used by the Wizard class
    """

    def __init__(self, name, magic_required, effect):
        self.name = name
        self.magic_required = magic_required
        self.effect = effect
