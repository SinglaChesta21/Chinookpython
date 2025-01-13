class Artist:
    def __init__(self, artist_id: int, artist_name: int):
        self.artist_id = artist_id
        self.artist_name = artist_name

    def __repr__(self):
        return f"PlaylistTrack(artist_id={self.playlist_id}, artist_name={self.artist_name})"
