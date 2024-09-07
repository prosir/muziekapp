from config import api_key
from toptracks import get_top_tracks
from artistinfo import get_artist_info

def muziekapp_menu():
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
            info = get_artist_info(artist_input, api_key)
            if not info:
                print(f"Geen informatie beschikbaar voor {artist_input}.")
            else:
                print(f"Naam: {info['artist_name']}")
                print(f"Genres: {', '.join(info['artist_genres'])}")
        elif input_user == "2":
            artist_input = input("Voer de naam van de artiest in: ")
            top_tracks = get_top_tracks(artist_input, api_key)
            if not top_tracks:
                print(f"Geen top tracks beschikbaar voor {artist_input}.")
            else:
                print(f"Best beluisterde nummers voor {artist_input}:")
                for nummering, track in enumerate(top_tracks, start=1):
                    print(f"{nummering}. {track}")


        elif input_user == "3":
            print("Het programma wordt afgesloten.")
            break

        else:
            print("Ongeldige keuze, probeer het opnieuw.")

