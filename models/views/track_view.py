from models.repos.track_repo import TrackRepo

def view_track():
    try:
        tr = TrackRepo()
        tracks = tr.get_all_tracks()
        if not tracks:
            print("No tracks found.")
        else:
            print("Track Table Data \n----------------")
            for track in tracks:
                print(
                    f"Track ID: {track.track_id}, Track Name: {track.track_name}, Album ID: {track.album_id}, "
                    f"Media Type ID: {track.media_type_id}, Genre ID: {track.genre_id}, Composer: {track.composer}, "
                    f"Milliseconds: {track.millisecond}, Bytes: {track.bytes}, Unit Price: {track.unit_price}"
                )
    except Exception as e:
        print(f"An error occurred: {e}")

def view_track_by_id(track_id: int):
    try:
        tr = TrackRepo()
        tracks = tr.get_track(track_id)

        if tracks:
            print(f"Details for Track ID {track_id}:")
            for track in tracks:
                print(
                    f"Track ID: {track.track_id}, Track Name: {track.track_name}, Album ID: {track.album_id}, "
                    f"Media Type ID: {track.media_type_id}, Genre ID: {track.genre_id}, Composer: {track.composer}, "
                    f"Milliseconds: {track.millisecond}, Bytes: {track.bytes}, Unit Price: {track.unit_price}"
                )
        else:
            print(f"No tracks found for Track ID {track_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. View all tracks")
    print("2. View track by ID")
    choice = input("Enter your choice: ")

    if choice == "1":
        view_track()
    elif choice == "2":
        try:
            track_id = int(input("Enter track ID: "))
            view_track_by_id(track_id)
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
    else:
        print("Invalid choice. Please choose 1 or 2.")
