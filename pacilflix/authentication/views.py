from django.shortcuts import render

def auth(request):
    return render(request, 'auth.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')