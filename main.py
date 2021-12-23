import os
import vkapi
import xkcd

from environs import Env


if __name__ == '__main__':
    env = Env()
    env.read_env()
    vk_group_id = env.int('VK_GROUP_ID')
    vk_access_token = env('VK_ACCESS_TOKEN')
    vk_api_version = '5.131'

    comic = xkcd.get_random_comic()
    comic_filename = xkcd.download_comic(comic)
    comic_message = comic['alt']

    comic_attachment = vkapi.upload_photo_to_group_wall(
        vk_access_token,
        api_version=vk_api_version,
        group_id=vk_group_id,
        filename=comic_filename
    )

    os.remove(comic_filename)

    vkapi.wall_post(
        vk_access_token,
        api_version=vk_api_version,
        group_id=vk_group_id,
        message=comic_message,
        attachments=comic_attachment
    )
