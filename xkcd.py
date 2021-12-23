import requests
import random


def get_comics_count():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    current_comic = response.json()
    return current_comic['num']


def get_random_comic():
    url_template = 'https://xkcd.com/{}/info.0.json'
    comics_count = get_comics_count()
    comic_id = random.randint(1, comics_count)
    comic_url = url_template.format(comic_id)
    response = requests.get(comic_url)
    response.raise_for_status()
    comic = response.json()
    return comic
