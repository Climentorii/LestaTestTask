from abc import ABC, abstractmethod
from scripts.characters.Character import Character
from pygame import image

class Perk(ABC):

    @abstractmethod
    def __init__(self, name: str, is_attack: bool, image: image, description: str = ""):
        self.name = name
        self.is_attack = is_attack
        self.image = image
        self.description = description
    @abstractmethod
    def count_damage(self, attacker: Character, defender: Character) -> int:
        pass