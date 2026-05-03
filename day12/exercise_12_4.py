# Exercise 12-4: Rocket
# Build a Rocket that can move in all four directions.
#
# Steps:
# 1. Create rocket.py with a Rocket class (like Ship but supports up/down too)
# 2. In __init__: start at center of screen, store float position
# 3. In update(): check four flags — moving_right, moving_left, moving_up, moving_down
# 4. In the main game loop: handle K_UP, K_DOWN, K_LEFT, K_RIGHT key events
# 5. The rocket should not fly off any edge of the screen
#
# TODO: Create rocket.py with all four movement directions
# TODO: Add boundary checks for all four edges
# TODO: Run and test all four arrow keys

# Hint — boundary check pattern:
# if self.moving_right and self.rect.right < self.screen.get_rect().right:
#     self.x += self.settings.rocket_speed
# if self.moving_up and self.rect.top > 0:
#     self.y -= self.settings.rocket_speed
