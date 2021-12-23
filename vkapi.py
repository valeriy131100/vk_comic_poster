import requests


def get_wall_uploading_server(access_token, api_version, group_id):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {
        'access_token': access_token,
        'v': api_version,
        'group_id': group_id
    }

    uploading_server = requests.get(url, params=params)
    return uploading_server.json()['response']


def upload_photo_to_vk(access_token, api_version, uploading_server_url, filename, group_id):
    params = {
        'access_token': access_token,
        'v': api_version,
        'group_id': -group_id
    }

    with open(filename, 'rb') as image:
        files = {
            'file1': image
        }

        uploaded_photo = requests.post(uploading_server_url, params=params, files=files).json()
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

    saved_photo = requests.post(url, params=params)
    return saved_photo.json()['response'][0]


def post_on_wall(access_token, api_version, group_id, from_group=True, message=None, attachments=None):
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'access_token': access_token,
        'v': api_version,
        'owner_id': -group_id,
        'message': message,
        'attachments': attachments,
        'from_group': from_group
    }
    post = requests.post(url, params=params).json()['response']
    return post


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

