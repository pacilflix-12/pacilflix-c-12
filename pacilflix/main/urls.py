from django.urls import path
from main.views import show_main, show_trailer, show_tayangan, kirim_ulasan, show_episode, show_detail_tayangan
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('trailer/', show_trailer, name='trailer'),
    path('tayangan/', show_tayangan, name='tayangan'),
    path('tayangan/<str:id_tayangan>',
         show_detail_tayangan, name='tayangan-detail'),
    path('tayangan/<str:id_tayangan>/episode/<str:sub_judul>/',
         show_episode, name='episode'),
    path('ulasan/<str:id_tayangan>', kirim_ulasan, name='ulasan'),
]
