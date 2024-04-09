#!/usr/bin/python3
"""
This module queries the Reddit API and returns a list containing the titles of
all hot articles for a given subreddit. If no results are found for the given
subreddit, the function returns None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function to query the Reddit API and return a list of the titles
    of all hot articles for a given subreddit. If an invalid subreddit is
    given, the function returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()['data']
    hot_list.extend([post['data']['title'] for post in data['children']])

    if data['after'] is not None:
        return recurse(subreddit, hot_list, data['after'])

    return hot_list
