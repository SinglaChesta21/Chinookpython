class PlaylistTrack:
    def __init__(self, playlist_id: int, track_id: int):
        self.playlist_id = playlist_id
        self.track_id = track_id

    def __repr__(self):
        return f"PlaylistTrack(playlist_id={self.playlist_id}, track_id={self.track_id})"
