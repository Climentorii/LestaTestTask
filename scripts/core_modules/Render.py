import pygame as p
from scripts.characters.Character import Character
from scripts.constants import config
from pygame import Surface
from scripts.ui.Tooltip import Tooltip
from scripts.ui.TooltipManagement import TooltipManager
from scripts.ui.Button import Button
from scripts.constants.config import BATTLE_STATES

WIDTH = config.SCREEN_WIDTH
HEIGHT = config.SCREEN_HEIGHT
TILE_SIZE = config.TILE_SIZE
N = WIDTH // TILE_SIZE

number_dict = {
            0 : p.image.load("./assets/NumberSprites/0.png").convert_alpha(),
            1 : p.image.load("./assets/NumberSprites/1.png").convert_alpha(),
            2 : p.image.load("./assets/NumberSprites/2.png").convert_alpha(),
            3 : p.image.load("./assets/NumberSprites/3.png").convert_alpha(),
            4 : p.image.load("./assets/NumberSprites/4.png").convert_alpha(),
            5 : p.image.load("./assets/NumberSprites/5.png").convert_alpha(),
            6 : p.image.load("./assets/NumberSprites/6.png").convert_alpha(),
            7 : p.image.load("./assets/NumberSprites/7.png").convert_alpha(),
            8 : p.image.load("./assets/NumberSprites/8.png").convert_alpha(),
            9 : p.image.load("./assets/NumberSprites/9.png").convert_alpha(),
}

