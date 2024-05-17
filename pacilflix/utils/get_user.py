from django.http import HttpRequest


def get_user(request: HttpRequest) -> str | None:
    return request.COOKIES.get('ticket')
