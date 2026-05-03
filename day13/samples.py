# Chapter 13 — Aliens!
# Builds on the Alien Invasion game from Chapter 12.

# --- Alien class ---
# class Alien(pygame.sprite.Sprite):
#     def __init__(self, ai_game):
#         super().__init__()
#         self.screen = ai_game.screen
#         self.settings = ai_game.settings
#         self.image = pygame.image.load('images/alien.bmp')
#         self.rect = self.image.get_rect()
#         self.rect.x = self.rect.width      # start near top-left
#         self.rect.y = self.rect.height
#         self.x = float(self.rect.x)
#
#     def update(self):
#         self.x += self.settings.alien_speed * self.settings.fleet_direction
#         self.rect.x = self.x
#
#     def check_edges(self):
#         screen_rect = self.screen.get_rect()
#         return self.rect.right >= screen_rect.right or self.rect.left <= 0

# --- Fleet direction: 1 = right, -1 = left ---
# settings.fleet_direction = 1
#
# def check_fleet_edges(ai_game):
#     for alien in ai_game.aliens.sprites():
#         if alien.check_edges():
#             drop_fleet(ai_game)         # drop down one row
#             ai_game.settings.fleet_direction *= -1  # reverse direction
#             break
#
# def drop_fleet(ai_game):
#     for alien in ai_game.aliens.sprites():
#         alien.rect.y += ai_game.settings.fleet_drop_speed

# --- Collision detection ---
# # groupcollide(group1, group2, kill1, kill2) → dict of collisions
# collisions = pygame.sprite.groupcollide(ai_game.bullets, ai_game.aliens, True, True)
#
# # spritecollideany(sprite, group) → first colliding sprite or None
# if pygame.sprite.spritecollideany(ai_game.ship, ai_game.aliens):
#     ship_hit(ai_game)

# --- Game state and restarting ---
# class GameStats:
#     def __init__(self, ai_game):
#         self.settings = ai_game.settings
#         self.reset_stats()
#         self.game_active = False        # game starts paused
#
#     def reset_stats(self):
#         self.ships_left = self.settings.ship_limit
#
# def ship_hit(ai_game):
#     if ai_game.stats.ships_left > 0:
#         ai_game.stats.ships_left -= 1
#         ai_game.bullets.empty()         # clear all bullets
#         ai_game.aliens.empty()
#         create_fleet(ai_game)           # fresh fleet
#         ai_game.ship.center_ship()      # ship back to start
#         sleep(0.5)                      # brief pause
#     else:
#         ai_game.stats.game_active = False

# --- Creating the alien fleet ---
# def create_fleet(ai_game):
#     alien = Alien(ai_game)
#     alien_width, alien_height = alien.rect.size
#     available_space_x = ai_game.settings.screen_width - (2 * alien_width)
#     number_aliens_x = available_space_x // (2 * alien_width)
#     ship_height = ai_game.ship.rect.height
#     available_space_y = (ai_game.settings.screen_height - (3 * alien_height) - ship_height)
#     number_rows = available_space_y // (2 * alien_height)
#     for row_number in range(number_rows):
#         for alien_number in range(number_aliens_x):
#             create_alien(ai_game, alien_number, row_number)

# --- Key ideas ---
# 1. Fleet moves by changing fleet_direction: 1 (right) / -1 (left)
# 2. groupcollide() returns a dict — keys are group1 sprites that were hit
# 3. .empty() clears a group completely — use on reset
# 4. GameStats separates game state from display and logic
# 5. spritecollideany() is faster than groupcollide() for single-sprite checks

print("Chapter 13: See the comments above for alien fleet and collision patterns.")
