from config import API_KEY
from api_functions import *
from country_translate import *


def musicapp_menu():
    """
    Displays a menu for the music application and processes user inputs.
    """
    while True:
        print("\n##########################################")
        print("#          Het Muziekapp Menu            #")
        print("##########################################")
        print("# 1. Informatie genres opvragen artiest  #")
        print("# 2. Top 5 tracks opvragen artiest       #")
        print("# 3. Top 10 artiesten per land opvragen  #")
        print("# 4. Afsluiten                           #")
        print("##########################################\n")
        input_user = input("Voer een keuze in (1, 2, 3, 4, 5): ")

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
            country_input = input("Voer de naam van het land in: ")
            translated_country = translate_country_name(country_input)
            top_artists = get_top_artists_by_country(translated_country, API_KEY)
            if not top_artists:
                print(f"Geen gevonden top artiesten voor het land {country_input}.")
            else:
                print(f"Best beluisterde artiesten voor {country_input}:")
                for index, artist in enumerate(top_artists, start=1):
                    print(f"{index}. {artist}")

        elif input_user == "4":
            print("Het programma wordt afgesloten.")
            break

        else:
            print("Ongeldige keuze, probeer het opnieuw.")
