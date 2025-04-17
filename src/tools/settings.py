import pygame
from pygame.font import SysFont
pygame.init()

# Colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (219, 216, 206)
LIGHT_GREY = (137, 137, 137)
RED = (181, 11, 65)
SKY = (12, 64, 94)
YELLOW = (224, 187, 123)
GREEN = (127, 255, 0)
GOLD = (255, 215, 0)
BLUE = (48, 48, 186)
LINE = (252, 78, 3, 5)
TURQ = (50, 168, 135)
FRAME_ALPHA = 255
# Game settings:
PRIMAL_WIDTH = 1200
PRIMAL_HEIGHT = 720
SCREEN_SIZES = {
    'small': (1200, 720),
    'normal': (1500, 900),
    'big': (1800, 1080)
}
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
SCALE = SCREEN_WIDTH / PRIMAL_WIDTH
FPS = 60
FPS_SHOW = True
TILE_SIZE = int(10 * SCALE)


# Buttons settings:
BUTTON_SIZE = (200, 40)
BUTTON_SMALL_SIZE = (100, 20)
BUTTONS_SPACE = 40
BUTTON_BASIC_COLOR = (105, 77, 86)
BUTTON_ACTIVE_COLOR = (181, 11, 65)
BUTTON_BALANCE_SIZE = (30, 30)

# Icons:
ICON_SIZE = (90, 72)
BALANCE_SPACE = 50
BALANCE_START = 5000

# Rolling:
ROLL_SPEED = 40
ROLL_STEP = 0.1

# Positioner
GRID = False

# Rolling
SQUARE_AMOUNT = 10

# --- Fonts ---------------------------------------------------------------------------------
FONT = 'calibri'
FONT_BIG = SysFont(FONT, 72)
FONT_TIMER = SysFont(FONT, 75, bold=True)
FONT_ROUND = SysFont(FONT, 50, bold=True)
FONT_End = SysFont('verdana', 50, bold=True)
FONT_NORMAL = SysFont('content/fonts/ARCADEPI.ttf', 30)
FONT_SMALL = SysFont(FONT, 15)
FONT_FPS = SysFont(FONT, 30)
FONT_BUTTON = SysFont(FONT, 25)
FONT_ROLL = SysFont(FONT, 20)
