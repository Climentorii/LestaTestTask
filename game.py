import pygame as p
from scripts.core_modules.GameEngine import GameEngine
from scripts.ui.Tooltip import Tooltip
from scripts.constants import config
from scripts.constants.config import BATTLE_STATES
from scripts.core_modules.Render import Renderer
from scripts.ui.TooltipManagement import TooltipManager
from scripts.core_modules.ProcessManager import ProcessManager

p.init()

screen = p.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = p.time.Clock()
tooltip = Tooltip()
T = TooltipManager(screen=screen)
R = Renderer(screen=screen, tooltip_manager=T)
game_engine = GameEngine()
PM = ProcessManager(game_engine=game_engine, renderer=R,
                    tooltip=tooltip, tooltip_manager=T)

running = True
while running:
    current_time = p.time.get_ticks()

    screen.fill((0, 0, 0))
    events = p.event.get()
    for event in events:
        if event.type == p.QUIT:
            running = False

    R.draw_background()
    
    if PM.get_current_state() == BATTLE_STATES.START:

        PM.state_start_func(events=events, screen=screen)

    elif PM.get_current_state() == BATTLE_STATES.SELECT_CHARACTER:

        PM.state_select_character_func(events=events, screen=screen)

    elif PM.get_current_state() == BATTLE_STATES.BEFORE_FIGHT:

        PM.state_before_fight_func(events=events, screen=screen)

    elif PM.get_current_state() == BATTLE_STATES.FIGHT_COMPILATION:

        PM.start_new_encounter(current_time=current_time)

    elif PM.get_current_state() == BATTLE_STATES.PLAYER_TURN:

        PM.state_player_turn_func(current_time=current_time, screen=screen)
        
    elif PM.get_current_state() == BATTLE_STATES.ENEMY_TURN:

        PM.state_enemy_turn_func(current_time=current_time, screen=screen)

    elif PM.get_current_state() == BATTLE_STATES.AFTER_FIGHT_DEATH:

        PM.state_after_fight_death_func(events=events, screen=screen)

    elif PM.get_current_state() == BATTLE_STATES.AFTER_FIGHT_WIN:

        PM.state_after_fight_win_func(current_time=current_time, events=events, screen=screen)

    elif PM.get_current_state() == BATTLE_STATES.PICK_PRIZE:

        PM.state_pick_prize_func(current_time=current_time, events=events, screen=screen)

    p.display.flip()
