from models.artists import Artist
from models.repos.a_artist import AArtist
import sqlite3

class ArtistRepo(AArtist):
    def create_artist(self, model: Artist) -> None:
        pass

    def update_artist(self, a_id: int, model: Artist) -> None:
        pass

    def delete_artist(self, a_id: int) -> None:
        pass

    def get_artist(self, a_id: int) -> list:
        try:
            with sqlite3.connect("chinook.db") as conn:
                data = conn.execute("SELECT * FROM artists WHERE ArtistId = ?", (a_id,))
                rows = data.fetchall()  # Fetch all rows matching the PlaylistId

                if rows:
                    # Create a list of PlaylistTrack objects for all matching rows
                    return [Artist(artist_id=row[0], artist_name=row[1]) for row in rows]
                else:
                    print(f"No tracks found for PlaylistId {a_id}")
                    return []
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []


    def get_all_artists(self) -> list[Artist]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM artists")
                for row in cursor:
                    plt = Artist(artist_id=row[0], artist_name=row[1])
                    data_list.append(plt)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
