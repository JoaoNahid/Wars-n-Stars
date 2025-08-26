import pygame

WIN_WIDTH = 540
WIN_HEIGHT = 360

#COLORS
COLOR_TEXT_YELLOW = (255,232,31)
COLOR_TEXT_DARK = (0, 0, 0)
COLOR_TEXT_WHITE = (255,255,255)

# Fonts
FONT_JEDI = 'Star Jedi'
FONT_JEDI_BORDERED = 'StarJedi Special Edition'
FONT_JEDI_OUTLINE = 'Star Jedi Hollow'

# Speed
ENTITY_SPEED = {
    # Player
    'Player1': 3,
    'Player2': 3,
    # Enemy
    'Enemy1': 3,
    'Enemy2': 5,
    # Level 1
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
}

# Event
EVENT_ENEMY = pygame.USEREVENT + 1
