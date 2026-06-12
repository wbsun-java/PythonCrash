from pygame.sprite import Sprite
import pygame


class Explosion(Sprite):
    """A class to manage explosions when an alien is hit."""

    def __init__(self, position):
        super().__init__()
        self.radius = 5
        self.timer = 20
        self.image = pygame.Surface((60, 60), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=position)

    def update(self):
        self.radius += 2
        pygame.draw.circle(self.image, (255, 200, 0), (30, 30), self.radius)
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
