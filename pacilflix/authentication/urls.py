from authentication.views import login, auth, register
from django.urls import path

appname = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('', auth, name='auth'),
    path('register/', register, name='register'),
]