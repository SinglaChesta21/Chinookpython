from models.genre import Genre
from models.repos.a_genre import AGenre
import sqlite3

class GenreRepo(AGenre):
    def create_genre(self, model: Genre) -> None:
        try:
            conn = sqlite3.connect("chinook.db")
            conn.execute(f" INSERT INTO genres VALUES({model.genre_id}, '{model.genre_name}')")
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            conn.close()


    def update_genre(self, gt_id: int, model: Genre) -> None:
        try:
            conn = sqlite3.connect("chinook.db")
            conn.execute(f"UPDATE genres set Name='{model.genre_name}' where GenreId={gt_id}")
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            conn.close()


    def delete_genre(self, gt_id: int) -> None:
        conn = sqlite3.connect("chinook.db")
        conn.execute(f"delete from genres where GenreId={gt_id}")
        conn.commit()
        

    def get_genre(self, gt_id: int) -> Genre:
        try:
            conn = sqlite3.connect("chinook.db")
            cursor = conn.execute("SELECT * FROM genres WHERE GenreId = ?", (gt_id,))
            row = cursor.fetchone()
            if row:
                return Genre(genre_id=row[0], genre_name=row[1])
            else:
                print(f"No genre found with ID {gt_id}")
                return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            conn.close()
        

    def get_all_genres(self) -> list[Genre]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM genres")
                for row in cursor:
                    g = Genre(genre_id=row[0], genre_name=row[1])
                    data_list.append(g)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
