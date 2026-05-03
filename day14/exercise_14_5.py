# Exercise 14-5: All-Time High Score
# Save the high score to a file so it persists between game sessions.
#
# Steps:
# 1. On game start, read the high score from a file (use json.loads or Path.read_text)
#    If the file doesn't exist, start with 0
# 2. In check_high_score(), write the new high score to the file whenever it's beaten
# 3. Use pathlib.Path for file operations (same pattern as Chapter 10)
#
# TODO: Load high score from high_score.json at game start
# TODO: Save high score to high_score.json whenever it's beaten

# Hint:
# from pathlib import Path
# import json
#
# path = Path('high_score.json')
# if path.exists():
#     high_score = json.loads(path.read_text())
# else:
#     high_score = 0
