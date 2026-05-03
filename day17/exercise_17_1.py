# Exercise 17-1: Other Languages
# Modify the GitHub API search to find the most-starred repos in a different language.
#
# Steps:
# 1. Change the query parameter: 'q': 'language:javascript' (or any language you like)
# 2. Run the search and print the top 10 repo names, owners, and star counts
# 3. Plot the results as a bar chart with plotly
#
# TODO: Change language in the API query
# TODO: Print top 10 results
# TODO: Plot with plotly bar chart

import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
# TODO: set params for your chosen language
# TODO: make request, process response, plot results
