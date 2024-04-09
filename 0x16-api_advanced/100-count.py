#!/usr/bin/python3
"""
This module queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""
from collections import Counter
import re
import requests


def count_words(subreddit, word_list, after=None, word_count=Counter()):
    """
    Recursive function to query the Reddit API, parse the titles of all
    hot articles, and print a sorted count of given keywords.
    If an invalid subreddit is given, the function prints nothing.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom'}
    params = {'after': after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()['data']
    titles = [post['data']['title'] for post in data['children']]

    for title in titles:
        words = re.findall(r'\b\w+\b', title.lower())
        for word in words:
            if word in word_list:
                word_count[word] += 1

    if data['after'] is not None:
        return count_words(subreddit, word_list, data['after'], word_count)

    word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    for word, count in word_count:
        print(f'{word}: {count}')
