#!/usr/bin/python3
"""Fetches the title of all hot posts for a given subreddit recursively."""

import requests


def count_words(subreddit, word_list=[], hot_list=[], after=""):
    """Main function to count word occurrences in hot post titles."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditApp/0.1"}
    params = {"after": after, "limit": 100}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        after = response.json().get("data").get("after")
        hot_posts = response.json().get("data").get("children")
        
        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))
        
        if after is not None:
            return count_words(subreddit, word_list, hot_list, after)

        word_count = {}
        word_list = set(wrd.lower() for wrd in word_list)
        
        for title in hot_list:
            for word in title.split():
                word_lower = word.lower()
                word_count[word_lower] = word_count.get(word_lower, 0) + 1
        
        sorted_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        
        for key, value in sorted_count:
            if key in word_list and value > 0:
                print(f"{key}: {value}")
                
    except Exception:
        return None

