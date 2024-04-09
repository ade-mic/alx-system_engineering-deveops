#!/usr/bin/python3
"""
This module queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit, after=None):
    """
    Recursive function to query the Reddit API and return the
    number of subscribersfor a given subreddit.
    If an invalid subreddit is given, the function
    returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom'}
    params = {'after': after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()['data']
    subscribers = data.get('subscribers', 0)

    if data['after'] is not None:
        subscribers += number_of_subscribers(subreddit, data['after'])

    return subscribers
