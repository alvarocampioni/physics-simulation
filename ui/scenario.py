import pygame, pymunk

class StaticScenario(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, paths, space):
        super().__init__()

        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Poly.create_box(self.body, (width, height))
        self.body.position = (x + width / 2, y + height / 2)

        self.shape.friction = 0.95
        self.shape.elasticity = 0.9

        space.add(self.body, self.shape)
        self.sprites = []

        self.sprites = [
            pygame.transform.scale(pygame.image.load(path).convert_alpha(), (width, height))
            for path in paths
        ]
        
        self.image = self.sprites[0]    
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = self.body.position

class Floor(StaticScenario):
    def __init__(self, x, y, width, height, paths, space):
        super().__init__(x, y, width, height, paths, space)
        self.current = 0

    def update(self, planet):
        if planet == 'Earth':
            self.current = 0
        elif planet == 'Moon':
            self.current = 1
        elif planet == 'Mars':
            self.current = 2

        self.image = self.sprites[self.current]
        self.rect = self.image.get_rect(center=self.body.position)

