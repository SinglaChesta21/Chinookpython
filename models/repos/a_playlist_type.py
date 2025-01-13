from abc import ABC, abstractmethod
from models.playlists import PlaylistType

class APlaylistType(ABC):
    @abstractmethod
    def create_playlist_type(self, model: PlaylistType) -> None:
        pass

    @abstractmethod
    def update_playlist_type(self, pt_id: int, model: PlaylistType) -> None:
        pass

    @abstractmethod
    def delete_playlist_type(self, pt_id: int) -> None:
        pass

    @abstractmethod
    def get_playlist_type(self, pt_id: int) -> PlaylistType:
        pass

    @abstractmethod
    def get_all_playlist_types(self) -> list[PlaylistType]:
        pass
