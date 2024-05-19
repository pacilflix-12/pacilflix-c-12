from datetime import datetime
from typing import Any, Literal
from utils.query import insert, select


def get_searched_film(keyword: str):
    return select(f"SELECT * FROM tayangan WHERE LOWER(judul) LIKE LOWER('%{keyword}%') ORDER BY judul")


def get_total_duration(id_tayangan: str) -> int:
    if get_tayangan_type(id_tayangan) == 'film':
        return select(f"select durasi_film from film where id_tayangan = '{id_tayangan}'")[0][0]
    else:
        total_duration = 0
        episodes = select(
            f"select * from episode where id_series = '{id_tayangan}'")

        for episode in episodes:
            total_duration += episode[3]

        return total_duration


def count_total_views(riwayat_nonton_list: list[tuple[Any, ...]]) -> int:
    total_views = 0
    for riwayat_nonton in riwayat_nonton_list:
        id_tayangan = riwayat_nonton[0]
        start_date_time = riwayat_nonton[2]
        end_date_time = riwayat_nonton[3]

        watch_time_in_minutes = (end_date_time -
                                 start_date_time).total_seconds() / 60
        total_duration = get_total_duration(id_tayangan=id_tayangan)

        if total_duration == 0:
            return 0

        watch_time_percentage = (
            watch_time_in_minutes / total_duration) * 100
        if watch_time_percentage >= 70:
            total_views += 1

    return total_views


def get_total_views_last_week(id_tayangan: str) -> int:
    riwayat_nonton_list = select(
        f"SELECT * FROM riwayat_nonton WHERE id_tayangan = '{id_tayangan}' AND end_date_time >= NOW() - INTERVAL '7 days'")

    return count_total_views(riwayat_nonton_list=riwayat_nonton_list)


def merge_sort(shows: list[tuple[Any]]) -> list[tuple[Any]]:
    if len(shows) <= 1:
        return shows

    mid = len(shows) // 2
    left_half = shows[:mid]
    right_half = shows[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left: list[tuple[Any]], right: list[tuple[Any]]) -> list[tuple[Any]]:
    merged: list[tuple[Any]] = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if get_total_views_last_week(left[left_idx][0]) > get_total_views_last_week(right[right_idx][0]):
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged


def get_top_10_from_tayangan_array(shows: list[tuple[Any]]) -> list[tuple[Any]]:
    sorted_shows = merge_sort(shows=shows)
    if len(sorted_shows) >= 10:
        return sorted_shows[:10]
    else:
        return sorted_shows[:len(sorted_shows)]


def get_tayangan_type(id_tayangan: str) -> Literal['film', 'series']:
    records = select(f"select * from film where id_tayangan = '{id_tayangan}'")
    if len(records) == 0:
        return 'series'
    else:
        return 'film'


def get_top_10_global():
    all_tayangan = select(f"select * from tayangan")
    return get_top_10_from_tayangan_array(all_tayangan)


def get_top_10_lokal(country: str):
    all_tayangan_lokal = select(
        f"select * from tayangan where asal_negara = '{country}'")
    return get_top_10_from_tayangan_array(all_tayangan_lokal)


def get_user_country(username: str):
    return select(f"select negara_asal from pengguna where username = '{username}'")[0][0]


def get_all_films():
    return select(f"select id, judul, sinopsis_trailer, url_video_trailer, release_date_trailer from film, tayangan where id_tayangan = id")


def get_all_series():
    return select(f"select id, judul, sinopsis_trailer, url_video_trailer, release_date_trailer from series, tayangan where id_tayangan = id")


def get_reviews(id_tayangan: str):
    return select(f"select * from ulasan u where id_tayangan = '{id_tayangan}'")


def get_players(id_tayangan: str):
    return select(
        f"select nama from memainkan_tayangan m, contributors c where m.id_pemain = c.id and id_tayangan = '{id_tayangan}'")


def get_writers(id_tayangan: str):
    return select(
        f"select nama from MENULIS_SKENARIO_TAYANGAN m, contributors c where m.id_pemain = c.id and id_tayangan = '{id_tayangan}'")


