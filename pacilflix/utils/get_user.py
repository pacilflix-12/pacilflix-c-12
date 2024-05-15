from django.http import HttpRequest


def get_user(request: HttpRequest):
    return request.COOKIES.get('ticket')