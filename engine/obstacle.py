import pygame
import pymunk
import math

class BasePhysicsObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, mass, elasticity, friction):
        super().__init__()
        moment = pymunk.moment_for_box(mass, (width, height))
        self.body = pymunk.Body(mass, moment)
        self.body.position = x, y

        self.shape = pymunk.Poly.create_box(self.body, (width, height))
        self.shape.elasticity = elasticity
        self.shape.friction = friction

        self.width = width
        self.height = height

class Obstacle(BasePhysicsObject):
    def __init__(self, x, y, isVertical, width, height, mass=2, elasticity=0.2, friction=0.9):
        super().__init__(x, y, width, height, mass, elasticity, friction)

        path = "./res/sprites/vertical.png" if isVertical else "./res/sprites/horizontal.png"
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.original = self.image
        self.rect = self.image.get_rect(center=self.body.position)

    def update(self):
        angle = -math.degrees(self.body.angle) 
        rotated_image = pygame.transform.rotate(self.original, angle)
        self.image = rotated_image
        self.rect = self.image.get_rect(center=self.body.position)

class MovingObstacle(BasePhysicsObject):
    def __init__(self, x, y, width, height, velocity, mass=50, elasticity=0.2, friction=0.9):
        super().__init__(x, y, width - 20, height - 40, mass, elasticity, friction)

        self.frames = [
            pygame.image.load("./res/sprites/bird.png").convert_alpha(),
            pygame.image.load("./res/sprites/bird2.png").convert_alpha(),
            pygame.image.load("./res/sprites/bird3.png").convert_alpha()
        ]
        self.frames = [pygame.transform.scale(f, (width, height)) for f in self.frames]
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 0.2

        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=self.body.position)
        self.body.isHit = False

        def zero_gravity(body, gravity, damping, dt):
            pymunk.Body.update_velocity(body, (0, 0), damping, dt)

        self.body.velocity_func = zero_gravity
        self.body.velocity = velocity
        self.shape.collision_type = 1

    def update(self, dt):
        self.animation_timer += dt

        if not self.body.isHit and self.body.position.x < -self.width:
            self.body.position = pymunk.Vec2d(2500, 300)

        if self.body.isHit:
            self.current_frame = 2 
        elif self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % 2

        angle = -math.degrees(self.body.angle)
        rotated_image = pygame.transform.rotate(self.frames[self.current_frame], angle)
        self.image = rotated_image
        self.rect = self.image.get_rect(center=self.body.position)
