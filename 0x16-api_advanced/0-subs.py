#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of subscribers
If an invalid subreddit is given, the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    """function that queries Reddit"""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'subreddit_subscriber_counter/0.1'}

    # make request to Reddit API
    response = requests.get(url, headers=headers, timeout=5)
    # Check if the subreddit is valid by looking at the status code
    if response.status_code == 200:
        # Parse the JSON response and return the subscriber count
        data = response.json()
        return data['data']['subscribers']
    else:
        # id the status code is not 200
        return 0
