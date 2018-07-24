import random
import time


class Creature:
    def __init__(self, name, level, exp, weapon, health):
        self.name = name
        self.level = level
        self.exp = exp
        self.weapon = weapon
        self.health = health

    def __repr__(self):
        return "A level {} {}".format(
            self.level, self.name
        )


class Wizard(Creature):
    def __init__(self, name, level, exp, weapon, health, magic):
        super().__init__(name, level, exp, weapon, health)
        self.magic = magic

    def attack(self, creature):
        print('Our hero attacks the {}!'.format(creature.name))

        my_roll = random.randint(1, 6) * self.level + self.exp + self.magic
        creature_roll = creature.get_defensive_roll()

        print('You roll a......{}'.format(my_roll))
        print('{} rolls a........{}'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The {} has been slayed by our hero.'.format(creature.name))
            return True
        else:
            print('\nOur hero has fallen...')
            time.sleep(3)
            print('\nOr has he?\n')
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = random.randint(1, 6) * self.level + self.weapon
        return base_roll / 2


class LargeAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = random.randint(1, 6) * self.level + self.weapon
        return base_roll + random.randint(2, 8)


class MedNPC(Creature):
    def get_defensive_roll(self):
        base_roll = random.randint(1, 6) * self.level + self.weapon
        return base_roll + random.randint(3, 20)


class Dragon(Creature):
    def __init__(self, name, level, exp, weapon, health, scales, fire):
        super().__init__(name, level, exp, weapon, health)
        self.scales = scales
        self.fire = fire

    def get_defensive_roll(self):
        base_roll = random.randint(1, 6) * self.level + self.weapon
        fire = 3 if self.fire else 1
        return base_roll + self.scales * fire

