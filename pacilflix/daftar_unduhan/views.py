from django.http import HttpRequest
from django.shortcuts import redirect, render
from daftar_unduhan.services import add_downloads, delete_downloads, get_all_user_downloads
from utils.get_user import get_user


def download_list(request: HttpRequest):
    user = get_user(request=request)
    if not user:
        return redirect('/login/')

    downloads = get_all_user_downloads(username=user)
    print(downloads)

    return render(request=request, template_name='daftar_unduhan.html', context={**downloads,"islogin": get_user(request=request) != None})


def downloads_delete(request: HttpRequest, id_tayangan: str, datetime: str):
    user = get_user(request=request)
    if not user:
        return redirect('/login/')

    if request.method == 'POST':
        try:
            delete_downloads(id_tayangan=id_tayangan,
                             username=user, datetime=datetime)
        except:
            return render(request=request, template_name='gagal_unduh.html', context={"islogin": get_user(request=request) != None})

    return redirect('/daftar_unduhan')


def downloads_add(request: HttpRequest, id_tayangan: str):
    user = get_user(request=request)
    if not user:
        return redirect('/login/')

    if request.method == 'POST':
        context_add = add_downloads(id_tayangan=id_tayangan,
                                    username=user)

        return render(request=request, template_name='sukses_unduh.html', context={**context_add, "islogin": get_user(request=request) != None})

    return redirect('/daftar_unduhan')
