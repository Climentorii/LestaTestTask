import random as r
import pygame as p
from scripts.constants import config
from pygame import Surface
from scripts.core_modules.GameEngine import GameEngine, enemy_chances_dict
from scripts.core_modules.Render import Renderer
from pygame.event import Event
from scripts.constants.config import BATTLE_STATES
from scripts.characters.CharacterTypes import Warrior, Rogue, Barbarian
from scripts.ui.TooltipManagement import TooltipManager
from scripts.ui.Tooltip import Tooltip
from scripts.ui.LogPanel import LogPanel

class ProcessManager:

    def __init__(self, game_engine: GameEngine, renderer: Renderer, tooltip: Tooltip, tooltip_manager: TooltipManager):
        self.game_engine = game_engine
        self.renderer = renderer
        self.tooltip = tooltip
        self.tooltip_manager = tooltip_manager
        self._current_state = BATTLE_STATES.START
        self.screen_fight_text_font = p.font.SysFont(config.DEFAULT_FONT_NAME, config.FONT_SIZE_LOG)
        self.log_panel = LogPanel(
            p.Rect(config.LOG_PANEL_MARGIN, config.SCREEN_HEIGHT - config.LOG_PANEL_MARGIN - config.LOG_PANEL_HEIGHT,
                   config.SCREEN_WIDTH - 2 * config.LOG_PANEL_MARGIN, config.LOG_PANEL_HEIGHT),
            self.screen_fight_text_font,
            bg_color=config.LOG_PANEL_BG,
            border_color=config.LOG_PANEL_BORDER,
            padding=config.LOG_PANEL_PADDING,
            capacity=100,
        )
        self.last_state_change_time = 0

    def get_current_state(self):
        return self._current_state

    def start_new_encounter(self, current_time: int):
        self.game_engine.recount_chances(self.game_engine.defeated_enemies_count)
        self.game_engine.enemy = self.game_engine.spawn_enemy()
        self.game_engine.initialize_fight(self.game_engine.enemy)
        self.log_panel.clear()
        self.log_panel.append(f"Встретили: {self.game_engine.enemy.name}")
        first = "Игрок" if self.game_engine.is_player_turn else "Противник"
        self.log_panel.append(f"Первым ходит: {first}")
        self._current_state = BATTLE_STATES.PLAYER_TURN if self.game_engine.is_player_turn else BATTLE_STATES.ENEMY_TURN
        self.last_state_change_time = current_time

    def state_start_func(self, events: list[Event], screen: Surface):
        for event in events:
            if self.renderer.button_select_class.handle_event(event):
                self._current_state = BATTLE_STATES.SELECT_CHARACTER
                self.renderer.button_select_class.disable()
                self.renderer.button_warrior_select.enable()
                self.renderer.button_rogue_select.enable()
                self.renderer.button_barbarian_select.enable()
                self.renderer.button_back_to_menu.enable()
                self.game_engine.defeated_enemies_count = 0
                self.game_engine.enemy_chances_dict = enemy_chances_dict
        self.renderer.button_select_class.draw(screen)

    def state_select_character_func(self, events: list[Event], screen: Surface):
        self.game_engine.level_dict['Barbarian'] = 0
        self.game_engine.level_dict['Warrior'] = 0
        self.game_engine.level_dict['Rogue'] = 0
        for event in events:
            if self.renderer.button_warrior_select.handle_event(event):
                self.renderer.button_warrior_select.disable()
                self.renderer.button_rogue_select.disable()
                self.renderer.button_barbarian_select.disable()
                player = Warrior(r.randint(1, 3), r.randint(1, 3), r.randint(1, 3))
                player.max_health = player.startMaxHealth
                player.health = player.max_health + player.stamina
                self.game_engine.add_main_player(player)
                self.game_engine.main_player.weapon = player.characterWeapon
                self._current_state = BATTLE_STATES.BEFORE_FIGHT
                self.renderer.button_back_to_select.enable()
                self.renderer.button_start_game.enable()

            if self.renderer.button_barbarian_select.handle_event(event):
                self.renderer.button_warrior_select.disable()
                self.renderer.button_rogue_select.disable()
                self.renderer.button_barbarian_select.disable()
                player = Barbarian(r.randint(1, 3), r.randint(1, 3), r.randint(1, 3))
                player.max_health = player.startMaxHealth
                player.health = player.max_health + player.stamina
                self.game_engine.add_main_player(player)
                self.game_engine.main_player.weapon = player.characterWeapon
                self.renderer.button_back_to_select.enable()
                self.renderer.button_start_game.enable()
                self._current_state = BATTLE_STATES.BEFORE_FIGHT

            if self.renderer.button_rogue_select.handle_event(event):
                self.renderer.button_warrior_select.disable()
                self.renderer.button_rogue_select.disable()
                self.renderer.button_barbarian_select.disable()
                player = Rogue(r.randint(1, 3), r.randint(1, 3), r.randint(1, 3))
                player.max_health = player.startMaxHealth
                player.health = player.max_health + player.stamina
                self.game_engine.add_main_player(player)
                self.game_engine.main_player.weapon = player.characterWeapon
                self.renderer.button_back_to_select.enable()
                self.renderer.button_start_game.enable()
                self._current_state = BATTLE_STATES.BEFORE_FIGHT

            if self.renderer.button_back_to_menu.handle_event(event):
                self.renderer.button_warrior_select.disable()
                self.renderer.button_rogue_select.disable()
                self.renderer.button_barbarian_select.disable()
                self.renderer.button_select_class.enable()
                self._current_state = BATTLE_STATES.START

        self.renderer.button_back_to_menu.draw(screen)
        self.renderer.button_warrior_select.draw(screen)
        self.renderer.button_barbarian_select.draw(screen)
        self.renderer.button_rogue_select.draw(screen)

    def state_before_fight_func(self, events: list[Event], screen: Surface):
        for event in events:
            if self.renderer.button_back_to_select.handle_event(event):
                self.renderer.button_back_to_select.disable()
                self.renderer.button_start_game.disable()
                self.renderer.button_warrior_select.enable()
                self.renderer.button_rogue_select.enable()
                self.renderer.button_barbarian_select.enable()
                self.renderer.button_back_to_menu.enable()
                self._current_state = BATTLE_STATES.SELECT_CHARACTER

            if self.renderer.button_start_game.handle_event(event):
                self.renderer.button_back_to_select.disable()
                self.renderer.button_start_game.disable()
                self.renderer.button_warrior_select.enable()
                self.renderer.button_rogue_select.enable()
                self.renderer.button_barbarian_select.enable()
                self.renderer.button_back_to_menu.enable()
                self._current_state = BATTLE_STATES.FIGHT_COMPILATION

        # BEFORE_FIGHT rendering
        self.renderer.button_start_game.draw(screen)
        self.renderer.button_back_to_select.draw(screen)
        screen.blit(self.game_engine.main_player.image, (90, 180))
        screen.blit(self.renderer.scroll_for_stats, (400, 70))
        screen.blit(self.game_engine.main_player.weapon.image, (190, 250))
        self.renderer.draw_number_image(self.game_engine.main_player.power, 600, 130)
        self.renderer.draw_number_image(self.game_engine.main_player.agility, 600, 175)
        self.renderer.draw_number_image(self.game_engine.main_player.stamina, 600, 220)
        self.renderer.draw_number_image(self.game_engine.main_player.health, 600, 263)
        self.renderer.draw_number_image(self.game_engine.main_player.weapon.damage, 560, 305)

        # Tooltips in BEFORE_FIGHT
        mouse_pos = p.mouse.get_pos()
        hover_text = None
        # Weapon
        if p.Rect(190, 250, 128, 128).collidepoint(mouse_pos):
            w = self.game_engine.main_player.weapon
            hover_text = f"Оружие: {w.name}\nУрон: {w.damage}\nТип атаки: {w.attack_type}"
        # Stats
        if hover_text is None:
            if self.tooltip_manager.hit_rect_for_number(self.game_engine.main_player.power, 600, 130).collidepoint(mouse_pos):
                hover_text = f"Сила: {self.game_engine.main_player.power}. \nВаш основной урон."
            elif self.tooltip_manager.hit_rect_for_number(self.game_engine.main_player.agility, 600, 175).collidepoint(mouse_pos):
                hover_text = f"Ловкость: {self.game_engine.main_player.agility}. \nВлияет на шансы попасть и порядок хода."
            elif self.tooltip_manager.hit_rect_for_number(self.game_engine.main_player.stamina, 600, 220).collidepoint(mouse_pos):
                hover_text = f"Выносливость: {self.game_engine.main_player.stamina}. \nДает прибавку к здоровью на свое значение."
            elif self.tooltip_manager.hit_rect_for_number(self.game_engine.main_player.health, 600, 263).collidepoint(mouse_pos):
                hover_text = f"Здоровье: {self.game_engine.main_player.health}. \nОпа, а это здоровьице!"
            elif self.tooltip_manager.hit_rect_for_number(self.game_engine.main_player.weapon.damage, 560, 305).collidepoint(mouse_pos):
                hover_text = f"Урон оружия: {self.game_engine.main_player.weapon.damage}. \nПрибавляется к силе."
        if hover_text:
            self.tooltip.draw(screen, hover_text, (mouse_pos[0] + 12, mouse_pos[1] + 12))

    def state_player_turn_func(self, current_time: int, screen: Surface):
        self.renderer.render_battle_state(self.game_engine.main_player,
                                          self.game_engine.enemy,
                                          self.renderer.scroll_for_stats,
                                          self.renderer.scroll_for_stats_player,
                                          self.tooltip)

        if current_time - self.last_state_change_time > config.STATE_DELAY_MS:
            if not self.game_engine.is_character_alive(self.game_engine.main_player):
                self.log_panel.append("Игрок пал в бою!")
                self._current_state = BATTLE_STATES.AFTER_FIGHT_DEATH
                self.renderer.button_new_game.enable()
                self.renderer.button_exit.enable()
                self.last_state_change_time = current_time
            elif self.game_engine.is_character_alive(self.game_engine.current_enemy):
                msg = self.game_engine.compile_character_turn(self.game_engine.main_player,
                                                              self.game_engine.current_enemy, "")
                self.log_panel.append(msg)
                self._current_state = BATTLE_STATES.ENEMY_TURN
                self.last_state_change_time = current_time
            else:
                self.log_panel.append(f"{self.game_engine.current_enemy.name} повержен!")
                self._current_state = BATTLE_STATES.AFTER_FIGHT_WIN
                self.game_engine.defeated_enemies_count += 1
                self.renderer.button_continue.enable()
                self.last_state_change_time = current_time

        self.log_panel.render(screen)

    def state_enemy_turn_func(self, current_time: int, screen: Surface):
        self.renderer.render_battle_state(self.game_engine.main_player,
                                          self.game_engine.enemy,
                                          self.renderer.scroll_for_stats,
                                          self.renderer.scroll_for_stats_player,
                                          self.tooltip)

        if current_time - self.last_state_change_time > config.STATE_DELAY_MS:
            if not self.game_engine.is_character_alive(self.game_engine.current_enemy):
                self.log_panel.append(f"{self.game_engine.current_enemy.name} повержен!")
                self._current_state = BATTLE_STATES.AFTER_FIGHT_WIN
                self.game_engine.defeated_enemies_count += 1
                self.renderer.button_continue.enable()
                self.last_state_change_time = current_time
            elif self.game_engine.is_character_alive(self.game_engine.main_player):
                msg = self.game_engine.compile_character_turn(self.game_engine.current_enemy, self.game_engine.main_player, "")
                self.log_panel.append(msg)
                self._current_state = BATTLE_STATES.PLAYER_TURN
                self.last_state_change_time = current_time
            else:
                self.log_panel.append("Игрок пал в бою!")
                self._current_state = BATTLE_STATES.AFTER_FIGHT_DEATH
                self.renderer.button_new_game.enable()
                self.renderer.button_exit.enable()
                self.last_state_change_time = current_time

        self.log_panel.render(screen)

    def state_after_fight_death_func(self, events: list[Event], screen: Surface):
        for event in events:
            if self.renderer.button_new_game.handle_event(event):
                self.renderer.button_new_game.disable()
                self.renderer.button_exit.disable()
                self.renderer.button_select_class.enable()
                self._current_state = BATTLE_STATES.START
            if self.renderer.button_exit.handle_event(event):
                exit()

        screen.blit(self.renderer.death_scroll, (130, 100))
        self.renderer.button_exit.draw(screen)
        self.renderer.button_new_game.draw(screen)

    def state_after_fight_win_func(self, current_time: int, events: list[Event], screen: Surface):
        screen.blit(self.renderer.win_scroll_1, (130, 100))
        self.renderer.draw_number_image(self.game_engine.defeated_enemies_count, 415, 215)

        if current_time - self.last_state_change_time > config.STATE_DELAY_MS:
            self.renderer.button_continue.draw(screen)
            for event in events:
                if self.renderer.button_continue.handle_event(event):
                    self.renderer.button_continue.disable()
                    self.renderer.button_barbarian_select_to_upgrade.enable()
                    self.renderer.button_warrior_select_to_upgrade.enable()
                    self.renderer.button_rogue_select_to_upgrade.enable()
                    self.renderer.button_take_prize_weapon.enable()
                    self.renderer.button_continue_after.enable()
                    self._current_state = BATTLE_STATES.PICK_PRIZE
                    self.last_state_change_time = current_time

    def state_pick_prize_func(self, current_time: int, events: list[Event], screen: Surface):
        if current_time - self.last_state_change_time < 1000:
            return
        if self.game_engine.defeated_enemies_count == 5:
            print("Поздравляю! Ты прошел игру. Пока")
            exit()
        if self.game_engine.count_sum_level() < 3:
            for event in events:
                if self.renderer.button_barbarian_select_to_upgrade.handle_event(event):
                    self.game_engine.level_up("barbarian", self.game_engine.level_dict['Barbarian'] + 1)
                    self._current_state = BATTLE_STATES.BEFORE_FIGHT
                    self.renderer.button_start_game.enable()
                    self.renderer.button_barbarian_select_to_upgrade.disable()
                    self.renderer.button_warrior_select_to_upgrade.disable()
                    self.renderer.button_rogue_select_to_upgrade.disable()
                    self.renderer.button_take_prize_weapon.disable()
                    self.game_engine.main_player.max_health += self.game_engine.main_player.stamina
                    self.game_engine.main_player.health = self.game_engine.main_player.max_health
                if self.renderer.button_warrior_select_to_upgrade.handle_event(event):
                    self.game_engine.level_up("warrior", self.game_engine.level_dict['Warrior'] + 1)
                    self._current_state = BATTLE_STATES.BEFORE_FIGHT
                    self.renderer.button_start_game.enable()
                    self.renderer.button_barbarian_select_to_upgrade.disable()
                    self.renderer.button_warrior_select_to_upgrade.disable()
                    self.renderer.button_rogue_select_to_upgrade.disable()
                    self.renderer.button_take_prize_weapon.disable()
                    self.game_engine.main_player.max_health += self.game_engine.main_player.stamina
                    self.game_engine.main_player.health = self.game_engine.main_player.max_health
                if self.renderer.button_rogue_select_to_upgrade.handle_event(event):
                    self.game_engine.level_up("rogue", self.game_engine.level_dict['Rogue'] + 1)
                    self._current_state = BATTLE_STATES.BEFORE_FIGHT
                    self.renderer.button_start_game.enable()
                    self.renderer.button_barbarian_select_to_upgrade.disable()
                    self.renderer.button_warrior_select_to_upgrade.disable()
                    self.renderer.button_rogue_select_to_upgrade.disable()
                    self.renderer.button_take_prize_weapon.disable()
                    self.game_engine.main_player.max_health += self.game_engine.main_player.stamina
                    self.game_engine.main_player.health = self.game_engine.main_player.max_health
            screen.blit(self.renderer.win_scroll_prize, (130, 100))
            self.renderer.button_barbarian_select_to_upgrade.draw(screen)
            self.renderer.button_warrior_select_to_upgrade.draw(screen)
            self.renderer.button_rogue_select_to_upgrade.draw(screen)

            # Tooltips for upgrade buttons
            mouse_pos = p.mouse.get_pos()
            hover_text = None

            def next_upgrade_text(cls_name: str) -> str:
                lvl = self.game_engine.level_dict[cls_name]
                if cls_name == 'Rogue':
                    if lvl == 0:
                        return "Разбойник: Скрытая атака — +1 к урону, если ловкость выше цели."
                    elif lvl == 1:
                        return "Разбойник: +1 к ловкости."
                    elif lvl == 2:
                        return "Разбойник: Яд — наносит дополнительные (номер хода - 1) урона."
                elif cls_name == 'Warrior':
                    if lvl == 0:
                        return "Воин: Порыв — в первый ход двойной урон оружием."
                    elif lvl == 1:
                        return "Воин: Щит — -3 к получаемому урону при большей силе."
                    elif lvl == 2:
                        return "Воин: +1 к силе."
                elif cls_name == 'Barbarian':
                    if lvl == 0:
                        return "Варвар: Ярость — первые 3 хода +2 урона, затем -1."
                    elif lvl == 1:
                        return "Варвар: Каменная кожа — уменьшает получаемый урон на выносливость."
                    elif lvl == 2:
                        return "Варвар: +1 к выносливости."
                return ""

            if self.renderer.button_barbarian_select_to_upgrade.rect.collidepoint(mouse_pos):
                hover_text = next_upgrade_text('Barbarian')
            elif self.renderer.button_warrior_select_to_upgrade.rect.collidepoint(mouse_pos):
                hover_text = next_upgrade_text('Warrior')
            elif self.renderer.button_rogue_select_to_upgrade.rect.collidepoint(mouse_pos):
                hover_text = next_upgrade_text('Rogue')

            if hover_text:
                self.tooltip.draw(screen, hover_text, (mouse_pos[0] + 12, mouse_pos[1] + 12))
        else:
            screen.blit(self.renderer.win_scroll_prize_max_level, (130, 100))
            for event in events:
                if self.renderer.button_continue_after.handle_event(event):
                    self.renderer.button_take_prize_weapon.disable()
                    self.renderer.button_continue_after.disable()
                    self.renderer.button_start_game.enable()
                    self._current_state = BATTLE_STATES.BEFORE_FIGHT
                    self.game_engine.main_player.health = self.game_engine.main_player.max_health
            self.renderer.button_continue_after.draw(screen)

        for event in events:
            if self.renderer.button_take_prize_weapon.handle_event(event):
                self.game_engine.main_player.weapon = self.game_engine.enemy.prizeWeapon
                self.renderer.button_take_prize_weapon.disable()
        self.renderer.button_take_prize_weapon.draw(screen)
        mouse_pos = p.mouse.get_pos()
        if self.renderer.button_take_prize_weapon.rect.collidepoint(mouse_pos):
            w = self.game_engine.enemy.prizeWeapon
            self.tooltip.draw(screen, f"Оружие:{self.game_engine.main_player.weapon.name} -> {w.name}\nУрон: "
                                 f"{self.game_engine.main_player.weapon.damage} -> {w.damage}\nТип атаки: "
                                 f"{self.game_engine.main_player.weapon.attack_type} -> {w.attack_type}",
                         (mouse_pos[0] + 12, mouse_pos[1] + 12))
