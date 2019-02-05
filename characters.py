
import random


class Creature:
    def __init__(self, name, health, level=10, speed=10, exp=10):
        self.name = name
        self.health = health
        self.level = level
        self.speed = speed
        self.exp = exp

    def __repr__(self):
        return "A {} of level {}".format(self.name, self.level)

    def defensive_roll(self):
        return random.randint(1, 50) + self.level + self.speed + self.exp


class Dragon(Creature):
    def __init__(self, name, health, level, speed, exp, scaliness,
                 breaths_fire):
        super().__init__(name, health, level, speed, exp)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        fire_modifier = 2 if self.breaths_fire else 1
        scale_modifier = self.scaliness

        return round(base_roll * fire_modifier + scale_modifier)


class Elf(Creature):
    def __init__(self, name, health, level, speed, exp, wisdom):
        super().__init__(name, health, level, speed, exp)
        self.wisdom = wisdom

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.wisdom

        return round(base_roll + modifier)


class Dwarf(Creature):
    def __init__(self, name, health, level, speed, exp, stamina):
        super().__init__(name, health, level, speed, exp)
        self.stamina = stamina

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.stamina

        return round(base_roll + modifier)


class Paladin(Creature):
    def __init__(self, name, health, level, speed, exp, combat):
        super().__init__(name, health, level, speed, exp)
        self.combat = combat

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        combat_modifier = self.combat

        return round(base_roll * combat_modifier)


class Archer(Creature):
    def __init__(self, name, health, level, speed, exp, distance):
        super().__init__(name, health, level, speed, exp)
        self.distance = distance

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.distance

        return round(base_roll * modifier)


class Thief(Creature):
    def __init__(self, name, health, level, speed, exp, dexterity):
        super().__init__(name, health, level, speed, exp)
        self.dexterity = dexterity

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.dexterity

        return round(base_roll * modifier)


class RogueWarrior(Creature):
    def __init__(self, name, health, level, speed, exp, strength):
        super().__init__(name, health, level, speed, exp)
        self.strength = strength

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.strength

        return round(base_roll * modifier)


class Ranger(Creature):
    def __init__(self, name, health, level, speed, exp, tracking, hunting):
        super().__init__(name, health, level, speed, exp)
        self.tracking = tracking
        self.hunting = hunting

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.hunting + self.tracking
        return round(base_roll + modifier)


class Infantry(Creature):
    def __init__(self, name, health, level, speed, exp, training):
        super().__init__(name, health, level, speed, exp)
        self.training = training

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.training
        return round(base_roll * modifier)


class Jedi(Creature):
    def __init__(self, name, health, level, speed, exp, force):
        super().__init__(name, health, level, speed, exp)
        self.force = force

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.force

        return round(base_roll + modifier)


class Cleric(Creature):
    def defensive_roll(self):
        base_roll = super().defensive_roll()
        return round(base_roll * .8)


class SmallAnimal(Creature):
    def defensive_roll(self):
        base_roll = super().defensive_roll()
        return round(base_roll / 2)


class Wizard(Creature):
    def __init__(self, name, health, level, speed, exp, magic):
        super().__init__(name, health, level, speed, exp)
        self.magic = magic

    def defensive_roll(self):
        base_roll = super().defensive_roll()
        modifier = self.magic

        return round(base_roll * modifier)

    def attack(self, creature):
        print()
        print(f'The wizard {self.name} has attacked the {creature.name}!')

        hero_roll = self.defensive_roll()
        creature_roll = creature.defensive_roll()

        print(f'{self.name} has rolled {hero_roll}..')
        print(f'  while the {creature.name} has rolled {creature_roll}.')
        print()

        if hero_roll >= creature_roll:
            print(f'{self.name} has inflicted {hero_roll} points of '
                  f'damage to the {creature.name}!')
            print(f'The wounded {creature.name} runs away!')
            print()
            return True
        else:
            print(f'{creature.name} has gravely wounded our hero '
                  f'{self.name}..')
            print(f'{self.name} staggers away in defeat, looking for refuge.')
            print()
            return False

