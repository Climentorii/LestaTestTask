from scripts.characters.Character import Character
from scripts.weapons.WeaponTypes import Dagger, NoWeapon, Bat, Spear, Sword, Axe, LegendarySword
from scripts.perks.PerkTypes import HiddenAttack, StoneSkin
from scripts.weapons.Weapon import Weapon
from pygame import image
import pygame as p

class Enemy(Character):

    def __init__(self, health: int, power: int, agility: int, stamina: int, start_weapon: Weapon, 
                 name: str, prizeWeapon: Weapon, weaponDamage: int, image: image):
        super().__init__(health=health, power=power, agility=agility, stamina=stamina, 
                         start_weapon=start_weapon, name=name, image=image)
        self.prizeWeapon = prizeWeapon
        self.weaponDamage = weaponDamage

class Goblin(Enemy):

    def __init__(self):

        weapon = NoWeapon()
        image = p.image.load("./assets/FaceSprites/GoblinFace.png")
        image = p.transform.scale(image, (256, 256))
        super().__init__(health=5, power=2, agility=1, stamina=1, start_weapon=weapon, 
                         name="Goblin", prizeWeapon=Dagger(), weaponDamage=2, image=image)

    def get_damage(self, damage: int, attack_type="", damageFromPerks=0):

        self.health -= damage

    def deal_damage(self):

        self.damage = self.weaponDamage + self.power
        return self.damage
    
class Skeleton(Enemy):

    def __init__(self):
        
        weapon = NoWeapon()
        image = p.image.load("./assets/FaceSprites/SkeletonFace.png")
        image = p.transform.scale(image, (256, 256))
        super().__init__(health=10, power=2, agility=2, stamina=1, start_weapon=weapon, 
                         name="Skeleton", prizeWeapon=Bat(), weaponDamage=2, image=image)

    def get_damage(self, damage: int, damageFromPerks: int, attack_type: str):

        if attack_type == "Crush":

            self.health -= (damage + damageFromPerks) * 2
            return
        self.health -= damage + damageFromPerks

    def deal_damage(self):
        
        self.damage = (self.weaponDamage + self.power)
        return self.damage
    
class Slime(Enemy):

    def __init__(self):
        weapon = NoWeapon()
        image = p.image.load("./assets/FaceSprites/SlimeFace.png")
        image = p.transform.scale(image, (256, 256))
        super().__init__(health=8, power=3, agility=1, stamina=2, start_weapon=weapon, 
                         name="Slime", prizeWeapon=Spear(), weaponDamage=1, image=image)
        
    def get_damage(self, damage: int, damageFromPerks: int, attack_type: str):
        
        if attack_type == "Splash":

            self.health -= damageFromPerks
            return
        
        self.health -= (damage + damageFromPerks)

    def deal_damage(self):
        
        self.damage = self.weaponDamage + self.power
        return self.damage
    
class Ghost(Enemy):

    def __init__(self):

        weapon = NoWeapon()
        image = p.image.load("./assets/FaceSprites/GhostFace.png")
        image = p.transform.scale(image, (192, 192))
        super().__init__(health=6, power=1, agility=3, stamina=1, start_weapon=weapon, 
                         name="Ghost", prizeWeapon=Sword(), weaponDamage=3, image=image)
        self.perks_list.append(HiddenAttack())

    def get_damage(self, damage: int, damageFromPerks: int, attack_type: str):
        
        self.health -= (damage + damageFromPerks)

    def deal_damage(self):
        
        self.damage = self.weaponDamage + self.power
        return self.damage
    
class Golem(Enemy):

    def __init__(self):

        weapon = NoWeapon()
        image = p.image.load("./assets/FaceSprites/GolemFace.png")
        image = p.transform.scale(image, (256, 256))
        super().__init__(health=10, power=3, agility=1, stamina=3, start_weapon=weapon, 
                         name="Golem", prizeWeapon=Axe(), weaponDamage=1, image=image)
        self.perks_list.append(StoneSkin())

    def get_damage(self, damage: int, damageFromPerks: int, attack_type: str):

        self.health -= (damage + damageFromPerks)

    def deal_damage(self):
        
        self.damage = self.weaponDamage + self.power
        return self.damage
    
class Dragon(Enemy):

    def __init__(self):

        weapon = NoWeapon()
        image = p.image.load("./assets/FaceSprites/DragonFace.png")
        image = p.transform.scale(image, (192, 192))
        super().__init__(health=20, power=3, agility=3, stamina=3, start_weapon=weapon, 
                         name="Dragon", prizeWeapon=LegendarySword(), weaponDamage=4, image=image)

    def get_damage(self, damage: int, damageFromPerks: int, attack_type: str, ):
        
        self.health -= (damage + damageFromPerks)

    def deal_damage(self):

        if self.turnCount % 3 == 0 and self.turnCount > 0:

            self.damage = self.weaponDamage + self.power + 3
        else:

            self.damage = self.weaponDamage + self.power
        return self.damage