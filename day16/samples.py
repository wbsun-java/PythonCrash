# Chapter 16 — Downloading Data
# Uses CSV files (weather data) and JSON files (earthquake data)
# Data files available from: https://ehmatthes.github.io/pcc_3e/

# --- Reading a CSV file ---
# import csv
# from pathlib import Path
# from datetime import datetime
#
# path = Path('weather_data/sitka_weather_07-2021_simple.csv')
# lines = path.read_text().splitlines()
# reader = csv.reader(lines)
# header_row = next(reader)           # first row = column names
#
# dates, highs = [], []
# for row in reader:
#     current_date = datetime.strptime(row[2], '%Y-%m-%d')  # parse date string
#     high = int(row[4])
#     dates.append(current_date)
#     highs.append(high)

# --- Plotting the CSV data ---
# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots()
# ax.plot(dates, highs, color='red')
# ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()                  # rotate date labels so they don't overlap
# ax.set_ylabel("Temperature (F)", fontsize=16)
# plt.show()

# --- Handling missing data ---
# for row in reader:
#     try:
#         high = int(row[4])
#     except ValueError:
#         print(f"Missing data for {row[2]}")
#     else:
#         highs.append(high)

# --- Reading a JSON file (earthquakes) ---
# import json
#
# path = Path('eq_data/eq_data_1_day_m1.json')
# contents = path.read_text()
# all_eq_data = json.loads(contents)
#
# all_eq_dicts = all_eq_data['features']       # list of earthquake dicts
# mags, titles, lons, lats = [], [], [], []
#
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     title = eq_dict['properties']['title']
#     lon = eq_dict['geometry']['coordinates'][0]
#     lat = eq_dict['geometry']['coordinates'][1]
#     mags.append(mag)
#     titles.append(title)
#     lons.append(lon)
#     lats.append(lat)

# --- Plotting earthquakes on a world map (plotly) ---
# import plotly.express as px
#
# fig = px.scatter_geo(title='Global Earthquakes',
#                      lat=lats, lon=lons,
#                      size=mags,
#                      color=mags,
#                      color_continuous_scale='Viridis',
#                      labels={'color': 'Magnitude'},
#                      projection='natural earth',
#                      hover_name=titles)
# fig.show()

# --- Key ideas ---
# 1. csv.reader() returns an iterator — call next() once to skip the header
# 2. datetime.strptime(string, format) converts a string to a datetime object
# 3. Always wrap int() or float() conversions in try/except for CSV data
# 4. JSON earthquake data is nested: data['features'][i]['properties']['mag']
# 5. plotly express (px) is simpler than raw plotly for common chart types

print("Chapter 16: See the comments above for CSV and JSON data patterns.")
print("Download sample data from the book's companion site.")
