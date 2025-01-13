from abc import ABC, abstractmethod
from models.artists import Artist

class AArtist(ABC):
    @abstractmethod
    def create_artist(self, model: Artist) -> None:
        pass

    @abstractmethod
    def update_artist(self, pl_t_id: int, model: Artist) -> None:
        pass

    @abstractmethod
    def delete_artist(self, pl_t_id: int) -> None:
        pass

    @abstractmethod
    def get_artist(self, pl_t_id: int) -> Artist:
        pass

    @abstractmethod
    def get_all_artists(self) -> list[Artist]:
        pass