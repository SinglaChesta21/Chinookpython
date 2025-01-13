from models.repos.artist_repo import ArtistRepo

def view_all_artists():
    try:
        ar = ArtistRepo()
        artists = ar.get_all_artists()
        if not artists:
            print("No artists found.")
        else:
            print("Artists Table Data \n----------------")
            for artist in artists:
                print(f"Artist ID: {artist.artist_id}, Artist Name: {artist.artist_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_artist_by_id(a_id: int):
    try:
        ar = ArtistRepo()
        artists = ar.get_artist(a_id)

        if artists:
            print(f"Details for Artist ID {a_id}:")
            for artist in artists:
                print(f"Artist ID: {artist.artist_id}, Artist Name: {artist.artist_name}")
        else:
            print(f"No artist found for Artist ID {a_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. View all artists")
    print("2. View artist by ID")
    choice = input("Enter your choice: ")

    if choice == "1":
        view_all_artists()
    elif choice == "2":
        try:
            artist_id = int(input("Enter artist ID: "))
            view_artist_by_id(artist_id)
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
    else:
        print("Invalid choice. Please choose 1 or 2.")
