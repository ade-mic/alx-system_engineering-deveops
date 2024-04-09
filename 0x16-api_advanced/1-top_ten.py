#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Function to query the Reddit API and print the titles of the first 10 hot
    posts for a given subreddit. If an invalid subreddit is given, the function
    prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    data = response.json()['data']['children']
    
    for i in range(min(10, len(data))):
        print(data[i]['data']['title'])

