from pygame.sprite import Sprite
import pygame


class Alien(Sprite):
    def __init__(self, ai_alien):
        super().__init__()
        self.screen = ai_alien.screen
        self.settings = ai_alien.settings
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x = (self.x +
                  self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        if self.rect.right >= self.screen.get_rect().right or self.rect.left <= 0:
            return True
        else:
            return False
