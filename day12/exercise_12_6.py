# Exercise 12-6: Sideways Shooter (stretch goal)
# Make the ship sit on the LEFT side and shoot bullets to the RIGHT.
#
# Steps:
# 1. Position the ship at midleft of screen: self.rect.midleft = screen.get_rect().midleft
# 2. Ship moves up/down (K_UP, K_DOWN) instead of left/right
# 3. Bullets travel RIGHT: self.x += self.settings.bullet_speed
#    Use self.rect.midright as the starting position for bullets
# 4. Remove bullets when they go off the right edge: bullet.rect.left >= screen_width
#
# TODO: Modify ship starting position to left side
# TODO: Change movement keys to up/down
# TODO: Change bullet direction to move right
# TODO: Update bullet removal condition
