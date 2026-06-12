from settings import Settings
import sys
import time
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_height)
        )
        self.aliens = pygame.sprite.Group()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
        self.ships_left = self.settings.ship_limit
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            self._update_aliens()
            self._check_fleet_edges()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_screen(self):
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):
        alien = Alien(self)
        alien.rect.x = alien.rect.width + 2 * alien.rect.width
        alien.rect.y = alien.rect.height + 2 * alien.rect.height
        available_space_x = self.settings.screen_width - 2 * alien.rect.width
        number_aliens_x = available_space_x // (2 * alien.rect.width)
        available_space_y = self.settings.screen_height - 2 * alien.rect.height
        number_aliens_y = available_space_y // (2 * alien.rect.height)

        for row_number in range(number_aliens_y):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien.x = alien.rect.width + 2 * alien.rect.width * alien_number    
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    def _update_aliens(self):
        self.aliens.update()
        group_collide = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
    
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        # Explosion animation: draw expanding circles at ship center
        cx, cy = self.ship.rect.centerx, self.ship.rect.centery
        for radius in range(5, 60, 5):
            self.screen.fill(self.settings.background_color)
            self.aliens.draw(self.screen)
            pygame.draw.circle(self.screen, (255, 120, 0), (cx, cy), radius, 4)
            pygame.draw.circle(self.screen, (255, 220, 50), (cx, cy), max(radius - 10, 1), 3)
            pygame.display.flip()
            time.sleep(0.03)

        self.ships_left -= 1
        if self.ships_left <= 0:
            print("Game Over!")
            sys.exit()

        # Reset for next life
        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()
        self.ship.rect.midbottom = self.screen.get_rect().midbottom
        self.ship.x = float(self.ship.rect.x)
        time.sleep(0.5)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
