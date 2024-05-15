from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from utils.get_user import get_user
from utils.query import insert, select

def auth(request: HttpRequest) -> HttpResponse:
    return render(request, 'auth.html')

def login(request: HttpRequest) -> HttpResponse:
    # jika sudah login, pergi ke halaman tayangan
    if get_user(request=request):
        return redirect('/tayangan/')
    
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        pass_pengguna = select(f"SELECT password from pengguna WHERE username = '{username}'")[0][0]
        
        # jika password sesuai, berhasil login
        if password == pass_pengguna:
            response = redirect('/tayangan/')
            response.set_cookie('ticket', username)
            return response

    return render(request, 'login.html')

def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        country = request.POST.get('country', None)

        insert(f"INSERT INTO PENGGUNA (username, password, negara_asal) VALUES ('{username}', '{password}', '{country}')")
        
        response = redirect('/tayangan/')
        # set cookie untuk ticket setiap login
        response.set_cookie('ticket', username)
        return response


    return render(request, 'register.html')

def logout(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        response = redirect('/login/')
        response.delete_cookie('ticket')
        return response