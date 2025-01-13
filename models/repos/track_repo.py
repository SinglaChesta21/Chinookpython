from models.track import Track
from models.repos.a_track import ATrack
import sqlite3

class TrackRepo(ATrack):
    def create_track(self, model: Track) -> None:
        pass

    def update_track(self, t_id: int, model: Track) -> None:
        pass

    def delete_track(self, t_id: int) -> None:
        pass

    def get_track(self, t_id: int) -> list:
        try:
            with sqlite3.connect("chinook.db") as conn:
                data = conn.execute("SELECT * FROM tracks WHERE TrackId = ?", (t_id,))
                rows = data.fetchall()  # Fetch all rows matching the TrackId

                if rows:
                    # Create a list of Track objects for all matching rows
                    return [
                        Track(
                            track_id=row[0],
                            track_name=row[1],
                            album_id=row[2],
                            media_type_id=row[3],
                            genre_id=row[4],
                            composer=row[5],
                            millisecond=row[6],
                            bytes=row[7],
                            unit_price=row[8],
                        )
                        for row in rows
                    ]
                else:
                    print(f"No tracks found for TrackId {t_id}")
                    return []
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def get_all_tracks(self) -> list[Track]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM tracks")
                for row in cursor:
                    track = Track(
                        track_id=row[0],
                        track_name=row[1],
                        album_id=row[2],
                        media_type_id=row[3],
                        genre_id=row[4],
                        composer=row[5],
                        millisecond=row[6],
                        bytes=row[7],
                        unit_price=row[8],
                    )
                    data_list.append(track)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
