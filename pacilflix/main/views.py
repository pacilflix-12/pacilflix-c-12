from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render

from utils.get_user import get_user

# Create your views here.


def show_trailer(request: HttpRequest) -> HttpResponse:

    return render(request, "trailer.html")


def show_tayangan(request: HttpRequest) -> HttpResponse:
    if get_user(request=request) == None:
        return redirect('/login/')

    return render(request, "tayangan.html")

def show_ulasan(request: HttpRequest) -> HttpResponse:

    return render(request, "ulasan.html")

def show_series(request: HttpRequest) -> HttpResponse:

    return render(request, "series.html")

def show_film(request: HttpRequest) -> HttpResponse:

    return render(request, "film.html")

def show_episode(request: HttpRequest) -> HttpResponse:

    return render(request, "episode.html")
def show_main(request: HttpRequest) -> HttpResponse:
    context = {
        'name': 'Kelompok',
        'class': 'Basdat F'
    }

    return render(request, "tayangan_dummy.html", context)
