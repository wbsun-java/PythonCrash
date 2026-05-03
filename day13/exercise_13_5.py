# Exercise 13-5: Sideways Shooter Part 2
# Continue Exercise 12-6: add aliens that enter from the right and move left.
#
# Steps:
# 1. Create a SidewaysAlien that starts off the right edge (rect.left = screen_width)
# 2. Each update(), move left: self.x -= self.settings.alien_speed
# 3. Remove aliens that move off the left edge
# 4. Detect bullet-alien collisions using groupcollide()
# 5. Detect ship-alien collisions using spritecollideany()
#
# TODO: Create sideways_alien.py moving from right to left
# TODO: Add collision detection for bullets and ship
# TODO: Remove aliens that pass the left edge (they "got through")
