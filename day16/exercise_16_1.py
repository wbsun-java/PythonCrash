# Exercise 16-1: Sitka Rainfall
# Plot daily rainfall amounts for Sitka, Alaska from a CSV file.
#
# Steps:
# 1. Download sitka_weather_2021_simple.csv from the book's resources
# 2. Inspect the header row — find which column index holds precipitation (PRCP)
# 3. Parse dates with datetime.strptime(row[col], '%Y-%m-%d')
# 4. Convert precipitation values to float (not int — rainfall has decimals)
#    Skip rows with missing data using try/except ValueError
# 5. Plot dates vs rainfall as a bar chart or line chart
#
# TODO: Load and parse the CSV
# TODO: Extract dates and precipitation values
# TODO: Plot with matplotlib

import csv
from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt

# TODO: read CSV, parse dates and rainfall, handle missing values
# TODO: plot and label the chart
