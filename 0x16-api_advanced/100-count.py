#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests

def count_words(subreddit, word_list, after=None, count_dict={}):
    if after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                count_dict[word] = count_dict.get(word, 0) + title.count(word.lower())
        
        after = data['data']['after']
        if after is not None:
            count_words(subreddit, word_list, after, count_dict)
        else:
            sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print("{}: {}".format(word, count))
    else:
        print("Invalid subreddit or no posts match.")


