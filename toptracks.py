import requests
from config import *

def get_top_tracks(artist_name, API_KEY):
    params = {
        'method': 'artist.getTopTracks',
        'artist': artist_name,
        'api_key': API_KEY,
        'format': 'json',
        'limit': 5
    }
    response = requests.get(API_URI, params=params)
    if response.status_code == 200:
        data = response.json()

    if 'toptracks' in data:
        top_tracks = data['toptracks']['track']
        return [track['name'] for track in top_tracks]
