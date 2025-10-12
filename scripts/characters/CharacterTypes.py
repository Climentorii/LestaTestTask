import pygame as p
from scripts.characters.Character import Character
from scripts.weapons.WeaponTypes import Dagger, Sword, Bat
from scripts.perks.PerkTypes import HiddenAttack, Rush, Rage

class Rogue(Character):

    def __init__(self, power: int, agility: int, stamina: int):
        weapon = Dagger()
        image = p.image.load("./assets/FaceSprites/RogueFace.png")
        image = p.transform.scale(image, (192, 192))
        super().__init__(health=4, power=power, agility=agility, stamina=stamina, 
                         start_weapon=weapon, name="Rogue", image=image)

        self.health = self.max_health
        self.perks_list.append(HiddenAttack())

    def deal_damage(self):

        self.damage = self.power + self.weapon.damage
        return self.damage
    
    def get_damage(self, character_damage: int, damage_from_perks: int, attack_type: str):
        
        self.health -= (character_damage + damage_from_perks)

class Warrior(Character):

    def __init__(self, power: int, agility: int, stamina: int):
        weapon = Sword()
        image = p.image.load("./assets/FaceSprites/WarriorFace.png")
        image = p.transform.scale(image, (192, 192))
        super().__init__(health=5, power=power, agility=agility, stamina=stamina, 
                         start_weapon=weapon, name="Warrior", image=image)

        self.health = self.max_health
        self.perks_list.append(Rush())

    def deal_damage(self):

        self.damage = self.power + self.weapon.damage
        return self.damage
    
    def get_damage(self, character_damage: int, damage_from_perks: int, attack_type: str):
        
        self.health -= (character_damage + damage_from_perks)

class Barbarian(Character):

    def __init__(self, power: int, agility: int, stamina: int):
        weapon = Bat()
        image = p.image.load("./assets/FaceSprites/BarbarianFace.png")
        image = p.transform.scale(image, (192, 192))
        super().__init__(health=6, power=power, agility=agility, stamina=stamina, 
                         start_weapon=weapon, name="Barbarian", image=image)

        self.health = self.max_health
        self.perks_list.append(Rage())

    def deal_damage(self):

        self.damage = self.power + self.weapon.damage
        return self.damage
    
    def get_damage(self, character_damage: int, damage_from_perks: int, attack_type: str):
        
        self.health -= (character_damage + damage_from_perks)
