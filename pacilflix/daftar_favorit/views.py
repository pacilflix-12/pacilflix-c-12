from datetime import datetime
from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect, render

from daftar_favorit.services import create_subfavorite, delete_favorite, delete_subfavorite, get_all_subfavorites, get_all_user_favorites
from utils.get_user import get_user


def favorite_list(request: HttpRequest) -> HttpResponse:
    user = get_user(request=request)
    if not user:
        return redirect('/login/')

    favorites = get_all_user_favorites(username=user)

    return render(request=request, template_name='daftar_favorit.html', context=favorites)


def sub_favorite_list(request: HttpRequest, timestamp: str):
    user = get_user(request=request)
    if not user:
        return redirect('/login/')

    new_timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")

    if request.method == 'POST':
        delete_favorite(username=user, timestamp=new_timestamp)
        return redirect('/daftar_favorit')

    sub_favorites = get_all_subfavorites(
        username=user, timestamp=new_timestamp)

    return render(request=request, template_name='daftar_subfavorit.html', context=sub_favorites)


def delete_sub_favorite(request: HttpRequest, timestamp: str, id_tayangan: str):
    user = get_user(request=request)
    if not user:
        return redirect('/login/')

    new_timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")

    if request.method == 'POST':
        delete_subfavorite(
            username=user, timestamp=new_timestamp, id_tayangan=id_tayangan)

    return redirect(f"/daftar_favorit/{timestamp}")


def modal_favorite(request: HttpRequest, id_tayangan: str) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    user = get_user(request=request)
    if not user:
        return redirect('/login/')

    if request.method == 'POST':
        favorite_list = request.POST.get('favorite_list')
        if favorite_list:
            new_timestamp = datetime.strptime(
                favorite_list, "%Y-%m-%dT%H:%M:%S")

            try:
                create_subfavorite(
                    username=user, timestamp=new_timestamp, id_tayangan=id_tayangan)
            except:
                pass

            return redirect(f'/daftar_favorit/{new_timestamp.isoformat()}')
        else:
            return redirect(f'/daftar_favorit')
    else:
        favorite_lists = get_all_user_favorites(username=user)

        return render(request=request, template_name='pilih_folder_favorit.html', context=favorite_lists)
