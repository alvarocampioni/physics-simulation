import pygame, pymunk, time
from simulation.core import random_level_generator, create_static_scenario
from data.config import (START_VEL, START_ANG, PIXELS_PER_METER, COLOR_INACTIVE, DAMPING, DEFAULT_THEME)
from ui.background import Background
from engine.physics import start_falling

class GameState:
    def __init__(self):
        self.running_simulation = False
        self.counter_proj = 0
        self.time_elapsed = 0.0
        self.traj_timer = 0.0
        
        self.text_velocity = START_VEL
        self.text_angle = START_ANG
        self.active_box = None

        self.simulation_theme = DEFAULT_THEME
        self.space = pymunk.Space()
        self.space.gravity = (0, self.simulation_theme.gravity * PIXELS_PER_METER)
        self.space.damping = DAMPING

        self.background = Background()

        self.scenario = pygame.sprite.Group()
        self.floor, self.wall = create_static_scenario(self.space, self.scenario)

        self.static_projectiles = []
        self.moving_projectiles = []

        self.structure_obstacles = []
        self.structure_sprites = pygame.sprite.Group()
        random_level_generator(self.space, self.structure_obstacles, self.structure_sprites)

        self.moving_obstacles = []
        self.moving_sprites = pygame.sprite.Group()
        self.moving_timer = 0.0

        self.selecting_target = False
        self.target_x = 0.0
        self.target_y = 0.0

        self.intercept = False
        self.last_time = time.time()
        self.required_velocity = 0.0

        self.color_angle = COLOR_INACTIVE
        self.color_velocity = COLOR_INACTIVE

        handler = self.space.add_collision_handler(1, 2)
        handler.begin = start_falling

    def reset(self):
        self._remove_bodies(self.structure_obstacles, self.structure_sprites)
        self._remove_bodies(self.static_projectiles)
        self._remove_bodies(self.moving_projectiles)
        self._remove_bodies(self.moving_obstacles, self.moving_sprites)

        self.structure_obstacles.clear()
        self.static_projectiles.clear()
        self.moving_projectiles.clear()
        self.moving_obstacles.clear()

        random_level_generator(self.space, self.structure_obstacles, self.structure_sprites)

        self.counter_proj = 0
        self.traj_timer = 0.0
        self.running_simulation = False
        self.time_elapsed = 0.0
        self.last_time = time.time()

    def _remove_bodies(self, objs, group=None):
        for obj in objs:
            if group:
                group.remove(obj)
            self.space.remove(obj.body, obj.shape)

