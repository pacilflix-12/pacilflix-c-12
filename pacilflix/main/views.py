from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render

from main.services import get_all_films, get_all_series, get_film_detail, get_searched_film, get_series_detail, get_tayangan_type, get_top_10_global, get_top_10_lokal, get_user_country
from utils.get_user import get_user

# Create your views here.


def show_trailer(request: HttpRequest) -> HttpResponse:
    if get_user(request=request):  # kalau udah login pergi ke halaman tayangan
        return redirect('/tayangan/')

    top_10_tayangan = get_top_10_global()
    films = get_all_films()
    series_list = get_all_series()

    context = {
        "top_10": top_10_tayangan,
        "films": films,
        "series_list": series_list,
        "islogin": False
    }

    return render(request, "trailer.html", context=context)


def show_search(request: HttpRequest, search: str) -> HttpResponse:
    tayangan_list = get_searched_film(keyword=search)

    context = {
        "searched_tayangan": tayangan_list
    }

    return render(request, 'search_tayangan.html', context=context)


def show_tayangan(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        search = request.POST.get('search')
        if search:
            return show_search(request=request, search=search)

    username = get_user(request=request)
    if username == None:  # kalau belum login pergi ke trailer
        return redirect('/trailer/')

    is_lokal = request.GET.get('lokal')
    user_country = get_user_country(username=username)

    top_10_tayangan = get_top_10_lokal(
        user_country) if is_lokal == 'true' else get_top_10_global()
    films = get_all_films()
    series_list = get_all_series()

    context = {
        "top_10": top_10_tayangan,
        "films": films,
        "series_list": series_list,
        "islogin": True
    }

    return render(request, "tayangan.html", context=context)


def show_ulasan(request: HttpRequest) -> HttpResponse:

    return render(request, "ulasan.html")


def show_series(request: HttpRequest, id_tayangan: str) -> HttpResponse:
    series_detail = get_series_detail(id_tayangan=id_tayangan)

    return render(request, "series.html", context=series_detail)


def show_film(request: HttpRequest, id_tayangan: str) -> HttpResponse:
    film_detail = get_film_detail(id_tayangan=id_tayangan)

    return render(request, "film.html", context=film_detail)


def show_detail_tayangan(request: HttpRequest, id_tayangan: str) -> HttpResponse:
    username = get_user(request=request)
    if username == None:  # kalau belum login pergi ke trailer
        return redirect('/trailer/')

    if get_tayangan_type(id_tayangan=id_tayangan) == 'film':
        return show_film(request=request, id_tayangan=id_tayangan)
    else:
        return show_series(request=request, id_tayangan=id_tayangan)


def show_episode(request: HttpRequest) -> HttpResponse:

    return render(request, "episode.html")


def show_main(request: HttpRequest) -> HttpResponse:
    context = {
        'name': 'Kelompok',
        'class': 'Basdat F'
    }

    return render(request, "tayangan_dummy.html", context)
