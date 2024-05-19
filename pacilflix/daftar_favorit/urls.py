from django.urls import path
from daftar_favorit.views import delete_sub_favorite, favorite_list, modal_favorite, sub_favorite_list

app_name = 'daftar_favorit'

urlpatterns = [
    path('', favorite_list, name='favorite_list'),
    path('<str:timestamp>', sub_favorite_list),
    path('modal/<str:id_tayangan>', modal_favorite),
    path('<str:timestamp>/<str:id_tayangan>', delete_sub_favorite)
]
