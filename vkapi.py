import requests


class VkApiError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        code = self.error.get('error_code')
        description = self.error.get('error_msg')
        return f'VkApiError code {code}: {description}'


def handle_vk_api_response(response: requests.Response):
    response.raise_for_status()
    api_answer = response.json()
    error = api_answer.get('error')
    if error:
        raise VkApiError(error)
    return api_answer


def get_wall_uploading_server(access_token, api_version, group_id):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {
        'access_token': access_token,
        'v': api_version,
        'group_id': group_id
    }

    response = requests.get(url, params=params)
    uploading_server = handle_vk_api_response(response)
    return uploading_server['response']


def upload_photo_to_vk(access_token, api_version, uploading_server_url,
                       filename, group_id):
    params = {
        'access_token': access_token,
        'v': api_version,
        'group_id': -group_id
    }

    with open(filename, 'rb') as image:
        files = {
            'file1': image
        }

        response = requests.post(
            uploading_server_url,
            params=params,
            files=files
        )
        uploaded_photo = handle_vk_api_response(response)
        return uploaded_photo


def save_wall_photo(access_token, api_version, group_id, photo, server, hash_):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = {
        'access_token': access_token,
        'v': api_version,
        'photo': photo,
        'server': server,
        'hash': hash_,
        'group_id': group_id
    }

    response = requests.post(url, params=params)
    saved_photo = handle_vk_api_response(response)
    return saved_photo['response'][0]


def post_on_wall(access_token, api_version, group_id,
                 from_group=True, message=None, attachments=None):
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'access_token': access_token,
        'v': api_version,
        'owner_id': -group_id,
        'message': message,
        'attachments': attachments,
        'from_group': from_group
    }
    response = requests.post(url, params=params)
    post = handle_vk_api_response(response)
    return post['response']


def upload_photo_to_group_wall(access_token, api_version, filename, group_id):
    uploading_server = get_wall_uploading_server(
        access_token,
        api_version=api_version,
        group_id=group_id
    )

    uploaded_photo = upload_photo_to_vk(
        access_token,
        api_version=api_version,
        uploading_server_url=uploading_server['upload_url'],
        group_id=group_id,
        filename=filename
    )

    saved_photo = save_wall_photo(
        access_token,
        api_version=api_version,
        group_id=group_id,
        server=uploaded_photo['server'],
        photo=uploaded_photo['photo'],
        hash_=uploaded_photo['hash']
    )

    owner_id = saved_photo['owner_id']
    media_id = saved_photo['id']
    return f'photo{owner_id}_{media_id}'
