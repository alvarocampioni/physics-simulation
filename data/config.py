import pygame
from ui.theme import Theme

# dimensoes
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1280 

# cores
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (50, 150, 255)
BLACK = (0, 0, 0)
GREEN = (50, 200, 50)
LIGHT_GRAY = (220, 220, 220)
DARK_GRAY = (80, 80, 80)

SPRITE_SETS = {
    "bird": [
        "./res/sprites/bird.png",
        "./res/sprites/bird2.png",
        "./res/sprites/bird3.png"
    ],
    "monkey": [
        "./res/sprites/monkey.png",
        "./res/sprites/monkey2.png"
    ],
    "floor": [
        "./res/sprites/floor.png", 
        "./res/sprites/floor_moon.png", 
        "./res/sprites/floor_mars.png"
    ],
    "wall": [
        "./res/sprites/wall.png"
    ]
}

# valores padrao para a simulacao
FPS = 60
PIXELS_PER_METER = 30
INITIAL_VELOCITY_REAL = 5.0 
LAUNCH_ANGLE_DEG = 20.0  
ENERGY_LOSS_FACTOR = 0.8
DAMPING = 1 
TRAJECTORY_INTERVAL = 0.1
SPAWN_INTERVAL = 20
INTERCEPT_SPEED_LIMIT = 20

# cenarios
PLANET_THEMES = [
    Theme("Earth", 9.81, (0, 0, 0)),
    Theme("Moon", 1.62, (255, 255, 255)),
    Theme("Mars", 3.71, (0, 0, 0))
]

DEFAULT_THEME = PLANET_THEMES[0]
START_VEL = "15"
START_ANG = "30"

# interface
INPUT_BG_COLOR = (245, 245, 245)
INPUT_BORDER_COLOR = (100, 100, 100)
INPUT_BOX_VELOCITY = pygame.Rect(20, 80, 220, 50)
INPUT_BOX_ANGLE = pygame.Rect(20, 170, 220, 50)

COLOR_INACTIVE = INPUT_BORDER_COLOR
COLOR_ACTIVE = BLUE

# propriedades do chao
FLOOR_HEIGHT = 250
FLOOR_Y = SCREEN_HEIGHT - FLOOR_HEIGHT

# propriedades da parede
WALL_X = 0
WALL_Y = SCREEN_HEIGHT - FLOOR_HEIGHT - 300
WALL_HEIGHT = 300
WALL_WIDTH = 180

START_X = WALL_X + 160 
START_Y = SCREEN_HEIGHT - FLOOR_HEIGHT - WALL_HEIGHT - 12

def get_font():
    return pygame.font.Font(None, 36), pygame.font.Font(None, 42)
