from models.playlists import PlaylistType
from models.repos.a_playlist_type import APlaylistType
import sqlite3

class PlaylistTypeRepo(APlaylistType):
    def create_playlist_type(self, model: APlaylistType) -> None:
        pass

    def update_playlist_type(self, pt_id: int, model: APlaylistType) -> None:
        pass

    def delete_playlist_type(self, pt_id: int) -> None:
        try:
            conn = sqlite3.connect('chinook.db')
            c = conn.cursor()

            # Check if the record exists before attempting to delete
            c.execute("SELECT * FROM playlists WHERE PlaylistId = ?", (pt_id,))
            result = c.fetchone()

            if result:
                c.execute("DELETE FROM playlists WHERE PlaylistId = ?", (pt_id,))
                conn.commit()
                print(f"Playlist type with ID {pt_id} deleted successfully.")
            else:
                print(f"No playlist type found with ID {pt_id}.")

            conn.close()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def get_playlist_type(self, pt_id: int) -> APlaylistType:
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM playlists WHERE PlaylistId = ?", (pt_id,))
                row = cursor.fetchone()
                if row:
                    return PlaylistType(playlist_id=row[0], playlist_name=row[1])
                else:
                    print(f"No playlist type found with ID {pt_id}")
                    return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def get_all_playlist_types(self) -> list[PlaylistType]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM playlists")
                for row in cursor:
                    pt = PlaylistType(playlist_id=row[0], playlist_name=row[1])
                    data_list.append(pt)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
    
