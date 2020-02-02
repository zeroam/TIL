import requests
import json
import time


def get_top_post(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}.json?limit=1'
    headers = {'User-agent': 'imdff0803@gmail.com try tutorial'}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    top_post = data['data']['children'][0]['data']
    return "'{title}' by {author} in {subreddit}".format(**top_post)


def get_top_from_subreddits(subreddits):
    for subreddit in subreddits:
        yield get_top_post(subreddit)
        time.sleep(2)


if __name__ == '__main__':
    get_top_post('test')
    for post in get_top_from_subreddits(['python', 'linux', 'learnpython']):
        print(post)