from django.db import IntegrityError, InternalError
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

        pass_pengguna = select(
            f"SELECT password from pengguna WHERE username = '{username}'")[0][0]

        # jika password sesuai, berhasil login
        if password == pass_pengguna:
            response = redirect('/tayangan/')
            response.set_cookie('ticket', username)
            return response

    return render(request, 'login.html')



def register(request: HttpRequest) -> HttpResponse:
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        country = request.POST.get('country', None)
        
        try:
            insert(
                f"INSERT INTO PENGGUNA (username, password, negara_asal) VALUES ('{username}', '{password}', '{country}')")
            response = redirect('/tayangan/')
            # Set cookie for the ticket on login
            response.set_cookie('ticket', username)
            return response
        except IntegrityError as e:
            # Check if the exception is due to the custom trigger
            if 'username' in str(e).lower():
                error_message = 'Error: Username already exists'
            else:
                error_message = 'An unexpected error occurred'
        except InternalError as e:
            # Handle InternalError separately if necessary
            if 'username' in str(e).lower():
                error_message = 'Error: Username already exists'
            else:
                error_message = 'An unexpected error occurred'

    return render(request, 'register.html', {'error': error_message, 'islogin': request.user.is_authenticated})


def logout(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        response = redirect('/')
        response.delete_cookie('ticket')
        return response