from datetime import datetime, timedelta
from utils.query import delete, insert, select


def get_all_user_downloads(username: str):
    downloads = select(
        f"select id_tayangan, username, timestamp, judul from tayangan_terunduh t, tayangan ta where username = '{username}' and id_tayangan = id")

    return {
        "downloads": [
            {
                "id_tayangan": download[0],
                "username": download[1],
                "timestamp_iso": download[2].isoformat(),
                "timestamp": download[2],
                "judul": download[3]
            } for download in downloads
        ]
    }


def add_downloads(id_tayangan: str, username: str):
    new_datetime = datetime.now()
    insert(
        f"insert into tayangan_terunduh values ('{id_tayangan}', '{username}', '{new_datetime}')")

    judul = select(
        f"select judul from tayangan where id = '{id_tayangan}'")[0][0]

    return {
        "judul_tayangan": judul,
        "expiry_date": (new_datetime + timedelta(days=7)),
    }


def delete_downloads(id_tayangan: str, username: str, datetime: str):
    delete(
        f"delete from tayangan_terunduh where id_tayangan = '{id_tayangan}' and username = '{username}' and timestamp = '{datetime}'")
