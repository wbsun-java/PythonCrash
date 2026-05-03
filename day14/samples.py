# Chapter 14 — Scoring
# Adds scoreboard, high score, difficulty levels, and Play button.

# --- Scoreboard class ---
# class Scoreboard:
#     def __init__(self, ai_game):
#         self.ai_game = ai_game
#         self.screen = ai_game.screen
#         self.screen_rect = self.screen.get_rect()
#         self.settings = ai_game.settings
#         self.stats = ai_game.stats
#         self.text_color = (30, 30, 30)
#         self.font = pygame.font.SysFont(None, 48)
#         self.prep_score()
#         self.prep_high_score()
#         self.prep_level()
#         self.prep_ships()
#
#     def prep_score(self):
#         rounded_score = round(self.stats.score, -1)  # round to nearest 10
#         score_str = f"{rounded_score:,}"              # e.g. "1,250"
#         self.score_image = self.font.render(score_str, True,
#                                             self.text_color, self.settings.bg_color)
#         self.score_rect = self.score_image.get_rect()
#         self.score_rect.right = self.screen_rect.right - 20
#         self.score_rect.top = 20
#
#     def show_score(self):
#         self.screen.blit(self.score_image, self.score_rect)
#         self.screen.blit(self.high_score_image, self.high_score_rect)
#         self.screen.blit(self.level_image, self.level_rect)
#         self.ships.draw(self.screen)

# --- Tracking score ---
# def check_bullet_alien_collisions(ai_game):
#     collisions = pygame.sprite.groupcollide(ai_game.bullets, ai_game.aliens, True, True)
#     if collisions:
#         for aliens in collisions.values():              # one bullet may hit multiple aliens
#             ai_game.stats.score += ai_game.settings.alien_points * len(aliens)
#         ai_game.sb.prep_score()
#         check_high_score(ai_game)
#
# def check_high_score(ai_game):
#     if ai_game.stats.score > ai_game.stats.high_score:
#         ai_game.stats.high_score = ai_game.stats.score
#         ai_game.sb.prep_high_score()

# --- Leveling up ---
# def check_aliens_bottom(ai_game):
#     for alien in ai_game.aliens.sprites():
#         if alien.rect.bottom >= ai_game.settings.screen_height:
#             ship_hit(ai_game)           # treat same as ship collision
#             break
#
# def check_level(ai_game):
#     if not ai_game.aliens:              # fleet is empty
#         ai_game.bullets.empty()
#         create_fleet(ai_game)
#         ai_game.settings.increase_speed()   # bump up speeds
#         ai_game.stats.level += 1
#         ai_game.sb.prep_level()

# --- Dynamic settings (increasing difficulty) ---
# class Settings:
#     def __init__(self):
#         self.speedup_scale = 1.1        # 10% faster each level
#         self.score_scale = 1.5          # 50% more points each level
#         self.initialize_dynamic_settings()
#
#     def initialize_dynamic_settings(self):
#         self.ship_speed = 1.5
#         self.bullet_speed = 2.5
#         self.alien_speed = 1.0
#         self.fleet_direction = 1
#         self.alien_points = 50
#
#     def increase_speed(self):
#         self.ship_speed *= self.speedup_scale
#         self.bullet_speed *= self.speedup_scale
#         self.alien_speed *= self.speedup_scale
#         self.alien_points = int(self.alien_points * self.score_scale)

# --- Play button ---
# class Button:
#     def __init__(self, ai_game, msg):
#         self.screen = ai_game.screen
#         self.width, self.height = 200, 50
#         self.button_color = (0, 135, 0)
#         self.text_color = (255, 255, 255)
#         self.font = pygame.font.SysFont(None, 48)
#         self.rect = pygame.Rect(0, 0, self.width, self.height)
#         self.rect.center = self.screen.get_rect().center
#         self._prep_msg(msg)
#
#     def draw_button(self):
#         self.screen.fill(self.button_color, self.rect)
#         self.screen.blit(self.msg_image, self.msg_image_rect)
#
# # Detect Play button click:
# def check_play_button(ai_game, mouse_pos):
#     button_clicked = ai_game.play_button.rect.collidepoint(mouse_pos)
#     if button_clicked and not ai_game.stats.game_active:
#         ai_game.settings.initialize_dynamic_settings()
#         ai_game.stats.reset_stats()
#         ai_game.stats.game_active = True
#         pygame.mouse.set_visible(False)

# --- Key ideas ---
# 1. font.render() produces an image — blit it to screen like any other image
# 2. f"{score:,}" formats numbers with commas (1,250 not 1250)
# 3. collisions.values() is a list of lists — multiply points by len(aliens) hit
# 4. speedup_scale multiplies each level — exponential difficulty increase
# 5. pygame.mouse.set_visible(False) hides cursor once game starts

print("Chapter 14: See the comments above for scoring and difficulty patterns.")
