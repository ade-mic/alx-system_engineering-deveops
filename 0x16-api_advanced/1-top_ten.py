#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles
of the first 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """Querries the Reddit API and prints the titles of
    the first 10 hot posts for a given subreddit.
    if not a valid subreddit prints None"""
    if subreddit is not None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        headers = {'User-Agent': 'my_reddit_bot/1.0'}
        response = requests.get(url, headers=headers,
                                allow_redirects=False, timeout=5)
        if response.status_code != 200:
            print("None")
        else:
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                for post in data['data']['children']:
                    print(post['data']['title'])
