from django.urls import path
from .views import download_list, downloads_delete, downloads_add

app_name = 'daftar_unduhan'

urlpatterns = [
    path('', download_list, name='download_list'),
    path('<str:id_tayangan>/<str:datetime>', downloads_delete),
    path('<str:id_tayangan>', downloads_add)
]
