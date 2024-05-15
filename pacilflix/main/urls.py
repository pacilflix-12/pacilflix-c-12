from django.urls import path
from main.views import show_main, show_trailer, show_tayangan, show_ulasan, show_series, show_film, show_episode
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('trailer/', show_trailer, name='trailer'),
    path('tayangan/', show_tayangan, name='tayangan'),
    path('ulasan/', show_ulasan, name='ulasan'),
    path('series/', show_series, name='series'),
    path('film/', show_film, name='film'),
    path('episode/', show_episode, name='episode'),
]