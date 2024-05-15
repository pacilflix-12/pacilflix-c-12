from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def auth(request: HttpRequest) -> HttpResponse:
    return render(request, 'auth.html')

def login(request: HttpRequest) -> HttpResponse:
    return render(request, 'login.html')

def register(request: HttpRequest) -> HttpResponse:
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        negara_asal = request.POST.get('country', None)
        print(username, password, negara_asal)

    return render(request, 'register.html')