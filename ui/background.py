import pygame
from data.config import (SCREEN_HEIGHT, SCREEN_WIDTH)

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.backgrounds = [
            pygame.image.load("./res/sprites/back.png").convert_alpha(),
            pygame.image.load("./res/sprites/back_moon.png").convert_alpha(),
            pygame.image.load("./res/sprites/back_mars.png").convert_alpha()
        ]
        self.backgrounds = [pygame.transform.scale(b, (SCREEN_WIDTH, SCREEN_HEIGHT)) for b in self.backgrounds]
        self.current = 0
        self.image = self.backgrounds[self.current]
        self.rect = self.image.get_rect()
    
    def update(self, planet):
        if planet == 'Earth':
            self.current = 0
        elif planet == 'Moon':
            self.current = 1
        elif planet == 'Mars':
            self.current = 2

    def draw(self, surface,):
        self.image = self.backgrounds[self.current]
        surface.blit(self.image, self.rect)
