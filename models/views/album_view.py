from models.repos.album_repo import AlbumRepo

def view_all_albums():
    try:
        repo = AlbumRepo()
        albums = repo.get_all_albums()
        if not albums:
            print("No albums found.")
        else:
            print("Albums Table Data \n----------------")
            for album in albums:
                print(f"Album ID: {album.album_id}, Title: {album.title}, Artist ID: {album.artist_id}")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_album_by_id(album_id: int):
    try:
        repo = AlbumRepo()
        album = repo.get_album(album_id)
        if album:
            print(f"Album ID: {album.album_id}, Title: {album.title}, Artist ID: {album.artist_id}")
        else:
            print(f"No album found for Album ID {album_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. View all albums")
    print("2. View album by ID")
    choice = input("Enter your choice: ")

    if choice == "1":
        view_all_albums()
    elif choice == "2":
        try:
            album_id = int(input("Enter album ID: "))
            view_album_by_id(album_id)
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
    else:
        print("Invalid choice. Please choose 1 or 2.")
