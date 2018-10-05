import random


# parent class 'Creature'
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

    def take_damage(self, damage_roll):
        self.health -= damage_roll
        if self.health < 0:
            self.health = 0
            self.is_alive = False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        def_roll = random.randint(1, 20) + self.level + self.exp  \
                   + self.defense
        return round(def_roll * .8)

    def attack(self):
        attack_roll = random.randint(1, 20) + self.level + self.exp  \
                    + self.weapon
        return round(attack_roll * .8)


class LargeAnimal(Creature):
    def get_defensive_roll(self):
        def_roll = random.randint(1, 20) + self.level + self.exp  \
                   + self.defense
        return round(def_roll * 1.1)

    def attack(self):
        attack_roll = random.randint(1, 20) + self.level + self.exp  \
                    + self.weapon
        return round(attack_roll * 1.1)


class MedNPC(Creature):
    def get_defensive_roll(self):
        def_roll = random.randint(1, 20) + self.level + self.exp  \
                   + self.defense
        return round(def_roll)

    def attack(self):
        attack_roll = random.randint(1, 20) + self.level + self.exp  \
                    + self.weapon
        return round(attack_roll)


class Dragon(Creature):
    def __init__(self, name, level, exp, weapon, health, defense, fire):
        super().__init__(name, level, exp, weapon, health, defense)
        self.fire = fire

    def get_defensive_roll(self):
        def_roll = random.randint(1, 20) + self.level + self.exp  \
                    + self.defense
        return round(def_roll * 1.3)

    def attack(self):
        fire_modifier = 10 if self.fire else 1
        attack_roll = random.randint(1, 20) + (self.level + self.exp +
                                               + self.weapon + fire_modifier)
        return round(attack_roll * 1.3)


class Wizard(Creature):
    def __init__(self, name, level, exp, weapon, health, defense, magic):
        super().__init__(name, level, exp, weapon, health, defense)
        self.magic = magic

    def get_defensive_roll(self):
        def_roll = random.randint(1, 20) + self.level + self.exp  \
                   + self.defense + self.magic
        return round(def_roll)

    def attack(self):
        attack_roll = random.randint(1, 20) + self.level + self.exp +  \
                      self.magic + self.weapon
        return round(attack_roll)
