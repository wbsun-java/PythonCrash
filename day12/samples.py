# Chapter 12 — A Ship That Fires Bullets (Pygame)
# Install first: pip install pygame
# Run the game: python alien_invasion.py

# --- The game loop pattern ---
# import pygame
# pygame.init()
# screen = pygame.display.set_mode((1200, 800))
# pygame.display.set_caption("Alien Invasion")
#
# while True:                          # game loop runs forever
#     for event in pygame.event.get():  # 1. process events
#         if event.type == pygame.QUIT:
#             sys.exit()
#     screen.fill((230, 230, 230))      # 2. update/draw (fill background)
#     pygame.display.flip()             # 3. show the new frame

# --- Settings class ---
# class Settings:
#     def __init__(self):
#         self.screen_width = 1200
#         self.screen_height = 800
#         self.bg_color = (230, 230, 230)
#         self.ship_speed = 1.5

# --- Ship class (uses a .bmp image) ---
# class Ship(pygame.sprite.Sprite):
#     def __init__(self, ai_game):
#         super().__init__()
#         self.screen = ai_game.screen
#         self.settings = ai_game.settings
#         self.image = pygame.image.load('images/ship.bmp')
#         self.rect = self.image.get_rect()
#         self.rect.midbottom = self.screen.get_rect().midbottom
#         self.x = float(self.rect.x)   # float for precise movement
#
#     def update(self):
#         if self.moving_right and self.rect.right < self.screen.get_rect().right:
#             self.x += self.settings.ship_speed
#         if self.moving_left and self.rect.left > 0:
#             self.x -= self.settings.ship_speed
#         self.rect.x = self.x          # rect only accepts int; x stores float
#
#     def blitme(self):
#         self.screen.blit(self.image, self.rect)

# --- Keyboard events ---
# for event in pygame.event.get():
#     if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_RIGHT:
#             ship.moving_right = True
#     if event.type == pygame.KEYUP:
#         if event.key == pygame.K_RIGHT:
#             ship.moving_right = False

# --- Bullet class ---
# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, ai_game):
#         super().__init__()
#         self.screen = ai_game.screen
#         self.settings = ai_game.settings
#         self.color = self.settings.bullet_color
#         self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
#                                 self.settings.bullet_height)
#         self.rect.midtop = ai_game.ship.rect.midtop
#         self.y = float(self.rect.y)
#
#     def update(self):
#         self.y -= self.settings.bullet_speed
#         self.rect.y = self.y
#
#     def draw_bullet(self):
#         pygame.draw.rect(self.screen, self.color, self.rect)

# --- Firing bullets (Space key) ---
# bullets = pygame.sprite.Group()
#
# def fire_bullet(ai_game):
#     if len(ai_game.bullets) < ai_game.settings.bullets_allowed:
#         new_bullet = Bullet(ai_game)
#         ai_game.bullets.add(new_bullet)
#
# # In game loop:
# bullets.update()
# for bullet in bullets.copy():       # remove bullets that go off screen
#     if bullet.rect.bottom <= 0:
#         bullets.remove(bullet)
# for bullet in bullets.sprites():
#     bullet.draw_bullet()

# --- Key ideas ---
# 1. The game loop: events → update → draw → flip. Every frame.
# 2. Store position as float (self.x), display as int (self.rect.x)
# 3. pygame.sprite.Group manages collections — call .update() once for all
# 4. KEYDOWN fires once; KEYUP fires once. Use a flag (moving_right) for smooth movement.
# 5. Settings class centralizes all magic numbers

print("Chapter 12: See the comments above for the full Pygame pattern.")
print("Main files to create: alien_invasion.py, settings.py, ship.py, bullet.py")
