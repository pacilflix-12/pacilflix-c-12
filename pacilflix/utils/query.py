from django.db import connection
from typing import Any

# create, update, delete
def _cud(query: str) -> None:
    with connection.cursor() as cursor:
        cursor.execute(sql=query)

# read
def _r(query: str) -> list[tuple[Any, ...]]:
    with connection.cursor() as cursor:
        cursor.execute(sql=query)
        rows: list[tuple[Any, ...]] = cursor.fetchall()
        return rows

# this could possibly throws error, so wrap this method with try catch
def select(query: str) -> list[tuple[Any, ...]]:
    return _r(query=query)

def insert(query: str) -> None:
    _cud(query=query)

def update(query: str) -> None:
    _cud(query=query)

def delete(query: str) -> None:
    _cud(query=query)