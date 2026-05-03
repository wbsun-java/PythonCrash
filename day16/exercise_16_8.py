# Exercise 16-8: Recent Earthquakes
# Filter the earthquake JSON data to show only the last 24 hours of quakes.
#
# Steps:
# 1. Load the earthquake JSON file (eq_data_30_day_m1.json or similar)
# 2. Each earthquake has a 'time' property — it's a Unix timestamp in milliseconds
#    Convert to seconds: timestamp = eq_dict['properties']['time'] / 1000
#    Convert to datetime: datetime.fromtimestamp(timestamp)
# 3. Filter to only keep earthquakes from the last 24 hours
# 4. Plot only those quakes on the world map
#
# TODO: Load earthquake JSON
# TODO: Convert timestamps and filter to last 24 hours
# TODO: Plot filtered results with plotly

import json
from pathlib import Path
from datetime import datetime, timedelta

# TODO: load data, filter by time, plot
