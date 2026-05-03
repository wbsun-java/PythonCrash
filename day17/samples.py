# Chapter 17 — Working with APIs
# Uses the requests library to fetch live data from web APIs
# Install first: pip install requests

# --- Fetching data from an API ---
# import requests
#
# url = "https://api.github.com/search/repositories"
# params = {'q': 'language:python', 'sort': 'stars', 'order': 'desc'}
# headers = {'Accept': 'application/vnd.github.v3+json'}
#
# response = requests.get(url, params=params, headers=headers)
# print(f"Status code: {response.status_code}")   # 200 = success
#
# response_dict = response.json()
# print(f"Total repos found: {response_dict['total_count']}")

# --- Processing the response ---
# repo_dicts = response_dict['items']
# for repo_dict in repo_dicts:
#     print(f"\nName: {repo_dict['name']}")
#     print(f"Owner: {repo_dict['owner']['login']}")
#     print(f"Stars: {repo_dict['stargazers_count']}")
#     print(f"Description: {repo_dict['description']}")

# --- Visualizing with plotly ---
# import plotly.express as px
#
# repo_links, stars, hover_texts = [], [], []
# for repo_dict in repo_dicts:
#     name = repo_dict['name']
#     url = repo_dict['html_url']
#     repo_link = f"<a href='{url}'>{name}</a>"    # clickable link in plotly HTML
#     repo_links.append(repo_link)
#     stars.append(repo_dict['stargazers_count'])
#     owner = repo_dict['owner']['login']
#     description = repo_dict.get('description', '')
#     hover_texts.append(f"{owner}<br />{description}")
#
# fig = px.bar(x=repo_links, y=stars, title="Most-Starred Python Repos on GitHub",
#              labels={'x': 'Repository', 'y': 'Stars'},
#              hover_name=hover_texts)
# fig.update_layout(title_font_size=28)
# fig.show()

# --- Hacker News API ---
# import requests
#
# url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
# r = requests.get(url)
# response_dict = r.json()
# comment_ids = response_dict.get('kids', [])   # list of comment IDs
# comment_count = len(comment_ids)

# --- Key ideas ---
# 1. requests.get(url, params=...) appends query string to the URL
# 2. response.status_code — always check this; 200 = OK, 404 = not found
# 3. response.json() converts the response body to a Python dict/list
# 4. .get('key', default) is safer than ['key'] for optional API fields
# 5. Plotly supports HTML in labels — use <a href=...> for clickable bars
# 6. APIs have rate limits — don't call in a tight loop

print("Chapter 17: See the comments above for API and visualization patterns.")
print("Install: pip install requests")