def get_series_detail(id_tayangan: str):
    series = select(
        f"select id_tayangan, judul, sinopsis, asal_negara, sinopsis_trailer, url_video_trailer, release_date_trailer, id_sutradara from series, tayangan where id_tayangan = id and id_tayangan = '{id_tayangan}'")[0]

    episodes = select(
        f"select * from episode where id_series = '{id_tayangan}'")
    sutradara = select(
        f"select nama from contributors where id = '{series[7]}'")[0]
    genres = select(
        f"select genre from genre_tayangan where id_tayangan = '{id_tayangan}'")
    players = get_players(id_tayangan=id_tayangan)
    writers = get_writers(id_tayangan=id_tayangan)
    reviews = get_reviews(id_tayangan=id_tayangan)

    return {
        "id_tayangan": series[0],
        "judul": series[1],
        "sinopsis": series[2],
        "asal_negara": series[3],
        "sinopsis_trailer": series[4],
        "url_video_trailer": series[5],
        "release_date_trailer": series[6],
        "total_views": 0,
        "rating_avg": 2.0,
        "episodes": [
            {
                "id_series": episode[0],
                "sub_judul": episode[1],
            } for episode in episodes
        ],
        "sutradara": {
            "nama": sutradara[0],
        },
        "genres": [
            {
                "nama": genre[0]
            } for genre in genres
        ],
        "players": [
            {
                "nama": player[0],
            } for player in players
        ],
        "writers": [
            {
                "nama": writer[0],
            } for writer in writers
        ],
        "reviews": [
            {
                "username": review[1],
                "timestamp": review[2],
                "rating": review[3],
                "deskripsi": review[4]
            } for review in reviews
        ]
    }


def get_film_detail(id_tayangan: str):
    film = select(
        f"select id_tayangan, url_video_film, release_date_film, durasi_film, judul, sinopsis, asal_negara, sinopsis_trailer, url_video_trailer, release_date_trailer, id_sutradara from film, tayangan where id_tayangan = id and id_tayangan = '{id_tayangan}'")[0]

    sutradara = select(
        f"select nama from contributors where id = '{film[10]}'")[0]
    genres = select(
        f"select genre from genre_tayangan where id_tayangan = '{id_tayangan}'")
    players = get_players(id_tayangan=id_tayangan)
    writers = get_writers(id_tayangan=id_tayangan)
    reviews = get_reviews(id_tayangan=id_tayangan)

    return {
        "id_tayangan": film[0],
        "url_video_film": film[1],
        "release_date_film": film[2],
        "durasi_film": film[3],
        "judul": film[4],
        "sinopsis": film[5],
        "asal_negara": film[6],
        "sinopsis_trailer": film[7],
        "url_video_trailer": film[8],
        "release_date_trailer": film[9],
        "total_views": 1,
        "rating_avg": 1.5,
        "sutradara": {
            "nama": sutradara[0],
        },
        "genres": [
            {
                "nama": genre[0]
            } for genre in genres
        ],
        "players": [
            {
                "nama": player[0],
            } for player in players
        ],
        "writers": [
            {
                "nama": writer[0],
            } for writer in writers
        ],
        "reviews": [
            {
                "username": review[1],
                "timestamp": review[2],
                "rating": review[3],
                "deskripsi": review[4]
            } for review in reviews
        ]
    }


def get_episode_detail(id_tayangan: str, sub_judul: str):
    episode = select(
        f"select * from episode where id_series = '{id_tayangan}' and sub_judul = '{sub_judul}'")[0]
    judul = select(
        f"select judul from tayangan where id = '{id_tayangan}'")[0][0]
    another_episodes = select(
        f"select sub_judul from episode where id_series = '{id_tayangan}'")

    return {
        "episode": {
            "id_series": episode[0],
            "sub_judul": episode[1],
            "sinopsis": episode[2],
            "durasi": episode[3],
            "url_video": episode[4],
            "release_date": episode[5],
            "judul": judul
        },
        "another_episodes": [
            {
                "id_series": episode[0],
                "sub_judul": i[0],
            } for i in another_episodes
        ]
    }


def create_ulasan(id_tayangan: str, username: str, timestamp: datetime, rating: int, deskripsi: str):
    insert(
        f"insert into ulasan values ('{id_tayangan}', '{username}', '{timestamp}', {rating}, '{deskripsi}')")
