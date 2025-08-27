import pygame

WIN_WIDTH = 540
WIN_HEIGHT = 360

#COLORS
COLOR_TEXT_YELLOW = (255,232,31)
COLOR_TEXT_DARK = (0, 0, 0)
COLOR_TEXT_WHITE = (255,255,255)
COLOR_TEXT_GREEN = (50,205,50)
COLOR_TEXT_GREENYELLOW = (173,255,47)

# Fonts
FONT_JEDI = 'Star Jedi'
FONT_JEDI_BORDERED = 'StarJedi Special Edition'
FONT_JEDI_OUTLINE = 'Star Jedi Hollow'

# Speed
ENTITY_SPEED = {
    # Level 1
    'Starfield': 1,
    # Player
    'Player1': 3,
    'Player2': 3,
}

# Health
ENTITY_HEALTH = {
    'Player1': 1000,
    'Player2': 1000,
    'sm_asteroid': 100,
    'md_asteroid': 300,
    'lg_asteroid': 800,
}

# Damage
ENTITY_DAMAGE = {
    'Player1': 1000,
    'Player2': 1000,
    'sm_asteroid': 100,
    'md_asteroid': 300,
    'lg_asteroid': 800,
}

# Event
EVENT_PLANETS = pygame.USEREVENT
EVENT_OBSTACLES = pygame.USEREVENT +1
