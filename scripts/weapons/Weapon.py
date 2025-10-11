from abc import ABC, abstractmethod
from pygame import image

class Weapon(ABC):
    
    @abstractmethod
    def __init__(self, name: str, damage: int, attack_type: str, image: image):
        self.name = name
        self.damage = damage
        self.attack_type = attack_type
        self.image = image