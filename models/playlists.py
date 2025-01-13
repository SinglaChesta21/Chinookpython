class PlaylistType:
    def __init__(self, playlist_id: int, playlist_name: str):
        self.playlist_id = playlist_id
        self.playlist_name = playlist_name
    def __repr__(self):
        return f"PlaylistType(id={self.playlist_id}, name={self.playlist_name})"