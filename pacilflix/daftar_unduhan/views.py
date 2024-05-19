from django.shortcuts import render


<<<<<<< Updated upstream
=======
def download_list(request: HttpRequest):
    user = get_user(request=request)
    if not user:
        return redirect('/register/')
>>>>>>> Stashed changes

downloads = [
    {'id': 1, 'title': 'Avengers', 'waktu_unduh' : '2024-04-11 23:46:22'},
    {'id': 2, 'title': 'Harry Potter', 'waktu_unduh' : '2024-01-31 10:35:04'}
]

<<<<<<< Updated upstream
def download_list(request):
    return render(request, 'daftar_unduhan.html', {'downloads': downloads})
=======
    return render(request=request, template_name='daftar_unduhan.html', context={**downloads, 'islogin': True})


def downloads_delete(request: HttpRequest, id_tayangan: str, datetime: str):
    user = get_user(request=request)
    if not user:
        return redirect('/register/')

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
        return redirect('/register/')

    if request.method == 'POST':
        context_add = add_downloads(id_tayangan=id_tayangan,
                                    username=user)

        return render(request=request, template_name='sukses_unduh.html', context={**context_add, "islogin": get_user(request=request) != None})

    return redirect('/daftar_unduhan')
>>>>>>> Stashed changes
