from config import API_KEY
from toptracks import get_top_tracks
from artistinfo import get_artist_info
from favorite_artist import load_favorite_artists, add_favorite_artist


def muziekapp_menu():
    favorite_artists = load_favorite_artists()
    while True:
        print("\n##########################################")
        print("#          Het Muziekapp Menu            #")
        print("##########################################")
        print("# 1. Informatie genres opvragen artiest  #")
        print("# 2. Top 5 tracks opvragen artiest       #")
        print("# 3. Afsluiten                           #")
        print("##########################################\n")
    input_user = input("Voer een keuze in (1, 2, 3): ")

      if input_user == "1":
            artist_input = input("Voer de naam van de artiest in: ")
            info = get_artist_info(artist_input, API_KEY)
            if not info:
                print(f"Geen informatie beschikbaar voor {artist_input}.")
            else:
                print(f"Naam: {info['artist_name']}")
                print(f"Genres: {', '.join(info['artist_genres'])}")
        elif input_user == "2":
            artist_input = input("Voer de naam van de artiest in: ")
            top_tracks = get_top_tracks(artist_input, API_KEY)
            if not top_tracks:
                print(f"Geen top tracks beschikbaar voor {artist_input}.")
            else:
                print(f"Best beluisterde nummers voor {artist_input}:")
                for index, track in enumerate(top_tracks, start=1):
                    print(f"{index}. {track}")
        elif input_user == "3":
            print("Het programma wordt afgesloten.")
            break

        else:
            print("Ongeldige keuze, probeer het opnieuw.")

