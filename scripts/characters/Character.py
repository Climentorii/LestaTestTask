from abc import ABC, abstractmethod
from scripts.weapons.Weapon import Weapon
from pygame import image

class Character(ABC):

    @abstractmethod
    def __init__(self, health: int, power: int, agility: int, 
                 stamina: int, start_weapon: Weapon, name: str,
                 image: image):

        self.health = health
        self.power = power
        self.agility = agility
        self.stamina = stamina
        self.damage : int
        self.perks_list = []
        self.max_health = self.health
        self.turnCount = 1
        self.weapon = start_weapon
        self.characterWeapon = self.weapon
        self.name = name
        self.image = image
        self.startMaxHealth = self.max_health

    @abstractmethod
    def deal_damage(self):

        pass

    @abstractmethod
    def get_damage(self, damage: int):

        pass