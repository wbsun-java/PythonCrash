from pathlib import Path
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        image_path = Path(__file__).with_name("alien.bmp")
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.topleft = self.screen_rect.topleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True
        return False
