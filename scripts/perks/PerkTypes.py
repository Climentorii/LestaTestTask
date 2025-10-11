from scripts.characters.Character import Character
from scripts.perks.Perk import Perk
import pygame as p

class HiddenAttack(Perk):

    def __init__(self):
        image = p.image.load("./assets/PerkSprites/HiddenAttack.png")
        image = p.transform.scale(image, (64, 64))
        super().__init__(name="HiddenAttack", is_attack=True, image=image,
                         description="Скрытая атака: +1 к урону, если ловкость персонажа выше ловкости цели.")

    def count_damage(self, attacker: Character, defender: Character) -> int:
        return 1 if attacker.agility > defender.agility else 0 
    
class Poison(Perk):

    def __init__(self):
        image = p.image.load("./assets/PerkSprites/Poison.png")
        image = p.transform.scale(image, (64, 64))
        super().__init__(name="Poison", is_attack=True, image=image,
                         description="Яд: Наносит дополнительные (номер хода) - 1 урона на каждом ходу.")

    def count_damage(self, attacker: Character, defender: Character) -> int:
        return attacker.turnCount - 1
    
class Rush(Perk):

    def __init__(self):
        image = p.image.load("./assets/PerkSprites/Rush.png")
        image = p.transform.scale(image, (64, 64))
        super().__init__(name="Rush", is_attack=True, image=image,
                         description="Порыв к действию: В первый ход наносится двойной урон оружием.")

    def count_damage(self, attacker: Character, defender: Character) -> int:
        return attacker.weapon.damage if attacker.turnCount == 1 else 0
        
class Shield(Perk):

    def __init__(self):
        image = p.image.load("./assets/PerkSprites/Shield.png")
        image = p.transform.scale(image, (64, 64))
        super().__init__(name="Shield", is_attack=False, image=image,
                         description="Щит: -3 к получаемому урону, если сила персонажа выше силы атакующего.")

    def count_damage(self, attacker: Character, defender: Character) -> int:
        return -3 if attacker.power < defender.power else 0

class Rage(Perk):

    def __init__(self):
        image = p.image.load("./assets/PerkSprites/Rage.png")
        image = p.transform.scale(image, (64, 64))
        super().__init__(name="Rage", is_attack=True, image=image,
                         description="Ярость: На первых трёх ходах +2 урона, затем -1.")

    def count_damage(self, attacker: Character, defender: Character) -> int:
        return 2 if attacker.turnCount <= 3 else -1
    
class StoneSkin(Perk):

    def __init__(self):
        image = p.image.load("./assets/PerkSprites/StoneSkin.png")
        image = p.transform.scale(image, (64, 64))
        super().__init__(name="StoneSkin", is_attack=False, image=image,
                         description="Каменная кожа: Уменьшает получаемый урон на величину выносливости персонажа.")

    def count_damage(self, attacker: Character, defender: Character) -> int:
        return -defender.agility