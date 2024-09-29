import requests
from config import API_URI, API_KEY


def get_top_tracks(artist_name, API_KEY):
    """Fetches the top tracks for a given artist from the Last.fm API."""
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


def get_artist_info(artist_name, API_KEY):
    """Fetches detailed information for a given artist from the Last.fm API."""
    params = {
        'method': 'artist.getInfo',
        'artist': artist_name,
        'api_key': API_KEY,
        'format': 'json'
    }

    response = requests.get(API_URI, params=params)
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

def get_top_artists_by_country(country, API_KEY):
    """Fetches the top 10 artists for a given country from the Last.fm API."""
    params = {
        'method': 'geo.getTopArtists',
        'country': country,
        'api_key': API_KEY,
        'format': 'json',
        'limit': 10
    }
    response = requests.get(API_URI, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'topartists' in data:
            top_artists = data['topartists']['artist']
            return [artist['name'] for artist in top_artists]

