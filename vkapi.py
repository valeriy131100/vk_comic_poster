import requests


def get_wall_upload_server(access_token, api_version, group_id):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {
        'access_token': access_token,
        'v': api_version,
        'group_id': group_id
    }

    upload_server = requests.get(url, params=params)
    return upload_server.json()['response']


def upload_photo_to_vk(access_token, api_version, upload_server_url, filename, group_id):
    params = {
        'access_token': access_token,
        'v': api_version,
        'group_id': -group_id
    }

    with open(filename, 'rb') as image:
        files = {
            'file1': image
        }

        uploaded_photo = requests.post(upload_server_url, params=params, files=files).json()
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

    saved_photo = requests.post(url, params)
    return saved_photo.json()['response'][0]
