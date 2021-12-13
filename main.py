import requests
from file_workers import download_image


if __name__ == '__main__':
    url_template = 'https://xkcd.com/{}/info.0.json'
    python_comic_id = 353
    python_comic_url = url_template.format(python_comic_id)
    python_comic = requests.get(python_comic_url).json()
    download_image(python_comic['img'], 'Python.png')
    print(python_comic['alt'])
