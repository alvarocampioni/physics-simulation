import pygame, pymunk

class Projectile:

    def __init__(self, x, y, color, radius=12, mass=1, elasticity=0.9, friction=2):
        moment = pymunk.moment_for_circle(mass, 0, radius)

        self.body = pymunk.Body(mass, moment, pymunk.Body.DYNAMIC)
        self.body.position = x, y

        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = elasticity
        self.shape.friction = friction
        self.shape.surface_velocity = (0, 0)
        self.last_pos = None
        self.shape.collision_type = 2
    
        self.color = color
        self.trajectory = []

    def draw_projectile(self, surface, border):
        pygame.draw.circle(surface, self.color, (int(self.body.position.x), int(self.body.position.y)), int(self.shape.radius))
        
        border_width = 2
        pygame.draw.circle(surface, border, (int(self.body.position.x), int(self.body.position.y)), int(self.shape.radius), border_width)


    def draw_trajectory(self, surface):
        if len(self.trajectory) > 0:
            for point in self.trajectory:
                pygame.draw.circle(surface, self.color, point, 3)

    