import requests
from environs import Env
from file_workers import download_image


if __name__ == '__main__':
    env = Env()
    env.read_env()
    client_id = env.int('CLIENT_ID')
    access_token = env('ACCESS_TOKEN')

    xkcd_url_template = 'https://xkcd.com/{}/info.0.json'
    python_comic_id = 353
    python_comic_url = xkcd_url_template.format(python_comic_id)
    python_comic = requests.get(python_comic_url).json()
    download_image(python_comic['img'], 'Python.png')
    print(python_comic['alt'])
