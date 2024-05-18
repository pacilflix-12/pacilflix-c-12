from django.http import HttpRequest

from utils.query import select


def get_user(request: HttpRequest) -> str | None:
    user = select(
        f"select * from pengguna where username = '{request.COOKIES.get('ticket')}'")
    if len(user) == 0:
        return None

    return request.COOKIES.get('ticket')
