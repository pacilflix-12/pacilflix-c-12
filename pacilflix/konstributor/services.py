from typing import Any, Literal
from utils.query import select

def get_gender(gender_code: int) -> str:
    return "perempuan" if gender_code == 1 else "laki-laki"

def get_all_contributors() -> list[tuple[Any]]:
    contributors = select("SELECT nama, jenis_kelamin, kewarganegaraan FROM contributors")
    return [(nama, get_gender(jenis_kelamin), kewarganegaraan) for nama, jenis_kelamin, kewarganegaraan in contributors]

def get_contributor_type(id_contributor: str) -> list[str]:
    types = []
    if select(f"SELECT * FROM pemain WHERE id = '{id_contributor}'"):
        types.append('pemain')
    if select(f"SELECT * FROM sutradara WHERE id = '{id_contributor}'"):
        types.append('sutradara')
    if select(f"SELECT * FROM penulis_skenario WHERE id = '{id_contributor}'"):
        types.append('penulis_skenario')
    return types

def get_contributor_detail(id_contributor: str) -> dict:
    contributor = select(f"SELECT id, nama, jenis_kelamin, kewarganegaraan FROM contributors WHERE id = '{id_contributor}'")[0]
    types = get_contributor_type(id_contributor)
    return {
        "id": contributor[0],
        "nama": contributor[1],
        "jenis_kelamin": get_gender(contributor[2]),
        "kewarganegaraan": contributor[3],
        "tipe": types
    }

def get_all_contributors_with_details() -> list[dict]:
    contributors = get_all_contributors()
    contributors_with_details = []
    for contributor in contributors:
        id_contributor = contributor[0]
        detail = get_contributor_detail(id_contributor)
        contributors_with_details.append(detail)
    return contributors_with_details
