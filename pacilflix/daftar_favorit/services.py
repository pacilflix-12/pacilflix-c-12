from datetime import datetime
from utils.query import delete, insert, select


def get_all_user_favorites(username: str):
    favorites = select(
        f"select * from daftar_favorit where username = '{username}'")

    return {
        "favorites": [
            {
                "timestamp": favorite[0],
                "timestamp_iso": favorite[0].isoformat(),
                "username": favorite[1],
                "judul": favorite[2],
            } for favorite in favorites
        ]
    }


def get_all_subfavorites(username: str, timestamp: datetime):
    subfavorites = select(
        f"select id_tayangan, timestamp, judul from TAYANGAN_MEMILIKI_DAFTAR_FAVORIT, tayangan where id_tayangan = id and username = '{username}' and timestamp = '{timestamp}'")

    judul_favorit = select(
        f"select judul from daftar_favorit where username = '{username}' and timestamp = '{timestamp}'")[0][0]

    # print(subfavorites)

    return {
        "judul": judul_favorit,
        "subfavorites": [
            {
                "id": subfavorite[0],
                "timestamp": subfavorite[1],
                "timestamp_iso": subfavorite[1].isoformat(),
                "judul": subfavorite[2],
            } for subfavorite in subfavorites
        ]
    }


def delete_favorite(username: str, timestamp: datetime):
    delete(
        f"delete from TAYANGAN_MEMILIKI_DAFTAR_FAVORIT where username = '{username}' and timestamp = '{timestamp}'")

    delete(
        f"delete from daftar_favorit where username = '{username}' and timestamp = '{timestamp}'")


def delete_subfavorite(username: str, timestamp: datetime, id_tayangan: str):
    delete(
        f"delete from TAYANGAN_MEMILIKI_DAFTAR_FAVORIT where username = '{username}' and timestamp = '{timestamp}' and id_tayangan = '{id_tayangan}'")


def create_subfavorite(username: str, timestamp: datetime, id_tayangan: str):
    insert(
        f"insert into TAYANGAN_MEMILIKI_DAFTAR_FAVORIT values ('{id_tayangan}', '{timestamp}', '{username}')")
