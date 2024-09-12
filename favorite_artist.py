from config import FAVORITE_FILE
def load_favorite_artists():
        with open(FAVORITE_FILE, 'r') as file:
            return [line.strip() for line in file.readlines()]


# Function to save favorite artists to the file
def save_favorite_artists(favorite_artists):
    with open(FAVORITE_FILE, 'w') as file:
        for artist in favorite_artists:
            file.write(f"{artist}\n")

# Function to add a favorite artist
def add_favorite_artist(artist_name, favorite_artists):
    if artist_name not in favorite_artists:
        favorite_artists.append(artist_name)
        save_favorite_artists(favorite_artists)
        print(f"{artist_name} is toegevoegd aan je favoriete artiesten.")
    else:
        print(f"{artist_name} staat al in je favoriete artiesten.")
