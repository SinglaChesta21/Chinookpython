from models.genre import GenreType
from models.repos.a_genre import AGenreType
import sqlite3

class GenreRepo(AGenreType):
    def create_genre(self, genre: GenreType) -> None:
        pass

    def update_genre(self, gt_id: int, genre: GenreType) -> None:
        pass

    def delete_genre(self, gt_id: int) -> None:
        pass

    def get_genre(self, gt_id: int) -> GenreType:
        conn=sqlite3.connect("chinook.db")
        print ("Opened database successfully")
        data=conn.execute(f"select * from genres where ID={gt_id}")
        row=data.fetchone()
        if data:
            return GenreType(genre_id=[10], genre_name=[1])
        else:
            print(f"No genre found with Id {gt_id}")
        
        # except sqlite3.Error as e:
        #     print(f"Database error:{e}")
        #     return None
        

    def get_all_genres(self) -> list[GenreType]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM genres")
                for row in cursor:
                    g = GenreType(genre_id=row[0], genre_name=row[1])
                    data_list.append(g)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
