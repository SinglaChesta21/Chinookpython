import sqlite3
from models.albums import Album
from models.repos.a_album import AAlbum

class AlbumRepo(AAlbum):
    def create_album(self, model: Album) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(
                    "INSERT INTO albums (Title, ArtistId) VALUES (?, ?)",
                    (model.title, model.artist_id),
                )
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def update_album(self, album_id: int, model: Album) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(
                    "UPDATE albums SET Title = ?, ArtistId = ? WHERE AlbumId = ?",
                    (model.title, model.artist_id, album_id),
                )
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def delete_album(self, album_id: int) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute("DELETE FROM albums WHERE AlbumId = ?", (album_id,))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def get_album(self, album_id: int) -> Album:
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute(
                    "SELECT AlbumId, Title, ArtistId FROM albums WHERE AlbumId = ?",
                    (album_id,),
                )
                row = cursor.fetchone()
                return Album(album_id=row[0], title=row[1], artist_id=row[2]) if row else None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def get_all_albums(self) -> list[Album]:
        albums = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT AlbumId, Title, ArtistId FROM albums")
                for row in cursor:
                    albums.append(Album(album_id=row[0], title=row[1], artist_id=row[2]))
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return albums
