import requests
import json


def get_wall_upload_server(access_token, api_version, group_id):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {
        'access_token': access_token,
        'v': api_version,
        'group_id': group_id
    }

    upload_server = requests.get(url, params=params)
    return upload_server.json()['response']


def upload_photo_to_vk(access_token, api_version, upload_server_url, filename, group_id=None):
    params = {
        'access_token': access_token,
        'v': api_version,
        'group_id': group_id
    }

    with open(filename, 'rb') as image:
        files = {
            'file1': image
        }

        uploaded_photo = requests.post(upload_server_url, params=params, files=files).json()
        uploaded_photo['photo'] = json.loads(uploaded_photo['photo'])
        return uploaded_photo
