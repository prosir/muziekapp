import requests
from config import *


def get_top_tracks(artist_name, api_key):
    params = {
        'method': 'artist.getTopTracks',
        'artist': artist_name,
        'api_key': api_key,
        'format': 'json',
        'limit': 5
    }
    response = requests.get(api_link, params=params)
    data = response.json()

    if 'toptracks' in data:
        top_tracks = data['toptracks']['track']
        return [track['name'] for track in top_tracks]
    else:
        return None