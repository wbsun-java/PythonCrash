# Exercise 17-2: Active Discussions
# Use the Hacker News API to find the current top stories with the most comments.
#
# Steps:
# 1. Fetch the top story IDs: https://hacker-news.firebaseio.com/v0/topstories.json
# 2. Loop through the first 30 IDs, fetch each story's details:
#    https://hacker-news.firebaseio.com/v0/item/{id}.json
# 3. Collect: title, comment count (kids), URL
# 4. Sort by comment count (descending) and print the top 10
# 5. Bonus: plot as a bar chart with plotly
#
# TODO: Fetch top story IDs
# TODO: Loop through first 30, fetch each story
# TODO: Sort and display top 10 by comment count

import requests

top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# TODO: fetch story IDs
# TODO: fetch details for first 30 stories
# TODO: sort and display top 10
