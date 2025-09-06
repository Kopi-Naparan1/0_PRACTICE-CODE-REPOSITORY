from abc import ABC, abstractmethod


class RPGGame(ABC):
    pass


class Character(RPGGame):
    def __init__(self, name, hp, b_attack):
        self.name = name
        self.hp = hp
        self.basic_attack = b_attack


class Hero(Character):

    def __init__(self, name, hp, b_attack, special_skill):
        super().__init__(name, hp, b_attack)
        self.skill = special_skill

    def use_skill(self, target):
        self.skill.use(self, target)



class Villain(Character):
    def __init__(self, name, hp, b_attack, special_attack):
        super().__init__(name, hp, b_attack)
        self.special_attack = special_attack


class CharacterFactory:
    def __init__(self):
        self.heros = []
        self.villains = []

    def create_hero(self, name, hp, b_attack, special_attack):
        hero = Hero(name, hp, b_attack, special_attack)
        if len(self.heros) <= 5:
            self.heros.append(hero)
        elif len(self.heros) == 5:
            print('Hero Slot is FULL')

    def make_villain(self, name, hp, b_attack, special_attack):
        villain = Villain(name, hp, b_attack, special_attack)
        if len(self.heros) <= 5:
            self.villains.append(villain)
        elif len(self.villains) == 5:
            print('Villain Slot is FULL')


class BattleSystem:

    def __init__(self, name, hp, b_attack, special_attack):
        super().__init__(name, hp, b_attack)
        self.special_attack = special_attack

    def use_basic_attack(self, attacker, target):
        target.hp -= attacker.b_attack
        print(f"{attacker.name} attacked {target.name}! {target.name}'s HP is now {target.hp}")

    def use_special_attack(self, attacker, target):
        target.hp -= attacker.special_attack
        print(f"{attacker.name} attacked {target.name}! {target.name}'s HP is now {target.hp}")


# region Special Skills
class FireBlast:
    def use(self, attacker, target):
        damage = 25
        target.hp -= attacker
        print(f'{attacker.name} uses Fire Blast to {target.name}.\n\t {target.name} takes {damage} of damage')


class WaterSlice:
    def use(self, attacker, target):
        damage = 25
        target.hp -= attacker
        print(f'{attacker.name} uses Water Slice to {target.name}.\n\t {target.name} takes {damage} of damage')


class WindCutter:
    def use(self, attacker, target):
        damage = 25
        target.hp -= attacker
        print(f'{attacker.name} uses Wind Cutter to {target.name}.\n\t {target.name} takes {damage} of damage')


class EarthPunch:
    def use(self, attacker, target):
        damage = 25
        target.hp -= attacker
        print(f'{attacker.name} uses Earth Punch to {target.name}.\n\t {target.name} takes {damage} of damage')


class HealSpell:
    def use(self, user, target):
        target.hp += 20
        print(f"{user.name} heals {target.name} for 20 HP!")


# endregion










