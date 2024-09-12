import requests
from config import api_link
def get_artist_info(artist_name, api_key):
    params = {
        'method': 'artist.getInfo',
        'artist': artist_name,
        'api_key': api_key,
        'format': 'json'
    }

    response = requests.get(api_link, params=params)
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: Status code {response.status_code}")

    if 'artist' in data:
        artist_info = data['artist']
        artist_details = {
            'artist_name': artist_info['name'],
            'artist_genres': [tag['name'] for tag in artist_info['tags']['tag']]
        }
        return artist_details
