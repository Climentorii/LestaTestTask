from scripts.weapons.Weapon import Weapon
import pygame as p

class NoWeapon(Weapon):
    def __init__(self):
        image = p.image.load("./assets/Empty.png").convert_alpha()
        image = p.transform.scale(image, (128, 128))
        super().__init__("NoWeapon", 0, "Crush", image=image)

class Sword(Weapon):
    def __init__(self):
        image = p.image.load("./assets/WeaponSprites/Sword.png").convert_alpha()
        image = p.transform.scale(image, (128, 128))
        super().__init__("Sword", 3, "Splash", image=image)

class Bat(Weapon):
    def __init__(self):
        image = p.image.load("./assets/WeaponSprites/Bat.png").convert_alpha()
        image = p.transform.scale(image, (128, 128))
        super().__init__("Bat", 3, "Crush", image=image)

class Dagger(Weapon):
    def __init__(self):
        image = p.image.load("./assets/WeaponSprites/Dagger.png").convert_alpha()
        image = p.transform.scale(image, (128, 128))
        super().__init__("Dagger", 2, "Pierce", image=image)

class Spear(Weapon):
    def __init__(self):
        image = p.image.load("./assets/WeaponSprites/Spear.png").convert_alpha()
        image = p.transform.scale(image, (128, 128))
        super().__init__("Spear", 3, "Pierce", image=image)

class Axe(Weapon):
    def __init__(self):
        image = p.image.load("./assets/WeaponSprites/Axe.png").convert_alpha()
        image = p.transform.scale(image, (128, 128))
        super().__init__("Axe", 4, "Splash", image=image)

class LegendarySword(Weapon):
    def __init__(self):
        image = p.image.load("./assets/WeaponSprites/LegendarySword.png").convert_alpha()
        image = p.transform.scale(image, (128, 128))
        super().__init__("LegendarySword", 10, "Splash", image=image)