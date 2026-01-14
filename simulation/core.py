import random

from ui.utils import generate_random_color

from engine.projectile import Projectile

from data.config import (
    FLOOR_HEIGHT, FLOOR_Y, WALL_HEIGHT, 
    WALL_WIDTH, WALL_X, WALL_Y, SCREEN_WIDTH, SPRITE_SETS
)

from engine.obstacle import Obstacle

from ui.scenario import StaticScenario, Floor

def create_static_scenario(space, group):
    floor = Floor(0, FLOOR_Y, SCREEN_WIDTH, FLOOR_HEIGHT, SPRITE_SETS["floor"], space)
    wall = StaticScenario(WALL_X, WALL_Y, WALL_WIDTH, WALL_HEIGHT, SPRITE_SETS["wall"], space)

    group.add(floor, wall)
    return floor, wall

def random_level_generator(space, obstacles, targets):
    min_x = 1000
    amount = random.randint(1, 3)
    
    dist = ((SCREEN_WIDTH - min_x) - amount*60) / amount
    sum_dist = min_x

    for i in range(amount):
        build_obstacles(space, sum_dist, obstacles, targets, random.randint(1, 5))
        sum_dist += dist        
    
def build_obstacles(space, x, obstacles, targets, levels=3):
    ground_y = FLOOR_Y
    tower_x = x

    vertical_width = 20
    vertical_height = 50
    horizontal_width = 60
    horizontal_height = 20
    gap_between = 10

    def add_box(x, y, width, height, is_vertical):
        obs = Obstacle(x, y, is_vertical, width, height)
        space.add(obs.body, obs.shape)
        obstacles.append(obs)
        targets.add(obs)

    def add_verticals(base_y):
        left_x = tower_x - horizontal_width // 2 + vertical_width // 2
        right_x = tower_x + horizontal_width // 2 - vertical_width // 2
        vert_y = base_y - vertical_height // 2

        add_box(left_x, vert_y, vertical_width, vertical_height, True)
        add_box(right_x, vert_y, vertical_width, vertical_height, True)

    def add_horizontal(base_y):
        top_y = base_y - vertical_height - gap_between - horizontal_height // 2
        add_box(tower_x, top_y, horizontal_width, horizontal_height, False)

    for level in range(levels):
        base_y = ground_y - level * (vertical_height + horizontal_height + gap_between)
        add_verticals(base_y)
        add_horizontal(base_y)

def add_projectile(static_projectiles, start_x, start_y, space):
    projectile = None
    if len(static_projectiles) == 0:
        projectile = Projectile(start_x, start_y, generate_random_color())
        static_projectiles.append(projectile)
        space.add(projectile.body, projectile.shape)

