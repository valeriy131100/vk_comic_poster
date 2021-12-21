import os
import vkapi
import xkcd

from environs import Env


if __name__ == '__main__':
    env = Env()
    env.read_env()
    group_id = env.int('GROUP_ID')
    access_token = env('ACCESS_TOKEN')
    api_version = env('API_VERSION')

    comic = xkcd.get_random_comic()
    comic_filename = xkcd.download_comic(comic)
    comic_message = comic['alt']

    comic_attachment = vkapi.upload_photo_to_group_wall(
        access_token,
        api_version=api_version,
        group_id=group_id,
        filename=comic_filename
    )

    os.remove(comic_filename)

    vkapi.wall_post(
        access_token,
        api_version=api_version,
        group_id=group_id,
        attachments=comic_attachment
    )
