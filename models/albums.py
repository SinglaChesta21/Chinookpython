class Album:
    def __init__(self, album_id: int, title: str, artist_id: int):
        self.album_id = album_id
        self.title = title
        self.artist_id = artist_id

    def __repr__(self):
        return f"Album(album_id={self.album_id}, title='{self.title}', artist_id={self.artist_id})"
