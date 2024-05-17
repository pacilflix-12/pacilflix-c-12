from django.urls import path
from daftar_favorit.views import favorite_list

app_name = 'daftar_favorit'

urlpatterns = [
    path('', favorite_list, name='favorite_list'),
]