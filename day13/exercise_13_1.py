# Exercise 13-1: Stars
# Fill the background with a field of stars instead of a plain color.
#
# Steps:
# 1. Create a Star class (like Alien) that loads a star image or draws a small circle
# 2. Create a Stars group and populate it with randomly positioned stars
#    Use: random.randint(0, screen_width) for x, random.randint(0, screen_height) for y
# 3. Draw all stars in the game loop before drawing the ship
#
# TODO: Create star.py with a Star sprite class
# TODO: Populate stars group with ~50 random positions
# TODO: Draw stars each frame before everything else

# Exercise 13-3: Raindrops
# Make raindrops fall from the top of the screen.
#
# Steps:
# 1. Create a Raindrop class that starts at a random x, y=0
# 2. Each update(), move the raindrop down: self.y += self.settings.drop_speed
# 3. When a raindrop goes below the screen, remove it and add a new one at top
#
# TODO: Create raindrop.py with downward movement
# TODO: Add new raindrops each frame to maintain a consistent number
