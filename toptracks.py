import requests
from config import api_link

def get_top_tracks(artist_name, api_key):
    params = {
        'method': 'artist.getTopTracks',
        'artist': artist_name,
        'api_key': api_key,
        'format': 'json',
        'limit': 5
    }
    response = requests.get(api_link, params=params)
    if response.status_code == 200:
        data = response.json()  # Fetch the JSON data if the request was successful
    else:
        print(f"Error: Status code {response.status_code}")

    if 'toptracks' in data:
        top_tracks = data['toptracks']['track']
        return [track['name'] for track in top_tracks]
    else:
        return None