# Core configuration values for the game. Centralize all magic numbers here.
# Tuning these in one place should affect the whole game once files import from config.
from enum import Enum
# Screen and grid
SCREEN_WIDTH = 768
SCREEN_HEIGHT = 768
TILE_SIZE = 32

# Timing
STATE_DELAY_MS = 5000  # milliseconds between turns

# Fonts
DEFAULT_FONT_NAME = 'Comic Sans MS'
FONT_SIZE_MAIN = 36
FONT_SIZE_LOG = 28

# Colors (RGB or RGBA where noted)
COLOR_TEXT = (255, 255, 255)
COLOR_BG = (0, 0, 0)

# Battle log panel defaults (RGBA for bg)
LOG_PANEL_HEIGHT = 110
LOG_PANEL_MARGIN = 10
LOG_PANEL_PADDING = 12
LOG_PANEL_BG = (20, 20, 20, 180)
LOG_PANEL_BORDER = (200, 180, 120)

# Tooltip defaults
TOOLTIP_BG = (32, 32, 32, 220)
TOOLTIP_TEXT = (240, 240, 240)

# UI layout positions (documented for clarity; adjust when extracting renderers)
# Player panel positions
PLAYER_IMAGE_POS = (115, 40)
PLAYER_WEAPON_POS = (215, 110)
PLAYER_STATS_SCROLL_POS = (70, 270)

# Enemy panel positions
ENEMY_IMAGE_POS = (430, 40)
ENEMY_WEAPON_POS = (560, 110)
ENEMY_STATS_SCROLL_POS = (407, 270)

# Number positions (top-left anchors for your number sprites)
PLAYER_POWER_POS = (120, 330)
PLAYER_AGILITY_POS = (120, 375)
PLAYER_STAMINA_POS = (120, 420)
PLAYER_HEALTH_POS = (120, 463)
PLAYER_WEAPON_DMG_POS = (120, 505)

ENEMY_POWER_POS = (607, 330)
ENEMY_AGILITY_POS = (607, 375)
ENEMY_STAMINA_POS = (607, 420)
ENEMY_HEALTH_POS = (607, 463)
ENEMY_WEAPON_DMG_POS = (607, 505)

class BATTLE_STATES(Enum):
    PLAYER_TURN = 0
    ENEMY_TURN = 1
    BEFORE_FIGHT = 2
    AFTER_FIGHT_DEATH = 3
    START = 4
    SELECT_CHARACTER = 5
    FIGHT_COMPILATION = 6
    AFTER_FIGHT_WIN = 7
    PICK_PRIZE = 8
