import requests


def download_image(image_url, image_path):
    response = requests.get(image_url)
    response.raise_for_status()

    with open(image_path, 'wb') as file:
        file.write(response.content)
