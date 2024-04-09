#!/usr/bin/python3
"""
This module queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function to query the Reddit API and return the number of subscribers
    for a given subreddit. If an invalid subreddit is given, the function
    returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    return response.json()['data']['subscribers']
