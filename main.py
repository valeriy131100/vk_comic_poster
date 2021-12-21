import requests
from environs import Env

import vkapi
from file_workers import download_image


if __name__ == '__main__':
    env = Env()
    env.read_env()
    client_id = env.int('CLIENT_ID')
    group_id = env.int('GROUP_ID')
    access_token = env('ACCESS_TOKEN')

    upload_server = vkapi.get_wall_upload_server(
        access_token,
        api_version='5.131',
        group_id=group_id
    )

    print(upload_server)

    xkcd_url_template = 'https://xkcd.com/{}/info.0.json'
    python_comic_id = 353
    python_comic_url = xkcd_url_template.format(python_comic_id)
    python_comic = requests.get(python_comic_url).json()
    download_image(python_comic['img'], 'Python.png')
    print(python_comic['alt'])

    uploaded_photo = vkapi.upload_photo_to_vk(
        access_token,
        api_version='5.131',
        upload_server_url=upload_server['upload_url'],
        group_id=group_id,
        filename='Python.png'
    )

    print(uploaded_photo)
