import requests
import random
from file_workers import download_image


def get_comics_count():
    url = 'https://xkcd.com/info.0.json'
    current_comic = requests.get(url).json()
    return current_comic['num']


def get_random_comic():
    url_template = 'https://xkcd.com/{}/info.0.json'
    comics_count = get_comics_count()
    comic_id = random.randint(1, comics_count)
    comic_url = url_template.format(comic_id)
    comic = requests.get(comic_url).json()
    return comic
