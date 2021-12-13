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
