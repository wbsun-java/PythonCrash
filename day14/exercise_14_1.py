# Exercise 14-1: Press P to Play
# Add a keyboard shortcut so pressing P starts the game (same as clicking Play).
#
# Steps:
# 1. In check_keydown_events(), add:
#    if event.key == pygame.K_p:
#        start_game(ai_game)
# 2. Extract the "start game" logic into a start_game() helper function
#    so both the Play button click and P key call the same code
#
# TODO: Add K_p handler in check_keydown_events()
# TODO: Refactor start logic into a reusable start_game() function

# Exercise 14-2: Target Practice
# Create a version where only one alien appears at a time in a random position.
# It's worth many points. When shot, a new one appears.
#
# TODO: Modify create_fleet() to create just one alien at a random x position
# TODO: Increase alien_points significantly (e.g. 1000)
# TODO: When the alien is shot, immediately create a new one
