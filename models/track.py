class Track:
    def __init__(self, track_id: int,track_name: str,  album_id: int, media_type_id: int, genre_id: int,composer: str, millisecond: int, bytes: int, unit_price: int):
        self.track_id = track_id
        self.track_name = track_name
        self.album_id = album_id
        self.media_type_id = media_type_id
        self.genre_id = genre_id
        self.composer = composer
        self.millisecond = millisecond
        self.bytes = bytes
        self.unit_price = unit_price


    def __repr__(self):
        return f"PlaylistTrack(track_id={self.track_id}, track_name={self.track_name}, album_id={self.album_id}, media_type_id={self.media_type_id}, genre_id={self.genre_id}, composer={self.composer}, millisecond={self.millisecond}, bytes={self.bytes}, unit_price={self.unit_price} )"
