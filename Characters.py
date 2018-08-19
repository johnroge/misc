import random


class Creature:
    def __init__(self, name, level, exp, weapon, health, defense):
        self.name = name
        self.level = level
        self.exp = exp
        self.weapon = weapon
        self.health = health
        self.defense = defense
        self.is_alive = True

    def __repr__(self):
        return "A level {} {}".format(
            self.level, self.name
        )

    def get_defensive_roll(self):
        raise NotImplemented

    def take_damage(self, damage_roll):
        self.health -= damage_roll
        if self.health < 0:
            self.health = 0
            self.is_alive = False


class Wizard(Creature):
    def __init__(self, name, level, exp, weapon, health, defense, magic):
        super().__init__(name, level, exp, weapon, health, defense)
        self.magic = magic

    def get_defensive_roll(self):
        def_roll = random.randint(1, 6) * self.level + self.defense
        return def_roll

    def attack(self):
        attack_roll = random.randint(1, 6) * self.level + self.exp + self.magic
        return attack_roll


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        def_roll = random.randint(1, 6) * self.level + self.defense
        return def_roll / 2

    def attack(self):
        attack_roll = random.randint(1, 3) * self.level + self.weapon
        return attack_roll


class LargeAnimal(Creature):
    def get_defensive_roll(self):
        def_roll = random.randint(1, 6) * self.level + self.defense
        return def_roll

    def attack(self):
        attack_roll = random.randint(1, 6) * self.level + self.weapon
        return attack_roll


class MedNPC(Creature):
    def get_defensive_roll(self):
        def_roll = random.randint(1, 6) * self.level + self.defense
        return def_roll

    def attack(self):
        attack_roll = random.randint(1, 6) * self.level + self.weapon
        return attack_roll


class Dragon(Creature):
    def __init__(self, name, level, exp, weapon, health, scales, fire):
        super().__init__(name, level, exp, weapon, health)
        self.scales = scales
        self.fire = fire

    def get_defensive_roll(self):
        def_roll = random.randint(1, 6) * self.level + self.scales
        return def_roll

    def attack(self):
        attack_roll = random.randint(1, 6) * self.level + self.weapon
        return attack_roll
