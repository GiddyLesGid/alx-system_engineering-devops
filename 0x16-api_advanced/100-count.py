#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the count of given keywords in the top hot posts of a subreddit
"""
import re
import requests
import sys


def add_title(dictionary, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile(r"^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """ Queries the Reddit API """
    user_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': user_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    data = res.json()
    hot_posts = data['data']['children']
    add_title(dictionary, hot_posts)
    after = data['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """ Initializes the count_words function """
    dictionary = {}

    for word in word_list:
        dictionary[word.lower()] = 0

    recurse(subreddit, dictionary)

    sorted_items = sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0]))

    for item in sorted_items:
        if item[1] != 0:
            print("{}: {}".format(item[0], item[1]))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Example: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x.lower() for x in sys.argv[2].split()])