class Renderer:

    def __init__(self, screen: p.Surface, tooltip_manager: TooltipManager):
        self.screen = screen
        self.T = tooltip_manager
        self.current_state: BATTLE_STATES
        self.initialize_sprites()
        
    def draw_number_image(self, number: int, x: int, y: int):
        margin = 0
        if number < 0:
            number = 0
        str_number = str(number)
        for ch in str_number:
            self.screen.blit(number_dict[int(ch)], (x + margin * 15, y))
            margin += 1

    def draw_perks(self, player: Character, x, y):
        margin = 0
        for perk in player.perks_list:
            self.screen.blit(perk.image, (x, y + margin * 70))
            margin += 1

    def initialize_sprites(self):
        
        self.button_select_class = Button(256, 340, "./assets/SelectScroll.png",
                             "./assets/SelectScrollHovered.png",
                             "./assets/SelectScrollClicked.png",
                             "./assets/Empty.png")
        self.button_warrior_select = Button(256, 150, "./assets/WarriorButton/WarriorButton.png",
                                    "./assets/WarriorButton/WarriorButtonHovered.png",
                                    "./assets/WarriorButton/WarriorButtonClicked.png",
                                    "./assets/Empty.png")

        self.button_barbarian_select = Button(256, 270, "./assets/BarbarianButton/BarbarianButton.png",
                                    "./assets/BarbarianButton/BarbarianButtonHovered.png",
                                    "./assets/BarbarianButton/BarbarianButtonClicked.png",
                                    "./assets/Empty.png")

        self.button_rogue_select = Button(256, 390, "./assets/RogueButton/RogueButton.png",
                                    "./assets/RogueButton/RogueButtonHovered.png",
                                    "./assets/RogueButton/RogueButtonClicked.png",
                                    "./assets/Empty.png")

        self.button_warrior_select_to_upgrade = Button(256, 660, "./assets/WarriorButton/WarriorButton.png",
                                    "./assets/WarriorButton/WarriorButtonHovered.png",
                                    "./assets/WarriorButton/WarriorButtonClicked.png",
                                    "./assets/Empty.png")

        self.button_barbarian_select_to_upgrade = Button(256, 560, "./assets/BarbarianButton/BarbarianButton.png",
                                    "./assets/BarbarianButton/BarbarianButtonHovered.png",
                                    "./assets/BarbarianButton/BarbarianButtonClicked.png",
                                    "./assets/Empty.png")

        self.button_rogue_select_to_upgrade = Button(256, 460, "./assets/RogueButton/RogueButton.png",
                                    "./assets/RogueButton/RogueButtonHovered.png",
                                    "./assets/RogueButton/RogueButtonClicked.png",
                                    "./assets/Empty.png")

        self.button_take_prize_weapon = Button(256, 360, "./assets/TakeWeaponButton.png",
                                    "./assets/TakeWeaponButton.png",
                                    "./assets/TakeWeaponButton.png",
                                    "./assets/Empty.png")

        self.button_back_to_menu = Button(256, 510, "./assets/ShortScrollBackButton.png",
                                    "./assets/ShortScrollBackButton.png",
                                    "./assets/ShortScrollBackButton.png",
                                    "./assets/Empty.png")

        self.button_back_to_select = Button(70, 610, "./assets/ShortScrollBackButton.png",
                                    "./assets/ShortScrollBackButton.png",
                                    "./assets/ShortScrollBackButton.png",
                                    "./assets/Empty.png")

        self.button_start_game = Button(440, 610, "./assets/ShortScrollStartButton.png",
                                    "./assets/ShortScrollStartButton.png",
                                    "./assets/ShortScrollStartButton.png",
                                    "./assets/Empty.png")

        self.button_new_game = Button(70, 510, "./assets/NewGameButton.png",
                                "./assets/NewGameButton.png",
                                "./assets/NewGameButton.png",
                                "./assets/Empty.png")

        self.button_exit = Button(440, 510, "./assets/ExitButton.png",
                                "./assets/ExitButton.png",
                                "./assets/ExitButton.png",
                                "./assets/Empty.png")

        self.button_continue = Button(256, 460, "./assets/ContinueButton.png",
                                "./assets/ContinueButton.png",
                                "./assets/ContinueButton.png",
                                "./assets/Empty.png")

        self.button_continue_after = Button(256, 520, "./assets/ContinueButton.png",
                                "./assets/ContinueButton.png",
                                "./assets/ContinueButton.png",
                                "./assets/Empty.png")
        
        self.scroll_for_stats = p.image.load("./assets/ScrollForStats.png").convert_alpha()
        self.scroll_for_stats = p.transform.scale(self.scroll_for_stats, (288, 360))

        self.scroll_for_stats_player = p.image.load("./assets/ScrollForStatsEnemy.png").convert_alpha()
        self.scroll_for_stats_player = p.transform.scale(self.scroll_for_stats_player, (288, 360))

        self.death_scroll = p.image.load("./assets/DeathScroll.png").convert_alpha()
        self.death_scroll = p.transform.scale(self.death_scroll, (512, 256))

        self.win_scroll_1 = p.image.load("./assets/WinScroll1.png").convert_alpha()
        self.win_scroll_1 = p.transform.scale(self.win_scroll_1, (512, 256))

        self.win_scroll_prize = p.image.load("./assets/WinPrizeScroll.png").convert_alpha()
        self.win_scroll_prize = p.transform.scale(self.win_scroll_prize, (512, 256))

        self.win_scroll_prize_max_level = p.image.load("./assets/WinPrizeScrollMaxLevel.png").convert_alpha()
        self.win_scroll_prize_max_level = p.transform.scale(self.win_scroll_prize_max_level, (512, 256))

        self.tile_image = p.image.load("./assets/backgroundTile.png").convert()
        self.tile_image = p.transform.scale(self.tile_image, (32, 32))
        
        self.button_warrior_select.disable()
        self.button_rogue_select.disable()
        self.button_barbarian_select.disable()
        self.button_warrior_select_to_upgrade.disable()
        self.button_barbarian_select_to_upgrade.disable()
        self.button_rogue_select_to_upgrade.disable()
        self.button_take_prize_weapon.disable()

        self.button_back_to_menu.disable()
        self.button_back_to_select.disable()
        self.button_start_game.disable()
        self.button_new_game.disable()
        self.button_exit.disable()
        self.button_continue.disable()
        self.button_continue_after.disable()

    def draw_battle_common(self, player: Character, enemy: Character,
                       scroll_enemy: Surface, scroll_player: Surface):
    # Sprites
        self.screen.blit(player.image, config.PLAYER_IMAGE_POS)
        self.screen.blit(player.weapon.image, config.PLAYER_WEAPON_POS)
        self.screen.blit(enemy.image, config.ENEMY_IMAGE_POS)
        self.screen.blit(enemy.prizeWeapon.image, config.ENEMY_WEAPON_POS)
        # Scrolls
        self.screen.blit(scroll_enemy, config.ENEMY_STATS_SCROLL_POS)
        self.screen.blit(scroll_player, config.PLAYER_STATS_SCROLL_POS)
        # Perks
        self.draw_perks(player, 0, 100)
        self.draw_perks(enemy, 700, 100)
        # Player number stats
        self.draw_number_image(player.power, *config.PLAYER_POWER_POS)
        self.draw_number_image(player.agility, *config.PLAYER_AGILITY_POS)
        self.draw_number_image(player.stamina, *config.PLAYER_STAMINA_POS)
        self.draw_number_image(player.health, *config.PLAYER_HEALTH_POS)
        self.draw_number_image(player.weapon.damage, *config.PLAYER_WEAPON_DMG_POS)
        # Enemy number stats
        self.draw_number_image(enemy.power, *config.ENEMY_POWER_POS)
        self.draw_number_image(enemy.agility, *config.ENEMY_AGILITY_POS)
        self.draw_number_image(enemy.stamina, *config.ENEMY_STAMINA_POS)
        self.draw_number_image(enemy.health, *config.ENEMY_HEALTH_POS)
        self.draw_number_image(enemy.weapon.damage, *config.ENEMY_WEAPON_DMG_POS)

    def render_battle_state(self, player: Character, enemy: Character,
                        scroll_for_stats: Surface, scroll_for_stats_player: Surface,
                        tooltip: Tooltip):
        self.draw_battle_common(player, enemy, scroll_for_stats, scroll_for_stats_player)
        mouse_pos = p.mouse.get_pos()
        hover_text = self.T.build_battle_hover_text(mouse_pos, player, enemy)
        if hover_text:
            tooltip.draw(self.screen, hover_text, (mouse_pos[0] + 12, mouse_pos[1] + 12))
    
    def draw_background(self):
        for y in range(N):
            for x in range(N):
                self.screen.blit(self.tile_image, (x * TILE_SIZE, y * TILE_SIZE))