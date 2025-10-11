from typing import Optional, Tuple
from scripts.characters.Character import Character
from scripts.constants import config
import pygame as p
from scripts.characters.EnemyTypes import Skeleton, Slime, Dragon
from pygame import Surface
from scripts.constants.Constants import number_dict

class TooltipManager:

    def __init__(self, screen: Surface):
        self.screen = screen
        
    def hit_rect_for_number(self, value: int, x: int, y: int) -> p.Rect:
        try:
            max_w = max(img.get_width() for img in number_dict.values())
            h = max(img.get_height() for img in number_dict.values())
        except Exception:
            max_w, h = 16, 24
        width = max_w + (len(str(value)) - 1) * 15
        if width < max_w:
            width = max_w
        return p.Rect(x, y, width, h)

    def build_battle_hover_text(self, mouse_pos: Tuple[int, int], player: Character, enemy: Character) -> Optional[str]:
        hover_text = None

        for i, perk in enumerate(player.perks_list):
            rect = p.Rect(0, 100 + i * 70, 64, 64)
            if rect.collidepoint(mouse_pos):
                hover_text = f"{perk.name}\n{getattr(perk, 'description', '')}"
                break

        if hover_text is None:
            for i, perk in enumerate(enemy.perks_list):
                rect = p.Rect(700, 100 + i * 70, 64, 64)
                if rect.collidepoint(mouse_pos):
                    hover_text = f"{perk.name}\n{getattr(perk, 'description', '')}"
                    break

        if hover_text is None:
            ex, ey = config.ENEMY_IMAGE_POS
            ew, eh = enemy.image.get_size()
            if p.Rect(ex, ey, ew, eh).collidepoint(mouse_pos):
                if isinstance(enemy, Skeleton):
                    hover_text = "Скелет: получает x2 урона от дробящего оружия."
                elif isinstance(enemy, Slime):
                    hover_text = "Слайм: при атаке оружием типа Splash получает урон только от силы и перков."
                elif isinstance(enemy, Dragon):
                    hover_text = "Дракон: каждый 3-й ход наносит +3 урона."

        if hover_text is None and p.Rect(*config.PLAYER_WEAPON_POS, 128, 128).collidepoint(mouse_pos):
            w = player.weapon
            hover_text = f"Оружие: {w.name}\nУрон: {w.damage}\nТип атаки: {w.attack_type}"
        if hover_text is None and p.Rect(*config.ENEMY_WEAPON_POS, 128, 128).collidepoint(mouse_pos):
            w = enemy.prizeWeapon
            hover_text = f"Трофей: {w.name}\nУрон: {w.damage}\nТип атаки: {w.attack_type}"

        if hover_text is None:
            if self.hit_rect_for_number(player.power, *config.PLAYER_POWER_POS).collidepoint(mouse_pos):
                hover_text = f"Сила: {player.power}. \nВаш основной урон."
            elif self.hit_rect_for_number(player.agility, *config.PLAYER_AGILITY_POS).collidepoint(mouse_pos):
                hover_text = f"Ловкость (игрок): {player.agility}. \nВлияет на шансы попасть и порядок хода."
            elif self.hit_rect_for_number(player.stamina, *config.PLAYER_STAMINA_POS).collidepoint(mouse_pos):
                hover_text = f"Выносливость (игрок): {player.stamina}. \nДает прибавку к здоровью на свое значение."
            elif self.hit_rect_for_number(player.health, *config.PLAYER_HEALTH_POS).collidepoint(mouse_pos):
                hover_text = f"Здоровье (игрок): {player.health}/{player.max_health}. \nОпа, а это здоровьице!"
            elif self.hit_rect_for_number(player.weapon.damage, *config.PLAYER_WEAPON_DMG_POS).collidepoint(mouse_pos):
                hover_text = f"Урон оружия (игрок): {player.weapon.damage}. \nПрибавляется к силе."

        if hover_text is None:
            if self.hit_rect_for_number(enemy.power, *config.ENEMY_POWER_POS).collidepoint(mouse_pos):
                hover_text = f"Сила (враг): {enemy.power}"
            elif self.hit_rect_for_number(enemy.agility, *config.ENEMY_AGILITY_POS).collidepoint(mouse_pos):
                hover_text = f"Ловкость (враг): {enemy.agility}"
            elif self.hit_rect_for_number(enemy.stamina, *config.ENEMY_STAMINA_POS).collidepoint(mouse_pos):
                hover_text = f"Выносливость (враг): {enemy.stamina}"
            elif self.hit_rect_for_number(enemy.health, *config.ENEMY_HEALTH_POS).collidepoint(mouse_pos):
                hover_text = f"Здоровье (враг): {enemy.health}"
            elif self.hit_rect_for_number(enemy.weapon.damage, *config.ENEMY_WEAPON_DMG_POS).collidepoint(mouse_pos):
                hover_text = f"Урон оружия (враг): {enemy.weapon.damage}"

        return hover_text