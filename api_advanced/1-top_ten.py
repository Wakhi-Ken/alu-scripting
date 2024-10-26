#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Fetches and prints the titles of the top 10 hot posts in a subreddit."""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        """checks status"""
        if response.status_code == 200:
            hot_posts = response.json().get("data", {}).get("children", [])
            for post in hot_posts:
                print(post.get('data', {}).get('title', 'No Title'))
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)